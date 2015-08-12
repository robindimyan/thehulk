#!/usr/bin/python2
import sys

greetings = '''
\033[33m	####################### \033[32mThe H.U.L.K \033[33m#######################	

\033[33m	# Creator:	\033[97mRobin DIMYANOGLU
\033[33m	# E-Mail:	\033[97mrobindimyan@gmail.com
\033[33m	# Website:	\033[97mhttp://www.robindimyanoglu.com/
\033[33m	# Github:	\033[97mhttps://github.com/robindimyan/

\033[33m	# Description:	\033[97mA tool for creating optimized Brute-Force
\033[33m			\033[97mcharsets by using the information gathered
\033[33m			\033[97mfrom analysis of large password wordlists.
\033[33m	############################################################
'''
print greetings

if len(sys.argv) != 2:
	print "\033[31m[\033[97m!\033[31m]\033[97m Usage: hulk.py <wordlist file>"
	exit(-1)

type_based_brute_string = ''
char_based_brute_string = ''

#	Character types which are allowed in creating passwords.
numbers = "0123456789"
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = " !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

#	Dictionaries which will hold the frequency values of types and characters.
type_frequencies = {'n' : 0, 'l' : 0, 'u' : 0, 's' : 0}
char_frequencies = {
'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,
'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0,
'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0,'K':0,'L':0,'M':0,'N':0,'O':0,'P':0,'Q':0,'R':0,'S':0,'T':0,'U':0,'V':0,'W':0,'X':0,'Y':0,'Z':0,
' ':0,'!':0,'"':0,'#':0,'$':0,'%':0,'&':0,'\'':0,'(':0,')':0,'*':0,'+':0,',':0,'-':0,'.':0,'/':0,':':0,';':0,'<':0,'=':0,'>':0,'?':0,'@':0,'[':0,'\\':0,']':0,'^':0,'_':0,'`':0,'{':0,'|':0,'}':0,'~':0
}

#	Attempting to read the content of our wordlist file.
try:
	with open(sys.argv[1], 'r') as f:
		wordlist = f.read()
	f.closed
except IOError as e:
	print "I/O error({0}): {1}".format(e.errno, e.strerror)
except:
	print "Unexpected error:", sys.exc_info()[0]

#	Calculating type and character frequencies of the passwords.
for password in wordlist:
	for character in password:
		if character in char_frequencies:
			char_frequencies[character] += 1
	
			if character in numbers:
				type_frequencies['n'] += 1
			elif character in lower:
				type_frequencies['l'] += 1
			elif character in upper:
				type_frequencies['u'] += 1
			elif character in symbols:
				type_frequencies['s'] += 1

#	Generation of Type Based Bruteforce String.
#	Selection sort algorithm has been used in this phase.
for i in range(0, len(type_frequencies)):
	maxim = 0;
	maxkey = ''
	for key in type_frequencies:
		if type_frequencies[key] > maxim:
			maxim = type_frequencies[key]
			maxkey = key
	if maxkey == 'n':
		type_based_brute_string += numbers
	elif maxkey == 'l':
		type_based_brute_string += lower
	elif maxkey == 'u':
		type_based_brute_string += upper
	elif maxkey == 's':
		type_based_brute_string += symbols

	del type_frequencies[maxkey]

#	Generation of Character Based Bruteforce String.
#	Selection sort algorithm has been used in this phase.
for i in range(0, len(char_frequencies)):
	maxim = 0
	maxkey = ''
	for key in char_frequencies:
		if char_frequencies[key] >= maxim:
			maxim = char_frequencies[key]
			maxkey = key

	char_based_brute_string += maxkey

	if maxkey != '':
		del char_frequencies[maxkey]

#	Printing out the Bruteforce strings.
#	You could use either of them or both simultaneously to get better results.
print "\n\033[32m[*] Generated TBBS : \033[97m%s" % (type_based_brute_string)
print "\033[32m[*] Generated CBBS : \033[97m%s" % (char_based_brute_string)
