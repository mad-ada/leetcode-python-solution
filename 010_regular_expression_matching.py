class Solution(object):
    # DP solution:
    # let res[i][j]: if s[0...i-1] matches p[0...j-1]
    # if p[j-1] != "*"
    #   res[i][j] = res[i-1][j-1] && (s[i-1] == p[j-1] || p[j-1] == ".")
    # if p[j-1] == "*"
    #   res[i][j] = res[i-2][j] || (s[i-i] == p[j-2] || p[j-2] == ".") && res[i-1][j]
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m = len(s)
        n = len(p)

        res = [[False for j in range(n+1)] for i in range(m+1)]
        for j in range(n+1):
            res[0][j] = j > 1 and p[j-1] == "*" and res[0][j-2]

        for i in range(m+1):
            for j in range(n+1):
                if p[j-1] != "*":
                    res[i][j] = (s[i-1] == p[j-1] or p[j-1] == ".") and res[i-1][j-1]
                else:
                    res[i][j] = (s[i-1] == p[j-2] or p[j-2] == ".") and res[i-2][j] or res[i][j-2]
        return res[m][n]

if __name__ == "__main__":
    print(Solution().isMatch("abab", "a*b*"))

