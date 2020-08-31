#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Interview17-13re-space-lcci.py
@Time    :   2020/07/09 08:49:57
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class Solution():
    def respace(self, dictionary, sentence):
        length = len(sentence)
        if length == 0:
            return 0

        word_set = set(dictionary)
        # 存储dictionary中最长字符串的长度
        max_len = max([len(_) for _ in word_set])

        # len[dp] = len[sentence] + 1 方便边界处理
        dp = [0] * (length + 1)

        for i in range(1, length + 1):
            # 当前位置最多有i个未识别字符（遍历到当前位置，一个都没有识别）
            temp = [i]
            for s in range(1, max_len + 1):
                if s > i:
                    break
                # if sentence[i - s:i] in word_set, means: 字符被识别，未识别的字符数 + 0
                # else: 未识别的字符数就是当前取到的字符总数
                temp.append(dp[i - s] + (0 if sentence[i - s:i] in word_set else s))
            # print("temp = ", temp)
            dp[i] = min(temp)
        # print(dp)
        return dp[-1]


def main():
    solution = Solution()
    tests = [
        [
            ["looked", "just", "like", "her", "brother"],
            "jesslookedjustliketimherbrother"
        ]
    ]
    for dictionary, sentence in tests:
        print(solution.respace(dictionary, sentence))


if __name__ == "__main__":
    main()
