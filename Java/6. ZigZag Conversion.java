public class Solution {
    public String convert(String s, int numRows) {
        int gap = numRows + numRows - 2;
        String res = "";
        
        if (gap == 0){
            return s;
        }
        
        for (int i = 0; i < numRows; i++){
            int j = 0;
            while(i + j * gap < s.length()){
                res += s.charAt(i + j * gap);
                if(i > 0 && i < numRows - 1 && (j + 1) * gap - i < s.length()){
                    res += s.charAt( (j + 1) * gap - i);
                }
                j++;
            }
        }
        return res;
    }
}