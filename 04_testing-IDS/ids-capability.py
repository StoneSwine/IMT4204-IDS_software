#!/usr/bin/env python3
import math
from decimal import *
from itertools import product
import numpy as np

# CHANGEME:
TP=200
TN=700
FP=90
FN=10

tot = TP+TN+FP+FN

print(f"N={tot}")

probtab = np.array([[TN/tot,FN/tot],[FP/tot,TP/tot]]).astype(Decimal)

print("The marginal probabilities of all the values of 𝑋")
print(probtab)
print("- " * 10)

px = np.sum(probtab, axis=0)
py = np.sum(probtab, axis=1)

print("P(X):", px)
print("P(Y):", py)

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
print("- " * 10)

print("The conditional entropy 𝐻(𝑋|𝑌)")
print("𝐻(𝑋|𝑌)=−∑y∑x𝑃(𝑥,𝑦)log2𝑃(𝑥|𝑦)")
hxy = 0
print("-(", end="")
for k, i in zip(py, probtab):
  for j in i:
    hxy += (j * math.log2(j / k))
    print(f"{j}*log2({j}/{k:.3f})", end=" + ")
hxy = -hxy
print(f") = {hxy:.3f} ")
print("- " * 10)

print("The intrusion detection capability:")
print("C_I_D=(𝐻(𝑋)−𝐻(𝑋|𝑌)) / 𝐻(𝑋)")
print(f"({hx:.3f} - {hxy:.3f})/{hx:.3f} = {((hx - hxy)/hx):.3f}")

