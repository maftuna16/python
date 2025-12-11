# Fan klassi
class Fan:
    def init(self, nomi):
        self.nomi = nomi

    def str(self):
        return self.nomi


# Shaxs klassi
class Shaxs:
    def init(self, ism, familiya, yosh):
        self.ism = ism
        self.familiya = familiya
        self.yosh = yosh

    def get_info(self):
        return f"{self.ism} {self.familiya}, {self.yosh} yosh"


# Talaba klassi, shaxsdan voris
class Talaba(Shaxs):
    def init(self, ism, familiya, yosh):
        super().init(ism, familiya, yosh)
        self.fanlar = []   # bo‘sh ro‘yxat

    def fanga_yozil(self, fan_obj):
        self.fanlar.append(fan_obj)
        print(f"{fan_obj} faniga yozildingiz!")

    def remove_fan(self, fan_obj):
        if fan_obj in self.fanlar:
            self.fanlar.remove(fan_obj)
            print(f"{fan_obj} fani ro‘yxatdan olib tashlandi.")
        else:
            print("Siz bu fanga yozilmagansiz")

    def get_info(self):
        fanlar = ', '.join([f.nomi for f in self.fanlar]) or "Fanlar yo‘q"
        return f"{super().get_info()} | Fanlar: {fanlar}"


#  Turli voris klasslar
class Professor(Shaxs):
    def init(self, ism, familiya, yosh, kafedra):
        super().init(ism, familiya, yosh)
        self.kafedra = kafedra

    def get_info(self):
        return f"Professor: {super().get_info()}, Kafedra: {self.kafedra}"


class Foydalanuvchi(Shaxs):
    def init(self, ism, familiya, yosh, username):
        super().init(ism, familiya, yosh)
        self.username = username

    def get_info(self):
        return f"Foydalanuvchi: {self.username} | {super().get_info()}"


# Foydalanuvchidan boshqa voris
class Admin(Foydalanuvchi):
    def init(self, ism, familiya, yosh, username):
        super().init(ism, familiya, yosh, username)

    def ban_user(self, user):
        print(f"Foydalanuvchi bloklandi: {user.username}")


# Misol uchun obyekt yaratish
fan1 = Fan("Matematika")
fan2 = Fan("Fizika")
fan3 = Fan("Ingliz tili")

talaba = Talaba("Ali", "Valiyev", 18)
talaba.fanga_yozil(fan1)
talaba.fanga_yozil(fan2)
print(talaba.get_info())

talaba.remove_fan(fan3)  # ro‘yxatda yo‘q fan
talaba.remove_fan(fan1)

# Admin bilan ishlash
admin = Admin("Aziz", "Aliyev", 30, "admin007")
fod = Foydalanuvchi("Bobur", "Valiyev", 20, "bobur21")

