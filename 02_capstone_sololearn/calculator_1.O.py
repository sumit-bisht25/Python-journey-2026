num1 = float(input("enter first value:"))
num2 = float(input("enter second value:"))
op = input("choose operator: +,-,*,/")
if op == "+":
   print ("result: ",num1 + num2)
elif op == "-":
   print ("result: ",num1 - num2)
elif op == "*":
   print ("result: ",num1*num2)
elif op == "/":
   if num2 != 0:
     print ("result: ",num1/ num2)
   else: print("error: zero can't devide")
else:
   print ("please enter valid value!")