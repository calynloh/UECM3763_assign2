from pandas.io.data import DataReader as DR
from datetime import datetime as dt
import pylab as p
import numpy as np

#download maybank(1155) data from 2013 to 2015
start = dt(2013, 1, 1)
end = dt(2015, 1, 1)
data = DR("1155.KL", 'yahoo', start, end)

#define a function for moving average
def moving_avg (values, days):
    weight =np.repeat(1.0, days)/days
    sma=np.convolve(values, weight,'valid')
    return sma

#calculate 5-day moving average for maybank
closevalue = data['Close'].values #take only the closing value of maybank
ma= moving_avg(closevalue, 5)

#plot the 5-day moving average of maybank
number= len(ma)
t= p.linspace(0,number,number);
p.title('5day moving average graph for Maybank')
p.xlabel('number of days')
p.ylabel('average of stock price (RM)')
p.plot(t,ma)
p.show()

#calculate the correlation of Maybank with FTSEKLCI
data_of_ftseklci= DR("^KLSE",'yahoo',start,end) #download FTSEKLCI data

x = ['1155.KL', '^KLSE']
maybank_klse_closevalue = DR(x, 'yahoo', start, end)['Close']

correlation_mayb_klci= maybank_klse_closevalue.corr()

print('the correlation of Maybank with FTSEKLCI is \n ', correlation_mayb_klci)