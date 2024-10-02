class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        '''
        buy_price = 1st day price
        keep going through the array and compare until there is a new minimum amount to buy on 
        from that day onward, we should calculate the price difference and the max from this will be the max profit
        '''
        buy_price = prices[0]
        max_profit = 0

        for price in prices:
            if price < buy_price:
                buy_price = price
            else:
                curr_profit = price - buy_price
            if curr_profit > max_profit:
                max_profit = curr_profit
        
        return max_profit

