from spft.multiprocess import multi_process, multi_process_generator
from tqdm import tqdm
import json
import numpy as np


def funcs(data):
    x = data[0]
    y = data[1]
    return x+y


if __name__ == '__main__':
    # multi_process(funcs, tqdm(list(zip(*[range(10000000), range(10000000)]))), 6, is_queue=False)
    for data in multi_process_generator(funcs, list(zip(*[range(100), range(100)])), 6):
        print(data)
