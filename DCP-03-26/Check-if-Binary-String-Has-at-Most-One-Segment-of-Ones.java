1class Solution {
2    public boolean checkOnesSegment(String s) {
3        // If the string contains "01", it means there is a break in the segment of 1s.
4        return !s.contains("01");
5    }
6}