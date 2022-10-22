print("1st num")
a = input()
if int(a) < 0:
    print("na")
    exit()
else:
    print("1st num is  " + a)


    print("2nd num")
    b = input()
    if  int(b) < 0:
        print("na")
        exit()
    else:
        print("2nd num is   " + b)

        sub = int(a)-int(b)
        print("results are")
        print(sub)
