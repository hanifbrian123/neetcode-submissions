class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def isWellFormed(par):
            st = []
            for x in par:
                if x == "(":
                    st.append(x)
                else:
                    if not st: return False
                    st.pop()
            return True

        def dfs(cur: list, cntOpen, cntClose):
            if cntOpen == n and cntClose == n:
                if isWellFormed(cur):
                    res.append(cur.copy())
                return
            if cntOpen < n:
                cur.append("(")
                dfs(cur, cntOpen+1, cntClose)
            elif cntClose < n:
                cur.append(")")
                dfs(cur, cntOpen, cntClose+1)
            
            popEl = cur.pop()
            if popEl == "(" and cntClose < n:
                cur.append(")")
                dfs(cur, cntOpen, cntClose+1)
                cur.pop()

        dfs([], 0, 0)
        toString = ["".join(x) for x in res]
        return toString
        