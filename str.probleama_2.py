s=str(input("introduceti sirul de date:"))
nr=0
for i in s:
    if ((ord(i))>64) and ((ord(i))<91):
        nr+=1
print("Sunt",nr,"majuscule")
nr=0
for o in s:
    if ((ord(o))>48) and ((ord(o))<57):
        nr+=1
print("Sunt",nr,"cifre")
nr=0
for o in s:
    if ((ord(o))>32) and ((ord(o))<48):
        nr+=1
print("Sunt",nr,"caractere speciale")