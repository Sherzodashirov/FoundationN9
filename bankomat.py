import os
os.system ("clear")
class Bankomat:
	__balans = 200000
	__password = "3104"
	__popitka = 0
	def __init__(self):
		self.lang = input("Tilni tanlang (1.Uzbek,2.Ruscha): ")
		if self.lang == "1":
			parol = input("Parolni kiriting: ")
			Bankomat.__popitka += 1
			while Bankomat.__password != parol and Bankomat.__popitka != 3:
				print (f"Parolni noto'g'ri kritdingiz urunishlar soni: {3 - Bankomat.__popitka} ta")
				Bankomat.__popitka += 1
				parol = input("Parolni kiriting: ")
			if Bankomat.__password == parol:
				os.system ("clear")
				self.kirish()
			else:
				os.system ("clear")
				print ("Sizning kartangiz bloklandi. Karta bankomatda qoladi !!!")
		if self.lang == "2":
			print ("\n\t\t\t\tUzur hozir bizda faqat uzbek tili mavjud !!!")
	def kirish(self):
		os.system ("clear")
		print ("""Quydagilarning birini tanlang: \n
1.SMS habarnoma\t\t\t\t2.Pul o'tkazmalari\n\n
3.Balans       \t\t\t\t4.Karta parolini almashtirish\n\n
             5.Naqt pul yechish""")
		self.natija = input("Kiriting: ")
		if self.natija == "1":
			self.sms()
		if self.natija == "2":
			self.money()
		if self.natija == "3":
			self.balans()
		if self.natija == "4":
			self.parol()
		if self.natija == "5":
			self.yechish()
	def qaytish(self):
		answer = input("Hurmatli mijoz bankomatdan yana foydalanasizmi(HA,YOQ): ")
		if answer.upper() == "HA":
			self.kirish()
		else:
			os.system ("clear")
			print ("Hayr salomat boling !!!")
	def sms(self):
		os.system ("clear")
		self.function = input("SMS habarnomalari \n\n 1.Yoqish\n 2.O'chirish\n Kiriting:")
		if self.function == "1":
			self.raqam = input("Telefin raqamingizni kiriting: ")
			if self.raqam.isdigit() and len(self.raqam) == 12 and self.raqam.startswith("998"):
				print ("SMS habarnoma hizmati muvaffaqiyatli ulandi !!!")
			else:
				print ("Raqam hato kiritildi")
		else:
			self.number = input ("Telefin raqamingizni kiriting: ")
			if self.number.isdigit() and len(self.number) == 12 and self.number.startswith("998"):
				print ("SMS hizmati muvaffaqiyatli uzuldi !!!")
			else:
				print ("Raqam hato kiritildi")
		self.qaytish()
	def money(self):
		os.system ("clear")
		self.karta = input("Karta raqamini kiriting: ")
		if len(self.karta) == 16 and self.karta.isdigit():
			self.summa = int(input("\nO'tkazma summasini kiriting: "))
			if self.summa <= Bankomat.__balans:
				Bankomat.__balans -= self.summa
				print ("\nO'tkazma muvaffaqiyatli yakunlandi !!!")
				print (f"Qolgan summa: {Bankomat.__balans}")
			else:
				print ("\nbalansinggizda buncha pul miqdori yoq !!!")
		else:
			print (" Karta parolini noto'g'ri kiritdingiz!!!")
		self.qaytish()
	def balans(self):
		os.system ("clear")
		print (f"Sizning balansingizda {Bankomat.__balans} pul bor")
		self.qaytish()
	def parol(self):
		os.system ("clear")
		self.new_parol = input("Yangi parolni kiriting: ")
		if self.new_parol != Bankomat.__password:
			Bankomat.__password = self.new_parol
			print ("Parol muvaffaqiyatli almashtirildi")
		self.qaytish()
	def yechish(self):
		os.system ("clear")
		self.naqt = input("""Quyidagilardan birini tanlang:\n\n
1. 100 000 so'm\t\t\t\t2. 200 000 so'm\n\n
3. 300 000 so'm\t\t\t\t4. 400 000 so'm\n\n
\t\t\t5. Boshqa summa
Kiriting: """)
		if self.naqt == "\n":
			self.pul = int(input("Summani kiriting: "))
			if self.pul <= Bankomat.__balans:
				Bankomat.__balans -= self.pul
				print (f"Marhamat pulingizni olishingiz mumkin qolgan balans {Bankomat.__balans} so'm")
			else:
				print ("Sizda buncha mablag' yoq")
		if self.naqt == 

		self.qaytish()



bnk = Bankomat()

