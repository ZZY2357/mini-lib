#!/usr/bin/python3

import platform
import os

import user
import book

def renderList(_list):
    for i in range(len(_list)):
        print('\t{}: {}'.format(i, _list[i]))

def printHr(msg=''):
    print(msg.center(100, '='))

def clear():
    if plf == 'Windows':
        os.system('cls')
    else:
        os.system('tput reset')
        os.system('clear')

def signIn():
    global nowUserIs
    un = input('用户名: ')
    pw = input('密码: ')
    if user.isInTheJson(un):
        for i in user.jsonOfUsers:
            if un == i['userName'] and user.sha256(pw) == i['password']:
                nowUserIs = user.User(un, user.sha256(pw))
                return True
    return False

# 创建书单
lib = book.jsonOfBooks
nowUserIs = None

plf = platform.system()

printHr('图书管理系统')

# 登录注册
while True:
    un = ''
    pw = ''
    optionOfSign = input('\t0: 注册\n \t1: 登录\n')
    if optionOfSign == '0':
        un = input('用户名: ')
        pw = input('密码: ')
        if user.isInTheJson(un) == False:
            user.newUser(un, pw)
            print('注册成功，试试登录吧！')
        else:
            print('已经被注册过啦，可以试试登录哦！')
    elif optionOfSign == '1':
        if signIn():
            print('登录成功！')
        else:
            print('登录失败')
            continue
        break
    else:
        print('不要乱输')
        continue

print('你好！要图书助手帮你做什么: ')
while True:
    message = input(''.center(108, '=') + '\n\tquit: 结束管理图书\n \t0: 展示书单\n \t1: 借书\n \t2: 还书\n \t3: 管理员菜单\n 输入选项: ')
    clear()
    book.writeData(lib)
    if message == 'quit':  # 结束管理图书
        print('再见！记得充钱哦！')
        break
    # 展示书单
    elif message == '0':
        print('执行: 展示书单')
        print('图书馆内的书: ')

        for i in range(len(lib)):
            if lib[i]['isBorrowed'] == False:
                print('\t{}: {}\t{}'.format(i, lib[i]['name'], '未被借走'))

            else:
                print('\t{}: {}\t{}'.format(i, lib[i]['name'], '已被{}借走'.format(lib[i]['isBorrowed'])))

    # 借书
    elif message == '1':
        print('执行: 借书')
        if len(lib) != 0:
            print('请问您要借哪本书呢: ')
            for i in range(len(lib)):
                if lib[i]['isBorrowed'] == False:
                    t = '未被借走'
                else:
                    t = '已被{}借走'.format(lib[i]['isBorrowed'])
                print('\t{}: {}\t{}'.format(i, lib[i]['name'], t))
            try:
                numOfTheBookToBorrow = int(input('哪一本书？输入书的编号: '))
            except:
                print('不能这么干')
                continue
            else:
                print('好的')
                try:
                    lib[numOfTheBookToBorrow]['isBorrowed'] = nowUserIs.userName
                except:
                    print('数字好像有错呢')
                    continue

        else:
            print('书被借完了呢')
            continue

    # 还书
    elif message == '2':
        print('执行: 还书')
        for i in range(len(lib)):
            if lib[i]['isBorrowed'] == nowUserIs.userName:
                print('\t{}: {}'.format(i, lib[i]['name']))
        try:
            numOfTheBookToReturn = int(input('哪一本书？输入书的编号: '))
        except:
            print('不能这么干')
            continue
        else:
            print('好的')
            lib[numOfTheBookToReturn]['isBorrowed'] = False

    elif message == '3':
        if nowUserIs.admin != True:
            print('你不是管理员哦！')
            continue
        print('执行: 管理员菜单')
        option = input('\t0: 添加图书\n \t1: 删除图书\n')
        if option == '0':
            lib.append({
                'isBorrowed': False,
                'name': input('书的名称: ')
            })
        elif option == '1':
            for i in range(len(lib)):
                print('\t{}: {}'.format(i, lib[i]['name']))
            try:
                numOfTheBookToDelete = int(input('书的编号: '))
                del lib[numOfTheBookToDelete]
            except:
                print('出错了哦！')
        else:
            print('不能这么干')
            continue
    

