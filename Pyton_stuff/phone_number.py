def rule_one(phone_list1):
    elems_lenght = 1
    found_elems = 0
    returned_list = []
    while(found_elems == 0):
        for elem in phone_list1:
            if len(elem) == elems_lenght:
                returned_list.append(elem)
                found_elems += 1
        elems_lenght += 1
    return returned_list

def rule_two(phone_list2):
    digit_aparition = []
    for elem in phone_list2:
        digit_numbers = 0
        for digit in range(10):
            if str(digit) in elem:
                digit_numbers += 1
        digit_aparition.append(digit_numbers)
    returned_list2 = []
    for counter in range(1, 11):
        if counter in digit_aparition:
            for a2 in range(len(phone_list2)):
                if digit_aparition[a2] == counter:
                    returned_list2.append(phone_list2[a2])
            return returned_list2

def rule_three(phone_list3):
    sorted_list = []
    for a3 in range(len(phone_list3)):
        sorted_list.append(int(phone_list3[a3]))
    return sorted(sorted_list)[0]

def solution(A):
    w1 = rule_one(A)
    w2 = rule_two(w1)
    w3 = rule_three(w2)
    return w3

initial_list = ["1233", "11111111", "1333", "34126", "3131"]
sec_rule_test = ["28388", "47477"]


print("Winner: ", solution(initial_list))
#print("Winner2: ", solution(sec_rule_test))
#trial_one = rule_one(initial_list)
#print(trial_one)
#trial_two = rule_two(initial_list)
#trial_two2 = rule_two(trial_one)
#trial_two3 = rule_two(sec_rule_test)
#print("t2", trial_two)
#print("t22", trial_two2)
#print("t222", trial_two3)
#trial_three = rule_three(initial_list)
#print(trial_three)



