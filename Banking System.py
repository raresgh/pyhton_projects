class Bank:
	def __init__(self, balance = 1.00, empty = False, name = "str", currency = "str", individual = True, account_type = "str", deposit_balance = 0, pin = 1234, final_money = 1.0, logged = False, ID = "ds",  **kwarg):
		for key, value in kwarg:
			setattr(self, key , value)
		
		
		self.balance = balance
		self.user_name = name
		self.is_empty = empty
		self.currency = currency
		self.individual = individual
		self.account_type = account_type
		self.deposit_balance = deposit_balance
		self.pin = pin
		self.final_money = final_money
		self.logged = logged
		self.ID = ID

		if self.balance > 0:
			self.is_empty = False
		else:
			self.is_empty = True

		if self.account_type == "individual person":
			self.individual = True
		else:
			self.individual = False

	def __str__(self):
		return("user{}".format(self.ID))

	def __del__(self):
		print("Account of user{} was deleted with success".format(self.ID))

	def login(self):
		print("Welcome to the bank system")
		x = int(input("Enter your PIN code:").strip())
		if x == self.pin:
			print("You're logged in")
			self.logged = True 
		else:
			print("Incorrect PIN code")
			self.logged = False


	def deposit(self):
		if self.logged:
			money_deposit = float(input("How much money do you want to deposit? ({})".format(self.currency)).strip())
			period = float(input("And for how long do you want to make the deposit?(months)").strip())
			if period <= 3:
				interest_rate = 0.01 # 1%
			elif period <= 6:
				interest_rate = 0.02 # 2%
			elif period <= 12:
				interest_rate = 0.028 # 2.8%
			elif period <= 24:
				interest_rate = 0.035 # 3.5%
			else:
				print("Invalid period of time")
				self.deposit()
			self.deposit_balance = self.deposit_balance + money_deposit
			self.final_money = money_deposit * interest_rate + money_deposit
			print("Money deposited!\n At the end of the deposit period you will have {} {}".format(round(self.final_money, 2), self.currency))
		else:
			print("Not logged on this account. Use the log in function first.")	
				
	def loan(self):
		if self.logged:
			if self.individual:
				money_loan = float(input("How much money do you want to borrow? ({})".format(self.currency)).strip())
				period2 = float(input("And for what period of time do you want this credit to be available?(keep in mind that this bank uses a fixed interest rate of 8%)").strip())
				monthly_rate = money_loan / period2 + money_loan * 0.08
				self.balance = self.balance + money_loan
				print("Loan successful, your money should be in your account\nAnd you will be paying {} {} back every month".format(round(monthly_rate,2),self.currency))
			else:
				money_loan = float(input("How much money does your organization want to borrow? ({})".format(self.currency)).strip())
				period2 = float(input("And for what period of time do you want this credit to be available?(keep in mind that this bank uses a fixed interest rate of 8%)").strip())
				if money_loan > 20000:
					guarantee = input("This is a big amount of money so you will have to guarantee with something of your own.(personal properties)\nIf you do not agree press Enter.").strip()
					if len(guarantee) > 1:
						monthly_rate = (money_loan / period2) + (money_loan * 0.08)
						self.balance = self.balance + money_loan
						print("Loan successful, your money should be in your account\nAnd you will be paying {} {} back every month".format(round(monthly_rate,2),self.currency))
					else:
						print("The loan can't be completed. Restart the program.")	
				else:
					monthly_rate = money_loan / period2 + money_loan * 0.08
					self.balance = self.balance + money_loan
					print("Loan successful, your money should be in your account\nAnd you will be paying {} {} back every month".format(round(monthly_rate,2),self.currency))	
					
		else:
			print("Not logged on this account. Use the log in function first.")	

	def break_deposit(self):
		if self.logged:
			answer1 = input("Is your deposit time finished?").strip()
			if answer1.lower() == "y" or answer1.lower() == "yes":
				self.deposit_balance = 0
				self.balance = self.balance + self.final_money
				print("Breaking the deposit was successful! Money have been transfered to the main account.")
			elif answer1.lower() == "n" or answer1.lower() == "no":
				answer2 = input("Are you sure you want to break the deposit before the deadline? The bank is going to take 7%  from the amount of money stored.").strip()
				if answer2.lower() == "y" or answer2.lower() == "yes":
					final_money2 = self.deposit_balance - (0.08 * self.deposit_balance)
					self.deposit_balance = 0
					self.balance = self.balance + final_money2
					print("Breaking the deposit was successful! Money have been transfered to the main account.")
				elif answer2.lower() == "n" or answer2.lower() == "no":
					print("Ok, it's your decision!")
				else:
					print("Invalid answer, try again!")
					
			else:
				print("Invalid answer, try again!")
				
		else:
			print("Not logged on this account. Use the log in function first.")	

	def transfer(self, user):
		if self.logged:
			if self.currency == user.currency:
				money_t = float(input("Enter the amount of money to be transfered").strip())
				if money_t > self.balance:
					print("Can't proceed the transfer, because you don't have enough money.")
				else:
					self.balance = self.balance - money_t
					user.balance = user.balance + money_t
					print("Money have been transfered!")
			else:
				print("The 2 accounts have different currencies. Apply the convert function first to have the same currency on both accounts. You have  {} and user {} has {}".format(self.currency, user.ID, user.currency))	
		else:
			print("Not logged on this account. Use the log in function first.")	

	def convert(self):
		if self.logged:
			currency2 = input("Which currency do you want this account to have? You currently have your account set on {}: ".format(self.currency)).strip()
			if self.currency == "EUR":
				if currency2 == "RON":
					self.currency = currency2
					self.balance *= 4.87
					self.deposit_balance *= 4.87
					print("Operation completed!")

				elif currency2 == "USD":
					self.currency = currency2
					self.balance *= 1.18
					self.deposit_balance *= 1.18
					print("Operation completed!")

				elif currency2 == "GBP":
					self.currency = currency2
					self.balance *= 0.89
					self.deposit_balance *= 0.89
					print("Operation completed!")

				elif currency2 == "YEN":
					self.currency = currency2
					self.balance *= 123.34
					self.deposit_balance *= 123.34
					print("Operation completed!")
				else:
					print("Invalid currency, try choosing from these \nEUR - Euro(€)\nRON - Romanian Leu(lei)\nUSD - U.S. Dollar($)\nGBP - British Pound(£)\nYEN - Japanese Yen(¥)")
					self.convert()

			elif self.currency == "RON":
				if currency2 == "EUR":
					self.currency = currency2
					self.balance *= 0.21
					self.deposit_balance *= 0.21
					print("Operation completed!")

				elif currency2 == "USD":
					self.currency = currency2
					self.balance *= 0.24
					self.deposit_balance *= 0.24
					print("Operation completed!")

				elif currency2 == "GBP":
					self.currency = currency2
					self.balance *= 0.18
					self.deposit_balance *= 0.18
					print("Operation completed!")

				elif currency2 == "YEN":
					self.currency = currency2
					self.balance *= 25.29
					self.deposit_balance *= 25.29
					print("Operation completed!")
				else:
					print("Invalid currency, try choosing from these \nEUR - Euro(€)\nRON - Romanian Leu(lei)\nUSD - U.S. Dollar($)\nGBP - British Pound(£)\nYEN - Japanese Yen(¥)")
					self.convert()

			elif self.currency == "USD":
				if currency2 == "RON":
					self.currency = currency2
					self.balance *= 4.12
					self.deposit_balance *= 4.12
					print("Operation completed!")

				elif currency2 == "EUR":
					self.currency = currency2
					self.balance *= 0.84
					self.deposit_balance *= 0.84
					print("Operation completed!")

				elif currency2 == "GBP":
					self.currency = currency2
					self.balance *= 0.75
					self.deposit_balance *= 0.75
					print("Operation completed!")

				elif currency2 == "YEN":
					self.currency = currency2
					self.balance *= 103.72
					self.deposit_balance *= 103.72
					print("Operation completed!")
				else:
					print("Invalid currency, try choosing from these \nEUR - Euro(€)\nRON - Romanian Leu(lei)\nUSD - U.S. Dollar($)\nGBP - British Pound(£)\nYEN - Japanese Yen(¥)")
					self.convert()

			elif self.currency == "YEN":
				if currency2 == "RON":
					self.currency = currency2
					self.balance *= 0.039
					self.deposit_balance *= 0.039
					print("Operation completed!")

				elif currency2 == "USD":
					self.currency = currency2
					self.balance *= 0.0096
					self.deposit_balance *= 0.0096
					print("Operation completed!")

				elif currency2 == "GBP":
					self.currency = currency2
					self.balance *= 0.0072
					self.deposit_balance *= 0.0072
					print("Operation completed!")

				elif currency2 == "EUR":
					self.currency = currency2
					self.balance *= 0.0081
					self.deposit_balance *= 0.0081
					print("Operation completed!")
				else:
					print("Invalid currency, try choosing from these \nEUR - Euro(€)\nRON - Romanian Leu(lei)\nUSD - U.S. Dollar($)\nGBP - British Pound(£)\nYEN - Japanese Yen(¥)")
					self.convert()
		
			elif self.currency == "GBP":
				if currency2 == "RON":
					self.currency = currency2
					self.balance *= 5.47
					self.deposit_balance *= 5.47
					print("Operation completed!")

				elif currency2 == "USD":
					self.currency = currency2
					self.balance *= 1.34
					self.deposit_balance *= 1.34
					print("Operation completed!")

				elif currency2 == "EUR":
					self.currency = currency2
					self.balance *= 1.12
					self.deposit_balance *= 1.12
					print("Operation completed!")

				elif currency2 == "YEN":
					self.currency = currency2
					self.balance *= 138.62
					self.deposit_balance *= 138.62
					print("Operation completed!")
				else:
					print("Invalid currency, try choosing from these \nEUR - Euro(€)\nRON - Romanian Leu(lei)\nUSD - U.S. Dollar($)\nGBP - British Pound(£)\nYEN - Japanese Yen(¥)")
					self.convert()

		else:
			print("Not logged in on this bank account, so you can't modify anything. Use the login function first.")


				
