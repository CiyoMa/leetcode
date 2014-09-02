public class Solution {
    public int maxProfit(int[] prices) {
        int profit = 0, curProf = 0;
        int i = 1, difference;
        while (i < prices.length){
            difference = prices[i] - prices[i-1];
            while (curProf >= 0){
                curProf += difference;
                profit = (profit < curProf)? curProf: profit;
                if (i >= prices.length - 1 || curProf < 0)
                    break;
                i++;
                difference = prices[i] - prices[i-1];
            }
            curProf = 0;
            i++;
        }
        return profit;
    }
}