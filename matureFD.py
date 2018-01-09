class matureFD():
    def __init__(self, matureDate, bank, accNum, amount):
        self.__matureDate = matureDate
        self.__bank = bank
        self.__accNum = accNum
        self.__amount = amount

    def get_matureDate(self):
        return self.__matureDate
    def set_matureDate(self, matureDate):
        self.__matureDate = matureDate

    def getbank(self):
        return self.__bank
    def setPeriod(self, bank):
        self.__bank = bank

    def get_accNum(self):
        return self.__accNum
    def set_accNum(self,accNum):
        self.__accNum = accNum

    def getAmount(self):
        return self.__amount
    def setAmount(self, amount):
        self.__amount = amount
