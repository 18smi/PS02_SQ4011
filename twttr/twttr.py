input_string = input("input please\n")
output_string = ""

for i in input_string:
    if i.lower() != 'a' and i.lower() != 'e' and i.lower() != 'i' and i.lower() != 'o' and i.lower() != 'u':
        output_string += i
print(output_string)