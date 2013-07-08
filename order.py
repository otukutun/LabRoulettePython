#!/Users/otukutun/dev/python/default33/bin/python
# -*- coding: utf-8 -*-
from os import system
import sys
import random
import time

def say(name,num):
    system('say ' + str(name) + 'わ' +  str(num) + 'ばんです')

def main():
    argvs = sys.argv #引数を格納したリスト
    del argvs[0]
    if len(argvs) == 0:
        print('引数を指定してください。')
        sys.exit()
    for i in range(1,len(argvs) + 1):
        tmp_num = random.sample(argvs,1)
        print(str(i) + '番は' + str(tmp_num[0]) + 'です。')
        say(tmp_num[0],i)
        argvs.remove(tmp_num[0])
        time.sleep(0.3)

if __name__ == '__main__':
    main()
