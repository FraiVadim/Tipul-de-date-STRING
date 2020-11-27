cnp = str(input("dati cnp-eul: "))
for i in cnp:
    if ord(i)>47 and ord(i)<58:
        if len(cnp)==13  :
            print (True)
            break
    else:
        print (False)
        break
