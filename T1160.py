#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T1160.py
@Time    :   2020/03/17 08:42:09
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class Solution:
    # def countCharacters(self, words: List[str], chars: str) -> int:
    # hashmap
    # 执行用时 :96 ms, 在所有 Python3 提交中击败了96.76%的用户
    # 内存消耗 :13.9 MB, 在所有 Python3 提交中击败了5.11%
    def countCharacters(self, words, chars):
        char_map, result = {}, 0
        for char in chars:
            if char in char_map:
                char_map[char] += 1
            else:
                char_map[char] = 1
        for word in words:
            for w in word:
                if word.count(w) > char_map.get(w, 0):
                    break
            else:
                result += len(word)
        return result


def main():
    tests = [
        (["cat", "bt", "hat", "tree"], "atach"),
        (["hello", "world", "leetcode"], "welldonehoneyr"),
        ([], [])
        ]
    solution = Solution()
    for words, chars in tests:
        print(solution.countCharacters(words, chars))


if __name__ == "__main__":
    main()
