x = input()
y = input()
if int(x) > 0 and int(y) > 0:
    print("1")
if int(x) < 0 and int(y) > 0:
    print("2")
if int(x) < 0 and int(y) < 0:
    print("3")
if int(x) > 0 and int(y) < 0:
    print("4")
