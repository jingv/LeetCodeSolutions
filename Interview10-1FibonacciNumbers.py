class Solution:
    # def fib(self, n: int) -> int:
    def fib(self, n):
        '''
        递归
        '''
        if n == 1 or n == 2:
            return 1
        else:
            return self.fib(n-2) + self.fib(n-1)

    def fib2(self, n):
        '''
        循环
        '''
        if n <= 0:
            return 0
        if n <= 2:
            return 1
        first, second, count = 1, 1, 2
        while count != n:
            first, second = second, first+second
            count += 1
        return second % 1000000007


def main():
    tests = [2, 5, 100]
    solution = Solution()
    for test in tests:
        print(solution.fib(test), " =?= ", solution.fib2(test))
        # print(solution.fib2(test))


if __name__ == "__main__":
    main()
