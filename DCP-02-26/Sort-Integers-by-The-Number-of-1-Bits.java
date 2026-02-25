1import java.util.Arrays;
2import java.util.Comparator;
3
4class Solution {
5    public int[] sortByBits(int[] arr) {
6        // Use Integer.bitCount for number of 1s and sort with a comparator
7        Integer[] boxed = new Integer[arr.length];
8        for (int i=0; i<arr.length; i++) boxed[i] = arr[i];
9
10        Arrays.sort(boxed, new Comparator<Integer>(){
11            @Override
12            public int compare(Integer a, Integer b){
13                int ca = Integer.bitCount(a);
14                int cb = Integer.bitCount(b);
15                if (ca != cb) return ca - cb;
16                return a - b;
17            }
18        });
19
20        for (int i=0; i<arr.length; i++) arr[i] = boxed[i];
21        return arr;
22    }
23}