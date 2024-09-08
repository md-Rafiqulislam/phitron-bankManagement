

from bankClass import Bank, Account, admin
from userChoice import userOptions, adminOption



print('\nwelcome to the bank\n')
user = 'undefined'
userFound = False
first_loop = True
second_loop_user = True
third_user_loop = True
fourth_user_loop = True
second_admin_loop = True

while(first_loop):
    print('\n')
    print('1. admin')
    print('2. user')
    print('3. quit')
    firstChoice = input('enter your choice: ')
    first_loop = False

    if firstChoice == '1':
        while(second_admin_loop):
            print('admin')
            adminChoice = adminOption()
        
            if adminChoice == '1':
                account_type = ''
                print('welcome to account creation:')
                print('1. saving account.')
                print('2. currect account.')
                print('3. go back.')
                accountTypeForUser = input('enter your option: ')
                
                if accountTypeForUser == '1':
                    account_type = 'saving account'
                elif accountTypeForUser == '2':
                    account_type = 'currect account'
                
                
                userName = input('enter your name: ')
                userEmail = input('enter your email address: ')
                userAddress = input('enter your address: ')
                account = Account(userName, userEmail, userAddress, account_type)
                print(userName, 'your account has been created.')
            
            
            elif adminChoice == '2':
                deleteAccountNumber = input('enter your desire account number: ')
                admin.deleteAccount(deleteAccountNumber)
                
                
            elif adminChoice == '3':
                admin.seeAllTheAccounts()
                
            
            elif adminChoice == '4':
                admin.seeTotalBankMoney()
                
                
            elif adminChoice == '5':
                admin.seeTotalLoanMoney()
                
                
            elif adminChoice == '6':
                account_number = input('enter the account number: ')
                admin.onTheLoanFeature(account_number)
               
                
            elif adminChoice == '7':
                account_number = input('enter the account number: ')
                admin.offTheLoanFeature(account_number)
                
                
            elif adminChoice == '8':
                second_admin_loop = False
                first_loop = True
                
                
            else:
                print('you have entered a wrong input.')
        
        
                        
                
        
        
        
        
    elif firstChoice == '2':
        first_loop = False
        while(second_loop_user):
            print('1. login your account.')
            print('2. create account.')
            print('3. go back.')
            secondChoiceUser = input('enter your choice: ')
            
            if secondChoiceUser == '1':
                userAccountNumber = input('enter your account number: ')
                userEmail = input('enter your email address: ')
                
                for account in Bank.allAccounts:
                    if account.email == userEmail and account.accountNumber == userAccountNumber:
                        userFound = True
                        
                    if userFound == True:
                        userAction = userOptions()
                
            elif secondChoiceUser == '2':
                account_type = ''
                print('welcome to account creation:')
                print('1. saving account.')
                print('2. currect account.')
                print('3. go back.')
                accountTypeForUser = input('enter your option: ')
                
                
                if accountTypeForUser == '1':
                    second_loop_user = False
                    while(third_user_loop):
                        userName = input('enter your name: ')
                        userEmail = input('enter your email address: ')
                        userAddress = input('enter your address: ')
                        account = Account(userName, userEmail, userAddress, 'saving account')
                        print(userName, 'your account has been created.')
                        userFound = userName
                        third_user_loop = False
                        while(fourth_user_loop):
                            
                            
                            if userAction == '1':
                                depositeAmount = int(input('enter your deposit amount: '))
                                if depositeAmount > 0:
                                    account.depositMoney(depositeAmount)
                                else:
                                    print('you have entered a wrong input.')
                                    
                            elif userAction == '2':
                                withdrawAmount = int(input('enter your withdraw amount: '))
                                if withdrawAmount > 0:
                                    account.withdrawMoney(withdrawAmount)
                            
                            elif userAction == '3':
                                recipentAccountNumber = input('enter your recepient account number: ')
                                transferAmount = int(input('enter your transfer amount: '))
                                account.transferMoney(recipentAccountNumber, transferAmount)
                            
                            elif userAction == '4':
                                account.seeBalance()
                                
                            elif userAction == '5':
                                requestLoanAmount = int(input('enter your loan amount: '))
                                if requestLoanAmount > 0:
                                    account.takeLoan(requestLoanAmount)
                            elif userAction == '6':
                                account.seeTransactionHistory()
                                
                            elif userAction == '7':
                                fourth_user_loop = False
                                second_loop_user = True
                            
                            else:
                                print('you have entered a wrong input.')
                            
                elif accountTypeForUser == '2':
                    second_loop_user = False
                    while(third_user_loop):
                        userName = input('enter your name: ')
                        userEmail = input('enter your email address: ')
                        userAddress = input('enter your address: ')
                        account = Account(userName, userEmail, userAddress, 'current account')
                        print(userName, 'your account has been created.')
                        userFound = userName
                        third_user_loop = False
                        while(fourth_user_loop):
                           
                            userAction = userOptions()
                            
                            if userAction == '1':
                                depositeAmount = int(input('enter your deposit amount: '))
                                if depositeAmount > 0:
                                    account.depositMoney(depositeAmount)
                                else:
                                    print('you have entered a wrong input.')
                                    
                            elif userAction == '2':
                                withdrawAmount = int(input('enter your withdraw amount: '))
                                if withdrawAmount > 0:
                                    account.withdrawMoney(withdrawAmount)
                            
                            elif userAction == '3':
                                recipentAccountNumber = input('enter your recepient account number: ')
                                transferAmount = int(input('enter your transfer amount: '))
                                account.transferMoney(recipentAccountNumber, transferAmount)
                            
                            elif userAction == '4':
                                account.seeBalance()
                                
                            elif userAction == '5':
                                requestLoanAmount = int(input('enter your loan amount: '))
                                if requestLoanAmount > 0:
                                    account.takeLoan(requestLoanAmount)
                            elif userAction == '6':
                                account.seeTransactionHistory()
                                
                            elif userAction == '7':
                                fourth_user_loop = False
                                second_loop_user = True
                            
                            else:
                                print('you have entered a wrong input.')
                    
                else:
                    print('you have entered a wrong input.')
                
                
                pass 
            
            
            elif secondChoiceUser == '3':
                second_loop_user = False
                first_loop = True
            else:
                print('you have entered wrong input.')
                
    elif firstChoice == '3':
        print('thank you visit us')
        exit()
                 
    else:
        print('you have entered wrong input.')