
def adminOption():
    print('here all the options for the admin.')
    print('1. create an account.')
    print('2. delete an account.')
    print('3. see all the accounts list.')
    print('4. total available balance of the bank.')
    print('5. see the total loan amount.')
    print('6. permission for the loan feather.')
    print('7. reject for the loan feather.')
    print('8. go back')

    choice = input('enter your option: ')
    return choice


def userOptions():
    print('hello, here is your options')
    print('1. deposit money.')
    print('2. withdraw money.')
    print('3. transfer money.')
    print('4. see balance.')
    print('5. take loan.')
    print('6. transaction history.')
    print('7. go back.')
    userAction = input('enter your option: ')