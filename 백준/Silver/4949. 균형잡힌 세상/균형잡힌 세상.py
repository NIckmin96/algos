# 균형잡힌 세상
import sys
input = sys.stdin.readline
while True:
    string = input().rstrip()
    if string == ".":
        break
    balanced = False
    for s in string:
        if s not in ['[',']','(',')','.']:
            string = string.replace(s,'')
    # print(string)
    while string!='.':
        new_string = string.replace('()','')
        new_string = new_string.replace('[]','')
        if new_string == string:
            break
        else:
            string = new_string
            continue
    
    if string=='.':
        print("yes")
    else:
        print("no")