class User1(Bank):
	def __init__(self):
		data = {
		"ID": "1",
		"name": "Stefan",
		"balance":5234.2,
		"deposit_balance": 0,
		"currency": "RON",
		"account_type": "individual person",
		"pin": 6267
		}
		super().__init__(**data)

class User2(Bank):
	def __init__(self):
		data = {
		"ID": "2",
		"name": "AGR.Inc",
		"balance":5323234.2,
		"deposit_balance": 0,
		"currency": "USD",
		"account_type": "organization",
		"pin": 3532
		}
		super().__init__(**data)

class User3(Bank):
	def __init__(self):
		data = {
		"ID": "3",
		"name": "Rares",
		"balance":10000000000.23,
		"deposit_balance": 78900,
		"currency": "EUR",
		"account_type": "individual person",
		"pin": 7325
		}
		super().__init__(**data)

class User4(Bank):
	def __init__(self):
		data = {
		"ID": "4",
		"name": "Itsuki Haruto",
		"balance":47000000000000,
		"deposit_balance": 473822889,
		"currency": "YEN",
		"account_type": "individual person",
		"pin": 8032
		}
		super().__init__(**data)

class User5(Bank):
	def __init__(self):
		data = {
		"ID": "5",
		"name": "Apple",
		"balance":100000003000,
		"deposit_balance": 78000000,
		"currency": "USD",
		"account_type": "organization",
		"pin": 3732
		}
		super().__init__(**data)

