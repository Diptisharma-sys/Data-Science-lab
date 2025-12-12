"""list1 = [1,2,3,4]
list2 =[]

for i in list1:
    list2.append(i)

list1.append(5)
list1.insert(1, "hello")
list1.append("hello")



print("list1:",list1)    
print("list2:",list2)

list3 = list1 + list2
print("list3:",list3)

list4=["Nepali", "song "]
list5=["another" ,"song"]

list4.append(list5)
print(list4)

nested =[list4,list5]
print(nested)

list4 = ["Nepali", "song "]
list5 = ["another", "song"]
for i in list5:
    list4.append(i)
for i in list4:
    print(i)"""

a = ["Nepali song", "English song", "Hindi song"]
b = ["Sathi ma timro", "Ladies gentle man", "bin tere"]

for i in b:
  a.append(i)
for i in a:
    print(i)

for a,b in zip(a,b):
   print(f"{a}:{b}")
   

a = ["Nepali song", "English song", "Hindi song"]
b = ["Sathi ma timro", "Ladies gentle man", "bina tera"]

for i in range(len(a)):
    print(a[i] + " : " + b[i])









