def max_steps(n, k, c, numbers):
    numbers.sort(reverse=True)
    steps = 0

    while numbers:
        selected = numbers[:k]
        numbers = numbers[k:]
        steps += 1

        for i in range(1, len(selected)):
            if selected[i] < selected[i - 1] * c:
                return steps - 1

    return steps

def main():
    t = int(input())
    for _ in range(t):
        n, k, c = map(int, input().split())
        numbers = list(map(int, input().split()))
        result = max_steps(n, k, c, numbers)
        print(result)

if __name__ == "__main__":
    main()
