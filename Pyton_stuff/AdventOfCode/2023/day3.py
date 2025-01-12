value_file = r"E:\Programare\Playground\Pyton_stuff\AdventOfCode\2023\input_day3.txt"
filereader = open(value_file)
values = filereader.readlines()
#print(values)

def clean_symbols(original_string, chars_to_replace, replacement_char):
    # Replace all occurrences of chars_to_replace with replacement_char
    modified_string = ''.join(
        replacement_char if ch in chars_to_replace else ch
        for ch in original_string
    )
    return modified_string

def is_signed(number, new_symbols):
    max_len = len(new_symbols[0])-1
    check_matrix = []
    #in fata
    if number[1][1] > 0:
        check_matrix.append([number[1][0],number[1][1]-1])
    #in spate
    if number[2][1] < max_len:
        check_matrix.append([number[1][0],number[2][1]+1])
    #sus
    if number[1][0] > 0:
        check_matrix.append([number[1][0]-1,number[1][1]])
        if number[0] > 9:
            check_matrix.append([number[1][0]-1,number[1][1]+1])
        if number[0]>99:
            check_matrix.append([number[1][0]-1,number[1][1]+2])
    #sus in fata
    if number[1][0] > 0 and number[1][1] > 0:
        check_matrix.append([number[1][0]-1,number[1][1]-1])
    #sus in spate
    if number[1][0] >  0 and number[2][1] < max_len:
        check_matrix.append([number[1][0]-1,number[2][1]+1])
    #jos
    if number[1][0] < max_len:
        check_matrix.append([number[1][0]+1,number[1][1]])
        if number[0] > 9:
            check_matrix.append([number[1][0]+1,number[1][1]+1])
        if number[0]>99:
            check_matrix.append([number[1][0]+1,number[1][1]+2])
    #jos in fata
    if number[1][0] < max_len and number[1][1] > 0:
        check_matrix.append([number[1][0]+1,number[1][1]-1])
    #jos in spate
    if number[1][0] < max_len and number[2][1] < max_len:
        check_matrix.append([number[1][0]+1,number[2][1]+1])
    signed_is_true = False
    for elem in check_matrix:
        if new_symbols[elem[0]][elem[1]] == '*':
            signed_is_true = True
    #signed_is_true = any(new_symbols[neighbour_sign[0]][neighbour_sign[1]]=="*" for neighbour_sign in check_matrix)
    return signed_is_true

new_symbols = []
adjacent_symbols = "+=%-#@/&$"
for line in values:
    #print("Original String:", line)
    replaced_line = clean_symbols(line, adjacent_symbols, "*")[:-1]
    new_symbols.append(replaced_line)
    #print("Modified String:", replaced_line)

#print(new_symbols)
number = 0
numbers=[]
number_start = [0,0]
number_end = [0,0]
for line_index in range(len(new_symbols)):
    for char_index in range(len(new_symbols[line_index])):
        if new_symbols[line_index][char_index] in ".*":
            #continue
            #print(line_index,char_index, new_symbols[line_index][char_index])
            if number != 0:
                numbers.append([number,number_start,number_end])
            number = 0
        else:
            if number == 0:
                number_start = [line_index, char_index]
            number=number*10 + int(new_symbols[line_index][char_index])
            #print(line_index,char_index, number, number_start,number_end)
        number_end = [line_index, char_index]
        #if number == 357:
            #print(number)
if number!=0:
    numbers.append([number,number_start,number_end])
final_sum = 0
for number in numbers:
    #print(number[0], number)
    sign_value = is_signed(number, new_symbols)
    if sign_value:
        final_sum += number[0]
        #print(number, "Signed")
    else:
        #print(number, "Unigned")
        pass
    if number[0] == 222:
        print(number, sign_value)
print(final_sum)
