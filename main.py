str = input().split()
#print(str)
for i in range(0, len(str)):
    if str[i][-1] == ":":
        print("fuck")
        print(str[i])
        for j in range(1, len(str)-i):
            if str[i+j][-1] != ":":
                print(": ", str[j])
    print(end="\n")
