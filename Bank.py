from datetime import datetime
class ATM:
	transactions=[]                         #list to store transaction History
	def __init__(self,balance=0):           #constructor 
		self.balance=balance
		self.pin="2005"						#pin number
		print("Card Inserted")              #message when object created
	def pinCheck(self,Enteredpin):          #function to check pin number
		return self.pin==Enteredpin
 
	def deposit(self,amount,time):			#function to deposit amount			
		self.balance+=amount
		return f"Deposited amount ${amount} :{time}"

	def withdraw(self,amount,time):			#function to withdraw amount
		if(amount> self.balance):			#condition to check insufficient balance
			return "Insufficient Balance"	
		else:
			self.balance-=amount									
			self.transactions.append(f"Withdrawn :${amount}  :{time}")
		return f"Withdrawn :${amount}"
	
	def change_pin(self,oldPin,newPin,time):		#function to change pin number
		if self.pinCheck(oldPin):
			self.pin=newPin
			self.transactions.append(f"Pin Changed Succesfully   :{time}") 
			return "Pin Changed Succesfully"
		else:
			return "Incorrect , Check Pin Number"

	def balance_inquiry(self,time):							#function to show balance
		self.transactions.append(f"Balance Inquiry  :{time}")		
		return f"Balance Amount ${self.balance}"

	def transaction_history(self):				#function to show transaction history
		return self.transactions


atm = ATM(2000) 			#Object creation 
print("Welcome To ATM ")
while(True):			#loop starts
	now=datetime.now()
	current_time=now.strftime("%H:%M:%S")		#used to show time
	print("\n1. Check Balance")
	print("\n2. Deposit ")
	print("\n3. Withdraw ")
	print("\n4. Change PIN")
	print("\n5. Transaction History")
	print("\n6. Exit")

	#choose the mode user want like switch case
	mode=input("Enter Your mode :")		
	if mode=="1":
		enterPin=input("Enter Pin Number :")
		if atm.pinCheck(enterPin):
			print(atm.balance_inquiry(current_time))
		else:
			print("Incorrect Check Pin Number")
	elif mode=="2":
		enterPin=input("Enter Pin Number :")
		if atm.pinCheck(enterPin):
			amount=int(input("Enter amount :"))
			print(atm.deposit(amount,current_time))
		else:
			print("Incorrect Check Pin Number")

	elif mode=="3":
		enterPin=input("Enter Pin Number :")
		if atm.pinCheck(enterPin):
			amount=int(input("Enter amount :"))
			print(atm.withdraw(amount,current_time))
		else:
			print("Incorrect Check Pin Number")

	elif mode=="4":
		enterPin=input("Enter Pin Number :")
		if atm.pinCheck(enterPin):
			new_pin=input("Enter new pin :")
			print(atm.change_pin(enterPin,new_pin,current_time)) 
		else:
			print("Incorrect Check Pin Number")

	elif mode=="5":
		enterPin=input("Enter Pin Number :")
		if atm.pinCheck(enterPin):
			print(atm.transaction_history())
		else:
			print("Incorrect Check Pin Number")

	elif mode=="6":
		print("Thank You !...")
		break
	else:
		print("Invalid Choice Please Choose Correct Mode")
	
	#Thank You !...