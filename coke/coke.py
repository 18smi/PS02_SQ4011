balance = 0# stores the current balance

while balance < 50:
    print("amount due:", 50 - balance)
    input_int = int(input("input please\n"))
    if input_int == 5 or input_int == 10 or input_int == 25:# if coin is valid
        balance += input_int

print("change:", balance % 50)