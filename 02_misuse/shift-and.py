
# CHANGEME
w="origin"
S="original"

B={}
or_mask=[0]*len(w)
or_mask[len(w)-1]=1
D=[0]*len(w)

for i in list(set(w)):
  tmp=[0]*len(w)
  for pos in [pos for pos, char in enumerate(w) if char == i]:
    tmp[len(w)-pos-1]=1
  B[i]=tmp

print(B)
print(f"D={D}")
print(f"D <-- ((D << 1) OR 1) AND B[S[i]]")

for i,c in enumerate(S):
  print(f"S[{i+1}]={c}")
  if B.get(c):
    b=B.get(c)
  else:
    b=[0]*len(w)
  str_current_b = "".join([str(x) for x in b])
  str_d = "".join([str(x) for x in D])
  print(f"B[S[{i+1}]]=B[{c}]={str_current_b}")
  D.pop(0)
  D.append(0)
  D = [a or b for a, b in zip(D, or_mask)]
  print(f"D = (({str_d} << 1) OR {''.join([str(x) for x in or_mask])}) = {''.join([str(x) for x in D])}", end="")
  D = [a and b for a, b in zip(D, b)]
  print(f" AND {str_current_b} = {''.join([str(x) for x in D])}")

  if D[0] == 1:
    print(f"Ocurrence found at pos {i+1} in S - {c}") 

  print("- "*10)

