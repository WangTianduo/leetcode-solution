/*
 * @lc app=leetcode id=4 lang=java
 *
 * [4] Median of Two Sorted Arrays
 */
class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int total = nums1.length + nums2.length;
        int half = (total + 1) / 2;

        int[] arrA;
        int[] arrB;

        if (nums1.length < nums2.length) {
            arrA = nums1;
            arrB = nums2;
        }else {
            arrB = nums1;
            arrA = nums2;
        }

        int aMin = 0;
        int aMax = arrA.length;

        int m = arrA.length;
        int n = arrB.length;

        while (aMin <= aMax) {
            int ptrA = (aMax + aMin) / 2;
            int ptrB = half - ptrA;
            if (ptrA < aMax && arrB[ptrB-1] > arrA[ptrA]){
                aMin = ptrA + 1; // i is too small
            }
            else if (ptrA > aMin && arrA[ptrA-1] > arrB[ptrB]) {
                aMax = ptrA - 1; // i is too big
            }
            else { // i is perfect
                int maxLeft = 0;
                if (ptrA == 0) { maxLeft = arrB[ptrB-1]; }
                else if (ptrB == 0) { maxLeft = arrA[ptrA-1]; }
                else { maxLeft = Math.max(arrA[ptrA-1], arrB[ptrB-1]); }
                if ( total % 2 == 1 ) { return maxLeft; }

                int minRight = 0;
                if (ptrA == m) { minRight = arrB[ptrB]; }
                else if (ptrB == n) { minRight = arrA[ptrA]; }
                else { minRight = Math.min(arrB[ptrB], arrA[ptrA]); }

                return (maxLeft + minRight) / 2.0;
            }
        }
        return 0.0;
    }
}

