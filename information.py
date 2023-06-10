class Etelat:
    def __init__(self, name, familyname, age, code):
        self.name = name
        self.family = familyname
        self.age = age
        self.code = code
        f = open("%s" % self.code, "w")
        f.write('Name: %s \nFamily Name: %s \nAge: %s \nCode: %s \n' % (self.name, self.family, self.age, self.code))
        f.close()


class Nomre(Etelat):
    def __init__(self, fizik, riazi, tarikh, cs, code):
        self.fizik = fizik
        self.riazi = riazi
        self.tarikh = tarikh
        self.cs = cs
        self.code = code
        f = open("%s" % (self.code), "+a")
        f.write('Fizik: %s \nRiazi: %s \nTarikh: %s \nCs: %s' % (self.fizik, self.riazi, self.tarikh, self.cs))
        f.close()
