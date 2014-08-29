public class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int[] residual = new int[gas.length];
        for(int i=0; i<gas.length; i++)
            residual[i] = gas[i] - cost[i];
        int start = 0, totalCost = 0, currentCost = 0;
        for(int i=0; i<gas.length; i++){
            totalCost += residual[i];
            currentCost += residual[i];
            if (currentCost < 0){
                currentCost = 0;
                start = i+1;
            }
        }
        return totalCost < 0? -1:start;
    }
}