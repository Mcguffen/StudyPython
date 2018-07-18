import csv
from utils import log


def head_low():
    filename = '11-info.csv'
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header_row = next(reader)
        log('header_row({})'.format(header_row))


if __name__ == '__main__':
    head_low()