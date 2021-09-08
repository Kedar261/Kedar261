class Bank:
    bank_name = 'SBI'
    IFSC = 'SBI0001'
    branch = 'Pune'
    birthyear = int(input('Enter your Birth year in format yyyy'))
    todayyear = int(input('Enter the current year in format yyyy'))
    minimumAge = todayyear - birthyear
    if minimumAge < 13:
        print('You are not eligible to open fresh Account')
        exit()
    else:
        print('You can open an account')
    def __init__(self,name,bal = 0.0):
        self.name = name
        self.bal = bal
        print('Welcome to',Bank.bank_name,name)
        self.bal = bal
        print('Your Account Balance is', self.bal)

    def deposit(self,amount):
        self.bal = self.bal + amount
        print('You have deposited Rs.',amount)
        print('Your current balance is',self.bal)
        if self.bal < 1500:
            print('Your min balance should be Rs.1500, Enter the amount accordingly')
            exit()
        else:
            print('Your entered amount is sufficient to open an account, Keep minimum balance of Rs. 1500/-')

    def withdrawl(self,wamount):

        if wamount > self.bal:
            print('Your current balance is Rs.',self.bal,'Please enter amount between Rs. 1500/- to Rs.',self.bal)
            exit()
        self.bal = self.bal - wamount
        print('Your remaining balance is', self.bal)
b = Bank(input('Enter name'))
amount = float(input('Enter the amount to be deposited'))
b.deposit(amount)
wamount = float(input('Enter the amount to be withdrawn'))
b.withdrawl(wamount)


