import sys
import argparse
import numpy as np


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--log", default='ir_exp.log')
    parser.add_argument("--prefix", default="ExecuteTimeMS")
    args = parser.parse_args()
    return args


def main(args):
    t = []
    with open(args.log, "r") as f:
        for l in f.readlines():
            sub_l = l[l.index(args.prefix) + len(args.prefix):]
            exec_time = sub_l[sub_l.index("[") + 1: sub_l.index("]")]
            t.append(int(exec_time))
    print("Total counts: ", len(t))
    print("Avg: ", np.average(t))
    print("Std: ", round(np.std(t), 2))
    print("Min: ", np.min(t))
    print("Max: ", np.max(t))
    print("P50 : ", round(np.percentile(t, 50), 2))
    print("P90 : ", round(np.percentile(t, 90), 2))
    print("P95 : ", round(np.percentile(t, 95), 2))
    print("P99 : ", round(np.percentile(t, 99), 2))


if __name__ == '__main__':
    args = parse_args()
    main(args)
