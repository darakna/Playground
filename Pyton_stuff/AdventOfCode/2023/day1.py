import os
print(os.getcwd())

def calculate_number(line):
    number = 0
    for decimal in line:
        if decimal >= "0" and decimal <= "9":
            #print("Number:", decimal)
            number = int(decimal) * 10
            break
    for decimal in reversed(line):
        if decimal >= "0" and decimal <= "9":
            #print("Number:", decimal)
            number = number + int(decimal)
            break
    #print("Number: {}, Line: {}".format(number,line))
    return number

def second_calculation_number(values):
    sum = 0
    for line in values:
        breaker1 = 0
        breaker2 = 0
        number = 0
        char_numbers = "123456789"
        written_numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        for index in range(len(line)):
            if breaker1 == 1:
                breaker1 = 0
                break
            if line[index] in char_numbers:
                number = int(line[index]) * 10
                breaker1 = 1
                break
            for number_range in range(len(written_numbers)):
                if written_numbers[number_range] in line[:index+1]:
                    number = (number_range + 1) * 10
                    index = len(line)
                    breaker1 = 1
                    break
        for index in range(len(line)):
            if breaker2 == 1:
                breaker2 = 0
                break
            reverse_index = len(line)-index-1
            if line[reverse_index] in char_numbers:
                number = number + int(line[reverse_index])
                breaker2 = 1
                break
            for number_range in range(len(written_numbers)):
                if written_numbers[number_range] in line[reverse_index:]:
                    number = number + (number_range + 1)
                    index = len(line)
                    breaker2 = 1
                    break
        sum += number
        #print("Number: {}, Line: {}".format(number, line))
    print("Second sum: ",sum)
        

        
            


def first_sum (values):
    final_sum = 0
    for line in values:
        final_sum += calculate_number(line)
    #print(final_sum)

def replace_lettered_number(line):
    written_numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for index in range(len(written_numbers)):
        if written_numbers[index] in line:
            line = line.replace(written_numbers[index], str(index+1))
            #print("Line: {}, replaced: {}".format(line, written_numbers[index]))
    return line

def second_sum(values):
    final_sum = 0
    for line in values:
        #print("Initial line: ", line)
        final_sum += calculate_number(replace_lettered_number(line))
    #print(final_sum)

value_file = r"E:\Programare\Playground\Pyton_stuff\AdventOfCode\2023\input_day1.txt"

filereader = open(value_file)
values = filereader.readlines()
first_sum(values)
second_calculation_number(values)
#second_sum(values)
print(values[:5])
