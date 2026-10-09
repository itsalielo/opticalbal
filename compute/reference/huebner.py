"""Reference implementations vendored from the Aesthetics Toolbox.

Source: Redies, C., Bartho, R., Kossmann, L., Spehar, B., Huebner, R.,
    Wagemans, J., & Hayn-Leichsenring, G. U. (2025). "A toolbox for
    calculating quantitative image properties in aesthetics research."
    Behavior Research Methods, 57(4), 117.
    DOI: 10.3758/s13428-025-02632-3 (open access, PMC11909096)
Code: https://github.com/RBartho/Aesthetics-Toolbox (AT/balance_qips.py)

Vendored functions: Balance()  (Huebner-group "Balance" QIP - APB-family:
    mean of 8 axis/inner-outer difference measures, 0 = balanced, 100 = max
    imbalance) and DCM() (Deviation of the Center of Mass; returns
    (rdist, htmp, vtmp), rdist 0..~141.42).

Vendored VERBATIM except: module-level skimage imports removed (these two
functions are numpy-only). The historical MATLAB double-counting quirk at
the 128 threshold (noted in the original comments) is preserved intentionally
- it is part of the reference behavior. Used here as the canonical
reference to validate our own implementations against. Do not edit the
function bodies; wrap them instead.
"""

import numpy as np

def Balance(img_gray):
    '''
    Calculates the "Balance" QIP from Ronald Huebner Group
    
    Input: Takes a grayscale image in Pillow format as input. 
    Output: Balance QIP
    
    Usage:
    Load images like this:
        
    Import Image from PIL    
    
    img_gray = np.asarray(Image.open( path_to_image_file ).convert('L')) 
    Balance(img_gray)
    '''
    
    height, width = img_gray.shape

    hist = np.histogram(img_gray, bins=256, range=(0, 256))

    counts = hist[0]
    
    thres = 128

    sum1 = sum(counts[:thres])
    sum2 = sum(counts[thres-1:])  # in the Matlab code, the treshold value 126 is added twice. This programming error has hardly any effect on the results and has been adopted here in the Python code.
    
    if sum1 <= sum2:
        im_comp = 255 - img_gray
    else:
        im_comp = img_gray

    nall = np.sum(im_comp)  
    
    ## to avoid division 0
    if nall == 0:
        nall = 1

    # Horizontal balance
    w = width // 2
    
    s1 = np.sum(im_comp[:, :w], dtype=int)
    s2 = np.sum(im_comp[:, -w:], dtype=int)
    bh = (abs(s1 - s2) / nall) * 100  
        
    w2 = width // 4 # adding center row of w to middle area if w uneven 

    s1 = np.sum(im_comp[:, :w2], dtype=int)
    s2 = np.sum(im_comp[:, -w2:], dtype=int)

    bioh = (abs((nall - (s1 + s2)) - (s1 + s2)) / nall) * 100 # %  inner-outer horizontal 

    # Vertical balance
    h = height // 2

    s1 = np.sum(im_comp[:h, :], dtype=int)
    s2 = np.sum(im_comp[-h:, :], dtype=int)
    bv = (abs(s1 - s2) / nall) * 100
    
    h2 = height // 4
    s1 = np.sum(im_comp[:h2, :], dtype=int)
    s2 = np.sum(im_comp[-h2:, :], dtype=int)

    biov = (abs((nall - (s1 + s2)) - (s1 + s2)) / nall) * 100

    # Main diagonal and inner-outer (bottom right top left)
    s1 = np.sum(np.triu(im_comp, 1), dtype=int)
    s2 = np.sum(np.tril(im_comp, -1), dtype=int)
    bmd = (abs(s1 - s2) / nall) * 100

    prop = 1 / np.sqrt(2)
    b1 = height - int(height * prop)
    b2 = width - int(width * prop)
    s1 = np.sum(np.tril(im_comp, -b1), dtype=int)
    s2 = np.sum(np.triu(im_comp, b2), dtype=int)
    biomd = (abs((nall - (s1 + s2)) - (s1 + s2)) / nall) * 100

    # Anti-diagonal and inner-outer (bottom right top left)
    im_comp = np.rot90(im_comp)
    s1 = np.sum(np.triu(im_comp, 1), dtype=int)
    s2 = np.sum(np.tril(im_comp, -1), dtype=int)
    bad = (abs(s1 - s2) / nall) * 100

    s1 = np.sum(np.tril(im_comp, -b2), dtype=int)
    s2 = np.sum(np.triu(im_comp, b1), dtype=int)
    bioad = (abs((nall - (s1 + s2)) - (s1 + s2)) / nall) * 100

    bs = (bh + bv + bioh + biov + bmd + biomd + bad + bioad) / 8

    return bs


def DCM(img_gray):
    '''
    Calculates the "DCM" QIP from Ronald Huebner Group
    
    Input: Takes a grayscale image in Pillow format as input. 
    Output: DCM QIP
    
    Usage:
    Load images like this:
        
    Import Image from PIL    
    
    img_gray = np.asarray(Image.open( path_to_image_file ).convert('L')) 
    DCM(img_gray)
    '''
    
    height, width = img_gray.shape

    hist = np.histogram(img_gray, bins=256, range=(0, 256))
    counts = hist[0]
       
    thres = 128

    sum1 = sum(counts[:thres])
    sum2 = sum(counts[thres:])
    
    if sum1 <= sum2:
        im_comp = 255 - img_gray  # Invert image
    else:
        im_comp = img_gray

    nall = np.sum(im_comp)   ### Number of Pixels with value of 0
    
    # Horizontal balance point
    r = 0
    for i in range(width):
        w = np.sum(im_comp[:, i],dtype=float)
        r += w * i
    Rh = np.round(r / nall) + 1  # x position of fulcrum
    Rhnorm = Rh / width  # Normalized
    
    # Vertical balance point
    r = 0
    for i in range(height):
        w = np.sum(im_comp[i, :],dtype=float)
        r += w * i
    Rv = np.round(r / nall) + 1  # y position of fulcrum
    Rvnorm = Rv / height  # Normalized

    htmp = 0.5 - Rhnorm
    vtmp = 0.5 - Rvnorm

    dist = np.sqrt(htmp ** 2 + vtmp ** 2)
    rdist = (dist / 0.5) * 100

    return rdist, htmp, vtmp
