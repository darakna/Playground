__author__ = 'darakna'
string_r="1H2e3l4l5o6 7w8o9r0l1d2!"
list_string=list(string_r)
print(list_string)
for element in list_string:
    if not element.isdigit():
        print (element,end="")