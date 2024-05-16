print("spark mart")
print()
print()
print()
print("----"*10,"welcome to spark mart","----"*10)
print()
print()
print("Product List :")
print()
print()
#print("(1)mobile","(2)Tv","(3)lap",sep="\t\t\t\t\t")
productList={
    "(1)mobile":["redmi","vivo","iphone"],
    "(2)Tv":["lg","one+","sony"],
    "(3)lap":["hp","mac","Dell"]
    
    }
for i,j in productList.items():
    print(i, end="\t"*5)
print("\n")

pick1=input("pick one :").lower()
print("\n")
print("\n")

print("----"*10,pick1.capitalize(),"----"*10)
print("\n")
print("\n")

if pick1 =="mobile":
    for i in productList["(1)mobile"]:
        print(i,end="\t"*5)
    
elif pick1 =="tv":
    for i in productList["(2)Tv"]:
        print(i,end="\t"*5)

elif pick1 =="lap":
    for i in productList["(3)lap"]:
        print(i,end="\t"*5)

print()


#2madule
#for i in productList["(1)mobile"]:
#    print(i)
brands={
    
     "Redmi":{"brand":"redmi","model":"10","ram":"8","price":200000},
     "Vivo":{"brand":"vivo","model":"12","ram":"8","price":31000},
     "Iphone":{"brand":"iphone","model":"14","ram":"2","price":60000},


     
     "Lg":{"brand":"lg","model":"led","price":60000},
     "One+":{"brand":"one+","model":"lcd","price":75000},
     "Sony":{"brand":"sony","model":"hd","price":65000},



     
     "Hp":{"brand":"hp","model":"","ram":"8","price":30000},
     "Mac":{"brand":"mac","model":"","ram":"2","price":80000},
     "Dell":{"brand":"Dell","model":"","ram":"16","price":37000}
    }
print()
print()
pick2=input("pick one :").lower()
print()

print("----"*3,pick2.capitalize(),"----"*3)
print()


if pick2 =="Redmi":
    for i,j in brands["Redmi"].items():
        if i=="price":
            print("-------"*3)
            print(i,":",j)
            print("-------"*3)
        else:
             print(i,":",j)
       
        
elif pick2 =="Vivo":
    for i,j in brands["Vivo"].items():
        if i=="price":
            print("-------"*3)
            print(i,":",j)
            print("-------"*3)
        else:
             print(i,":",j)


elif pick2 =="Iphone":
     for i,j in brands["Iphone"].items():
         if i=="price":
            print("-------"*3)
            print(i,":",j)
            print("-------"*3)
         else:
             print(i,":",j)


             

if pick2 =="Lg":
    for i,j in brands["Lg"].items():
        if i=="price":
            print("-------"*3)
            print(i,":",j)
            print("-------"*3)
        else:
             print(i,":",j)

if pick2 =="One+":
    for i,j in brands["one+"].items():
        if i=="price":
            print("-------"*3)
            print(i,":",j)
            print("-------"*3)
        else:
             print(i,":",j)
       
if pick2 =="Sony":
    for i,j in brands["sony"].items():
        if i=="price":
            print("-------"*3)
            print(i,":",j)
            print("-------"*3)
        else:
             print(i,":",j)



             

if pick2 =="Hp":
    for i,j in brands["hp"].items():
        if i=="price":
            print("-------"*3)
            print(i,":",j)
            print("-------"*3)
        else:
             print(i,":",j)

if pick2 =="Mac":
    for i,j in brands["mac"].items():
        if i=="price":
            print("-------"*3)
            print(i,":",j)
            print("-------"*3)
        else:
             print(i,":",j)


if pick2 =="Dell":
    for i,j in brands["dell"].items():
        if i=="price":
            print("-------"*3)
            print(i,":",j)
            print("-------"*3)
        else:
             print(i,":",j) 
              

print()
#module3
print("Buy now","close",sep="\t"*15)
print()
pick3=input("pick one :").lower()
print()
if pick3=="buy now" or "buynow":
    name=input("Full name \t:")
    mob=int(input("mobile number \t:"))
    add= input("Address \t:")
    qua=int(input("Quantity \t:"))

    productD= brands[pick2.capitalize()]["brand"]+brands[pick2.capitalize()]["model"]
    final_price=brands[pick2.capitalize()]["price"]*qua
    
    print("--------"*10,"Bill","---------"*10)
    print("Name","mobile number","Address","product Details","Quantity","Total Price",sep="\t"*2)
    print()
    print()
    print(name,mob,add,productD,qua,final_price,sep="\t"*2)
    print()
    print()
    print("--------"*10,"Thank You","---------"*8)
else:
    print("--------"*10,"Thank You","---------"*8)
   
    exit()


'''print("----"*3,pick3.capitalize(),"----"*3)'''





