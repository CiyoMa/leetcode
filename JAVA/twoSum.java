public class Solution {
    public int[] twoSum(int[] numbers, int target) {
        Map<Integer, Set<Integer>> positions = new HashMap<Integer, Set<Integer>>();
        Set<Integer> hs;
        for (int n=0; n < numbers.length; n++)
            if (positions.containsKey(numbers[n]))
                positions.get(numbers[n]).add(n);
            else{
                hs = new HashSet<Integer>();
                hs.add(n);
                positions.put(numbers[n], hs);
            }
        int[] index = new int[2];
        for (int n=0; n< numbers.length; n++){
            hs = positions.get(numbers[n]);
            hs.remove(n);
            if (positions.containsKey(target-numbers[n]) && !positions.get(target-numbers[n]).isEmpty()){
                Iterator<Integer> i = positions.get(target-numbers[n]).iterator();
                index[0] = n+1;
                index[1] = i.next()+1;
                break;
            }
        }
        return  index;
    }
}

// TRY ONE PASS PROCESS.


/*

public class Solution {
    public int[] twoSum(int[] numbers, int target) {
    HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
    int[] result = new int[2];
 
    for (int i = 0; i < numbers.length; i++) {
        if (map.containsKey(numbers[i])) {
            int index = map.get(numbers[i]);
            result[0] = index+1 ;
            result[1] = i+1;
            break;
        } else {
            map.put(target - numbers[i], i);
        }
    }
 
    return result;
    }
}

*/