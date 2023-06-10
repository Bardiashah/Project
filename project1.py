from information import *

Start = input('add or search?')
if Start == 'add':
    while Start == 'add':
        aval = input('Start?')
        if aval == 'y':
            name = input('Name:')
            family = input('Family Name: ')
            age = input('Age:')
            code = input('Code: ')
            fizik = input('Fizik: ')
            riazi = input('Riazi: ')
            tarikh = input('Tarikh: ')
            cs = input('Cs: ')
            a = Etelat(name, family, age, code)
            b = Nomre(fizik, riazi, tarikh, cs, code)
        else:
            break
else:
    code = input('Code:')
    f = open("%s" % code, "r")
    print(f.read())
    f.close()
