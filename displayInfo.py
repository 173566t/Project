class displayInfo():
    def __init__(self,choice,rates,minAmt):
        self.__choice = choice
        self.__rates = rates
        self.__minAmt = minAmt

    def getChoice(self):
        return self.__choice
    def setChoice(self,choice):
        self.__choice = choice

    def getRates(self):
        return self.__rates
    def setRates(self,rates):
        self.__rates = rates

    def get_minAmt(self):
        return self.__minAmt
    def set_minAmt(self,minAmt):
        self.__minAmt = minAmt
