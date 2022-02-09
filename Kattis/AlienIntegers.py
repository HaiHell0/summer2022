uniqueNums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
temp = str(input())
N = [int(a) for a in temp]

for a in N:
    if a in uniqueNums:
        uniqueNums.remove(a)

if len(uniqueNums) == 0:
    print("Impossible")


count = 0

under = []
over = []
while count < len(uniqueNums):
    if N[0] < uniqueNums[count]:
        under.append(uniqueNums[count - 1])
        over.append(uniqueNums[count])
        break
    else:
        under.append(uniqueNums[count - 1])
    count = count + 1

count = 1
while count < len(N):
    under.append(uniqueNums[len(uniqueNums) - 1])
    over.append(uniqueNums[0])
    count = count + 1

under = int("".join(temp))
over = int("".join(temp))
a = int(temp) - under
b = over - int(temp)
if a - b > 0:
    print(over)
elif a - b < 0:
    print(under)
else:
    print(under, over)
