first_number = []
def get_multiplied_digits(number):

    str_number_1 = str(number)
    str_number = str_number_1.replace('0', '')
    long = int(len(str_number))
    first = int(str_number[0])

    if long == 1:
            first_number.append(first)

    else:
            first_number.append(first)
            number = str_number[1:]
            get_multiplied_digits(number)

    result = 1
    for i in  first_number:
        result = result*i

    return result

print(get_multiplied_digits(40203))


