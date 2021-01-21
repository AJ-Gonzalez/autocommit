#!/usr/bin/python3
from os import system as cmd
from random import randrange
add='git add .'
with open('messages.txt') as f:
    ls=[line for line in f]
commit='git commit -m "{text}"'.format(text=ls[randrange(0,len(ls))].strip())
push='git push -u origin main'
#print(add, commit, push)
with open('reference.txt') as ref:
    lsR=[line for line in ref]
with open('reference.md','a') as docs:
    print(lsR[randrange(0,len(lsR))],file=docs)
cmd(add)
cmd(commit)
cmd(push)