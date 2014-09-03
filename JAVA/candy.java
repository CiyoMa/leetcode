public class Solution {
    public int candy(int[] ratings) {
        if (ratings.length <= 1)
            return ratings.length;
        int[] kids = new int[ratings.length];
        int count = 0;
        for (int j = 0; j < ratings.length; j++)
            kids[j] = 1;
        for (int j = 1; j < ratings.length; j++)
            if (ratings[j] > ratings[j-1] && kids[j] <= kids[j-1])
                kids[j] = kids[j-1]+1;
        
        for (int j = ratings.length - 2; j >= 0 ; j--)
            if (ratings[j] > ratings[j+1] && kids[j] <= kids[j+1])
                kids[j] = kids[j+1]+1;
        
        for (int j = 0; j < ratings.length; j++)
            count += kids[j];
        return count;
    }
}