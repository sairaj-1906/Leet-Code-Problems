1import java.util.ArrayList;
2import java.util.List;
3class Solution {
4    public List<String> generateParenthesis(int n) {
5        List<String> result = new ArrayList<>();
6        // Start the backtracking process
7        backtrack(result, new StringBuilder(), 0, 0, n);
8        return result;
9    }
10
11    private void backtrack(List<String> result, StringBuilder currentString, int open, int close, int max){
12        // Base case: If the string is fully formed (length is 2 * n)
13        if (currentString.length() == max * 2){
14            result.add(currentString.toString());
15            return;
16        }
17        // Choice 1: Add an open parenthesis if we still have some left
18        if (open < max){
19            currentString.append("(");
20            backtrack(result, currentString, open + 1, close, max);
21            // Backtrack: remove the character we just added before exploring other branches
22            currentString.deleteCharAt(currentString.length() - 1);
23        }
24        // Choice 2: Add a close parenthesis if it's valid to do so
25        if (close < open){
26            currentString.append(")");
27            backtrack(result, currentString, open, close + 1, max);
28            // Backtrack: remove the character we just added
29            currentString.deleteCharAt(currentString.length() - 1);
30        }
31    }
32}