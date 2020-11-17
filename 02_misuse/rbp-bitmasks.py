# CHANGEME
w = input("Pattern: ")

B = {}
done = []

for i in list(set(w)):
    tmp = [1]*len(w)
    for pos in [pos for pos, char in enumerate(w) if char == i]:
        tmp[len(w)-pos-1] = 0
    B[i] = tmp

for c in w:
    if c not in done:
        print(f"B[{c}]: {''.join([str(i) for i in B.get(c)])}")
        done.append(c)
