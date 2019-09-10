#!/usr/bin/env python
# -*- coding: utf-8 -*-


r_path = './data/txt_example.txt'
w_path = './data/txt_example.txt'
content = ['1', '2', '3', '4', '5']


def read_txt(r_path):
    #  txt 一般是存取一行的数据
    data = []
    with open(r_path, encoding='utf-8', mode='r') as f:
        for line in f:
            if not line:
                continue
            line = line.strip()
            data.append(line)
            print(line)
    print('len(content):', len(data))


def write_txt(content, w_path):
    if not content:
        print('没有content内容')
        return
    with open(w_path, encoding='utf-8', mode='w') as f:
        for line in content:
            f.write(line + '\n')
    print('write ok!!!')


if __name__ == '__main__':
    read_txt(r_path=r_path)
    # write_txt(content=content, w_path=w_path)