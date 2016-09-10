public class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashMap<Character,Integer> hm = new HashMap<Character,Integer>();
        // char[] ca = s.toCharArray();
        int l = 0, lastendpos = -1, maxlen = 0;
        // System.out.println(ca);
        for (int i = 0; i < s.length(); i++){
            if(hm.get(s.charAt(i)) != null && hm.get(s.charAt(i)) > lastendpos){
                l = i - hm.get(s.charAt(i));
                lastendpos = hm.get(s.charAt(i));
                hm.put(s.charAt(i),i);
                
                
            } else{
                hm.put(s.charAt(i),i);
                l++;
                if (l > maxlen){
                    maxlen = l;
                }
            }
            // System.out.println(s.charAt(i));
            // hm.get(s[i]);
        }
        return maxlen;
    }
}


public class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashMap<Character,Integer> hm = new HashMap<Character,Integer>();
        char[] ca = s.toCharArray();
        int l = 0, lastendpos = -1, maxlen = 0;
        for (int i = 0; i < ca.length; i++){
            if(hm.get(ca[i]) != null && hm.get(ca[i]) > lastendpos){
                l = i - hm.get(ca[i]);
                lastendpos = hm.get(ca[i]);
                hm.put(ca[i],i);
                
                
            } else{
                hm.put(ca[i],i);
                l++;
                if (l > maxlen){
                    maxlen = l;
                }
            }
            // System.out.println(s.charAt(i));
            // hm.get(s[i]);
        }
        return maxlen;
    }
}