# 숫자 카드2
import sys
input = sys.stdin.readline
n = int(input())
cards = {}
for i in input().split():
    if int(i) in cards.keys():
        cards[int(i)]+=1
    else:
        cards[int(i)]=1
m = int(input())
targets = list(map(int,input().split()))

for target in targets:
    if target in cards.keys():
        print(cards[target], end=' ')
    else:
        print(0, end=' ')