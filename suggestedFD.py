class suggestedFD():
    def __init__(self,bank,period,rates,minAmt):
        self.__bank = bank
        self.__period = period
        self.__rates = rates
        self.__minAmt = minAmt

    def getBank(self):
        return self.__bank
    def setBank(self,bank):
        self.__bank = bank

    def getPeriod(self):
        return self.__period
    def setPeriod(self,period):
        self.__period = period

    def getRates(self):
        return self.__rates
    def setRates(self,rates):
        self.__rates = rates

    def get_minAmt(self):
        return self.__minAmt
    def set_minAmt(self,minAmt):
        self.__minAmt = minAmt
