
# CHANGEME
w="snort"
S="snorting"

B={}
D=[1]*len(w)

for i in list(set(w)):
  tmp=[1]*len(w)
  for pos in [pos for pos, char in enumerate(w) if char == i]:
    tmp[len(w)-pos-1]=0
  B[i]=tmp

print(B)
print(f"D={D}")
print(f"D <-- (D << 1) OR B[S[i]]")

for i,c in enumerate(S):
  print(f"S[{i+1}]={c}")
  if B.get(c):
    b=B.get(c)
  else:
    b=[1]*len(w)
  str_current_b = "".join([str(x) for x in b])
  str_d = "".join([str(x) for x in D])
  print(f"B[S[{i+1}]]=B[{c}]={str_current_b}")
  D.pop(0)
  D.append(0)
  print(f"D = (({str_d} << 1) = {''.join([str(x) for x in D])}", end="")
  D = [a or b for a, b in zip(D, b)]
  print(f" OR {str_current_b} = {''.join([str(x) for x in D])}")
  if D[0] == 0:
    print(f"Ocurrence found at pos {i+1} in S - {c}") 
  print("- "*10)

