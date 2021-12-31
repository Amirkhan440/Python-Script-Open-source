#coding=utf-8
#!/usr/bin/python2
#This Script Write By Tech Baba
#Public Script free
'''
app apne comamnd me Password laga na chate hai to yah script app :)
log use kar sate ho Aur Apne script me password laga sakte hai :)
Aur jinko sikhna hai oh sikh sakte hai python ki coding simple hai :)
''' #This multi line comment
import os 
import time
import base64
logo_base = 'G1swOzk3bQkkJCQkJCQkJCAgJCQkJCQkJCQgICQkICAgICAkJAoJJCQgICAgICQkICQkICAgICAkJCAgJCQgICAkJAoJJCQgICAgICQkICQkICAgICAkJCAgICQkICQkCgkkJCQkJCQkJCAgJCQgICAgICQkICAgICQkJAoJJCQgICAkJCAgICQkICAgICAkJCAgICQkICQkCgkkJCAgICAkJCAgJCQgICAgICQkICAkJCAgICQkCgkkJCAgICAgJCQgJCQkJCQkJCQgICQkICAgICAkJAotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQogfHwgG1swOzk3bRtbMDs0MW0gUHJvZ3JhbW1pbmcgaXMgdGhpbmtpbmcgbm90IHR5cGluZyA6KSAbWzBtIHx8Ci0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tChtbMDs5N20g4p6kIEF1dGhvciAgOiBZZXN3YW50IE1pc2hyYQobWzA7OTdtIOKepCBWZXJzaW9uIDogMy4wChtbMDs5N20g4p6kIGZiLXBhZ2UgOiBodHRwczovL2ZiLmNvbS9UZWNobmljYWwuTWlzaHJhCi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0t'
logo = base64.b64decode(logo_base) # logo with base64 encodeing :)
# You can change logo And input your our logo
password = "baba" # Tool Password You can change tool password
def menu(): 
    os.system("clear")
    print logo
    print("||• Input Tool password for login •||").center(50)
    print 47*("-")
    print""
    xox = raw_input("\033[1;97m➤ Password : \033[1;92m ")
    if password in xox: #Password Corect :)
        print""
        print("\033[1;92m\t   Login Sucessfull :)\033[1;97m")
        #Call Your Other Class()
    else: #Password Incorect and invalid :(
        print""
        print""
        print("\033[1;91m \t   Sorry Incorect Password \033[1;97m")
        time.sleep(1)
        menu() #return same
if __name__ == '__main__':
	menu()
