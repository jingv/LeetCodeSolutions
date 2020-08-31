class Solution:
    # def findContinuousSequence(self, target: int) -> List[List[int]]:
    def findContinuousSequence(self, target):
        """
        这个应该算是滑动窗口？
        """
        result = []
        li = list(range(1, (target+1)//2+1))
        if len(li) == 1:
            return result
        for i in range(len(li)):
            for j in range(i+2, len(li)+1):
                if sum(li[i: j]) == target:
                    result.append(li[i:j])
                    break
                elif sum(li[i:j]) > target:
                    break
        return result



def main():
    tests = [9 ,15, 1, 2, 3]
    solution = Solution()
    for test in tests:
        print(solution.findContinuousSequence(test))
    

if __name__ == "__main__":
    main()
    