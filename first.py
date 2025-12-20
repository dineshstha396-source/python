# print("Hello world!")
# print("This is my first code")
# sum=int(input("Enter a number "))
# print(sum)
# print(sum)
# print("Hello guys.whats up whats up")
rent={
    "food":200,
    "health care":400,
    "entertainment":300,
    "internet":30,
    "books":400,
    "travel":40,
    "insurance":30
    
}
total=0
active=True
while active:
    new_expense=input("any other expense  ")
    rent ["new expense"]=int(input("what is that price for expense  "))
    ans=input("Type N/n if you want to stop \n  ")
    ans.lower()
    if ans=="n":
        active=False
    else:
        continue


for key,value in rent.items():
    print(f"your expense tittle is: {key}")
    total+=value
    print(f"the total cost for this expense is: {value}\n")
    # ("\n")
("\n")
num=int(input("Give me the total people here\n"))
print(f"the total expense of the month is: {total}")
each=total/num
("\n")
print("so the each has to pay ", each)
        
# for key in