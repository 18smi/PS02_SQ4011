input_string = input("variable name\n")
output_string = ""# empty string to write to

for i in input_string:# loops over input string and adds a makes it camel case
    if i.isupper():
        output_string += '_'
    output_string += i.lower()
print(output_string)