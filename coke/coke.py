balance = 0
while balance < 50:
    print("amount due:", 50 - balance)
    input_int = int(input("input please\n"))
    if input_int == 5 or input_int == 10 or input_int == 25:
        balance += input_int
print("change:", balance % 50)