def divide(dividend, divisor):
    signal = 1 if (dividend < 0 and divisor < 0) or (dividend > 0 and divisor > 0) else -1
    dividend = abs(dividend)
    divisor = abs(divisor)
    if dividend < divisor:
        return 0
    now_dicisor, result = divisor, 1
    while dividend-now_dicisor > now_dicisor:
        now_dicisor += now_dicisor
        result += result
    result += divide(dividend-now_dicisor, divisor)
    if signal < 0:
        result = -result
    if result not in range(-2147483648, 2147483648):
        result = 2147483647
    return result


def main():
    tests = [(10, 3), (7, -3), (100, 20), (100, -2), (-2147483648, -1)]
    for test in tests:
        print("{0}/{1}={2}".format(test[0], test[1], divide(test[0], test[1])))


if __name__ =="__main__":
    main()
    