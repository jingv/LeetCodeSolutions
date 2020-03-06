class Solution:
    def myAtoi(self, str):
        new_str = str.strip()
        rule = "-+1234567890"
        result = 0
        try:      
            if new_str[0] not in rule:
                return 0
            sub_str = ""
            for i in new_str:
                if i not in rule:
                    break
                else:
                    sub_str += i
            result = eval(sub_str)
            if result not in range(-2**31, 2**31):
                result =  -2**31 if result < 0 else 2**31-1            
        finally:
            return result


def main():
    solution = Solution()
    tests = ["42", "   -42", "4193 with words", "words and 987", "-91283472332", "", "+", "-"]
    # tests = ["   -42"]
    for test in tests:
        print(solution.myAtoi(test))


if __name__ == "__main__":
    main()