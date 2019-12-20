__author__ = 'darakna'
TLD=open("TLD_suffix.txt")
TLD_words=TLD.read()
def is_valid_domain(adress):
    dpos=adress.rfind(".")
    #print(dpos,adress[dpos+1:])
    if adress[dpos+1:].upper() in TLD_words:
        return True
    else:
        return False

print(is_valid_domain("app1.prod.collab.uhi.ac.uk"))
print(is_valid_domain("v2.2.12"))
print(is_valid_domain("8.12.11.200603088.12.11Submit"))
