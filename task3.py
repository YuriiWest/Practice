import random
x = input ('\n')
x = int(x)
arr = random.sample(range(-10, 10), x)
print("our random list: ", arr)
r = arr[:]
for y in arr:
    if y<0 in arr:
        d = arr.index(y)
        del r[d]
        break

for b in r:
    if b<0 in r:
        c = r.index(b)
        del r[c]
        break
sum = arr[d:c+1]
def listsum(numList):
    theSum = 0
    for i in numList:
        theSum = theSum + i
    return theSum
print ('сумма між першими двома відємними числами = ', listsum(sum)-arr[d])

