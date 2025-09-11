data = [4, -30, 100, -100, 123, 1, 0, -1, -4]

if __name__ == '__main__':
    result = list(sorted(data, key=abs, reverse=True))
    print(result)

    result_with_lambda = list(sorted(data, key=lambda x: -abs(x)))
    print(result_with_lambda)
