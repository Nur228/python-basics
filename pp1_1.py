a = int(input())
c = 0
b = input()
for i in range (len(b)):
    if b[i].isdigit():
        c += int(b[i])
print (c)