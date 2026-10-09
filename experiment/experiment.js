'use strict';
/* =====================================================================
   OPTICAL BALANCING — online method-of-adjustment prototype (v0.1.0)
   ---------------------------------------------------------------------
   HONESTY HEADER: This is a PROTOTYPE research instrument. It has NOT
   been validated, carries no ethics approval (consent text is an explicit
   PLACEHOLDER), and NO HUMAN DATA has ever been collected with it. It is
   the secondary/fallback instrument for the optical-balancing mission
   (lab study is primary). Do not treat its outputs as scientific findings.

   Paradigm lineage: the spatial-balance-of-color-pairs tradition —
   Moon & Spencer (1944, JOSA), Granger (1953, Science), Morriss & Dunlap
   (1982 Am J Psych; 1987 J Gen Psych; 1988 Emp Stud Arts; 1988 Color Res
   Appl). Their method: the observer ADJUSTS AN AREA until two color
   regions feel balanced; the adjusted area is the dependent variable.
   Our extension (implementer decision, no literature source): the null
   point is found by MATCHING TWO SIDE-BY-SIDE COMPOSITIONS — the observer
   adjusts the area of one patch in the test composition until it feels
   equally balanced to a fixed reference composition.

   Six-factor framing (from the computational track, §3 of
   optical-balancing-compute.md): saturation, hue, lightness (= HSV value
   V here), area (always the DV), position, contrast (luminance-based,
   against the ground; varied even at fixed HSV value by varying the
   ground). Each main trial varies the test patch's factors against a
   fixed reference; the adjusted area ratio recovers relative visual
   weight. An exact-null trial (test == reference) and a 2x2
   position x saturation block are included for calibration and
   interaction probing.
   ===================================================================== */

/* ---------------- 1. Configuration & constants ---------------- */

const CFG = {
  seed: 20261009,          // mulberry32 seed — DOCUMENTED, fixed across participants (see README)
  panel: 400,              // logical stimulus units per side
  rRef: 40,                // reference patch radius (area_ref = PI * 40^2)
  rMin: 14, rMax: 66,      // slider range — implementer choice (see README)
  rStep: 0.5,
  anchorA: { s: 0, v: 0.22, x: 120, y: 200, r: 40 }, // dark-gray anchor disk, fixed everywhere
  refB:    { h: 0, s: 0.80, v: 0.70, x: 280, y: 200, r: 40 }, // reference test-patch
  groundRef: 0.78,         // reference ground gray (V)
  attPassMax: 56,          // attention-check thresholds — implementer choice (see README)
  attPassMin: 22,
};

/* ---------------- 2. Seeded RNG (mulberry32) ---------------- */

