Num = int(input('Enter your loop: '))
NumMM = []
for i in range(Num):
    data = int(input('Enter Your Data:'))
    NumMM += [data]
print(NumMM)
NumMM.sort(reverse= False)
print(NumMM[0])
nvm = len(NumMM)
print(NumMM[nvm-1])