uniqueNums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
temp = int(input())
N = [int(a) for a in str(temp)]

for a in N:
    if a in uniqueNums:
        uniqueNums.remove(a)

if len(uniqueNums) == 0:
    print("Impossible")
    exit()

count = 0

under = []
over = []
if len(N) == 1:
    if temp == 0:
        print(1)
        exit()
    elif temp ==9:
        print(8)
        exit()

while count < len(uniqueNums):
    if N[0] < uniqueNums[count]:
        under.append(uniqueNums[count - 1])
        over.append(uniqueNums[count])
        break
    count = count + 1

count = 1
while count < len(N):
    under.append(uniqueNums[len(uniqueNums) - 1])
    over.append(uniqueNums[0])
    count = count + 1

under = int("".join([str(a) for a in under]))
over = int("".join([str(a) for a in over]))
a = temp - under
b = over - temp
if a - b > 0:
    print(over)
elif a - b < 0:
    print(under)
else:
    print(under, over)
