#!/Users/otukutun/dev/python/default33/bin/python
# -*- coding: utf-8 -*-
from os import system
import sys
import random
import time

def say(name,num):
    system('say ' + 'チーム' + str(num) + 'のメンバーわ' +  str(name) + 'さんです')


def main():
    members = sys.argv #引数を格納したリスト
    team_len = 3 #チーム数の指定
    del members[0]
    if len(members) == 0:
        print('引数を指定してください。')
        sys.exit()
    
    members_len = len(members)

    if team_len >= members_len:
        print('メンバーの人数が少ないので、チーム数かメンバー数を変えてください。')
        sys.exit()

    team_members_len = members_len // team_len
    
    print('チーム数' + str(team_len))
    print('メンバー数' + str(members_len))
    print('チームのメンバー数' + str(team_members_len))
    random.shuffle(members)
    h = 0 #メンバー数
    j = 1 #チーム数
    for i in members:
        h = h + 1
        print('チーム' + str(j) + 'のメンバーは' + str(i) + 'さんです')
        say(i,j)
        if h == team_members_len:
            h = 0 #チームメンバーのカウントをゼロに
            if team_len > j:
                j = j + 1 #チームの番号を増やす

if __name__ == '__main__':
        main()