function mulberry32(a) {
  return function () {
    a |= 0; a = (a + 0x6D2B79F5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

/* ---------------- 3. Color math (documented choices) ----------------
   - Stimulus colors are specified in HSV: H in degrees [0,360),
     S and V in [0,1]. "Lightness" in the six-factor framing is
     implemented as HSV value V (documented simplification; NOT CIELAB L*).
   - HSV -> RGB: the standard sector algorithm (Foley & van Dam /
     CSS Color 4 formulation). Hues wrap; S=0 yields achromatic gray.
   - Luminance: Rec. 709 luma computed on GAMMA-ENCODED 8-bit sRGB
     components, NOT linearized. Documented simplification: contrast
     values are display-referred, not photometric. A real deployment
     would linearize (sRGB EOTF) and calibrate the display.
   - Contrast (per §3): |L_elem - L_ground|, in [0,1]. For an achromatic
     ground, L_ground == V_ground exactly. Hue-as-hue is NOT encoded
     anywhere — consistent with the computational finding that no model
     sees hue as hue (only via luminance). */

function hsvToRgb(h, s, v) {
  h = ((h % 360) + 360) % 360;
  s = Math.min(1, Math.max(0, s));
  v = Math.min(1, Math.max(0, v));
  const c = v * s;
  const x = c * (1 - Math.abs(((h / 60) % 2) - 1));
  const m = v - c;
  let rp, gp, bp;
  if (h < 60)       { rp = c; gp = x; bp = 0; }
  else if (h < 120) { rp = x; gp = c; bp = 0; }
  else if (h < 180) { rp = 0; gp = c; bp = x; }
  else if (h < 240) { rp = 0; gp = x; bp = c; }
  else if (h < 300) { rp = x; gp = 0; bp = c; }
  else              { rp = c; gp = 0; bp = x; }
  const q = (n) => Math.round((n + m) * 255);
  return [q(rp), q(gp), q(bp)];
}

function luminance709(rgb) {
  return (0.2126 * rgb[0] + 0.7152 * rgb[1] + 0.0722 * rgb[2]) / 255;
}

function elemRecord(h, s, v, x, y, r, groundV) {
  const rgb = hsvToRgb(h, s, v);
  const lum = luminance709(rgb);
  return {
    h: round3(h), s: round3(s), v: round3(v),
    x: x, y: y, r: round3(r),
    rgb: rgb,
    lum: round4(lum),
    contrast: round4(Math.abs(lum - groundV)), // |L_elem - L_ground|
  };
}

function round3(n) { return Math.round(n * 1000) / 1000; }
function round4(n) { return Math.round(n * 10000) / 10000; }

/* ---------------- 4. Trial construction ----------------
   Fixed seed => identical trial order, slider starts, and adjustable
   sides for every participant (documented; a real deployment would draw
   a fresh recorded seed per participant). Attention checks are spliced
   into positions 8 and 16 of the 24-trial main loop. */

function buildMainTrials() {
  const rng = mulberry32(CFG.seed);
  const list = [];
  const add = (block, testOverrides, groundV) => {
    list.push({
      block: block,
      trial_type: 'main',
      expect: null,
      testOverrides: testOverrides || {},
      groundV: (groundV == null) ? CFG.groundRef : groundV,
    });
  };

  // OFAT sweeps (one factor varied, rest at reference)
  [0.20, 0.45, 0.65, 1.00].forEach((s) => add('saturation', { s: s }));
  [60, 120, 240, 300].forEach((h) => add('hue', { h: h }));
  [0.35, 0.50, 1.00].forEach((v) => add('lightness', { v: v }));
  [250, 295, 325].forEach((x) => add('position', { x: x }));
  // Contrast sweep: ground varies at fixed element HSV (per §3)
  [0.45, 0.60, 0.92].forEach((g) => add('contrast', {}, g));
  // Exact-null calibration trial (test == reference)
  add('null', {}, CFG.groundRef);
  // 2x2 position x saturation interaction block
  [[0.35, 250], [0.35, 310], [0.95, 250], [0.95, 310]].forEach(([s, x]) =>
    add('interaction', { s: s, x: x }));

  // Fisher–Yates shuffle of the 22 experimental trials
  for (let i = list.length - 1; i > 0; i--) {
    const j = Math.floor(rng() * (i + 1));
    [list[i], list[j]] = [list[j], list[i]];
  }

  // Attention checks: extreme stimuli, any reasonable observer pushes
  // the slider to an end. Flagged in data, never judged to the participant.
  const attMax = { // near-invisible patch on the ground -> expect MAX
    block: 'attention', trial_type: 'attention', expect: 'max',
    testOverrides: { h: 0, s: 0, v: round3(CFG.groundRef + 0.05) },
    groundV: CFG.groundRef,
  };
  const attMin = { // very dark saturated red -> expect MIN
    block: 'attention', trial_type: 'attention', expect: 'min',
    testOverrides: { h: 0, s: 1.0, v: 0.12 },
    groundV: CFG.groundRef,
  };
  list.splice(7, 0, attMax);
  list.splice(15, 0, attMin);

  // Per-trial randomization: slider start + adjustable side.
  // Random starts counteract anchoring bias (cheap substitute for the
  // classical ascending/descending series). Random sides counteract
  // reading-direction position-weight asymmetries (§3 break c).
  list.forEach((t) => {
    t.rStart = Math.round((18 + rng() * 44) * 2) / 2; // 18..62, step 0.5
    t.side = rng() < 0.5 ? 'left' : 'right';
  });
  return list;
}

function buildPracticeTrials() {
  // Fixed, easy, non-seeded: mechanics training only.
  return [
    { block: 'practice', trial_type: 'practice', expect: null,
      testOverrides: { h: 40 }, groundV: CFG.groundRef, rStart: 40, side: 'right' },
    { block: 'practice', trial_type: 'practice', expect: null,
      testOverrides: { s: 0.60 }, groundV: CFG.groundRef, rStart: 40, side: 'right' },
    { block: 'practice', trial_type: 'practice', expect: null,
      testOverrides: { v: 0.55 }, groundV: CFG.groundRef, rStart: 40, side: 'right' },
  ];
}

// Expand a trial spec into a full parameter record (stimulus side only;
// the response is attached at confirm time).
function finalizeTrial(spec, trialNumber) {
  const g = spec.groundV;
  const A = CFG.anchorA;
  const aRec = elemRecord(0, A.s, A.v, A.x, A.y, A.r, g);
  const refB = Object.assign({}, CFG.refB, { r: CFG.rRef });
  const testB = Object.assign({}, CFG.refB, spec.testOverrides, { r: spec.rStart });
  return {
    trial_number: trialNumber,
    trial_type: spec.trial_type,
    block: spec.block,
    adjustable_side: spec.side,
    attention_expected: spec.expect,
    ref: {
      ground_v: round3(g),
      ground_lum: round4(g), // achromatic ground => L == V
      a: aRec,
      b: elemRecord(refB.h, refB.s, refB.v, refB.x, refB.y, refB.r, g),
    },
    test: {
      a: aRec,
      b: elemRecord(testB.h, testB.s, testB.v, testB.x, testB.y, testB.r, g),
      r_start: spec.rStart,
    },
    response: null,
  };
}

/* ---------------- 5. Canvas rendering (DPR-aware) ---------------- */

function drawComposition(canvas, spec) {
  const dpr = window.devicePixelRatio || 1;
  canvas.width = CFG.panel * dpr;
  canvas.height = CFG.panel * dpr;
  const ctx = canvas.getContext('2d');
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  const gv = Math.round(spec.groundV * 255);
  ctx.fillStyle = 'rgb(' + gv + ',' + gv + ',' + gv + ')';
  ctx.fillRect(0, 0, CFG.panel, CFG.panel);
  // Flat fills only — no shadows/gradients (they would add luminance confounds).
  [spec.a, spec.b].forEach((e) => {
    ctx.fillStyle = 'rgb(' + e.rgb[0] + ',' + e.rgb[1] + ',' + e.rgb[2] + ')';
    ctx.beginPath();
    ctx.arc(e.x, e.y, e.r, 0, Math.PI * 2);
    ctx.fill();
  });
}

/* ---------------- 6. Session state & event log ---------------- */

const sessionT0 = performance.now();
const session = {
  instrument: 'opticalbal-adjustment-prototype',
  version: '0.1.0',
  honesty: 'PROTOTYPE — not validated; no human data collected with this tool ' +
           'prior to this session; consent text is a placeholder.',
  seed: CFG.seed,
  session_id: 'OB-' + randomId(),
  started_at: new Date().toISOString(),
  user_agent: navigator.userAgent,
  viewport_w: window.innerWidth,
  viewport_h: window.innerHeight,
  device_pixel_ratio: window.devicePixelRatio || 1,
  trials: [],
  events: [],
};

function randomId() {
  const buf = new Uint8Array(6);
  (window.crypto || {}).getRandomValues
    ? window.crypto.getRandomValues(buf)
    : buf.forEach((_, i) => { buf[i] = Math.floor(Math.random() * 256); });
  return Array.from(buf).map((b) => b.toString(16).padStart(2, '0')).join('');
}

function logEvent(type, data) {
  const e = { t_ms: Math.round((performance.now() - sessionT0) * 100) / 100, type: type };
  if (data) for (const k in data) e[k] = data[k];
  session.events.push(e);
}

/* ---------------- 7. Screen flow ---------------- */

const el = (id) => document.getElementById(id);
const screens = ['screen-consent', 'screen-instructions', 'screen-trial', 'screen-debrief'];

function showScreen(id) {
  screens.forEach((s) => el(s).classList.toggle('active', s === id));
  logEvent('screen_show', { screen: id });
  if (id === 'screen-instructions') drawExampleFigure();
}

let practiceTrials = [];
let mainTrials = [];
let trialActive = false;
let currentTrial = null;
let currentPhase = null;   // 'practice' | 'main'
let trajectory = [];
let trialT0 = 0;
let nInputs = 0;

function guardUnload(e) {
  e.preventDefault();
  e.returnValue = '';
}

el('consent-yes').addEventListener('click', () => {
  logEvent('consent', { given: true });
  showScreen('screen-instructions');
});
el('consent-no').addEventListener('click', () => {
  logEvent('consent', { given: false });
  el('consent-decline-msg').hidden = false;
  el('consent-yes').disabled = true;
});

el('instr-begin').addEventListener('click', () => {
  practiceTrials = buildPracticeTrials().map((s, i) => finalizeTrial(s, i + 1));
  mainTrials = buildMainTrials().map((s, i) => finalizeTrial(s, i + 1));
  logEvent('protocol_ready', {
    n_practice: practiceTrials.length, n_main: mainTrials.length,
    seed: CFG.seed,
  });
  window.addEventListener('beforeunload', guardUnload);
  runPhase('practice');
});

/* ---------------- 8. Trial runner ---------------- */

function runPhase(phase) {
  currentPhase = phase;
  const queue = phase === 'practice' ? practiceTrials : mainTrials;
  logEvent('phase_start', { phase: phase, n_trials: queue.length });
  showScreen('screen-trial');
  runNext(queue, 0);
}

function runNext(queue, idx) {
  if (idx >= queue.length) {
    if (currentPhase === 'practice') {
      logEvent('phase_end', { phase: 'practice' });
      runPhase('main');
    } else {
      logEvent('phase_end', { phase: 'main' });
      finishSession();
    }
    return;
  }
  const trial = queue[idx];
  currentTrial = trial;
  renderTrial(trial, idx, queue.length, () => runNext(queue, idx + 1));
}

function refSpec(trial) {
  return { groundV: trial.ref.ground_v, a: trial.ref.a, b: trial.ref.b };
}
function testSpec(trial, r) {
  const b = Object.assign({}, trial.test.b, { r: r });
  return { groundV: trial.ref.ground_v, a: trial.test.a, b: b };
}

function renderTrial(trial, idx, total, onDone) {
  const leftIsTest = trial.adjustable_side === 'left';
  pendingDone = onDone; // continuation for the Enter-key path

  drawComposition(el('canvas-left'), leftIsTest ? testSpec(trial, trial.test.r_start) : refSpec(trial));
  drawComposition(el('canvas-right'), leftIsTest ? refSpec(trial) : testSpec(trial, trial.test.r_start));

  el('label-left').textContent = leftIsTest ? 'Adjustable' : 'Reference';
  el('label-right').textContent = leftIsTest ? 'Reference' : 'Adjustable';

  // The single slider block moves under the adjustable panel.
  el(leftIsTest ? 'slot-left' : 'slot-right').appendChild(el('slider-block'));
  el('slider-block').hidden = false;
  el('practice-note').hidden = true;

  const slider = el('size-range');
  slider.min = CFG.rMin; slider.max = CFG.rMax; slider.step = CFG.rStep;
  slider.value = trial.test.r_start;

  // Counter + progress (progress bar during the main task).
  const phaseLabel = currentPhase === 'practice' ? 'Practice' : 'Trial';
  el('trial-counter').textContent = phaseLabel + ' ' + (idx + 1) + ' of ' + total;
  el('trial-progress').style.visibility = currentPhase === 'main' ? 'visible' : 'hidden';
  el('trial-progress-fill').style.width = currentPhase === 'main'
    ? Math.round((idx / total) * 1000) / 10 + '%' : '0%';

  trajectory = [[0, trial.test.r_start]];
  nInputs = 0;
  trialActive = true;
  trialT0 = performance.now();
  logEvent('trial_start', {
    phase: currentPhase, trial_number: trial.trial_number,
    trial_type: trial.trial_type, block: trial.block,
    adjustable_side: trial.adjustable_side, r_start: trial.test.r_start,
  });

  slider.oninput = () => {
    if (!trialActive) return;
    const r = parseFloat(slider.value);
    const t = Math.round((performance.now() - trialT0) * 100) / 100;
    trajectory.push([t, r]);
    nInputs++;
    const canvas = el(leftIsTest ? 'canvas-left' : 'canvas-right');
    drawComposition(canvas, testSpec(trial, r));
  };

  const confirmBtn = el('confirm-btn');
  confirmBtn.onclick = () => confirmTrial(trial, parseFloat(slider.value), onDone);

  // Focus the slider so native arrow-key support works immediately.
  try { slider.focus({ preventScroll: true }); } catch (e) { slider.focus(); }
}

// Document-level keys: +/- adjust, Enter confirms. Arrow keys are handled
// natively by the focused range input; we only add them here when focus is
// elsewhere (avoiding double steps).
document.addEventListener('keydown', (e) => {
  if (!trialActive || !currentTrial) return;
  const slider = el('size-range');
  const tag = (e.target && e.target.tagName) || '';
  if (e.key === 'Enter') {
    if (tag !== 'BUTTON') { e.preventDefault(); confirmTrial(currentTrial, parseFloat(slider.value), pendingDone); }
    return;
  }
  if (tag === 'INPUT' && e.target.type === 'text') return;
  const step = CFG.rStep * (e.shiftKey ? 10 : 2);
  if (e.key === '+' || e.key === '=') {
    e.preventDefault(); nudgeSlider(step);
  } else if (e.key === '-' || e.key === '_') {
    e.preventDefault(); nudgeSlider(-step);
  } else if ((e.key === 'ArrowLeft' || e.key === 'ArrowDown') && e.target !== slider) {
    e.preventDefault(); nudgeSlider(-CFG.rStep);
  } else if ((e.key === 'ArrowRight' || e.key === 'ArrowUp') && e.target !== slider) {
    e.preventDefault(); nudgeSlider(CFG.rStep);
  }
});

function nudgeSlider(delta) {
  if (!trialActive) return;
  const slider = el('size-range');
  slider.value = parseFloat(slider.value) + delta;
  slider.dispatchEvent(new Event('input', { bubbles: true }));
}

let pendingDone = null;

function confirmTrial(trial, rFinal, onDone) {
  if (!trialActive) return;
  trialActive = false;
  const rtMs = Math.round((performance.now() - trialT0) * 100) / 100;
  trajectory.push([rtMs, rFinal]);

  let attentionPass = null;
  if (trial.trial_type === 'attention') {
    attentionPass = trial.attention_expected === 'max'
      ? rFinal >= CFG.attPassMax
      : rFinal <= CFG.attPassMin;
  }

  trial.response = {
    r_final: round3(rFinal),
    area_final: round3(Math.PI * rFinal * rFinal),
    area_ratio_vs_ref: round4((rFinal * rFinal) / (CFG.rRef * CFG.rRef)),
    trajectory: trajectory,           // [[elapsed_ms, radius], ...]
    rt_ms: rtMs,
    n_inputs: nInputs,
    attention_pass: attentionPass,     // null for non-attention trials
  };
  session.trials.push(flattenTrial(trial));
  logEvent('trial_confirm', {
    phase: currentPhase, trial_number: trial.trial_number,
    trial_type: trial.trial_type, block: trial.block,
    r_final: trial.response.r_final, rt_ms: rtMs, n_inputs: nInputs,
    attention_pass: attentionPass,
  });

  if (currentPhase === 'main') {
    el('trial-progress-fill').style.width =
      Math.round(((trial.trial_number) / mainTrials.length) * 1000) / 10 + '%';
    onDone();
  } else {
    // Practice: confirm the mechanics worked — no correctness feedback,
    // because there is no right answer.
    el('slider-block').hidden = true;
    const notes = [
      'That was practice 1 of 3. The mechanics work the same way every trial.',
      'Practice 2 of 3 recorded. One more to go.',
      'Practice 3 of 3 recorded. The main task (24 trials) starts next.',
    ];
    el('practice-note-text').textContent = notes[trial.trial_number - 1] || 'Recorded.';
    el('practice-note').hidden = false;
    el('practice-continue').onclick = () => { onDone(); };
    el('practice-continue').focus();
  }
}

// One flat object per trial for the session record (CSV uses a subset).
function flattenTrial(t) {
  const r = t.response;
  return {
    trial_number: t.trial_number,
    trial_type: t.trial_type,
    block: t.block,
    adjustable_side: t.adjustable_side,
    ground_v: t.ref.ground_v,
    ref_b_h: t.ref.b.h, ref_b_s: t.ref.b.s, ref_b_v: t.ref.b.v,
    ref_b_r: t.ref.b.r, ref_b_x: t.ref.b.x, ref_b_y: t.ref.b.y,
    ref_b_lum: t.ref.b.lum, ref_b_contrast: t.ref.b.contrast,
    ref_a_v: t.ref.a.v, ref_a_lum: t.ref.a.lum, ref_a_contrast: t.ref.a.contrast,
    test_b_h: t.test.b.h, test_b_s: t.test.b.s, test_b_v: t.test.b.v,
    test_b_x: t.test.b.x, test_b_y: t.test.b.y,
    test_b_lum: t.test.b.lum, test_b_contrast: t.test.b.contrast,
    r_start: t.test.r_start,
    r_final: r.r_final,
    area_final: r.area_final,
    area_ratio_vs_ref: r.area_ratio_vs_ref,
    rt_ms: r.rt_ms,
    n_inputs: r.n_inputs,
    attention_expected: t.attention_expected,
    attention_pass: r.attention_pass,
    trajectory: r.trajectory,
  };
}

/* ---------------- 9. Debrief & export ---------------- */

function finishSession() {
  window.removeEventListener('beforeunload', guardUnload);
  logEvent('session_end', { n_trials: session.trials.length });
  el('sum-session').textContent = session.session_id + ' · ' + session.started_at;
  const nP = session.trials.filter((t) => t.trial_type === 'practice').length;
  const nM = session.trials.filter((t) => t.trial_type === 'main').length;
  const nA = session.trials.filter((t) => t.trial_type === 'attention').length;
  el('sum-trials').textContent =
    session.trials.length + ' total (' + nP + ' practice + ' + nM + ' main + ' + nA + ' attention checks)';
  showScreen('screen-debrief');
}

function sessionFilename(ext) {
  return 'opticalbal-' + session.session_id + '.' + ext;
}

el('export-json').addEventListener('click', () => {
  logEvent('export', { format: 'json' });
  download(sessionFilename('json'), JSON.stringify(session, null, 2), 'application/json');
  setStatus('JSON downloaded.');
});

el('export-csv').addEventListener('click', () => {
  logEvent('export', { format: 'csv' });
  download(sessionFilename('csv'), buildCsv(), 'text/csv');
  setStatus('CSV downloaded.');
});

el('export-copy').addEventListener('click', () => {
  logEvent('export', { format: 'clipboard' });
  copyText(JSON.stringify(session, null, 2)).then(
    () => setStatus('JSON copied to clipboard.'),
    () => setStatus('Copy failed — use the download buttons instead.')
  );
});

function setStatus(msg) { el('export-status').textContent = msg; }

function buildCsv() {
  // trial_number restarts per phase (practice 1..3, main 1..24); trial_type disambiguates.
  const cols = ['session_id', 'trial_number', 'trial_type', 'block', 'adjustable_side',
    'ground_v', 'ref_b_h', 'ref_b_s', 'ref_b_v', 'ref_b_r', 'ref_b_x',
    'ref_b_lum', 'ref_b_contrast', 'ref_a_v', 'ref_a_lum', 'ref_a_contrast',
    'test_b_h', 'test_b_s', 'test_b_v', 'test_b_x',
    'test_b_lum', 'test_b_contrast',
    'r_start', 'r_final', 'area_final', 'area_ratio_vs_ref',
    'rt_ms', 'n_inputs', 'attention_expected', 'attention_pass'];
  const rows = session.trials.map((t) =>
    cols.map((c) => {
      if (c === 'session_id') return session.session_id;
      const v = t[c];
      return v === null || v === undefined ? '' : v;
    }).join(',')
  );
  return cols.join(',') + '\n' + rows.join('\n') + '\n';
}

function download(name, text, mime) {
  const blob = new Blob([text], { type: mime });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url; a.download = name;
  document.body.appendChild(a); a.click();
  setTimeout(() => { URL.revokeObjectURL(url); a.remove(); }, 800);
}

function copyText(text) {
  if (navigator.clipboard && window.isSecureContext) {
    return navigator.clipboard.writeText(text);
  }
  return new Promise((resolve, reject) => {
    const ta = document.createElement('textarea');
    ta.value = text;
    ta.style.position = 'fixed'; ta.style.opacity = '0';
    document.body.appendChild(ta); ta.select();
    try {
      if (document.execCommand('copy')) resolve();
      else reject(new Error('execCommand returned false'));
    } catch (e) { reject(e); }
    ta.remove();
  });
}

/* ---------------- 10. Instructions figure (static, non-interactive) ---------------- */

function drawExampleFigure() {
  const canvas = el('fig-canvas');
  if (canvas.dataset.drawn) return;
  canvas.dataset.drawn = '1';
  const dpr = window.devicePixelRatio || 1;
  const W = 760, H = 300;
  canvas.width = W * dpr; canvas.height = H * dpr;
  const x = canvas.getContext('2d');
  x.setTransform(dpr, 0, 0, dpr, 0, 0);
  x.fillStyle = '#ffffff'; x.fillRect(0, 0, W, H);

  const drawMini = (ox, dashed) => {
    const pw = 220, ph = 220, y0 = 10, s = pw / 400;
    const g = Math.round(CFG.groundRef * 255);
    x.fillStyle = 'rgb(' + g + ',' + g + ',' + g + ')';
    x.fillRect(ox, y0, pw, ph);
    x.strokeStyle = '#d5d5d5'; x.strokeRect(ox + 0.5, y0 + 0.5, pw - 1, ph - 1);
    // anchor A
    const aRgb = hsvToRgb(0, CFG.anchorA.s, CFG.anchorA.v);
    x.fillStyle = 'rgb(' + aRgb[0] + ',' + aRgb[1] + ',' + aRgb[2] + ')';
    x.beginPath(); x.arc(ox + CFG.anchorA.x * s, y0 + CFG.anchorA.y * s, CFG.anchorA.r * s, 0, Math.PI * 2); x.fill();
    // test B
    const bRgb = hsvToRgb(CFG.refB.h, CFG.refB.s, CFG.refB.v);
    x.fillStyle = 'rgb(' + bRgb[0] + ',' + bRgb[1] + ',' + bRgb[2] + ')';
    x.beginPath(); x.arc(ox + CFG.refB.x * s, y0 + CFG.refB.y * s, CFG.refB.r * s, 0, Math.PI * 2); x.fill();
    if (dashed) {
      x.save();
      x.strokeStyle = '#141414'; x.lineWidth = 1.5; x.setLineDash([6, 4]);
      x.beginPath(); x.arc(ox + CFG.refB.x * s, y0 + CFG.refB.y * s, (CFG.refB.r + 8) * s, 0, Math.PI * 2); x.stroke();
      x.restore();
    }
  };

  drawMini(30, false);
  drawMini(500, true);

  // Arrow between panels
  x.strokeStyle = '#141414'; x.lineWidth = 1.5;
  x.beginPath(); x.moveTo(285, 120); x.lineTo(465, 120); x.stroke();
  x.beginPath(); x.moveTo(465, 120); x.lineTo(451, 113); x.lineTo(451, 127); x.closePath();
  x.fillStyle = '#141414'; x.fill();

  x.fillStyle = '#3a3a3a';
  x.font = '12px -apple-system, "Segoe UI", Inter, Roboto, sans-serif';
  x.textAlign = 'center';
  x.fillText('make both feel equally balanced', 375, 100);
  x.textAlign = 'left';
  x.fillStyle = '#6f6f6f';
  x.font = '11px -apple-system, "Segoe UI", Inter, Roboto, sans-serif';
  x.fillText('R E F E R E N C E  —  fixed', 30, 258);
  x.fillText('A D J U S T A B L E  —  you change this patch\u2019s size', 500, 258);
}

/* ---------------- 11. Init ---------------- */

logEvent('init', { href: location.href, protocol: location.protocol });
