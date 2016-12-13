#-*- coding: utf-8 -*-
import subprocess
from multiprocessing import Pool
import random
import time
import itertools

'''
バカ並列
'''


USER_NUM = [100, 200, 400, 800, 1600]

REGULARIZE = [1, 2, 3]

RANK = [5, 6, 7]

STEP_SIZE = [0.01,]

SCRIPT = 'hoge.py'


def f(args):
    with open('result_{}.txt'.format('_'.join(list(map(str, args)))), 'w') as f:
        subprocess.call(['python3', SCRIPT]+list(map(str, args)), stdout=f)
    return True


if __name__ == '__main__':

    # 引数の順番でおねがいします
    params = itertools.product(USER_NUM, REGULARIZE, RANK, STEP_SIZE)

    p = Pool()
    p.map(f, params)
