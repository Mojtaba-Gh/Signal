import MyTime
from colorama import init
from colorama import Fore, Back, Style

init()

class Candle:
    def __init__(self):
        # Start price
        self.Start = None
        # Stop price
        self.Close = None
        # Maximum price
        self.Max = None
        # Minimum price
        self.Min = None
        # Time duration in minute
        self.Duration = 1
        # Candle start time
        self.StartTime = None

    def SetStart(self, st):
        self.Start = st
    def SetClose(self, cl):
        self.Close = cl
    def SetMax(self, mx):
        self.Max = mx
    def SetMin(self, mn):
        self.Min = mn
    def SetStartTime(self, stTime):
        self.StartTime = stTime

    def GetStart(self):
        return self.Start
    def GetClose(self):
        return self.Close
    def GetMax(self):
        return self.Max
    def GetMin(self):
        return self.Min
    def GetStartTime(self):
        return self.StartTime
    def GetDuration(self):
        return self.Duration

    def Add(self, price):
        if self.GetStartTime() == None:
            hour, minute = MyTime.GetTime()
            self.SetStartTime([hour, minute])

        if self.GetStart() == None:
            self.SetStart(price)

        self.SetClose(price)

        if self.GetMax() == None or self.GetMax() < price :
            self.SetMax(price) 

        if self.GetMin() == None or self.GetMin() > price :
            self.SetMin(price) 

    def ShowCandle(self):
        if self.GetStart() == None:
            print(Fore.LIGHTYELLOW_EX + 'Candle is empty !' + Fore.RESET)
            return False
        if self.GetClose() >= self.GetStart():
            print(str(self.GetStartTime()[0]) + ':' + str(self.GetStartTime()[1]) + ' => ' , end='')
            print(str(self.GetMax()) )
            print(Fore.LIGHTGREEN_EX + '\t ' + str(self.GetClose()) )
            print(Fore.LIGHTGREEN_EX + '\t ' + str(self.GetStart()) + Fore.RESET )
            print('\t ' + str(self.GetMin()) )
        else:
            print(str(self.GetStartTime()[0]) + ':' + str(self.GetStartTime()[1]) + ' => ' , end='')
            print(str(self.GetMax()) )
            print(Fore.LIGHTRED_EX + '\t ' + str(self.GetStart()) )
            print(Fore.LIGHTRED_EX + '\t ' + str(self.GetClose()) + Fore.RESET )
            print('\t ' + str(self.GetMin()) )
        
# a = Candle()
# a.Add(3000)
# a.Add(3005)
# a.Add(3020)
# a.Add(2900)
# a.Add(2800)
# a.Add(2950)
# a.ShowCandle()