import copy
# CHANGEME
w = input("Pattern: ")
S = str(input("Search string (s): "))
K = int(input("K: "))
B = {}
done = []
R = []
R_p = []


def sify(ar):
    return "".join([str(i) for i in ar])

def shor(x,y):
    v1 = copy.copy(x)
    v2 = copy.copy(y)
    v1.pop(0)
    v1.append(0)
    return [a or b for a, b in zip(v1, v2)]

def lsh(x):
    v1 = copy.copy(x)
    v1.pop(0)
    v1.append(0)
    return v1

def inv(x):
    return [i^1 for i in x]


for i in range(K+1):
    R.append([1]*(len(w)-i) + [0]*i)
    R_p.append([])

for i in list(set(w)):
    tmp = [1]*len(w)
    for pos in [pos for pos, char in enumerate(w) if char == i]:
        tmp[len(w)-pos-1] = 0
    B[i] = tmp

for c in w:
    if c not in done:
        print(f"B[{c}]: {''.join([str(i) for i in B.get(c)])}")
        done.append(c)

for i, c in enumerate(R):
    print(f"R_{i} => {c}")

print("R_0' = (R_0 << 1) OR B[S_j]")
print(
    "R_i' = ((R_i << 1) OR B[S_j]) AND R_i-1 AND ((R_i-1 << 1) OR NOT B[S_j]) AND (R_i-1' << 1)")
for i, c in enumerate(S):
    if B.get(c):
        b = B.get(c)
    else:
        b = [1]*len(w)

    print(f"S_{i+1} = {c}")

    print(f"R_O' = ({sify(R[0])} << 1) OR {sify(b)})", end = "")
    R_p[0] = shor(R[0], b)
    print(f" = {sify(R_p[0])}")
    print("- "*10)
    for k in range(1,K+1):
        print(f"R_{k}' = (({sify(R[k])} << 1) OR {sify(b)}) AND {sify(R[k-1])} AND (({sify(R[k-1])} << 1) OR NOT {sify(b)}) AND ({sify(R_p[k-1])} << 1)")
        s1 = shor(R[k], b)
        s2 = shor(R[k-1], inv(b))
        s3 = lsh(R_p[k-1])
        print(f"R_{k}' = {sify(s1)} AND {sify(R[k-1])} AND {sify(s2)} AND {sify(s3)}")
        s4 = [x and y for x,y in zip(s1, R[k-1])]
        s5 = [x and y for x,y in zip(s2, s3)]
        print(f"R_{k}' = {sify(s4)} AND {sify(s5)}", end = "")
        R_p[k] = [x and y for x,y in zip(s4, s5)]
        print(f" = {sify(R_p[k])}")
        
        print("- "*10)
    
    print(f"set R to be R'")
    R = None
    R = copy.copy(R_p)

    for x in range(len(R)):
        if R[x][0] == 0:
            print(f"A match is found in R_{x}, on position {i+1} in S")

    print("- "*10)




        

