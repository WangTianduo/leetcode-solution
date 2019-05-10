/*
 * @lc app=leetcode id=5 lang=java
 *
 * [5] Longest Palindromic Substring
 */
class Solution {
    public String longestPalindrome(String s) {
        if (s == null || s.length() == 0) {
            return "";
        }
        String result = "";
        String potential = "";
        for (int i = 0; i < s.length(); i++) {
            int len1 = expandAtCenter(s, i, i);
            int len2 = expandAtCenter(s, i, i+1);
            int len = Math.max(len1, len2);

            int start = i - ((len-1)/2); // same as len/2 when len is odd number 
            int end = i + (len/2);

            System.out.println("start: " + start);
            System.out.println("end: " + end);
            System.out.println("len: " + len);

            potential = s.substring(start, end+1);
            if (potential.length() >= result.length()) {
                result = potential;
            }
        }
        return result;
    }

    private int expandAtCenter(String s, int left, int right) {
        int L = left;
        int R = right;

        while (L >= 0 && R < s.length() && s.charAt(L) == s.charAt(R)) {
            L--;
            R++;
        }

        return R-L-1;
    }
    // public String longestPalindrome(String s) {
    //     if (s.length() == 0) {
    //         return "";
    //     }
    //     if (isPalindrome(s, 0, 0)) {
    //         return s;
    //     }
    //     String possible1 = longestPalindrome(s.substring(1));
    //     String possible2 = longestPalindrome(s.substring(0, s.length()-1));

    //     if (possible1.length() > possible2.length()) {
    //         return possible1;
    //     }else {
    //         return possible2;
    //     }
    // }

    // private boolean isPalindrome(String s, int start, int end) {

    //     int i, j;
    //     if (start == 0 && end == 0) {
    //         i = 0;
    //         j = s.length()-1;
    //     }else {
    //         i = start;
    //         j = end;
    //     }

    //     while (i <= j) {
    //         if (s.charAt(i) != s.charAt(j)) {
    //             return false;
    //         }else {
    //             i ++;
    //             j --;
    //         }
    //     }
    //     return true;
    // }
}

