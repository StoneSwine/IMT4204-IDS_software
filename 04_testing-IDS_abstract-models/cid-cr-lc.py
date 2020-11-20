#!/usr/bin/env python3
import math
import copy
from decimal import *
from itertools import product
import numpy as np

# CHANGEME:
TP=50
TN=800
FP=100
FN=50

tot = TP+TN+FP+FN

print(f"N={tot}")

probtab = np.array([[TN/tot,FN/tot],[FP/tot,TP/tot]]).astype(Decimal)

print("The marginal probabilities of all the values of 𝑋")

row_labels = ["N", "A"];
px = np.sum(probtab, axis=0)
py = np.sum(probtab, axis=1)
print("     N    A     P(y)")
for row_label, row in zip(row_labels, probtab):
  print('%s  [%s]' % (row_label, ' '.join('%04s' % i for i in row)), end=" ")
  print(f"- {np.sum(row, axis=0):.2f}")

print("p(x) " + ' '.join(f"{i:.2f}" for i in px))

print("- " * 10)

# sum of all columns and rows must be one
assert sum(px) == 1
assert sum(py) == 1

print("Entropy of the input")
print("𝐻(𝑋)=−∑𝑃(𝑥)log2𝑃(𝑥)")
hx = -sum([i * math.log2(i) for i in px])
print("-(", end="")
for i in px:
  print(f"{i:.3f}*log2({i:.3f})", end=" + ")
print(f") = {hx:.3f}")
print("- " * 10)


print("The joint probabilities:")
print("P(X|Y)=𝑃(𝑥,𝑦)/𝑃(𝑦)")
for k, i in zip(py, probtab):
  for j in i:
    print(f"({j}/{k:.3f})={(j/k):.2f}")
print("- " * 10)

print("The conditional entropy 𝐻(𝑋|𝑌)")
print("𝐻(𝑋|𝑌)=−∑y∑x𝑃(𝑥,𝑦)log2𝑃(𝑥|𝑦)")
hxy = 0
print("-(", end="")
for k, i in zip(py, probtab):
  for j in i:
    hxy += (j * math.log2(j / k))
    print(f"{j}*log2({(j/k):.2f})", end=" + ")
hxy = -hxy
print(f") = {hxy:.3f} ")
print("- " * 10)

print("The intrusion detection capability:")
print("C_I_D=(𝐻(𝑋)−𝐻(𝑋|𝑌)) / 𝐻(𝑋)")
cid = ((hx - hxy)/hx)
print(f"({hx:.3f} - {hxy:.3f})/{hx:.3f} = {cid:.3f}")

print("\n##### Abstract IDS models ####\n")
px_ol = copy.copy(px)
probtab = np.array([[TN/tot,0],[FP/tot,FN/tot],[0,TP/tot]]).astype(Decimal)
print("The marginal probabilities of all the values of 𝑋")
row_labels = ["N", "U", "A"];
px = np.sum(probtab, axis=0)
pz = np.sum(probtab, axis=1)
print("     N    A     P(z)")
for row_label, row in zip(row_labels, probtab):
  print('%s  [%s]' % (row_label, ' '.join('%04s' % i for i in row)), end=" ")
  print(f"- {np.sum(row, axis=0):.2f}")

print("p(x) " + ' '.join(f"{i:.2f}" for i in px))
print("- " * 10)

# sum of all columns and rows must be one
assert sum(px) == 1
assert sum(pz) == 1

if set(px_ol) == set(px):
  print("Entropy of the input is still the same as above")
  print(f"recall, H(𝑋)=−∑𝑃(𝑥)log2𝑃(𝑥) = {hx:.3f}")
  print("- " * 10)
else:
  print("Entropy of the input")
  print("𝐻(𝑋)=−∑𝑃(𝑥)log2𝑃(𝑥)")
  hx = -sum([i * math.log2(i) for i in px])
  print("-(", end="")
  for i in px:
    print(f"{i:.3f}*log2({i:.3f})", end=" + ")
  print(f") = {hx:.3f}")
  print("- " * 10)

print("The joint probabilities:")
print("𝑃(𝑥,𝑦)/𝑃(𝑦)=P(X|Y)")
for k, i in zip(pz, probtab):
  for j in i:
    if j != 0:
      print(f"({j}/{k:.3f})={(j/k):.2f}")
print("- " * 10)

print("The conditional entropy 𝐻(𝑋|𝑌)")
print("𝐻(𝑋|𝑌)=−∑y∑x𝑃(𝑥,𝑦)log2𝑃(𝑥|𝑦)")
hxy = 0
print("-(", end="")
for k, i in zip(pz, probtab):
  for j in i:
    if j != 0:
      hxy += (j * math.log2(j / k))
      print(f"{j}*log2({(j/k):.2f})", end=" + ")
hxy = -hxy
print(f") = {hxy:.3f} ")
print("- " * 10)

print("The feature representation capability:")
print("C_r=(𝐻(𝑋)−𝐻(𝑋|𝑌)) / 𝐻(𝑋)")

cr = ((hx - hxy)/hx)
print(f"({hx:.3f} - {hxy:.3f})/{hx:.3f} = {cr:.3f}")

print("- " * 10)

print("The classification information loss:")
print(f"L_c = C_r - C_I_D = {cr:.3f} - {cid:.3f} = {(cr-cid):.3f}")

