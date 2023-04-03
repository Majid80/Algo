import sys

def solve(plates, n, k, p):
    dp = [[-1 for _ in range(p+1)] for _ in range(n+1)]
    dp[0][0] = 0

    for i in range(1, n+1):
        b_so_far = 0
        for j in range(p+1):
            for take in range(k+1):
                if j+take > p:
                    break
                dp[i][j+take] = max(dp[i][j+take], dp[i-1][j] + b_so_far)
                if take != k:
                    b_so_far += plates[i-1][take]

    return dp[n][p]

def main():
    input = sys.stdin.readline
    t = int(input())

    for tt in range(t):
        n, k, p = map(int, input().split())

        plates = []
        for i in range(n):
            row = list(map(int, input().split()))
            plates.append(row)

        result = solve(plates, n, k, p)
        print(f"Case #{tt+1}: {result}")

if __name__ == "__main__":
    main()
The solve fun