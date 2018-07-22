# c测试列表
from utils import log

import csv
import xlwt
import os
import glob
import csv
from xlsxwriter.workbook import Workbook


def csv_to_xlsx():
    with open('after-11-info.csv', 'r', encoding='utf-8') as f:
        read = csv.reader(f)
        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet('data')  # 创建一个sheet表格
        l = 0
        for line in read:
            print(line)
            r = 0
            for i in line:
                print(i)
                sheet.write(l, r, i)  # 一个一个将单元格数据写入
                r = r + 1
            l = l + 1

        workbook.save('after-11-info.xlsx')  # 保存Excel


def csv_to_excel():

    for csvfile in glob.glob(os.path.join('.', '*.csv')):
        workbook = Workbook(csvfile[:-4] + '.xlsx')
        worksheet = workbook.add_worksheet()
        with open(csvfile, 'rt', encoding='utf8') as f:
            reader = csv.reader(f)
            for r, row in enumerate(reader):
                for c, col in enumerate(row):
                    worksheet.write(r, c, col)
        log("debug @@@@@ ({}) ({})({})".format(r, c, col))
        workbook.close()


def testlist():

    list1 =[]
    a = ['100', '键盘', '忻府区', '80']
    list1.append(a)
    list1.append('ccc')

    # log('debug list({})'.format(list1))
    csv_to_excel()


if __name__ == '__main__':
    # csv_to_xlsx()
    testlist()
