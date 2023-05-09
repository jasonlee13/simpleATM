class Accounts:
    def __init__(self):
        self.info = {}
    
    def addUser(self, name, card_number, accounts_and_balances, pin):
        """
        name = type(str)
        card_number = type(int)
        accounts_and_balances = type(dic) --> (int, int)
        """
        self.info[card_number] = {}
        if type(name) != str:
            return "Please enter a name with alphabetical characters."
        else:
            self.info[card_number]["Name"] = name

        self.info[card_number]["Pin"] = pin
        self.info[card_number]["Accounts"] = {}

        for account_number in accounts_and_balances.keys():
            self.info[card_number]["Accounts"][account_number] = accounts_and_balances[account_number]

    def pin_check(self, card_number, pin):
        if card_number in self.info and self.info[card_number]["Pin"] == pin:
            return True
        else:
            return False
        
    def change_amount(self, card_number, account_number, new_balance):
        self.info[card_number]["Accounts"][account_number] = new_balance
    
    def getATM(self, card_number):
        return self.info[card_number]

class ATM:
    def __init__(self, Accounts, cash):
        self.Accounts = Accounts
        self.cash = cash
        self.accounts = None
        self.swiped = False
    
    def insert(self, card_number, pin):
        if self.Accounts.pin_check(card_number, pin):
            self.accounts = self.Accounts.getATM(card_number)["Accounts"]
            self.swiped = True
            return "Hello, " + f'{self.Accounts.getATM(card_number)["Name"]}' "! " + "Here are your accounts:"
        else:
            return "Invalid Pin"
    
    def getBalance(self, account):
        if self.swiped:
            if account not in self.accounts:
                return "You do not have the entered account"
            else:
                return self.accounts[account]
        else:
            return "Please insert card."
    
    def addMoney(self, card_number, account, money):
        if self.swiped:
            new_balance = self.accounts[account] + money
            self.Accounts.change_amount(card_number, account, new_balance)
            self.cash += money
            return self.accounts[account]
        else:
            return "Please insert card."

    def takeMoney(self, card_number, account, money):
        if self.swiped:
            new_balance = self.accounts[account] - money
            if new_balance < 0:
                return "Not enough money in your balance"
            elif money > self.cash:
                return "Not enough money in the ATM"
            else:
                self.Accounts.change_amount(card_number, account, new_balance)
                self.cash -= money
                return self.accounts[account]
        else:
            return "Please insert card."

    def getAccounts(self, card_number):
        if self.swiped:
            return self.accounts[card_number]["Accounts"]
        else:
            return "Please insert card."
        
    def closeAccount(self):
        self.swiped = False
        return "Thank you for using our ATM today"


