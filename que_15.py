# Imagine you are designing a banking application. What would a
# customer look like? What attributes would s/he have? What methods
# would she have?

class Users:
    def __init__(self,account_number,account_name,account_type,__balance):
        self.account_number = account_number
        self.account_name = account_name
        self.acount_type = account_type
        self.__balance = __balance

    def dep_amount(self,amount):
        self.__balance += amount
        print("Successfully deposited ",amount ," amount to your account")
        print("Total amount= ",self.__balance)

    def withdraw_amount(self,amount):
        if amount > self.__balance:
            print("Insufficient Balance")
        else:
            self.__balance -= amount
            print(amount," has been withdrawn from the account.")
            print("Remaining amount= ",self.__balance)
            
    def show_Informations(self):
        print("Account Number =",self.account_number)
        print("Account Name =",self.account_name)
        print("Account Type =",self.acount_type)
        print("Balance =",self.__balance)




users= Users(1234,'pujan gautam','saving',30000)
users.show_Informations()
users.dep_amount(20000)
users.show_Informations()
users.withdraw_amount(10000)
users.show_Informations()