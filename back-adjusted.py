import pandas as pd
import matplotlib.pyplot as plt
import os.path

class Backadj:
    def __init__(self, directory, code, start, xdays):
        self.file = open("C:/Users/Kubrat/Desktop/Python/" + directory + "/" + code + ".txt", "r")
        self.content = self.file.read()
        self.symbols = self.content.split(",")

        self.start = start
        self.xdays = xdays # days before the last trading day of the contract, where the rollover occures

    def timeseries(self):
        loop_1 = []

        observed = 0
        last_price = float(0)
        last_date = None

        for symbol in self.symbols:
            if os.path.isfile("C:/Users/Kubrat/Desktop/Python/" + directory + "/" + symbol + ".csv") == True:
                df = pd.read_csv("C:/Users/Kubrat/Desktop/Python/" + directory + "/" + symbol + ".csv",
                                 index_col='date', parse_dates=['date'])[-self.start:]
                df['Contract'] = symbol

                if observed == 1:
                    df = df[last_date:]
                    adj_value = df.close[0] - last_price

                    update = pd.concat(loop_1)
                    update.open = update.open + adj_value
                    update.high = update.high + adj_value
                    update.low = update.low + adj_value
                    update.close = update.close + adj_value

                    last_price = df.close.iloc[-self.xdays]
                    last_date = df.index[-self.xdays]
                    df = df[:-self.xdays]

                    del loop_1[:]
                    loop_1.append(update)
                    loop_1.append(df)


                elif observed == 0:
                    last_price = df.close.iloc[-self.xdays]
                    last_date = df.index[-self.xdays]
                    df = df[:-self.xdays]
                    observed = 1
                    loop_1.append(df)

        data = pd.concat(loop_1)
        data['openShift'] = data.open.shift(-1)
        data.reset_index(inplace=True)
        data['date'] = pd.to_datetime(data['date'], errors='coerce')
        data['Month'] = data['date'].dt.month
        data['Year'] = data['date'].dt.year
        data = data.set_index('date')

        data['Unrlzd'] = float(0)
        data['RetDiff'] = data.openShift.diff()
        data['Point'] = range(len(data.index))
        data['Pnl'] = float(0)
        data['Positive'] = 0
        data['Negative'] = 0
        data['Position'] = 0
        data['DaysInpos'] = 0

        years = [2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021,
                 2022]

        return data

directory = 'zw'
code = 'zw'
start = 110

backadj = Backadj(directory, code, start)
df = backadj.timeseries()
