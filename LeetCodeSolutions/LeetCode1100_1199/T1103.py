class Solution:
    # def distributeCandies(self, candies: int, num_people: int) -> List[int]:
    def distributeCandies(self, candies, num_people):
        # 1 <= candies <= 10^9
        # 1 <= num_people <= 1000
        count, index, result = 0, 0, [0]
        # while len(result) < num_people:
        #     result.append(0)
        result = result * num_people
        while candies > 0:
            if index >= num_people:
                index = 0
            count += 1
            result[index] += count if candies >= count else candies
            candies -= count            
            index += 1
        return result

    def distributeCandies_authority(self, candies, num_people):
        ans = [0] * num_people
        i = 0
        while candies != 0:
            ans[i % num_people] += min(i + 1, candies)
            candies -= min(i + 1, candies)
            i += 1
            return ans


def main():
    solution = Solution()
    tests = [(7, 4), (10, 3)]
    for candies, people in tests:
        print(solution.distributeCandies(candies, people))
    

if __name__ == "__main__":
    main()