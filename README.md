# back-adjusted_continuous_futures
Adjusting futures contracts with the method of back-adjustment, based on X-days before expiration.

Futures contracts have "limited life". In order to make a proper back-testing and take into account the price difference between the contracts, we have to adjust the timeseries data properly. One of the most popular methods is the so called back-adjustment. 

This code takes the price data for every single contract for the specific commodity, which is stored in a folder. It than 'stiches' and adjusts every contract to turn it into one continuous timeseries data. This assures, that when back-testing different strategies, rolling-over is taken into account.
