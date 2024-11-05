import argparse
from math import isclose, cos


def pi_half(epsilon, left=0.0, right=2.0):
    mid = (left + right) / 2
    if isclose(cos(mid), 0, abs_tol=float(epsilon)):
        return (left + right) / 2
    elif cos(mid) < 0:
        return pi_half(epsilon, left, mid)
    elif cos(mid) > 0:
        return pi_half(epsilon, mid, right)


parser = argparse.ArgumentParser(
    prog="half_pi", description="find pi/2 within a certain error", epilog="fuck"
)
parser.add_argument("-e", "--epsilon", nargs="?", default=1e-5)
args = parser.parse_args()

print(pi_half(args.epsilon))
