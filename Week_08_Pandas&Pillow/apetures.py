import numpy as np

def gen_rect(xs, ys, a, b):
    ap = (np.abs(xs) < a/2) & (np.abs(ys) < b/2)
    return np.where(ap, 1., 0.)

def gen_circle(xs, ys, r):
    ap = xs**2 + ys**2 < r**2
    return np.where(ap, 1., 0.)