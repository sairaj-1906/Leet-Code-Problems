1from typing import List
2class Solution:
3    def letterCombinations(self, digits: str) -> List[str]:
4        if not digits:
5            return []
6
7        # Mapping of digits to corresponding letters
8        phone_map = {
9            "2":"abc", "3":"def", "4":"ghi", "5":"jkl",
10            "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"
11        }
12        result = []
13
14        def backtrack(index: int, path: str):
15            if index == len(digits):
16                result.append(path)
17                return
18            possible_letters = phone_map[digits[index]]
19            for letter in possible_letters:
20                backtrack(index + 1, path + letter)
21            
22        backtrack(0, "")
23        return result