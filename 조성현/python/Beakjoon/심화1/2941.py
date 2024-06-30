p = ['c=','c-','dz=','d-','lj','nj','s=','z=']
str = input()

for i in p:
    str = str.replace(i,'*')
print(len(str))