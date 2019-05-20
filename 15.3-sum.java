/*
 * @lc app=leetcode id=15 lang=java
 *
 * [15] 3Sum
 */
import java.util.*;
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();//var results [][]int
        List<Integer> sorted = Arrays.stream(nums).sorted().boxed().collect(Collectors.toList());//sort.Ints(nums)

        for (int i = 0; i < sorted.size() - 2; i++) {
            if (i > 0 && sorted.get(i).equals(sorted.get(i - 1))) {
                continue; // to prevent the repeat
            }
            int target = -sorted.get(i);
            int left = i + 1;
            int right = nums.length - 1;

            while (left < right) {
                int sum = sorted.get(left) + sorted.get(right);

                if (sum == target) {
                    List<Integer> tmp = new ArrayList<>();
                    tmp.add(sorted.get(i));
                    tmp.add(sorted.get(left));
                    tmp.add(sorted.get(right));
                    result.add(tmp);
                    left++;
                    right--;
                    while (left < right && sorted.get(left).equals(sorted.get(left - 1))) {
                        left++;
                    }
                    while (left < right && sorted.get(right).equals(sorted.get(right + 1))) {
                        right--;
                    }
                } else if (sum > target) {
                    right--;
                } else {
                    left++;
                }
            }
        }

        return result;
    }
}

