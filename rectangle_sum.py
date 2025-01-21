        m,n = len(mat), len(mat[0])
        pref = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                a = pref[i+1][j]
                b = pref[i][j+1]
                c = pref[i][j]
                pref[i+1][j+1] = a + b - c + mat[i][j]
        def get(r, c):
            return pref[r+1][c+1]
        def queryByCorner(r1, c1, r2, c2):
            #r1, c1 (A)      #r1,c2 (B)


            #r2, c1 (C)     #r2,c2 (D)
            a = get(r1-1,c1-1)
            b = get(r1-1,c2)
            c = get(r2,c1-1)
            d = get(r2,c2)
            res = d + a - c - b
            return res
