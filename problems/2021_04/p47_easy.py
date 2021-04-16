import sys
sys.path.append('../..')
from helpers import helpers # only works if the script is in problems/month_folder/

print('''
[easy] apr. 12, 2021
This problem was asked by Facebook.

Given a array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock once. You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars.
''')

'''
Implement solution
'''
def buy_sell_0(stockprices):
    '''
    this function does not work for this problem. it is better suited for when one can buy and sell multiple times and add profit each time.
    see buy_sell_1 instead.
    '''
    n = len(stockprices)

    if n<=1:
        print('not enough data')
        pass

    i=0
    buy_index=0
    sell_index=0
    profit = 0

    # traverse through data
    while(i < (n-1)):
        b = buy_index
        s = sell_index

        # find local min and buy
        while (i < (n-2)):
            if (stockprices[i+1] < stockprices[i]):
                i+=1
            else:
                print(f'buy at i{i} for {stockprices[i]}?')
                b = i
                break 
        
        i+=1

        # find local max and sell
        while (i < n):
            if (i==n-1):
                print(f'last price. sell at i{i} for {stockprices[i]}?')
                s = i
                break
            if (stockprices[i+1] > stockprices[i]):
                i+=1
            else:
                print(f'sell at i{i} for {stockprices[i]}?')
                s = i
                break
        
        p = stockprices[s] - stockprices[b]
        print(f'the profit in this iteration is {p}. the max profit before was {profit}.')
        if p > profit:
            buy_index, sell_index, profit = b, s, p
    
    print(f'\nmax one-time profit:\nbuy at i{buy_index} for {stockprices[buy_index]}, then sell at i{sell_index} for {stockprices[sell_index]}\nfor a profit of {profit}')

def buy_sell_1(stockprices):
    n = len(stockprices)

    if n<=1:
        print('not enough data')
        pass

    i=0
    buy_index=0
    sell_index=0
    profit = 0

    # traverse through data
    while(i < (n-1)):
        b = 0
        # find local min and buy
        while (i < (n-2)):
            if (stockprices[i+1] < stockprices[i]):
                i+=1
            else:
                print(f'buy at i{i} for {stockprices[i]}?')
                b = i
                break 
        
        i+=1 # look at next price now
        localmax = stockprices[i] # initialize localmax

        j = i
        s = j
        # find 'global' (after buy index) max. idea is we will see if that point is the best to sell.
        while (j < n):
            if stockprices[j] > localmax:
                localmax = stockprices[j]
                s = j
            j+=1
        print(f'sell at i{s} for {stockprices[s]}?')
        
        p = stockprices[s] - stockprices[b]
        print(f'the profit in this iteration is {p}. the max profit before was {profit}.')
        if p > profit:
            buy_index, sell_index, profit = b, s, p
    
    print(f'\nmax one-time profit:\nbuy at i{buy_index} for {stockprices[buy_index]}, then sell at i{sell_index} for {stockprices[sell_index]}\nfor a profit of {profit}')
'''
Driver
'''
if __name__ == '__main__':
    print('Driver code...')
    stockprices = [9,11,8,5,7,10,9,11,8,5,7,10]
    print(f'using these stock prices: {stockprices}')
    buy_sell_1(stockprices)
