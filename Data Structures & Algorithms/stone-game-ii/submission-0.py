class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        dp = {} # max alice's piles each i and m
        n = len(piles)
        # print(f"{piles=}")
        def dfs(i, m, aTake):
            # print(f">> {piles[i] if i<n else 'N/A'} {m=} {aTake=} e={min(2*m, n-i)}")
            if i >= n:
                # print(f"IF i>=n")
                return 0
            if i == n-1:
                # print(f"IF i==n-1")
                return piles[i] if aTake else 0
            if (i, min(m, n), aTake) in dp:
                # print(f"IF in dp")
                return dp[(i, m, aTake)]

            # DEBUG
            # print(f"ELSE")
            e = min(2*m, n-i)
            maxScore = 0
            num = 0
            cnt = 1
            while cnt <= e:
                num += piles[i - 1 + cnt]
                # print(f"cnt={cnt} num={num}")
                cnt += 1
            # print()
            # DEBUG

            e = min(2*m, n-i)
            maxScore, minScore = 0, float('inf')
            num = 0
            cnt = 1
            while cnt <= e:
                num += piles[i - 1 + cnt]
                if aTake:
                    maxScore = max(
                        maxScore, 
                        num + dfs(i + cnt, max(m, cnt), not aTake) 
                    )
                else:
                    minScore = min(
                        minScore, 
                        dfs(i + cnt, max(m, cnt), not aTake) 
                    )

                cnt += 1
            dp[(i, m if m < n else n, aTake)] = maxScore if aTake else minScore
            return dp[(i, m if m < n else n, aTake)]
        return dfs(0, 1, True)
        # print(dp)
"""
3 1 2 5 7
dp => (l, r, M)


"""