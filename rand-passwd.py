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
import random

dict = { 
    'a': 'jqohzxwfykvuiegdpmbscrtnl',
    'b': 'zqkgwfnvhpmjctdysuroaeil',
    'c': 'fgbwpdzmqnsylkurtiehao',
    'd': 'qzktpcjbfvhwmsgnyulroaie',
    'e': 'jzkqyhwbvfgiuxopmcatldsnr',
    'f': 'vzjkgcpdmbnhwsytralueoi',
    'g': 'vjzckpfdbtwsmyhnuolraie',
    'h': 'jqzvkgcdpsbfwmnlturyaoie',
    'i': 'yjwhqxukbefgrzpmvldaotscn',
    'j': 'kbtlpmndhryioeau',
    'k': 'zvjgcdpftbmwrhusynolaie',
    'l': 'xjqzrhwbkfgsnvcmpdtuoyaie',
    'm': 'qzjkgtvdhcrwflsnyubpoiea',
    'n': 'xqjzwhbmvlrykpfuscdoagite',
    'o': 'jqzyhkxfeawbvidgctspmlurn',
    'p': 'qvjdgkcfbwmnysutliaoreh',
    'q': 'raoeiu',
    'r': 'xzqjwfvkhlbgpndscumtyoiae',
    's': 'zjvdgrbfqwknylmpaocuheit',
    't': 'xqjkvdgzpbfnmwscluyhraoei',
    'u': 'wqjhyzxvkfogediacpbtmrlsn',
    'v': 'gdkzclnsryuoaie',
    'w': 'jvqzgcpuftmkybdslrnheoia',
    'x': 'zvkgrndqwmbflshucepoyati',
    'y': 'jqvkuzfhxwbigedoartncmspl',
    'z': 'fvpknmhgsrcwtbdulyioae'}

vowels = "aeiou"
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

for w in range(numwords):
    myword = []
    last_char = random.choice(string.ascii_lowercase)
    sout(last_char)
    for x in range(realwordlen):
        if last_char not in vowels:
            last_char = random.choice(vowels)
        else:
            last_char = random.choice(dict[last_char])
        sout(last_char)
    for x in range(padding):
        sout(str(random.randint(0,9)))
    sout("\n")
