class Solution:
    # def minArray(self, numbers: List[int]) -> int:
    def minArray(self, numbers):
        if not numbers:
            return 
        if len(numbers) == 1:
            return numbers[0]
        for i in range(1, len(numbers)):
            if numbers[i] < numbers[i-1]:
                return numbers[i]
        return numbers[0]


def main():
    tests = [[3, 4, 5, 1, 2], [2, 2,2 ,0, 1], [1, 3, 5]]
    solution = Solution()
    for test in tests:
        print(solution.minArray(test))


if __name__ == "__main__":
    main()