class User6(Bank):
	def __init__(self):
		data = {
		"ID": "6",
		"name": "British American Tobacco",
		"balance":50000000,
		"deposit_balance": 450000,
		"currency": "GBP",
		"account_type": "organization",
		"pin": 9073
		}
		super().__init__(**data)

class User7(Bank):
	def __init__(self):
		data = {
		"ID": "7",
		"name": "Jack Williams ",
		"balance":302045,
		"deposit_balance": 20000,
		"currency": "GBP",
		"account_type": "individual person",
		"pin": 5416
		}
		super().__init__(**data)

class User8(Bank):
	def __init__(self):
		data = {
		"ID": "8",
		"name": "Antoine Roux",
		"balance":2000105.23,
		"deposit_balance": 70893,
		"currency": "EUR",
		"account_type": "individual person",
		"pin": 7816
		}
		super().__init__(**data)

class User9(Bank):
	def __init__(self):
		data = {
		"ID": "9",
		"name": "BMW",
		"balance":23900000000,
		"deposit_balance": 50000000,
		"currency": "EUR",
		"account_type": "organization",
		"pin": 6459
		}
		super().__init__(**data)

class User10(Bank):
	def __init__(self):
		data = {
		"ID": "10",
		"name": "Jeff Bezos",
		"balance":123096078063.9,
		"deposit_balance": 100000000,
		"currency": "EUR",
		"account_type": "individual person",
		"pin": 1482
		}
		super().__init__(**data)

class User11(Bank):
	def __init__(self):
		data = {
		"ID": "11",
		"name": "Honda",
		"balance":800983200324333000.463,
		"deposit_balance": 67832221,
		"currency": "YEN",
		"account_type": "organization",
		"pin": 3874
		}
		super().__init__(**data)

class User12(Bank):
	def __init__(self):
		data = {
		"ID": "12",
		"name": "Sir Andrew Norris",
		"balance":100000.23,
		"deposit_balance": 0,
		"currency": "GBP",
		"account_type": "individual person",
		"pin": 1156
		} 
		super().__init__(**data)

user1 = User1()
user2 = User2()
user3 = User3()
user4 = User4()
user5 = User5()
user6 = User6()
user7 = User7()
user8 = User8()
user9 = User9()
user10 = User10()
user11 = User11()
user12 = User12()				

users = [User1(), User2(), User3(), User4(), User5(), User6(), User7(), User8(), User9(), User10(), User11(), User12()]
for user in users:
	arguments = [user, user.user_name, user.balance, user.currency, user.account_type]
	string = "{} - name: {}, balance: {}, currency: {}, type: {}".format(*arguments)
	print(string)
