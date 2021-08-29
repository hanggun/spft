from spft.multiprocess import multi_process
from tqdm import tqdm


def funcs(data):
    x = data[0]
    y = data[1]
    return x+y


if __name__ == '__main__':
    multi_process(funcs, tqdm(list(zip(*[range(10000000), range(10000000)]))), 6, is_queue=False)