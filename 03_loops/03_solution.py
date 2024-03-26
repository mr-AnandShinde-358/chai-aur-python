num=7;

for i in range(1,11):
    if i==5:
        continue
    # print("{}X{} = {}".format(num,i,i*num))# also work
    print(num,'X',i,'=',num*i)