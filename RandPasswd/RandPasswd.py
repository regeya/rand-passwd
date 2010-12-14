#!/usr/bin/env  python
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

for x in dict.keys():
    dict[x][0] = list(dict[x][0])

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

sout = sys.stdout.write
rn = 0
rand = 0
len = 0

for w in xrange(numwords):
    last_char = chars[randint(0,25)]
    sout(last_char)
    for x in xrange(realwordlen):
        len = dict[last_char][1]
        rn = 0
        rand = randint(0, len)
        last_char = dict[last_char][0][randint(rn,len)]
        sout(last_char)
    for x in xrange(padding):
        sout(str(randint(0,9)))
    print
