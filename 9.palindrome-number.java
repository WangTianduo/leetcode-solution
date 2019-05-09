/*
 * @lc app=leetcode id=9 lang=java
 *
 * [9] Palindrome Number
 */
class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        }

        String str = String.valueOf(x);
        int len = str.length();

        for (int i = 0; i < len; i++) {
            if (i > len - i) {
                break;
            }
            if (str.charAt(i) != str.charAt(len-i-1)) {
                return false;
            }
        }
        return true;
    }
}

