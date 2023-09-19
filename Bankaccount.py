class bankaccount():
    def __init__(self) -> None:
        self.balance = 0
        self.transaction = 0
        self.dict = {}
        print('''
            Welcome to Times bank
            1. open account
            # 2. deposit money
            # 3.withdraw money
            # 4.check
            # 5. exit/quit
            # 6.dictionary 
'''
        )
        choice = int(
            input('Select your choice from the above:')
        )
        if choice == int(1):
            self.new_account()
            self.deposit()
            self.withdraw()
            self.checkbalance()
        elif choice == int(2):
            self.deposit()
        elif choice == int(3):
            self.withdraw()
        elif choice == int(4):
            self.check()
        elif choice == int(5):
            self.exit()
        else:
            self.__init__()
    def new_account(self):
        print("deposit minimum 500rs")
        _m = int(input("enter init"))