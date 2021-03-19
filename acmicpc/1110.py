a = b = int(input())
count= 0
while True:
    f = a // 10
    s = a % 10
    t = f + s
    count += 1
    a = int(str(a%10)+str(t%10))
    if(a == b):
        break
print(count)
    