1#include <string>
2#include <algorithm>
3using namespace std;
4class Solution {
5public:
6    bool isPalindrome(int x) 
7    {
8        //Negative numbers are never palindromes
9        if (x < 0)
10        return false;
11
12        //convert to string
13        string s = to_string (x);
14
15        //create a reverse copy
16        string reverse_s = s;
17        reverse(reverse_s.begin(), reverse_s.end());
18
19        //compare
20        return s == reverse_s;
21    }
22};