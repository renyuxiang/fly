#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv


def read_csv():
    r_path = './csv_example.csv'
    csv_file=csv.reader(open(r_path,'r', encoding='utf-8'))
    print(csv_file)  # 可以先输出看一下该文件是什么样的类型
    content = []
    for line in csv_file:
        print(line)  # 打印文件每一行的信息
        content.append(line)

if __name__ == '__main__':
    read_csv()