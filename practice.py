N = int(input("Enter the no of inputs : "))
ins = []
j = 0
sum = 0
for i in range(N):
    ins1 = int(input("Enter the number : "))
    ins.append(ins1)
maxs = max(ins)
fibb = [0,1]
while(True):
    fibb.append(fibb[j]+fibb[j+1])
    j = j + 1
    if fibb[j+1] > maxs:
        break
for i in ins:
    if i <0 :
        print("Invalid input ")
        continue
    for j in range(len(fibb)):
        if i >= fibb[j] and fibb[j]%2 == 0:
            sum = sum + fibb[j]
    print("the sum is : ",sum)
    sum = 0