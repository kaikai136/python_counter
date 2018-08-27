#!/usr/bin/python
# -*- coding:utf-8 -*-
# project : 正则计算器
# user :taihe
# Author: 冀恩开
# createtime :2018/8/24 15:06
import copy
import re
# 检验字符串是否合法
def check_exp(s):
    flag = True
    if re.findall('[a-zA-Z{}~`!@#$%&]', s):
        print('Invalid')
        flag = False
    if re.findall('\(', s).count('(') != re.findall('\)', s).count(')'):
        print('输入的括号不相等')
        flag = False
    return flag
# 将表达式进行格式化
def format_str(s):
    s = s.replace(' ','')
    s = s.replace('++','+')
    s = s.replace('--','+')
    s = s.replace('+-','-')
    s = s.replace('-+','-')
    s = s.replace('*+','*')
    s = s.replace('/+','/')
    return s
# 计算乘除法
def calc_mul_div(str1):
    reg = '[\-]?\d+\.?\d*[*/][\-]?\d+\.?\d*'
    # 匹配判断是否还存在*/
    while re.search(reg, str1):
        # 去除第一个运算的表达式
        expression = re.search(reg,str1).group()
        if expression.count('*') == 1:
            x, y = expression.split('*')
            mul_result = str(float(x) * float(y))
            # 将计算的结果与原来的字符串进行替换
            str1 = str1.replace(expression,mul_result)
            # 进行格式化
            str1 = format_str(str1)
        if expression.count('/') == 1:
            x, y = expression.split('/')
            mul_result = str(float(x) / float(y))
            str1 = str1.replace(expression, mul_result)
            str1 = format_str(str1)
    return str1
# 计算加减
def calc_add_sub(str1):
    reg = '[\-]?\d+\.?\d*[+-][\-]?\d+\.?\d*'
    while re.search(reg, str1):
        expression = re.search(reg,str1).group()
        if expression.count('+') == 1:
            x, y = expression.split('+')
            mul_result = str(float(x) + float(y))
            str1 = str1.replace(expression,mul_result)
            str1 = format_str(str1)
        # 判断开头是否有-号 是否是减法运算
        if re.match('-',expression) and expression.count('-') > 1:
            list_str = expression.split('-')
            print(list_str[0])
            if not list_str[0]:
                mul_result = str(-float(list_str[1]) - float(list_str[2]))
                print(mul_result)
                str1 = str1.replace(expression, mul_result)
                str1 = format_str(str1)
        # 开头没有-号，但是是减法运算
        elif expression.count('-') == 1 and re.match('-',expression)== None:
            x, y = expression.split('-')
            mul_result = str(float(x) - float(y))
            str1 = str1.replace(expression, mul_result)
            str1 = format_str(str1)
    return str1
# 计算幂运算
def calc_pow(str1):
    reg = '[\-]?\d+\.?\d*[\^][\-]?\d+\.?\d*'
    while re.search(reg, str1):
        expression = re.search(reg, str1).group()
        x,y = expression.split('^')
        mul_result = str(pow(float(x), float(y)))
        str1 = str1.replace(expression, mul_result)
        str1 = format_str(str1)
    return str1
# 计算逻辑入口
def main(source):
    if check_exp(source):
        source = copy.copy(source)
        # 将计算的表达式进行格式化
        result = format(source)
        # 判断是否存在括号运算
        while result.count('(')>0:
            # 取出最里面的括号进行计算
            strs = re.search('\([^()]*\)',result).group()
            # print(strs)
            replace_str = calc_pow(strs)
            # 先计算乘除
            replace_str = calc_mul_div(replace_str)
            # 在计算加键法
            replace_str = calc_add_sub(replace_str)
            # 计算结果去点括号
            result = format_str(result.replace(strs, replace_str[1:-1]))
        else:
            replace_str = calc_pow(result)
            replace_str = calc_mul_div(replace_str)
            replace_str = calc_add_sub(replace_str)
            result = format_str(result.replace(result, replace_str))
    return source + ' = ' + result

if __name__ == '__main__':
    # 数据源
    source = '2^3+12-8+(96-(5*60-(23+6^4)+(3+5*2*2))+46)'
    result = main(source)
    print(result)





