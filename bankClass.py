

class Bank:
    allAccounts = []
    bankMoney = 10000
    totalLoanAmount = 0
    
class Account(Bank):
    def __init__(self,name, email, address, accountType):
        self.name = name
        self.email = email
        self.address = address
        self.accountType = accountType
        
        self.balance = 0
        self.loanMoney = 0
        self.loanTaken = 0
        self.loanLimit = 2
        self.accountNumber = self.generateAccountNumber(self.name, self.accountType)
        self.transactionHistory = []

        
        self.allAccounts.append(self)
        
        
        
    def seeTotalBankMoney(self):
        bankBalance = Bank.bankMoney
        print(bankBalance)
        
        
    def takeLoan(self, amount):
        if self.loanTaken < self.loanLimit and amount < self.bankMoney:
            self.balance = self.balance + amount
            self.loanMoney = self.loanMoney + amount
            self.loanTaken += 1
            self.bankMoney -= amount
            self.totalLoanAmount -= amount
            self.transactionHistory.append(f"loan: {self.name} take {amount} taka from the bank")
            print(f"loan: {self.name} take {amount} taka from the bank")
            print(self.balance)
        
        
    def withdrawMoney(self, amount):
        if amount < self.bankMoney:
            if self.balance >= amount:
                self.balance -= amount
                self.bankMoney -= amount
                print(amount)
                self.transactionHistory.append(f"withdraw: {self.name} withdraw {amount} taka from the bank")
                print(f"withdraw: {self.name} withdraw {amount} taka from the bank")
            else:
                print('Withdrawal amount exceeded')
        if self.balance >= amount and amount > self.bankMoney:
            print(' the bank is bankrupt.')
            
            
    def depositMoney(self, amount):
        if amount > 0:
            self.balance += amount
            self.bankMoney += amount
            self.transactionHistory.append(f"deposit: {self.name} deposit {amount} taka to the bank")
            print(f"deposit: {self.name} deposit {amount} taka to the bank")
        else:
            print('negative amount is not valid.')
         
            
    def generateAccountNumber(self, name, accountTyupe):
        accountLast = len(self.allAccounts)
        accountLetter = ''
        if accountTyupe == 'saving':
            accountLetter = 's'
        elif accountTyupe == 'current':
            accountLetter = 'c'
        
        accountNumber = f"{name}-{accountLetter}{accountLast}"
        return accountNumber    
          
    
    def seeTotalLoanMoney(self):
        totalLoanMoney = Bank.totalLoanAmount
        print(totalLoanMoney)
     
            
    def transferMoney(self, recipientAccount, amount):
        for ac in self.allAccounts:
            if ac.accountNumber == recipientAccount:
                if amount <= self.balance:
                    self.balance -= amount
                    ac.balance += amount
                    print(f"${amount} transferred successfully to {ac.name}.")
                    self.transactionHistory.append(f"transfer: {self.name} transfer {amount} taka to {recipientAccount}")
                   
                else:
                    print("Insufficient balance for transfer.")
            else:
                print("Account does not exist.")
                
          
                
    def deleteAccount(self, deletedAccountNumber):
        isAvailable = False
        for account in self.allAccounts:
            if account.accountNumber == deletedAccountNumber:
                self.allAccounts.remove(account)
                isAvailable = True
        if isAvailable == False:
            print('this account is not exists')               
                
                
    def seeTransactionHistory(self):
        for transaction in self.transactionHistory:
            print(transaction)
                
                
    def seeBalance(self):
        print('balance: ', self.name, self.balance)
            
            
    def seeAllTheAccounts(self):
        print('\n\nAll the Accounts in the Bank:\n')
        for account in self.allAccounts:
            print(f"\tAccount Holder    : {account.name}")
            print(f"\tAccount Type      : {account.accountType}")
            print(f"\tAccount Number    : {account.accountNumber}")
            print(f"\tBalance           : ${account.balance}")
            print(f"\tloan money        : ${account.loanMoney}")
            print(f"\tloan taken        : {account.loanTaken} times")
            print(f"\tloan taken limit  : {account.loanLimit} times\n")
            print("-" * 40)
            print()
                    
   
    def offTheLoanFeature(self, actionAccountNumber):
        for account in Bank.allAccounts:
           if account.accountNumber == actionAccountNumber:
               account.loanTaken = 2
        print('this user can not take loan')
               
               
    def onTheLoanFeature(self, actionAccountNumber):
        for account in Bank.allAccounts:
           if account.accountNumber == actionAccountNumber:
               account.loanTaken = 0
        print('this user can take loan')
    

admin = Account('admin', 'admin@gmail.com', 'admin address', 'super-admin')