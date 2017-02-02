import libkeepass
 
filename = 'keepass.kdbx' # Enter name of keepass database
f = open('passwords.txt') # Enter name of password list
 
for line in f:
    line = line.strip()
    try:      
        with libkeepass.open(filename, password=line) as kdb:
            print '\n \n Password has been found. Your password is ' + `line` 
            break
    except IOError:
        print 'Trying password:  ' + `line`
