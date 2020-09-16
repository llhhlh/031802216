# coding: utf-8
import os
import time
import sys

arg0=sys.argv[0]# 传的是执行的py文件名
arg1=sys.argv[1]# 传的是命令行的第一个参数
arg2=sys.argv[2]# 传的是命令行的第二个参数
arg3=sys.argv[3]# 传的是命令行的第二个参数


#读取文件代码
def readlin(filepath):
    wds = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            wds = f.readlines()
            f.close()
    except Exception:
        with open(filepath, 'r', encoding='gbk') as f:
            wds = f.readlines()
            f.close()
    return wds
#查重代码
def compare(file1, file2):
    lines1 = readlin(file1)
    lines2 = readlin(file2)

    count = 0.
    for line in lines1:
        if lines2.count(line) > 0:
            count += 1
    return count / max(len(lines1), len(lines2))

degree = compare(arg1, arg2)
ans = open(arg3,'w',encoding='utf-8')# 覆盖添加答案文件
ans.write(str("%.2f%%" % (degree * 100)))#先变成百分比，在变成str才能写入
ans.close()#使用这种方式打开,要关闭文件
