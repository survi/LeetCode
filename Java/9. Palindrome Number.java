public class Solution {
    public boolean isPalindrome(int x) {
        if(x<0){
            return false;
        }
        int m = x, n = 0, max = 2147447412;
        if (x > max){
            return false;
        }
        // System.out.println("#####################################");
        // System.out.print("m:");
        // System.out.println(m);
        // System.out.print("n:");
        // System.out.println(n);
        while (m > 0){
            n = n * 10 + m % 10;
            m = m / 10;
            // System.out.println("====================================");
            // System.out.print("m:");
            // System.out.println(m);
            // System.out.print("n:");
            // System.out.println(n);
        }
        return (n == x?true:false);
        
    }
}