public class Solution {
    public double pow(double x, int n) {
        if (n == 0)
            return 1.0;
        else if (n == 1)
            return x;
            
        double temp = pow(x,n/2);
        if (n < 0)
            return temp*temp*((n%2 == -1)?1.0/x:1.0);
        return temp*temp*((n%2 == 1)?x:1.0);
    }
}