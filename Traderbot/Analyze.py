from Collect import Collect
from Report import Report

import time as time

HOUR = 60*60
DAY = HOUR * 24

def main():
    analyze = Analyze()

    data = analyze.market.update_chart_data(start=DAY, period=HOUR/12)

    report = Report()
    header = [
        'date','volume',
        'open', 'high',
        'low', 'close',
        'quoteVolume',
        'weightedAverage'
    ]
    report.write_csv(data=data, header=header, file_name='somefile')
    print("Done!")

class Analyze(object):
    """Analyze data collected from exchange.

    Attributes:
    market: an object for collecting data from market.

    """

    #TODO: add parameter for an exchange/market. Such as Polonix, Coinbase, etc
    def __init__(self):
        """
        Initializes
        Objects:
        market: a Collect object for collecting data from market.

        """
        super(Analyze, self).__init__()
        self.market = Collect()

    # TODO: calculate SMA
    def calc_SMA(self):
        data = self.market.get_chart_data(start=DAY, period=HOUR/4)
        print(data)

    # TODO: calculate EMA
    def calc_EMA(self, arg):
        pass

if __name__ == '__main__':
    main()
