/*
 * @lc app=leetcode id=8 lang=java
 *
 * [8] String to Integer (atoi)
 */
import java.util.ArrayList;
import java.util.List;
class Solution {
    public int myAtoi(String str) {

        int result;
        boolean resultAssign = false;

        int flag = 0; // -1 or 1

        StringBuffer containInt = new StringBuffer();
        ArrayList<Integer> preApprove = new ArrayList<>();
        preApprove.add(43);
        preApprove.add(45);
        preApprove.add(32);
        for (int i = 48; i <= 57; i++) {
            preApprove.add(i);
        }

        for (int i = 0; i < str.length(); i++) {
            int ascii = (int)(str.charAt(i));
            if (preApprove.contains(ascii)) {
                if (ascii == 43 || ascii == 45) {
                    preApprove.remove(Integer.valueOf(43));
                    preApprove.remove(Integer.valueOf(45));
                    preApprove.remove(Integer.valueOf(32));
                    if (ascii == 43) {
                        flag = 1;
                    }else {
                        flag = -1;
                    }
                }
                else if (ascii == 32) {
                    continue;
                }
                else {
                    if (preApprove.contains(Integer.valueOf(43))) {
                        preApprove.remove(Integer.valueOf(43));
                        preApprove.remove(Integer.valueOf(45));
                        preApprove.remove(Integer.valueOf(32));
                    }
                    containInt.append((char)(ascii));
                }
            }else {
                break;
            }
        }

        String intStr = containInt.toString();
        int zeroPos = 0;
        for (int i = 0; i < intStr.length(); i++) {
            if (intStr.charAt(i) == '0') {
                if (i != intStr.length()-1) {
                    zeroPos++;
                }
            }else {
                break;
            }
        }

        intStr = intStr.substring(zeroPos);
        if (intStr.length() == 0) {
            return 0;
        }
        else if (intStr.length() > 10) {
            return (flag==-1)? Integer.MIN_VALUE :Integer.MAX_VALUE;
        }
        else if (intStr.length() == 10 && Integer.valueOf(intStr.substring(0, intStr.length()-1)) > 214748364) {
            return (flag==-1)? Integer.MIN_VALUE :Integer.MAX_VALUE;
        }
        else if (intStr.length() == 10 && (Integer.valueOf(intStr.substring(0, intStr.length()-1)) == 214748364 &&
                Integer.valueOf(intStr.substring(intStr.length()-1)) > 7 && flag != -1 )) {
            return (flag==-1)? Integer.MIN_VALUE :Integer.MAX_VALUE;
        }
        else if (intStr.length() == 10 && (Integer.valueOf(intStr.substring(0, intStr.length()-1)) == 214748364 &&
                Integer.valueOf(intStr.substring(intStr.length()-1)) > 8 && flag == -1 )) {
            return (flag==-1)? Integer.MIN_VALUE :Integer.MAX_VALUE;
        }
        else {
            if (flag == -1) {
                intStr = "-" + intStr;
            }
            return Integer.valueOf(intStr);
        }
    }
}

