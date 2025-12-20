# # col={1,2,"a",2,2,2,"hello world!"}
# # print(col)
# # print(type(col))
# #creating empty set
# # col={}#empty dic ho yo ta
# #so this is empty set
# col=set()
# col.add(1)
# col.add(2)
# col.add(22)
# col.add(222)
# col.add(2222)
# print(col)
# # col.clear()
# print(col)
# col.add(1)
# col.add(2)
# print(col)
# # col.clear()
# col.pop()
# col.pop()
# print(col)
# h={1,2,23,"python","her"}
# h.pop()
# print(h.pop())
# set1={1,2,3,4,5,6}
# set2={1,2,7,8,9}
# set3=set1.union(set2)
# set4=set1.intersection(set2)
# print(set3)
# print(set4)
# print(set1)
# print(set2)

# dic={
#     tabel:"chair, bench","tall,beautiful",

# }
table={
    "furniture":"chair,bench",
    "fact":"tall,beautiful",
    "figure":"3cm tall,5 cm long"
}
cat={
    "apperance":"four leged, two eyes",
    "color":"dark,blue,white"
}
print("\n")
for key,value in table.items():
    print(f"{key}:{value}")
print("\n")
for key,value in cat.items():
    print(f"{key}:{value}")
print("\n")


classroom={"python","java","C++","python","javascript","java","python","java","C++","C"}
print(f"The total classroom required is {len(classroom)}")

dic={

}
count=0
while count<3:
    count+=1
    sub=input("Enter the subject ")
    dic[sub]=int(input("Enter its marks  \n"))
for key,value in dic.items():
    print(f"{key}={value}\n")

set={9,"9.0"}
print(set)

