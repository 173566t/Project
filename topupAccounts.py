class topupAccounts():
    def __init__(self,bank,accNum,type,balance,minAmt):
        self.__bank = bank
        self.__accNum = accNum
        self.__type = type
        self.__balance = balance
        self.__minAmt = minAmt

    def getbank(self):
        return self.__bank
    def setPeriod(self, bank):
        self.__bank = bank

    def get_accNum(self):
        return self.__accNum
    def set_accNum(self, accNum):
        self.__accNum = accNum

    def getType(self):
        return self.__type
    def setType(self,type):
        self.__type = type

    def getBalance(self):
        return self.__balance
    def setBalance(self,balance):
        self.__balance = balance

    def get_minAmt(self):
        return self.__minAmt
    def set_minAmt(self,minAmt):
        self.__minAmt = minAmt

