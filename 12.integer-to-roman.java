/*
 * @lc app=leetcode id=12 lang=java
 *
 * [12] Integer to Roman
 */
class Solution {
    public String intToRoman(int num) {
        HashMap<Integer, String> map = new HashMap<>();
        map.put(1, "I"); map.put(5, "V"); map.put(10, "X");
        map.put(50, "L"); map.put(100, "C"); map.put(500, "D"); map.put(1000, "M");

        String strNum = String.valueOf(num);

        int digit = 0;
        int ten = 0;
        int hundred = 0;
        int thousand = 0;

        switch (strNum.length()) {
            case 1:
                digit = Integer.valueOf(strNum);
                break;
            case 2:
                digit = Integer.valueOf(strNum.substring(1));
                ten = Integer.valueOf(strNum.substring(0, 1));
                break;
            case 3:
                digit = Integer.valueOf(strNum.substring(2));
                ten = Integer.valueOf(strNum.substring(1, 2));
                hundred = Integer.valueOf(strNum.substring(0, 1));
                break;
            case 4:
                digit = Integer.valueOf(strNum.substring(3));
                ten = Integer.valueOf(strNum.substring(2, 3));
                hundred = Integer.valueOf(strNum.substring(1, 2));
                thousand = Integer.valueOf(strNum.substring(0, 1));
                break;
                default:
                    break;
        }


        StringBuffer result = new StringBuffer();

        // thousand
        for (int i = 0; i < thousand; i++) {
            result.append(map.get(1000));
        }

        // hundred
        if (hundred < 4) {
            for (int i = 0; i < hundred; i++) {
                result.append(map.get(100));
            }
        }else if (hundred == 4) {
            result.append(map.get(100));
            result.append(map.get(500));
        }else if (hundred < 9) {
            result.append(map.get(500));
            for (int i = 0; i < (hundred - 5); i++) {
                result.append(map.get(100));
            }
        }else {
            result.append(map.get(100));
            result.append(map.get(1000));
        }

        // ten
        if (ten < 4) {
            for (int i = 0; i < ten; i++) {
                result.append(map.get(10));
            }
        }else if (ten == 4){
            result.append(map.get(10));
            result.append(map.get(50));
        }else if (ten < 9) {
            result.append(map.get(50));
            for (int i = 0; i < (ten - 5); i++) {
                result.append(map.get(10));
            }
        }else {
            result.append(map.get(10));
            result.append(map.get(100));
        }

        // digit
        if (digit < 4) {
            for (int i = 0; i < digit; i++) {
                result.append(map.get(1));
            }
        }else if(digit == 4) {
            result.append(map.get(1));
            result.append(map.get(5));
        }else if (digit < 9) {
            result.append(map.get(5));
            for (int i = 0; i < (digit - 5); i++) {
                result.append(map.get(1));
            }
        }else {
            result.append(map.get(1));
            result.append(map.get(10));
        }

        return result.toString();
    }
}

