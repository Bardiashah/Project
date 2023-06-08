class Etelat:
    def __init__(self,name,familyname,age,code):
        self.name = name
        self.family = familyname
        self.age = age 
        self.code = code
        f = open("%s" % (self.code),"w")
        f.write('Name: %s \nFamily Name: %s \nAge: %s \nCode: %s \n' % (self.name,self.family,self.age,self.code))
        f.close()
class Nomre(Etelat):
    def __init__(self,fizik,riazi,tarikh,cs,code):
        self.fizik = fizik
        self.riazi = riazi
        self.tarikh = tarikh
        self.cs = cs
        self.code = code
        f = open("%s" % (self.code),"+a")
        f.write('Fizik: %s \nRiazi: %s \nTarikh: %s \nCs: %s'% (self.fizik,self.riazi,self.tarikh,self.cs))
        f.close()
Start = input('add or search?')
if Start =='add':
    while Start =='add':
        aval = input ('Start?')
        if aval == 'y':
            name = input ('Name:')
            family = input ('Family Name: ')
            age = input ('Age:')
            code = input('Code: ')
            fizik = input('Fizik: ')
            riazi = input ('Riazi: ')
            tarikh = input ('Tarikh: ')
            cs = input ('Cs: ')
            a = Etelat(name,family,age,code)
            b = Nomre(fizik,riazi,tarikh,cs,code)
        else:
            break
else:
    code = int(input('Code:'))
    f = open("%s" % (code),"r")
    print(f.read())