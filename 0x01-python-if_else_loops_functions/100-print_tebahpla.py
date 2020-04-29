#!/usr/bin/python3
cnt = 122
while (cnt > 96 and cnt < 123):
    if cnt % 2 != 0:
        cnt -= 32
    print('{:c}'.format(cnt), end="")
    if cnt < 96 and cnt > 65:
        cnt += 32
    cnt -= 1
