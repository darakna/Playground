__author__ = 'darakna'
import itertools
def lenght_str(st):
    print("String: \n",st)
    print("Lenght: ",len(st))
    print("Number of letters: ", len(st.replace(" ","")))
    letters = ""
    working_str=st.replace(" ","")
    for letter in range(ord("A"),ord("Z")+1):
        if (chr(letter) in working_str):
            letters += chr(letter)
            working_str.replace(chr(letter),"")
    print("Unique letters in string: ", len(letters), letters)
    pseudokey = "ETAOINHSRDLUMCWFYGPBVKXJQZ"
    calckey   = "ABHSGIXYPREUZFLOTWQCJKdfmn"
    alphabet  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    #for a in range (26):



def pema(text,key):
    fileh = open("strings.txt","w")
    ll = []
    for letter in key:
        print(letter," : ",text.count(letter))
        ll.append((letter,text.count(letter)))
    print(ll)
    st = ""
    for a in sorted(ll, key=lambda letter: letter[1], reverse=True):
        st+=a[0]
    print (st)
    #for a in itertools.permutations(text,len(text)):
    #fileh.write("".join(a)+"\n")
    #print("".join(a),"\n")
    fileh.close()

def swap_letters(str,word,key):
    result = ""
    for letter in str:
        if letter in word:
            result += (key[word.index(letter)])
        else:
            result += letter
    print (result)


std = "KP BZA IGUSFZBP FHE PHO WIX RAIE BZSY UP TRSAXE S IU SUQRAYYAE JARP LAGG EHXA PHOR YHGOBSHX CAP SY AUFXWTHRTXQU BZSY GSBBGA WZIGGAXFA LIY XHB BHH ZIRE LIY SB"
word = "WZIGGAXFABSYLHERTUQPOJCK"
key = "challengetiswodrfmpyuvkb"


stc = "ABCEFGHIJKLOPQRSTUWXYZ"
#lenght_str(std)
#lenght_str(stc)
#pema(std,stc)
#lenght_str("WZIGGAXFABSYLHERTUQPOJCK")


std = "ER WTB UASIXTWR XDO RDV HUF PBUO WTIG SR MPIBFO I US ISZPBGGBO JBPR KBAA ODFB RDVP GDAVWIDF YBR IG BSXFHMDPMFZS WTIG AIWWAB HTUAABFXB KUG FDW WDD TUPO KUG IW"
word = "HTUAABFXBWKIGDPOSZRVYMJE"
key = "challengetwisordmpyukfvb"
swap_letters(std,word,key)
lenght_str(word)
lenght_str(key.upper())