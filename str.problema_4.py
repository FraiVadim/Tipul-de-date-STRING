s1=str(input("Introduceti primul cuvant exprimat printro variabila: "))
s2=str(input("Introduceti al doilea cuvant exprimat printro variabila: " ))
s3=str(input("Introduceti al treilea cuvant exprimat printro variabila: "))
s4=str(input("Introduceti al patrulea cuvant exprimat printro variabila: "))
if len(s1)>2 and len(s2)>2 and len(s3)>2 and len(s4)>2:
    print (s1[:2]+s2[0]+s3[:3]+s4[0:((len(s4))//2)])