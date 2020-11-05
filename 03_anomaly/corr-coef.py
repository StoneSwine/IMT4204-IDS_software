#!/usr/bin/env python3
import math
import copy
from itertools import product
import numpy as np

# CHANGEME:
setval = [1, 2, 3, 4]
col=str(input("X or Y in column: "))
probtab = np.loadtxt(open("data/corr-coef-pt.csv", "rb"),
                     delimiter=",", dtype='float')
col_v = row_v = ""


print("The marginal probabilities of all the values of 𝑋")
if col.lower() == "x":
  col_v = "y"
  row_v = "x"
  px = np.sum(probtab, axis=0)
  py = np.sum(probtab, axis=1)
else:
  col_v = "x"
  row_v = "y"
  py = np.sum(probtab, axis=0)
  px = np.sum(probtab, axis=1)

print(f"     {'    '.join([str(i) for i in setval])}     P({col_v})")
for rl, row in zip(setval, probtab):
    print('%s   [%s]' % (rl, ' '.join('%04s' % i for i in row)), end=" ")
    print(f"- {np.sum(row, axis=0):.2f}")

print(f"p({row_v}) " + ' '.join(f"{i:.2f}" for i in px))

print("- " * 10)

# sum of all columns and rows must be one
assert sum(px) == 1
assert sum(py) == 1

print("\nmean and variance for the variable 𝑋:")
m_x = sum([(x*y) for x, y in zip(setval, px)])
print("𝜇_x=", end="")
for x, y in zip(setval, px):
    print(f"{x}*{y:.3f} + ", end="")
print(f"={m_x:.3f}")

s_xs = sum([((x-m_x)**2)*y for x, y in zip(setval, px)])
print("𝜎_x^2=", end="")
for x, y in zip(setval, px):
    print(f"({x}-{m_x})^2 *{y:.3f} + ", end="")
print(" = \n\t",end="")
for x, y in zip(setval, px):
    print(f"{((x-m_x)**2):.3f} *{y:.3f} + ", end="")
print(f"={s_xs:.3f}")


print("\nMean and variance for the variable 𝑌:")
m_y = sum([(x*y) for x, y in zip(setval, py)])
print("𝜇_y=", end="")
for x, y in zip(setval, py):
    print(f"{x}*{y:.3f} + ", end="")
print(f"={m_y:.3f}")

s_ys = sum([((x-m_y)**2)*y for x, y in zip(setval, py)])
print("𝜎_y^2=", end="")
for x, y in zip(setval, py):
    print(f"({x}-{m_y})^2 *{y:.3f} + ", end="")
print(" = \n\t",end="")
for x, y in zip(setval, py):
    print(f"{((x-m_y)**2):.3f} *{y:.3f} +", end="")
print(f"={s_ys:.3f}")


print("\nCovariance: (𝜎_𝑋𝑌 = 𝜇_𝑋𝑌 − 𝜇_𝑋 * 𝜇_𝑌)")
c_v = 0
for x in range(len(setval)):
    for y in range(len(setval)):
        c_v+=(setval[x]*setval[y]*probtab[x][y])
c_v-=(m_x*m_y)

print("𝜎_𝑋𝑌 = ", end="")
for x in range(len(setval)):
    for y in range(len(setval)):
        print(f"{setval[x]}*{setval[y]}*{probtab[x][y]} + ", end="")
print(f"- {m_x}*{m_y} = \n\t",end="")
for x in range(len(setval)):
    for y in range(len(setval)):
        print(f"{(setval[x]*setval[y]*probtab[x][y]):.3f} + ", end="")
print(f"- {(m_x*m_y):.3f} = {c_v:.3f}")


print("\nCorrelation coefficient between X and Y:")
print("P_xy = ( 𝜎_𝑋𝑌 )/( 𝜎_𝑋 * 𝜎_𝑌 )")
print(f"({c_v:.3f})/(√({s_xs:.3f})*√({s_ys:.3f})) = {c_v/(math.sqrt(s_xs)*math.sqrt(s_ys)):.3f}")
