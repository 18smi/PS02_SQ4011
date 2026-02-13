input_string = input("variable name\n")
output_string = ""

for i in input_string:
    if i.isupper():
        output_string += '_'
    output_string += i.lower()
print(output_string)