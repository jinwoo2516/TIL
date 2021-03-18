H, M = map(int, input().split())
if H >= 0 and H <= 23 and M >= 0 and M <= 59:
    if H == 0:
        if M >= 45:
            print(0, M-45)
        else:
            print(23,60+M-45)
    else:    
        if M >= 45:
            print(H, M-45)
        else:
            print(H-1,60+M-45)