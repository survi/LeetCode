public class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        // HashSet keys = new HashSet();
        ArrayList out = new ArrayList();
        Arrays.sort(nums);
        for (int i = 0; i < nums.length; i++){
            if (nums[i] > 0){
                break;
            }
            if (i > 0){
                if (nums[i-1] == nums[i]){
                    continue;
                }
            }
            for (int j = i + 1; j < nums.length; j++){
                if (j>i+1 && nums[j-1] == nums[j]){
                    continue;
                }
                for (int k = nums.length -1; k > j; k--){
                    
                    if (nums[i] + nums[j] + nums[k] < 0){
                        j++;
                        k++;
                    }else if (nums[i] + nums[j] + nums[k] > 0){
                        continue;
                    }else if (k<nums.length-1 && nums[k+1] == nums[k]){
                        continue;
                    }else if (nums[i] + nums[j] + nums[k] == 0){
                        out.add(new int[] {nums[i], nums[j], nums[k]});
                    }
                }
            }
        }
        return out;
    }
}