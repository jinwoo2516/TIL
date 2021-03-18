import sys

t = sys.stdin.readline()
n = t.split()
for i in range(int(t)):
    a, b = map(int, sys.stdin.readline().split())
    print("Case #%d: %d + %d = %d" %(1+i, a, b, a+b))