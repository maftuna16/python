class Shaxs:
    odamlar_soni = 0

    def __init__(self, ism, yosh):
        self.__ism = ism
        self.__yosh = yosh
        Shaxs.odamlar_soni += 1


    def get_ism(self):
        return self.__ism

    def get_yosh(self):
        return self.__yosh


    def set_ism(self, ism):
        self.__ism = ism

    def set_yosh(self, yosh):
        if yosh > 0:
            self.__yosh = yosh
        else:
            print("Yosh musbat bo‘lishi kerak!")

    # Klass metodlari
    @classmethod
    def get_odamlar_soni(cls):
        return cls.odamlar_soni

    @classmethod
    def reset_odamlar_soni(cls):
        cls.odamlar_soni = 0




class Talaba(Shaxs):
    talabalar_soni = 0

    def __init__(self, ism, tyil, kurs):
        super().__init__(ism, tyil)
        self.__kurs = kurs
        Talaba.talabalar_soni += 1


    def get_kurs(self):
        return self.__kurs

    def set_kurs(self, kurs):
        if 1 <= kurs <= 4:
            self.__kurs = kurs
        else:
            print("Kurs 1–4 oralig‘ida bo‘lishi kerak!")

    #Klass metodlari
    @classmethod
    def get_talabalar_soni(cls):
        return cls.talabalar_soni

    @classmethod
    def reset_talabalar_soni(cls):
        cls.talabalar_soni = 0




t1 = Talaba("Ali", 20, 2)
t2 = Talaba("Olim", 19, 1)

s1 = Shaxs("Bek", 30)

print(t1.get_ism())
print(t1.get_kurs())

print(Shaxs.get_odamlar_soni())
print(Talaba.get_talabalar_soni())
