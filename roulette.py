# -*- coding: utf-8 -*-
from os import system
import sys
import random
import time
#import pygame

def say(name,score):
    system('say ' + str(name) + str(score) + 'てんです')
    #commands.getoutput('say ' + str(name) + str(score) + 'てんです')

def output_score():
    return random.randint(1,10)

def main():
    argvs = sys.argv #引数を格納したリスト
    del argvs[0]
    argc = len(argvs)
    if argc == 0:
        print('引数を指定してください。')
        sys.exit()

    test = []
    for i in argvs:
        test.append({'name' : i, 'score': output_score()})
    min = {'score': 10,'name': 'a'}
    for i in test:
        print(str(i['name']) + 'さん:' + str(i['score']) + '点です。')
        say(i['name'],i['score'])
        time.sleep(0.3)
        if min['score'] > i['score']:
            min['name'] = i['name']
            min['score'] = i['score']
    
    system("afplay gaki.mp3")
    print(str(min['name']) + 'あうとーーーーーー')
    system('say ' + str(min['name']) + 'あうとーーーーーー')

if __name__ == '__main__':
    main()
