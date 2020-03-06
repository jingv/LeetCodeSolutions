class Solution:
    # def numWays(self, n: int) -> int:
    def numWays(self, n):
        '''
        递归
        '''
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.numWays(n-1) + self.numWays(n-2)

    def numWays2(self, n):
        if n <= 0:
            return n
        li_numWays = [1, 2]
        if n <= 2:
            return li_numWays[n - 1]
        count = 2
        while count < n:
            li_numWays[0], li_numWays[1] = li_numWays[1], li_numWays[0] + li_numWays[1]
            count += 1
        return li_numWays[1]%1000000007


def main():
    tests = [2, 7]
    solution = Solution()
    for test in tests:
        print(solution.numWays(test), " =?= ", solution.numWays2(test))


if __name__ == "__main__":
    main()