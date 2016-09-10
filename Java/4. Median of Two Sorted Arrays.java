public class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int[] nums3 = new int[nums1.length+nums2.length];
        int pos1 = 0, pos2 = 0, pos3 = 0;
        double mdl = (nums1.length +nums2.length + 1) / 2.0;
        int mdlint = (nums1.length +nums2.length + 1) / 2;
        boolean is05 = false;
        if (mdl % 1 == 0.5){
            is05 = true;
        }
        while (pos1 < nums1.length || pos2 < nums2.length){
            int v3 = 0;
            if (pos1 >= nums1.length){
                v3 = nums2[pos2];
                pos2++;
            }else if (pos2 >= nums2.length){
                v3 = nums1[pos1];
                pos1++;
            }else if(nums1[pos1] > nums2[pos2]){
                v3 = nums2[pos2];
                pos2++;
            }else{
                v3 = nums1[pos1];
                pos1++;
            }
            nums3[pos3] = v3;
            if (is05 && pos3 == mdlint){
                return (nums3[mdlint-1] + nums3[mdlint])/2.0;
            }else if (!is05 && pos3 == mdlint-1){
                return nums3[mdlint-1];
            }
            pos3++;
            
        }
        return -1;
    }
}