public class Solution {
    public int reverse(int x) {
        boolean posi = (x > 0?true:false);
        int reint = 0;
        // int maxint = 2147483647;
        if (!posi){
            x *= -1;
        }
        String s = String.valueOf(x), res = "";
        for(int i = s.length() - 1; i >= 0; i--){
            res += s.charAt(i);
        }
        try{
            reint = Integer.parseInt(res);
        }catch(Exception e){
            return 0;
        }
        
        if (posi){
            return reint;
        }else{
            return reint * (-1);
        }
        
    }
} ';h