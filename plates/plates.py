def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) > 6 or len(s) < 2:
        return False
    pos = 0
    number_detected = False
    for i in s:
        if i.isalpha() == False and pos < 2:
            return False
        if i.isalpha() == i.isdigit():
            return False
        if number_detected and i.isalpha():
            return False
        if i.isdigit():
            if number_detected == False and i == '0':
                return False
            number_detected = True
        pos += 1        

    return True
    


main()