if __name__ == "__main__":
    ### Run a simulation - Uncomment code ###
    # print("Welcome to Jason's Bank.")
    # print("Please enter the following information, and we will get you all set up.")

    # temp = input("First, please enter your first name: ")
    # while not temp.isalpha():
    #     print("Please enter your name in alphabetical characters.")
    #     temp = input("First, please enter your first name: ")
    # name = temp

    # temp = input("Please enter your card number: ")
    # while not temp.isnumeric():
    #     print("Please enter your name in numbers.")
    #     temp = input("Please enter your card number: ")
    # card_number = temp

    # temp = input("Please enter a four digit pin: ")
    # while len(temp) != 4:
    #     print("Please enter four digits.")
    #     temp = input("Please enter a four digit pin: ")
    # pin = temp

    # account = {}
    # temp = input("Please enter your account number: ")
    # while not temp.isnumeric():
    #     print("Please enter your account number in numbers.")
    #     temp = input("Please enter your account number: ")
    # account[temp] = 0

    # temp = input("Do you have any more accounts? Enter [Y] for Yes and [N] for No: ")
    # while temp != "Y" and temp != "N":
    #     temp = input("Please enter [Y] for Yes and [N] for No: ")
    # while temp != "N":
    #     temp = input("Please enter your account number: ")
    #     while not temp.isnumeric():
    #         print("Please enter your account number in numbers.")
    #         temp = input("Please enter your account number: ")
    #     if temp in account:
    #         temp = input("That account is already in our system. Please enter a new account number: ")
    #     account[temp] = 0
    #     temp = input("Do you have any more accounts? Enter [Y] for Yes and [N] for No: ")
    #     while temp != "Y" and temp != "N":
    #         temp = input("Please enter [Y] for Yes and [N] for No: ")

    # print("Processing your information.")
    # print("Processing your information.")
    # print("Processing your information.")
    # print("Processing your information.")

    # newAccounts = Accounts()
    # newATM = ATM(newAccounts, 1000000)
    # newAccounts.addUser(name, card_number, account, int(pin))

    # temp = input("All set up. Please insert your card by entering your card number: ")
    # while temp not in newAccounts.info:
    #     print("You have entered a wrong card number.")
    #     temp = input("Please re-enter your card number: ")
    # card_number = temp

    # temp = input("Please enter your pin: ")
    # while newATM.insert(card_number, int(temp)) == "Invalid Pin":
    #     print("You have entered a wrong pin number.")
    #     temp = input("Please re-enter your pin number: ")
    # pin = temp
    # newATM.insert(card_number, pin)

    # print("What would you like to do today?")

    # temp = input("Please enter Deposit, Withdraw, Check Balance, or Exit: ")
    # while temp != "Deposit" and temp != "Withdraw" and temp != "Check Balance" and temp != "Exit":
    #     temp = input("Please enter Deposit, Withdraw, Check Balance, or Exit: ")

    # if temp == "Deposit":
    #     temp = input("Choose the account you would like to deposit in: ")
    #     while temp not in account:
    #         print("Cannot find that account.")
    #         temp = input("Choose the account you would like to deposit in: ")
    #     account_number = temp
    #     amount = input("Please enter how much would you like to deposit: ")
    #     while int(amount) < 1:
    #         print("Please enter a value greater than 0.")
    #         amount = input("Please enter how much would you like to deposit: ")
    #     print("Success! Your new balance is: $" + str(newATM.addMoney(card_number, account_number, int(amount))))
    #     print("Thank you, " + newAccounts.info[card_number]["Name"] + ", for using our ATM today.")

    # if temp == "Withdraw":
    #     print("Congratulations! As you're just starting your account, we filled your account(s) with $100")
    #     for i in account:
    #         newATM.addMoney(card_number, i, 100)
    #     temp = input("Choose the account you would like to withdraw from: ")
    #     while temp not in account:
    #         print("Cannot find that account.")
    #         temp = input("Choose the account you would like to withdraw: ")
    #     account_number = temp
    #     amount = input("Please enter how much would you like to withdraw: ")
    #     while int(amount) < 1:
    #         print("Please enter a value greater than 0.")
    #         amount = input("Please enter how much would you like to withdraw: ")
        
    #     while int(amount) > newAccounts.info[card_number]["Accounts"][account_number]:
    #         print("You do not have enough money in your balance.")
    #         amount = input("Please enter how much would you like to withdraw or exit by pressing ctrl-c: ")
    #         while int(amount) < 1:
    #             print("Please enter a value greater than 0.")
    #             amount = input("Please enter how much would you like to withdraw: ")
            
    #     while int(amount) > newATM.cash:
    #         print("There is not enough money in the ATM.")
    #         amount = input("Please enter a smaller amount or exit by pressing ctrl-c: ")
    #         while int(amount) < 1:
    #             print("Please enter a value greater than 0.")
    #             amount = input("Please enter how much would you like to withdraw: ")

    #     print("Success! Your new balance is: $" + str(newATM.takeMoney(card_number, account_number, int(amount))))
    #     print("Thank you, " + newAccounts.info[card_number]["Name"] + ", for using our ATM today.")
    
    # if temp == "Check Balance":
    #     for i in newAccounts.info[card_number]["Accounts"]:
    #         print("Your account " + str(i) + " has $" + str(newAccounts.info[card_number]["Accounts"][i]) + ".")
    #     print("Thank you, " + newAccounts.info[card_number]["Name"] + ", for using our ATM today.")

    # if temp == "Exit":
    #     print("Thank you, " + newAccounts.info[card_number]["Name"] + ", for using our ATM today!")



    import unittest

    class TestATM(unittest.TestCase):

        def test_addAccount(self):
            # Test Case: User adds account with incorrect name
            name = 189
            card_number = 12345
            accounts_and_balances = {1: 100, 2: 0}
            pin = 123
            newAccounts = Accounts()
            newATM = ATM(newAccounts, 0)
            newAccounts.addUser(name, card_number, accounts_and_balances, pin)
            self.assertEqual(newAccounts.addUser(name, card_number, accounts_and_balances, pin), 'Please enter a name with alphabetical characters.', "Test Case Failed")

        def test_Pin(self):
            # Test Case: User enters wrong pin
            name = "Jason"
            card_number = 12345
            accounts_and_balances = {1: 100, 2: 0}
            pin = 123
            newAccounts = Accounts()
            newATM = ATM(newAccounts, 0)
            newAccounts.addUser(name, card_number, accounts_and_balances, pin)

            # Test Case: User correctly enters pin
            self.assertEqual(newATM.insert(card_number, 123), "Hello, " + f'{name}' + "! " + "Here are your accounts:", "Test Case Failed")
            
            # Test Case: User incorrectly enters pin
            self.assertEqual(newATM.insert(card_number, 1234), "Invalid Pin", "Test Case Failed")

        def test_checkAccount(self):
            name = "Jason"
            card_number = 12345
            accounts_and_balances = {1: 100, 2: 0}
            pin = 123
            newAccounts = Accounts()
            newATM = ATM(newAccounts, 0)
            newAccounts.addUser(name, card_number, accounts_and_balances, pin)

            # Test Case: User checks account before inserting card
            self.assertEqual(newATM.getBalance(1), "Please insert card.", "Test Case Failed")

            # Test Case: User enters wrong account
            newATM.insert(card_number, pin)
            self.assertEqual(newATM.getBalance(3), "You do not have the entered account", "Test Case Failed")

            # Test Case: User successfully obtains balance
            newATM.insert(card_number, pin)
            self.assertEqual(newATM.getBalance(1), 100, "Test Case Failed")

        def test_Withdrawal(self):
            name = "Jason"
            card_number = 12345
            accounts_and_balances = {1: 100, 2: 0}
            pin = 123
            newAccounts = Accounts()
            newATM = ATM(newAccounts, 50)
            newAccounts.addUser(name, card_number, accounts_and_balances, pin)

            # Test Case: User adds money before inserting card
            self.assertEqual(newATM.takeMoney(card_number, 1, 49), "Please insert card.", "Test Case Failed")

            newATM.insert(card_number, pin)

            # Test Case: User withdraws successfully
            self.assertEqual(newATM.takeMoney(card_number, 1, 49), 51, "Test Case Failed")
            self.assertEqual(newATM.getBalance(1), 51, "Test Case Failed")

            # Test Case: User withdraws more than they have
            self.assertEqual(newATM.takeMoney(card_number, 1, 101), "Not enough money in your balance", "Test Case Failed")

            # Test Case: User withdraws more than the ATM has
            self.assertEqual(newATM.takeMoney(card_number, 1, 51), "Not enough money in the ATM", "Test Case Failed")

            # Test Case: ATM has correct cash bin
            newATM.takeMoney(card_number, 1, 49)
            self.assertEqual(newATM.cash, 1, "Test Case Failed")

        def test_Deposit(self):
            name = "Jason"
            card_number = 12345
            accounts_and_balances = {1: 100, 2: 0}
            pin = 123
            newAccounts = Accounts()
            newATM = ATM(newAccounts, 50)
            newAccounts.addUser(name, card_number, accounts_and_balances, pin)

            # Test Case: User adds money before inserting card
            self.assertEqual(newATM.addMoney(card_number, 1, 50), "Please insert card.", "Test Case Failed")

            newATM.insert(card_number, pin)

            # Test Case: User adds money successfully
            self.assertEqual(newATM.addMoney(card_number, 1, 50), 150, "Test Case Failed")
            self.assertEqual(newATM.getBalance(1), 150, "Test Case Failed")

            # Test Case: ATM has correct cash bin
            newATM.addMoney(card_number, 1, 50)
            self.assertEqual(newATM.cash, 150, "Test Case Failed")

    
    unittest.main()