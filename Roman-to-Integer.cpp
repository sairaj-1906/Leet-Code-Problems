1#include <iostream>
2#include <string>
3#include <unordered_map>
4using namespace std;
5class Solution {
6public:
7    int romanToInt(string s) 
8    {
9        //Map to store Roman values
10        unordered_map<char, int> romanMap =
11        {
12            {'I',1}, {'V',5}, {'X',10}, {'L',50}, {'C',100}, {'D',500}, {'M',1000}
13        };
14        int total = 0;
15        int n = s.length();
16        for (int i=0; i<n; i++)
17        {
18            //Check if we are at the last character OR if the current value is >= the next value
19            if (i == n-1 || romanMap[s[i]] >= romanMap[s[i+1]])
20            {
21                //Normal addition case (e.g., VI, II, MC)
22                total += romanMap[s[i]];
23            }
24            else
25            {
26                //Subtraction case (e.g., IV, IX, CM)
27                //Because current value is less than nect value
28                total -= romanMap[s[i]];
29            }
30        }
31        return total;
32    }
33};