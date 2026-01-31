1#include <iostream>
2#include <vector>
3#include <string>
4using namespace std;
5class Solution {
6public:
7    string longestCommonPrefix(vector<string>& strs) {
8        if (strs.empty())
9        return "";
10        //Start with the first string as the initial prefix
11        string prefix = strs[0];
12
13        for (int i=1; i<strs.size(); i++){
14            //Shorten the prefix until it matches the start of strs[i]
15            while (strs[i].find(prefix) != 0){
16                prefix = prefix.substr(0, prefix.length() - 1);
17
18                //If the prefix becomes empty, no common prefix exists
19                if (prefix.empty())
20                return "";
21            }
22        }
23        return prefix;
24        
25    }
26};
27
28/*int main()
29{
30    Solution sol;
31    vector<string> example_1 = {"flower", "flow", "flight"};
32    vector<string> example_2 = {"dog", "racecar", "car"};
33
34    cout<< "Example 1: "<< sol.longestCommonPrefix(example_1)<< endl;
35    cout<< "Example 2: "<< sol.longestCommonPrefix(example_2)<< endl;
36
37}
38*/