from nltk.corpus import words
import sys

words_used =["BLIGHT", "SLAYER","FROZEN","MINUET","PICKET","WICKET"]
bigword =""
for f in words_used:
    bigword+=f
    print(bigword)
bad = "".join(sorted(set(sorted(bigword))))
print("Short bad list:", bad)
good=""
for elem in range(65,91):
    if chr(elem) not in bigword:
        good+=chr(elem)
print("Short good list:", good)
good=good.lower()
bad=bad.lower()
print("Short bad list:", bad)
print("Short good list:", good)
root="*I**ET"
print("All words:", len(words.words()))
newlist=[]
shortlist = []
for elem in words.words():
    if len(elem)==6:
        shortlist.append(elem.lower())
print("Short words:", len(shortlist))    
ranking = [[],[],[],[],[],[]]    
for elem in shortlist:
    good_tmp = good
    if elem[4:6]=='et' and elem[1]=='i' and elem[0] not in bad and elem[2] not in bad and elem[3] not in bad:
        newlist.append(elem)
    
for elem in shortlist:
    good_tmp = good
    if elem == 'dodded':
        pass
    rating = 0
    for letter in elem:
        if letter in good_tmp:
            rating+=1
            good_tmp = good_tmp.replace(letter,"")
    if rating > 3:
        pass
    ranking[rating].append(elem)

print(len(newlist),newlist)
for index in range(6):
    print(len(ranking[index]))
    if index > 1:
        print(ranking[index])

long_list = []
for elem1 in good:
    for elem2 in good:
        for elem3 in good:
            current_word = elem1 + "i" + elem2 + elem3 + "et"
            long_list.append(current_word)
print(long_list)