/*
 * @lc app=leetcode id=5 lang=java
 *
 * [5] Longest Palindromic Substring
 */
class Solution {
    public String longestPalindrome(String s) {

        int c = 0;
        int r = 0;
        String q = generateNewString(s);
        int[] P = new int[q.length()];

        for (int i = 1; i < q.length() - 1; i++) {
            // find the corresponding letter in the palidrome subString
            int iMirror = c - (i - c);

            if(r > i) {
                P[i] = Math.min(r - i, P[iMirror]);
            }

            // expanding around center i
            while (true){
                if ((i+1+P[i]) >= q.length() || (i-1-P[i]) < 0) {
                    break;
                }
                if (q.charAt(i + 1 + P[i]) != q.charAt(i - 1 - P[i])) {
                    break;
                }
                P[i]++;
            }
            
            // Update c,r in case if the palindrome centered at i expands past r,
            if (i + P[i] > r) {
                c = i;              // next center = i
                r = i + P[i];
            }
        }

        int maxPalind = 0;
        int center = 0;

        for (int i = 0; i < q.length(); i++) {
            if (P[i] > maxPalind) {
                maxPalind = P[i];
                center = i;
            }
        }

        return s.substring((center-maxPalind)/2, (center+maxPalind)/2);
    }
    
    private String generateNewString(String s) {
        String star = "*";
        StringBuffer bufferResult = new StringBuffer();
        for (int i = 0; i < s.length() * 2 + 1; i++) {
            if (i % 2 == 0) {
                bufferResult.append(star);
            }else {
                bufferResult.append(s.charAt(i/2));
            }
        }

        return bufferResult.toString();
    }
    // public String longestPalindrome(String s) {
    //     if (s == null || s.length() == 0) {
    //         return "";
    //     }
    //     String result = "";
    //     String potential = "";
    //     for (int i = 0; i < s.length(); i++) {
    //         int len1 = expandAtCenter(s, i, i);
    //         int len2 = expandAtCenter(s, i, i+1);
    //         int len = Math.max(len1, len2);

    //         int start = i - ((len-1)/2); // same as len/2 when len is odd number 
    //         int end = i + (len/2);

    //         System.out.println("start: " + start);
    //         System.out.println("end: " + end);
    //         System.out.println("len: " + len);

    //         potential = s.substring(start, end+1);
    //         if (potential.length() >= result.length()) {
    //             result = potential;
    //         }
    //     }
    //     return result;
    // }

    // private int expandAtCenter(String s, int left, int right) {
    //     int L = left;
    //     int R = right;

    //     while (L >= 0 && R < s.length() && s.charAt(L) == s.charAt(R)) {
    //         L--;
    //         R++;
    //     }

    //     return R-L-1;
    // }
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

