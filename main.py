#!/usr/bin/env python3

import sys
import math
import csv
import os
import string

def compute_confidence_interval_coefficients(v):
    partial = lambda x: x * 100.0 / 2.0
    return partial(2 * 1.96 * math.sqrt(v)), partial(2 * 2.58 * math.sqrt(v))

def task(pop, ss, vt):
    print('Population size:\t%i'% pop)
    print('Sample size:\t\t%i'% ss)
    print('Voting intentions:\t%.2f%%'% vt)
    vt /= 100
    var = (vt * (1 - vt)) *(pop - ss)
    emean = ss * (pop - 1)
    variance = var / emean
    print('Variance: \t\t%.6f'% variance)
    c95, c99 = compute_confidence_interval_coefficients(variance)
    vt *= 100
    show_confidence_interval(95, vt - c95, vt + c95)
    show_confidence_interval(99, vt - c99, vt + c99)

def show_confidence_interval(ci, border_inf, border_sup):
    print('%i%% confidence interval: [%.2f%%; %.2f%%]'% (ci, max(0, border_inf), min(100, border_sup)))

def is_arg_good(i, c, arg):
    if c == 3:
        try:
            float(i)
        except:
            print(i, "Must be a float")
            return 84
        if float(i) <= 0 and float(i) >= 100:
            print(i, "Must be between 0 and 100")
            return 84
    else:
        try:
            int(i)
        except:
            print(i, "Must be a int")
            return 84
        if int(i) <= 0:
            print(i, "Must be higher than 0")
            return 84
        if arg[1] <= arg[2]and c == 2:
            print(arg[1], "Must be higher than", arg[2])
            return 84
    return 0

if len(sys.argv) == 2 and sys.argv[1] == "-h":
    print('USAGE\n\t%s pSize sSize p\n\nDESCRIPTION' % sys.argv[0])
    print('\tpSize\tsize of the population')
    print('\tsSize\tsize of the sample (supposed to be representative)')
    print('\tp\tpercentage of voting intentions for a specific candidate')
    exit(0)
elif len(sys.argv) == 4:
    err = 0
    nbr = list()
    for i in range(1, len(sys.argv)):
        err = err + is_arg_good(sys.argv[i], i, sys.argv)
    if err != 0:
        exit(84)
    for i in range(1, len(sys.argv)):
        nbr.append(float(sys.argv[i]))
    task(int(nbr[0]), int(nbr[1]), float(nbr[2]))
    exit(0)
else:
    print("Err: try -h for help")
    exit(84)
