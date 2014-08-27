public class Solution {
    public void merge(int A[], int m, int B[], int n) {
        while (m + n > 0)
            if (m > 0 && n > 0 && A[m-1] >= B[n-1])
                A[m+n-1] = A[--m];
            else if (n == 0)
                break;
            else
                A[m+n-1] = B[--n];
    }
}