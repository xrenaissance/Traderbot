import requests
import time

def main():
    pass

class Collect(object):
    """Collects Data from exchange

    Attributes:
    candles: The last candle chart data recieved from the market.

    """

    #TODO: add parameter for an exchange/market. Such as Polonix, Coinbase, etc
    def __init__(self):
        super(Collect, self).__init__()
        self.candles = self.update_chart_data()

    # TODO: handle exceptions for requests that return bad/no data
    def update_chart_data(
        self,
        currency_pair='USDT_BTC',
        start=60*60,
        end=time.time(),
        period=900):
        """Returns the candle chart data.

        Inputs
        currecyPair: such as "USDT_BTC"
        start: how long ago to start retrieving chart data
        end: when to stop retrieving the chart data
        period: the period of the candle data. Excepted periods are
        300, 900, 1800, 7200, 14400, and 86400, and are given
        in seconds.

        "Start" and "end" are given in UNIX timestamp format and used
        to specify the date range for the data returned. By default,
        the method will return BTC in USDT, starting an hour ago,
        ending now, with a period of 900 seconds.

        Output
        candles: returns a list of dictionaries. Each dictionary
        contains one candle.

        Sample output looks like this...
        [{"date":1405699200,"high":0.0045388,"low":0.00403001,
        "open":0.00404545, "close":0.00427592,"volume":44.11655644,
        "quoteVolume":10259.29079097,"weightedAverage":0.00430015}, ...]
        """

        url = 'https://poloniex.com/public?command=returnChartData'
        params = {'currencyPair': currency_pair, 'period': period,'start': int(time.time()) - start , 'end': int(end) }
        r = requests.get(url, params=params)
        data = r.json()
        self.candles = data
        return self.candles

    def get_order_trades(self, arg):
        pass

if __name__ == '__main__':
    main()
