
#filehandler = open('input_str.txt', 'r')
filehandler = open('input_strp2.txt', 'r')
text=filehandler.read()
circuit_operations = text.split("\n")

all_operations = {}

def check_if_has_value(strg):
    try:
        int(strg)
        return True
    except:
        return False


for elem in circuit_operations:
    current_elem = (elem.split(" -> "))
    all_operations[current_elem[1]] = current_elem[0]
is_done = 0
while not is_done:
    is_done = 1
    if check_if_has_value(all_operations["a"]):
        break

    for elem in all_operations:
        if not check_if_has_value(all_operations[elem]):
            if all_operations[elem].count(" ") == 0:
                if check_if_has_value(all_operations[all_operations[elem]]):
                    print("%s = %s = %s" % (elem, all_operations[elem], all_operations[all_operations[elem]]))
                    all_operations[elem] = all_operations[all_operations[elem]]
            elif all_operations[elem].count(" ") == 1:
                temp = all_operations[elem].split(" ")
                temp_operation = temp[0]
                temp_value = temp[1]
                if check_if_has_value(all_operations[temp_value]):
                    print("%s = %s = %s %s = %s" % (elem, all_operations[elem], temp_operation, all_operations[temp_value], int(all_operations[temp_value]) ^ 65535))
                    all_operations[elem] = int(all_operations[temp_value]) ^ 65535
            elif all_operations[elem].count(" ") == 2:
                temp = all_operations[elem].split(" ")
                temp_v0 = check_if_has_value(temp[0]) or check_if_has_value(all_operations[temp[0]])
                temp_v2 = check_if_has_value(temp[2]) or check_if_has_value(all_operations[temp[2]])
                if temp_v0 and temp_v2:
                    value_v0 = int(temp[0]) if check_if_has_value(temp[0]) else int(all_operations[temp[0]])
                    value_v2 = int(temp[2]) if check_if_has_value(temp[2]) else int(all_operations[temp[2]])
                    if temp[1] == "LSHIFT":
                        all_operations[elem] = value_v0 << value_v2
                        print("%s = %s %s %s = %s" % (elem, temp[0], temp[1], temp[2], all_operations[elem]))
                    elif temp[1] == "RSHIFT":
                        all_operations[elem] = value_v0 >> value_v2
                        print("%s = %s %s %s = %s" % (elem, temp[0], temp[1], temp[2], all_operations[elem]))
                    elif temp[1] == "OR":
                        all_operations[elem] = value_v0 | value_v2
                        print("%s = %s %s %s = %s" % (elem, temp[0], temp[1], temp[2], all_operations[elem]))
                    elif temp[1] == "AND":
                        all_operations[elem] = value_v0 & value_v2
                        print("%s = %s %s %s = %s" % (elem, temp[0], temp[1], temp[2], all_operations[elem]))
                    else:
                        print(temp[1])
                        exit()
            is_done = 0