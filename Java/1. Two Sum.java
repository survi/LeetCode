public class Solution {
    public int[] twoSum(int[] nums, int target) {
        for(int i=0;i<nums.length;i++){
            for(int j=i+1;j<nums.length;j++){
                if(nums[i]+nums[j]==target){
                    return new int[] {i,j};
                }
            }
        }
    return null;
    }
}



public class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> nm = new HashMap<Integer,Integer>(nums.length);
        for(int i=0;i<nums.length;i++){
            if(nm.get(target-nums[i]) != null){
                if(nm.get(target-nums[i]) != i){
                    return new int[] {nm.get(target-nums[i]),i};
                }
            }
            else{
                nm.put(nums[i],i);
            }
        }
    return null;
    }
}


