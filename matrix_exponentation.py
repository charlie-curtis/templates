MOD = 10**9 + 7
def mat_multiply(A,B):
    m1,n1 = len(A), len(A[0])
    m2,n2 = len(B), len(B[0])

    if n1 != m2:
        raise ValueError("Wrong dimensions for multiplication")

    out = [[0 for _ in range(n2)] for _ in range(m1)]
    for i in range(m1):
        for j in range(n2):
            for k in range(n1):
                #all pairs should be from the ith row, jth col
                a = A[i][k]*B[k][j]
                out[i][j]+=a
                out[i][j] %=MOD
    return out


def mat_exp(A, t):
    m,n = len(A), len(A[0])
    if t == 0:
        raise ValueError("Why is T = 0?")
    if t == 1:
        return A

    if t % 2 == 0:
        B = mat_exp(A, t//2)
        return mat_multiply(B,B)
    else:
        B = mat_exp(A, t//2)
        return mat_multiply(mat_multiply(B,B),A)
