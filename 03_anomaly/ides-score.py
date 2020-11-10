import numpy as np

# CHANGEME:
setval = ["c_1", "c_2", "c_2"]
C = [[1, 0.3, 0.2], [0.3, 1, 0.1], [0.2, 0.1, 1]]
S = [0.2, 0.4, 0.3]

print("The correlation matrix C:")

print(f"     {'   '.join([str(i) for i in setval])}")
for rl, row in zip(setval, C):
    print('%s [%s]' % (rl, ' '.join('%04s' % i for i in row)))

print("- " * 10)

assert len(C) == 3
for i in C:
    assert len(i) == 3

inv_c = [3*[None] for _i in range(3)]

print("The Leibniz formula for the determinant of a 3 × 3 matrix:")
print("detC = c_11​⋅(c_22​⋅c_33​ − c_32​⋅c_23​) − c_12​⋅(c_21​⋅c_33 ​− c_31​⋅c_23​) + c_13​⋅(c_21​⋅c_32​ − c_31​⋅c_22​)\n")

det = (C[0][0] * ((C[1][1]*C[2][2]) - (C[2][1]*C[1][2]))) - (C[0][1] * ((C[1][0] *
                                                                         C[2][2]) - (C[2][0]*C[1][2]))) + (C[0][2] * ((C[1][0]*C[2][1]) - (C[2][0]*C[1][1])))
print(f"{C[0][0]} * ({C[1][1]}*{C[2][2]} - {C[2][1]}*{C[1][2]}) - ", end="")
print(f"{C[0][1]} * ({C[1][0]}*{C[2][2]} - {C[2][0]}*{C[1][2]}) + ", end="")
print(f"{C[0][2]} * ({C[1][0]}*{C[2][1]} - {C[2][0]}*{C[1][1]}) = ")

print(f"{C[0][0]} * ({C[1][1]*C[2][2]:.3f} - {C[2][1]*C[1][2]:.3f}) - ", end="")
print(f"{C[0][1]} * ({C[1][0]*C[2][2]:.3f} - {C[2][0]*C[1][2]:.3f}) + ", end="")
print(f"{C[0][2]} * ({C[1][0]*C[2][1]:.3f} - {C[2][0]*C[1][1]:.3f}) = ")

print(f"{C[0][0]} * ({(C[1][1]*C[2][2]) - (C[2][1]*C[1][2]):.3f}) - ", end="")
print(f"{C[0][1]} * ({(C[1][0]*C[2][2]) - (C[2][0]*C[1][2]):.3f}) + ", end="")
print(f"{C[0][2]} * ({(C[1][0]*C[2][1]) - (C[2][0]*C[1][1]):.3f}) = ")

print(f"{C[0][0] * ((C[1][1]*C[2][2]) - (C[2][1]*C[1][2])):.3f} - ", end="")
print(f"{C[0][1] * ((C[1][0]*C[2][2]) - (C[2][0]*C[1][2])):.3f} + ", end="")
print(f"{C[0][2] * ((C[1][0]*C[2][1]) - (C[2][0]*C[1][1])):.3f} = {det:.3f}")

print("- " * 10)

print(f"The invered correlation matrix at C_ij is (-1)^(i+j) * (new C_ij) / detC")
print(f"Example C_12 = (-1)^(1+2) * (C_21*C_33 - C_31*C23) / detC")

for i in range(3):
    for j in range(3):
        adj = [[n for ii, n in enumerate(row) if ii != i]
               for jj, row in enumerate(C) if jj != j]
        d = adj[0][0]*adj[1][1] - adj[0][1]*adj[1][0]
        print(
            f"C_{i+1}{j+1}\t= (-1)^({i+1}+{j+1}) * ({adj[0][0]}*{adj[1][1]} - {adj[0][1]}*{adj[1][0]}) / {det:.3f}")
        sgn = (-1)**(i+j)
        inv_c[i][j] = sgn * d / det
        print(
            f"\t= {'-' if (-1)**(i+j) < 0 else ''}{adj[0][0]*adj[1][1] - adj[0][1]*adj[1][0]:.3f} / {det:.3f} = {inv_c[i][j]:.3f}")


print("\nThe invered correlation matrix C:")

print(f"     {'     '.join([str(i) for i in setval])}")
for rl, row in zip(setval, inv_c):
    print('%s [%s]' % (rl, ' '.join(f"{i:.3f}" for i in row)))

print("- " * 10)

c = 0
for row in inv_c:
    if c == 1:
        print("SC^(-1)\t= ", end="")
    else:
        print(" \t  ", end="")
    print('[%s]' % (' '.join(f"{i:.3f}" for i in row)), end="")
    c+=1
    if c == 2: 
        print(' * [%s] = ' % (' '.join(f"{i:.3f}" for i in S)))
    else: 
        print()
print()
sc_inv = []
for i in range(len(inv_c[0])):  # this loops through columns of the matrix
    total = 0
    for j in range(len(S)):  # this loops through vector coordinates & rows of matrix
        total += S[j] * inv_c[j][i]
        print(f"({S[j]} * {inv_c[j][i]:.3f}) + ", end="")
    print(f" = {total:.3f}")
    sc_inv.append(total)
print()
print('SC^(-1) = [%s]' % (' '.join(f"{i:.3f}" for i in sc_inv)))
print("- " * 10)


c = 0
for row in S:
    if c == 1:
        print('SC^(-1) * S^T\t= ', end="")
    else:
        print("\t\t  ", end="")
    print(row, end="")
    c+=1
    if c == 2: 
        print(' * [%s] = %f' % (' '.join(f"{i:.3f}" for i in sc_inv), np.array(S).T.dot(sc_inv)))
    else: 
        print()

