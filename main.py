import MyTime
import CandleClass
from CandleClass import Candle
from colorama import init
from colorama import Fore, Back, Style

Candles = []
R4 = 360
R3 = 340
R2 = 325
R1 = 310
Pivot = 300
S1 = 295
S2 = 289
S3 = 280

CurrentPivot = Pivot
R = [R1, R2, R3, R4]

def Add2Candle(price):
    hour, minute = MyTime.GetTime()
    if len(Candles) == 0:
        Candles.append(Candle())
        Candles[-1].Add(price)
    else:
        # if current candle duration get end, create new candle.
        if MyTime.TimeDifrence(hour, minute, Candles[-1].GetStartTime()[0], Candles[-1].GetStartTime()[1]) > Candles[-1].GetDuration() - 1 :
            Candles.append(Candle())
            Candles[-1].Add(price)
            print('Candle Number: ' , len(Candles))
            Candles[-2].ShowCandle()
        # add current candle.
        else:
            Candles[-1].Add(price)

def GetAction():
    global CurrentPivot
    # SELL ALL if last price gets lower than Pivot.
    if Candles[-2].GetClose() < CurrentPivot:
        print(Fore.LIGHTRED_EX + 'SELL ALL => Close Candle[' + str(len(Candles)-1) + '] < CurrentPivot(' + str(CurrentPivot) + ')' + Fore.RESET)
        return False
    else:
        # Do nothing, if price dont get lower than pivot or upper than Resistant.
        if Candles[-2].GetClose() < R[0]:
            print(Fore.LIGHTYELLOW_EX + 'Do Nothing ...' + Fore.RESET)
            return True    
        # Buy signal, if price get upper than next Resistant.
        else:
            print(Fore.LIGHTMAGENTA_EX + 'Pivot upgraded from (' + str(CurrentPivot) + ') to (' + str(R[0]) + ').' + Fore.RESET)
            CurrentPivot = R.pop(0)
            print(Fore.LIGHTBLUE_EX + 'You Can BUY!' + Fore.RESET)


CandlesSeed = len(Candles) + 1

while (True):
    Add2Candle( int(input('Enter current price : ')) )
    if len(Candles) > CandlesSeed:
        GetAction()
        CandlesSeed += 1