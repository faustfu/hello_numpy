import pandas as pd
import numpy as np

from statistics import median 
from random import randrange

class API:
    @staticmethod
    def getOrderbook(n):
        # create an orderbook sample by random here
        orderbook = {'bid':'','ask':''}
        book = []
        for i in range(0,n):
            rate = randrange(10, 500, 1) / 10000
            volume = randrange(1, 200, 1) ** 2 + randrange(1, 100, 1)
            if len([order[0] for order in book if rate == order[0]])==0:
                book.append([rate,volume])
        split_rate = round(median([order[0] for order in book]),4)
        orderbook['bid'] = [order for order in book if order[0]<split_rate]
        orderbook['ask'] = [order for order in book if order[0]>=split_rate]
        orderbook['bid'] = sorted(orderbook['bid'],key=lambda l:l[0], reverse=True) #interest rate from large to small
        orderbook['ask'] = sorted(orderbook['ask'],key=lambda l:l[0]) # from small to large
        return orderbook

class MAIN:
    def __init__(self, TotalAmount, RetainAmount, SplitAmount, lendingPeriod,
                 CrazyRate, CrazyLendingPeriod, CrazyOrderAmount,
                 triggerLargeVol, triggerRank, triggerVol
                ):
        self.param = self.setParam(TotalAmount, RetainAmount, SplitAmount, lendingPeriod,
                                     CrazyRate, CrazyLendingPeriod, CrazyOrderAmount,
                                     triggerLargeVol, triggerRank, triggerVol)
        self.orderbook = {}
        self.optOrder = []
    def setParam(self,TotalAmount, RetainAmount, SplitAmount, lendingPeriod,
                                     CrazyRate, CrazyLendingPeriod, CrazyOrderAmount,
                                     triggerLargeVol, triggerRank, triggerVol):
        param = {}
        param['TotalAmount'] = TotalAmount
        param['RetainAmount'] = RetainAmount
        param['SplitAmount'] = SplitAmount
        param['lendingPeriod'] = lendingPeriod
        param['CrazyRate'] = CrazyRate
        param['CrazyLendingPeriod'] = CrazyLendingPeriod
        param['CrazyOrderAmount'] = CrazyOrderAmount
        param['triggerLargeVol'] = triggerLargeVol
        param['triggerRank'] = triggerRank
        param['triggerVol'] = triggerVol
        return param
    def run(self):
        self.orderbook = API.getOrderbook(500)
        Logics = {}
        Logics['ByLargeVol'] = LOGIC.LargeVol(self.orderbook, self.param['triggerLargeVol'])
        Logics['ByRank'] = LOGIC.ByRank(self.orderbook, self.param['triggerRank'])
        Logics['ByVol'] = LOGIC.ByVol(self.orderbook, self.param['triggerVol'])
        OptOrder = []
        tmpMaxRate = 0
        tmpOrderSize = self.param['SplitAmount']
        for logic in Logics.keys():
            if Logics[logic][0] >= tmpMaxRate:
                tmpMaxRate = Logics[logic][0]
        if tmpMaxRate >= self.param['SplitAmount']:
            tmpOrderSize = param['CrazyOrderAmount']
        OptOrder = [tmpMaxRate, tmpOrderSize]
        return OptOrder
    
class LOGIC:
    #put lending bot logic here
    @staticmethod
    def LargeVol(orderbook, triggerVol):
        LargeVolOrders = [order for order in orderbook['ask'] if order[1]>=triggerVol][0]
        return LargeVolOrders
    @staticmethod
    def ByRank(orderbook, triggerRank):
        return orderbook['ask'][triggerRank]
    @staticmethod
    def ByVol(orderbook, triggerVol):
        cumuVol = np.cumsum([order[1] for order in orderbook['ask']])
        order = orderbook['ask'][[i for i in range(0,len(cumuVol)) if cumuVol[i] >= triggerVol][0]]
        return order
    
    
TotalAmount = 10000
RetainAmount = 0
SplitAmount = 50
lendingPeriod = 2
CrazyRate = 0.075
CrazyLendingPeriod = 30
CrazyOrderAmount = 150
triggerLargeVol = 20000
triggerRank = 25
triggerVol = 10000
a = MAIN(TotalAmount, RetainAmount, SplitAmount, lendingPeriod,
                 CrazyRate, CrazyLendingPeriod, CrazyOrderAmount,
                 triggerLargeVol, triggerRank, triggerVol)
a.run()