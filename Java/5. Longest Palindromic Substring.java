public class Solution {
    public String longestPalindrome(String s) {
        String res = "";
        int l = 0;
        for (int i = 0; i < s.length(); i++){
            if (i + 1 < s.length()){
                if(s.charAt(i) == s.charAt(i+1)){
                    res = loopString(s, res, i, 0, 1, l);
                    l = res.length();
                }
            }
            res = loopString(s, res, i, 0, 0, l);
            l = res.length();
        }
        return res;
    }
    public String loopString(String s, String res, int i, int j, int k, int l){
        while(i - j >= 0 && i + j + k <= s.length() - 1 && s.charAt(i-j) == s.charAt(i+j + k)){
            j++;
        }
        j--;
        if (2 * j + 1 + k > l){
            l = 2 * j + 1 + k;
            res = s.substring(i - j, i + j + 1 + k);
        }
        return res;
    }
}



public class Solution {
    public String longestPalindrome(String s) {
        String res = "";
        int l = 0;
        if(s == null) return null;
		if(s.length() <= 2) return s;
        for (int i = s.length() / 2 - 1, h = i - 1; i < s.length() - l / 2 + 1; i++, h--){
            if ( h < 0){
                h = 0;
            }
            if (i + 1 < s.length()){
                if(s.charAt(i) == s.charAt(i+1)){
                    res = loopString(s, res, i, 0, 1, l);
                    l = res.length();
                }
                if(s.charAt(h) == s.charAt(h+1)){
                    res = loopString(s, res, h, 0, 1, l);
                    l = res.length();
                }
                
            }
            res = loopString(s, res, i, 0, 0, l);
            l = res.length();
            res = loopString(s, res, h, 0, 0, l);
            l = res.length();
        }
        return res;
    }
    public String loopString(String s, String res, int i, int j, int k, int l){
        while(i - j >= 0 && i + j + k <= s.length() - 1 && s.charAt(i-j) == s.charAt(i+j + k)){
            j++;
        }
        j--;
        if (2 * j + 1 + k > l){
            l = 2 * j + 1 + k;
            res = s.substring(i - j, i + j + 1 + k);
        }
        return res;
    }
}