#!/usr/bin/env  python3.1
def usage():
    print ("""
RandPasswd: A generator for Sort-of-pronounceable passwords.
Version: 0.9999
License: GPL
Usage: RandPasswd [OPTION]
   -h, --help:       this message
   -l, --wordlen:    Change the length of the word (default: 8)
   -n, --numwords:   Default number of words (default: 20)
   -p, --padding:    Default number of numerical padding (default: 2)
    """)

import getopt
import sys
import string
from random import randint, choice

dict = { 
    'a': ['jqohzxwfykvuiegdpmbscrtnl', 24],
    'b': ['zqkgwfnvhpmjctdysuroaeil', 23],
    'c': ['fgbwpdzmqnsylkurtiehao', 21],
    'd': ['qzktpcjbfvhwmsgnyulroaie', 23],
    'e': ['jzkqyhwbvfgiuxopmcatldsnr', 24],
    'f': ['vzjkgcpdmbnhwsytralueoi', 22],
    'g': ['vjzckpfdbtwsmyhnuolraie', 22],
    'h': ['jqzvkgcdpsbfwmnlturyaoie', 23],
    'i': ['yjwhqxukbefgrzpmvldaotscn', 24],
    'j': ['kbtlpmndhryioeau', 15],
    'k': ['zvjgcdpftbmwrhusynolaie', 22],
    'l': ['xjqzrhwbkfgsnvcmpdtuoyaie', 24],
    'm': ['qzjkgtvdhcrwflsnyubpoiea', 23],
    'n': ['xqjzwhbmvlrykpfuscdoagite', 24],
    'o': ['jqzyhkxfeawbvidgctspmlurn', 24],
    'p': ['qvjdgkcfbwmnysutliaoreh', 22],
    'q': ['raoeiu', 5],
    'r': ['xzqjwfvkhlbgpndscumtyoiae', 24],
    's': ['zjvdgrbfqwknylmpaocuheit', 23],
    't': ['xqjkvdgzpbfnmwscluyhraoei', 24],
    'u': ['wqjhyzxvkfogediacpbtmrlsn', 24],
    'v': ['gdkzclnsryuoaie', 14],
    'w': ['jvqzgcpuftmkybdslrnheoia', 23],
    'x': ['zvkgrndqwmbflshucepoyati', 23],
    'y': ['jqvkuzfhxwbigedoartncmspl', 24],
    'z': ['fvpknmhgsrcwtbdulyioae', 21]}

wordlen = 8
numwords = 20
padding = 2

try:
    opts, args = getopt.getopt(sys.argv[1:], "l:n:h:p:",["wordlen","numwords","help","padding"])
except getopt.GetoptError as err:
    print (err)
    usage()
    sys.exit(2)
for opt, arg in opts:
    if opt in ("-h","--help"):
        usage()
        sys.exit(2)
    elif opt in ("-l","--wordlen"):
        wordlen = int(arg)
    elif opt in ("-n","--numwords"):
        numwords = int(arg)
    elif opt in ("-p","--padding"):
        padding = int(arg)

realwordlen = wordlen - padding - 1
chars = list(string.ascii_letters[:26])
last_char = ""
nl = "\n"

randomloop = ["sout(str(randint(0,9))); " for x in range(padding)] 

sout = sys.stdout.write
blah = "for x in range(int(numwords / 10)): "

innerloop = []

blah2 = "list_len = dict[last_char][1]; last_char = dict[last_char][0][randint(randint(0,list_len-1),list_len)]; "
blah2 += "sout(last_char); "

for x in range(10):
    innerloop += ["last_char = choice(chars); sout(last_char); "]
    innerloop += [blah2 for x in range(realwordlen)]
    innerloop +=  randomloop
    innerloop += ["sout(nl); "]

exec("".join(innerloop))

blah = ""

innerloop = [] 

for x in range(int(numwords % 10)):
    innerloop += ["last_char = choice(chars); sout(last_char); "]
    innerloop += [blah2 for x in range(realwordlen)]
    innerloop +=  randomloop
    innerloop += ["sout(nl); "]

exec("".join(innerloop))

#for x in range(numwords):
#    last_char = choice(chars)
#    sout(last_char);
#    exec(il)
#    sout("\n");
