"""Task 1 (re-run): head-to-head comparison on the 17-image corpus.

Models: DCM, VME, VME-ninegrid, Russian position-only (faithful default),
Russian extended (our extension, not the paper), Saliency, Toolbox DCM
(canonical reference), Toolbox Balance QIP (canonical reference).
"""
import json, os, sys
import numpy as np
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from models import (DCMModel, VMEModel, RussianModel, SaliencyModel,
                    ToolboxDCMModel, ToolboxBalanceModel)

CORPUS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "corpus")

models = [
    DCMModel(),
    VMEModel(),
    VMEModel(nine_grid=True),
    RussianModel(mode="position_only"),
    RussianModel(mode="extended"),
    SaliencyModel(),
    ToolboxDCMModel(),
    ToolboxBalanceModel(),
]
colnames = ["DCM", "VME", "VME-9g", "Rus-pos", "Rus-ext", "Saliency",
            "Tbx-DCM", "Tbx-Bal"]

with open(os.path.join(CORPUS, "metadata.json")) as f:
    meta = json.load(f)

rows = []
for entry in meta:
    name = entry["name"]
    img = Image.open(os.path.join(CORPUS, name + ".png"))
    scores = [m.score(img)["balance"] for m in models]
    rows.append((name, entry["manipulation"], scores))

print("| image | manipulation | " + " | ".join(colnames) + " |")
print("|---|---|" + "---|" * len(colnames))
for name, manip, scores in rows:
    print(f"| {name} | {manip} | " + " | ".join(f"{s:.3f}" for s in scores) + " |")

print("\n# per-model stats over corpus")
arr = np.array([s for _, _, s in rows])
for i, c in enumerate(colnames):
    v = arr[:, i]
    print(f"{c:10s} min={v.min():.3f} max={v.max():.3f} mean={v.mean():.3f} std={v.std():.3f}")

# VALIDATION: hand-rolled DCM vs canonical toolbox DCM
d_hand = arr[:, 0]
d_tbx = arr[:, 6]
maxdiff = float(np.abs(d_hand - d_tbx).max())
meandiff = float(np.abs(d_hand - d_tbx).mean())
print(f"\n# VALIDATION hand-DCM vs toolbox-DCM: max|diff|={maxdiff:.4f} "
      f"mean|diff|={meandiff:.4f} over {len(rows)} corpus images")

print("\n# pairwise Pearson correlation of balance scores across corpus")
n = len(colnames)
for i in range(n):
    for j in range(i + 1, n):
        r = np.corrcoef(arr[:, i], arr[:, j])[0, 1]
        print(f"  corr({colnames[i]}, {colnames[j]}) = {r:.3f}")

print("\n# artifact checks")
by_name = {name: scores for name, _, scores in rows}
for img in ["dark_vs_light", "bar_left_heavy", "big_vs_small",
            "mark_symmetric", "disk_centered", "disk_left",
            "two_inverse_ratio", "red_vs_blue", "sat_high_vs_low",
            "quadrants_heavy_UL", "three_triangle"]:
    s = by_name[img]
    print(f"  {img:22s} " + " ".join(f"{c}={v:.3f}" for c, v in zip(colnames, s)))

# per-image per-model detail dump for degeneracy inspection
print("\n# Russian position-only element weights on big_vs_small (expect equal "
      "weights -> 1.0)")
img = Image.open(os.path.join(CORPUS, "big_vs_small.png"))
res = RussianModel(mode="position_only").score(img)
print(f"  balance={res['balance']:.4f}")
for w in res["detail"]["element_vW"]:
    print(f"  element {w['label']}: vW={w['vW']:.4f} pos={w['vWsS_position']:.4f} "
          f"size={w['vWs_size']:.4f} color={w['vWc_color']:.4f}")

print("\n# Russian position-only on disk_centered (expect zero mass -> 1.0 by "
      "convention, flagged)")
img = Image.open(os.path.join(CORPUS, "disk_centered.png"))
res = RussianModel(mode="position_only").score(img)
print(f"  balance={res['balance']:.4f} total_vW={res['detail']['total_vW']:.6f} "
      f"note={res['detail'].get('note', res['detail'].get('mode'))}")

print("\n# Toolbox Balance QIP on disk_centered (expect ~0.5: inner-outer "
      "penalty on concentrated central mass)")
img = Image.open(os.path.join(CORPUS, "disk_centered.png"))
res = ToolboxBalanceModel().score(img)
print(f"  balance={res['balance']:.4f} bs={res['detail']['bs_0_100']:.2f}")

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "headtohead.json"), "w") as f:
    json.dump([{"image": n, "manipulation": m,
                "scores": {c: float(s) for c, s in zip(colnames, sc)}}
               for n, m, sc in rows], f, indent=2)
print("\nsaved headtohead.json")
