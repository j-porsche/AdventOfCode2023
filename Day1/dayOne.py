import re


def delete_letters(input_string):
    # regex to find all letters
    letter_regex = re.compile('[a-zA-Z]')

    # sub function to remove all letters from the string by using the given regex
    result_string = letter_regex.sub('', input_string)

    return result_string


def delete_middlepart(input_string):
    if len(input_string) <= 2:
        input_string = input_string + input_string
        return input_string

    # Only use the first and the last character of the given string
    result_string = input_string[0] + input_string[len(input_string) - 2]

    return result_string


f = open('puzzle.txt', 'r')
lines = f.readlines()

# final result
calibration = 0

for line in lines:
    x = delete_letters(line)
    if len(x) > 2:
        y = delete_middlepart(x)
        calibration += int(y)
    else:
        # 11 * x because if x is i.e. 3 you have to add 33 and not only 3. To 33 you can either multiply by 11 or concatenate x with x
        calibration = calibration + 11 * int(x)

    print("Calibration: " + str(calibration))

print("Total calibration value = " + str(calibration))
f.close()
