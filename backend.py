from nsepython import *
import pandas as pd
import urllib.parse


class StockExchangeData:
    def __init__(self):
        pass

    def get_index_list(self):
        indices_list = nse_get_index_list()
        return indices_list
    
    def fetch_details(self, index = "NIFTY 50"):
        encoded_index = urllib.parse.quote(index)
        positions = nsefetch(f"https://www.nseindia.com/api/equity-stockIndices?index={encoded_index}")
        df = pd.DataFrame(positions['data'])
        drop_columns = ['priority', 'series', 'ffmc', 'stockIndClosePrice', 'identifier', 'totalTradedVolume', 'totalTradedValue', 'lastUpdateTime', 'yearHigh', 'yearLow', 'nearWKH', 'nearWKL', 'date365dAgo', 'chart365dPath', 'date30dAgo', 'chart30dPath', 'chartTodayPath', 'meta']
        df.drop(columns=drop_columns, axis=None, inplace=True)
        # print(df)
        return df.to_html(index=True, border=1, classes='table table-striped table-responsive', justify='center')
    
    
