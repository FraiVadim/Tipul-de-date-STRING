c=str(input("dati cuvantul: "))
l=str(input("dati litera: "))
x=(len(c))
print(l+c[1:])
print(c[:1]+l+c[2:])
for i in range (1,x):
    while i+1!=x:
        print(c[:i+1]+l+c[2+i:x])
        break
  



