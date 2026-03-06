class Solution:
    def pascalTriangle(self, r, c):
        triangle = []
        for i in range(r):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
            triangle.append(row)

        return triangle[r-1][c-1]


sol = Solution()
pt = sol.pascalTriangle(4, 2)
print(pt)