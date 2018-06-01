#!/usr/bin/env python
# -*- coding:utf-8 -*-
def xiugai(mudi, style='数据'):
    while 1:
        if mudi in '新建修改删除':
            account = input('请输入您想要%s谁的%s:\n' % (mudi, style))
            if mudi != '新建':
                with open( 'C:/users/administrator/files/users.txt', 'r', encoding = 'utf-8') as f:
                    line = f.readlines()
                with open( 'C:/users/administrator/files/users.txt', 'w', encoding = 'utf-8') as f:
                    for i in line:
                        if account in i:
                            # 修改
                            if mudi == '修改':
                                i = i.strip('\n')
                                b = i.split(' ')
                                if style == '名字':
                                    s = 0
                                elif style == '年龄':
                                    s = 1
                                else:
                                    s = 2
                                n = 0
                                b[s] = input('请输入您修改后的数据:\n')
                                print(b)
                                for z in b:
                                    if n == 2:
                                        f.write(z + '\n')
                                        break
                                    f.write(z + ' ')
                                    n += 1
                                continue
                            # 删除
                            else:
                                continue
                        f.write(i)
            elif mudi == '新建':
                # 新建
                with open( 'C:/users/administrator/files/users.txt', 'a', encoding = 'utf-8') as f:
                    f.write(account + '\n')
            break
        else:
            mudi = input('指令错误，请重新输入:\n')

def main()
    actionList = [ '新建', '修改', '删除', '退出' ]
    action = input('请输入您想进行的操作（新建、修改或者删除）:\n')

    while action != '退出' ：
        if action in actionList:
            if action = '新建' :
                new()
            elif action = '修改' :
                change()
            elif action = '删除' :
                delete()
    
        else:
            print( 'Error: Invaild Action' )
         action = input('请输入您想进行的操作（新建、修改或者删除）:\n')


def new()
    account = input('请输入您想要新建谁的数据')
    with open( 'C:/users/administrator/files/users.txt', 'a', encoding = 'utf-8') as f:
    f.write(account + '\n')

def change()
    account = input('请输入您想要修改谁的数据')
    style = input('请输入您想要修改的数据类型（名字、年龄或者手机号）:\n')
    with open( 'C:/users/administrator/files/users.txt', 'r', encoding = 'utf-8') as f:
        line = f.readlines()
    with open( 'C:/users/administrator/files/users.txt', 'w', encoding = 'utf-8') as f:
        for i in line:
            if account in i:
                # 修改
                i = i.strip('\n')
                b = i.split(' ')
                if style == '名字':
                    s = 0
                elif style == '年龄':
                    s = 1
                else:
                    s = 2
                n = 0
                b[s] = input('请输入您修改后的数据:\n')
                print(b)
                for z in b:
                    if n == 2:
                        f.write(z + '\n')
                        break
                    f.write(z + ' ')
                    n += 1
                continue

def delete()
    account = input('请输入您想要修改谁的数据')

