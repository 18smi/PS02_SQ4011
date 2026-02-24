def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) > 6 or len(s) < 2:# if number plate is too big or small return False
        return False
    if not s[:2].isalpha():# if the first two letters are not letters return False
        return False


    number_detected = False
    for i in s:
        if i.isalpha() == i.isdigit():# if the string contains a non-digit, non-letter charicter return False
            return False
        if number_detected and i.isalpha():# if a letter is detected after the first number return False
            return False
        if i.isdigit():
            if number_detected == False and i == '0':# if first number is a 0 return False
                return False
            number_detected = True# saves the fact that a numeber has been read 

    return True# if no fail conditions are found return True
    


main()