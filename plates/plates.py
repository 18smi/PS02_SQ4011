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
    for i in range(len(s)):
        if s[i].isalpha() == s[i].isdigit():# if the string contains a non-digit, non-letter charicter return False
            return False
        if number_detected and s[i].isalpha():# if a letter is detected after the first number return False
            return False
        if i.isdigit():
            if s[i] == '0':# if first number is a 0 return False
                return False
            if not s[i:].isdigit():# if there are non digits after the first return False
                return False
            return True# if the rest of the string is digits return True

    return True# if no fail conditions are found return True
    


main()