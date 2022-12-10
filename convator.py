name=input("Enter your name: ")

print("hii",name,"kindely follow the instruction to convert the currency: ")
first_currency=input("Enter the fist currency name: ")
amount=float(input("Enter the amount that you want to convert: "))
second_currency=input("Enter second currency name: ")
Exhange_rate=float(input("please enter the exhange rate: "))
result=amount/Exhange_rate
R=("%.2f"%(result))
print(first_currency,"to",second_currency,"=",R,second_currency)# thid line helps to print the result
