#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xlwt
import xlrd
r_path = './data/txt_example.txt'
w_path = './data/txt_example.txt'


def read_data(r_path, sheet_index=0, start_line=0, cols=2):
    """
    :param r_path: 文件
    :param sheet_index:
    :param start_line: 哪一行开始读取
    :param cols: 读取几列
    :return:
    """
    data = xlrd.open_workbook(r_path)
    table = data.sheets()[sheet_index]
    # 行数
    rows = table.nrows
    # 列数
    cols = table.ncols
    print('rows: ', rows)
    print('cols: ', cols)
    result = []
    for row_num in range(start_line, rows):
        row_data = table.row_values(row_num)
        data = []
        for col_temp in range(0, cols):
            data.append(row_data[col_temp])
        result.append(data)
    print('result len: %s' % len(result))
    return result


def get_lxsx_write(f=None):
    if not f:
        f = xlwt.Workbook()
    style0 = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = '宋体'
    font.height = 0x00FF
    style0.font = font
    return f, style0


def w2excle_with_col(data, sheet_name, file_name, col, head=None):
    writer, style = get_lxsx_write()
    sheet_train = writer.add_sheet(sheet_name, cell_overwrite_ok=True)
    num = 0
    if head:
        for head_index, temp in enumerate(head):
            sheet_train.write(num, head_index, temp, style)
        num += 1
    for index, temp in enumerate(data):
        for col_temp in range(0, col):
            try:
                sheet_train.write(index + num, col_temp, temp[col_temp], style)
            except Exception as err:
                print(err)
    writer.save(file_name)
    print('save successful')


if __name__ == '__main__':
    result = read_data(r_path, start_line=0, cols=6)
    print(len(result))