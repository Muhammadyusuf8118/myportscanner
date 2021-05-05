
#!/usr/bin/python

from socket import *
import optparse
from threading import *
from termcolor import colored

def Scan(tgtHost, tgtPort):
	try:
		sock = socket(AF_INET, SOCK_STREAM)
		sock.connect((tgtHost, tgtPort))
		print(colored('[*] ' + str(tgtPort) + " /tcp porti ochiq!  ", 'green'))
	except:
		print(colored('[*] ' + str(tgtPort) + " /tcp porti yopiq!  ", 'red'))

	finally:
		sock.close()

def portscaner(tgtHost, tgtPorts):
	try:
		tgtIP = gethostbyname(tgtHost)
	except:
		print(colored('[*]' + tgtHost + '.ning ip adresi topilmadi! ', 'red'))
	try:
		tgtName = gethostbyaddr(tgtIP)
		print(colored('[*]' + tgtName[0] + ' uchun Scaner Natijalari: ', 'yellow'))
	except:
		print(colored('[*]' + tgtIP + ' uchun Scaner Naijalari: ', 'yellow'))
	setdefaulttimeout(1)
	for tgtPort in tgtPorts:
		t = Thread(target = Scan, args= (tgtHost, int(tgtPort)) )
		t.start()



def main():

	parser = optparse.OptionParser("Programmadan foydalanish texnikasi:-->"+ "--H <Nishon IP> --p <Nishon Porti>")
	parser.add_option('--H', dest='tgtHost', type ='string', help='IP addresni aniqlashtiring')
	parser.add_option('--p', dest='tgtPort', type ='string', help='Nishon portini aniqlashtiring')
	(options, args) = parser.parse_args()
	tgtHost = options.tgtHost
	tgtPorts = str(options.tgtPort).split(',')
	if (tgtHost ==None) | (tgtPorts[0] == None):
		print(parser.usage)
		exit()
	else:
		portscaner(tgtHost, tgtPorts)

if __name__=='__main__': 
	main()
