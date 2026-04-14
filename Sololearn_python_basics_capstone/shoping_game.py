# day9_if_elif_discount.py
# Practice: nested if/else, input validation

age = int(input("Enter age: "))

if age <= 18:
    student = input("Are you a student? yes/no: ").lower()
    if student == "yes":
        print("20% student discount applied")
    else:
        print("Regular price - no discount")
elif age >= 85:
    print("Senior discount: 25% off")
else:
    print("Regular price - no discount")

print("Proceeding to payment method...")

print("Select payment method: Cash(0), Online(1), Card(2)")
choose = int(input())

if choose == 0:
    print("Thanks for shopping with cash")
elif choose == 1:
    pin = input("Enter your PIN: ")  # use input() not print
    print("Online payment processing...")
elif choose == 2:
    another_m = input("Choose: credit card or debit card: ").lower()
    if another_m == 'credit card':
        print('Sorry, not available right now')
    elif another_m == 'debit card':
        print('Not enough balance')
    else:
        print('Please choose from options')
else:
    print('Please choose 0, 1, or 2')