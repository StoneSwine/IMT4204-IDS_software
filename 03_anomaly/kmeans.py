import numpy as np
import math
import os
from operator import itemgetter
np.set_printoptions(precision=3)

# CHANGEME:
fv = np.loadtxt(open(os.path.join(os.path.dirname(__file__), "data/kmeans-pt.csv"), "rb"), delimiter=",", dtype='float')
iterations=1
if input("Euclidian distance OK? ").lower() in ["n","no","noo"]:
  print("Exiting...")
  exit()
k=int(input("K: "))
clusters=[None]*k
centroids=[None]*k
c_val=[None]*k

for i in range(k):
  clusters[i] = set()
  clusters[i].add(int(input(f"C{i+1}: ")))
  centroids[i]=fv[list(clusters[i])[0]-1]

def d(x, y):
  return math.sqrt(sum([(xi-yi)**2 for xi, yi in zip(x, y)]))

for _ in range(iterations):
  print("Input feature vector to the iteration")
  for i,arr in enumerate(fv):
    if i not in clusters:
      print(f"V_{i+1}={arr}")
  print("Input centroids")
  for i,v in enumerate(centroids):
    print(f"C_{i+1}={v}")
  print()
  for i,arr in enumerate(fv):
    i=i+1
    d_vals = []
    for ci,c in enumerate(centroids):
      print(f"d(V_{i},C_{ci+1})=√(", end="")
      for x,y in zip(arr, c):
        print(f"({x}-{y})^2+", end="")
      d_vals.append(d(arr, c))
      print(f")={d_vals[-1]:.3f}")

    clusters[np.argmin(d_vals)].add(i)
    print(f"V_{i} ==> C_{np.argmin(d_vals)+1}\n")

  for i in range(k):
    c_val[i] = np.array([fv[i-1] for i in clusters[i]])
    print(f"Cluster {i+1}:")
    for i,arr in zip(clusters[i], c_val[i]):
          print(f"V_{i}={arr}")
    print()

  print("New centroids: (average of the clusters)")
  centroids=[None]*k  
  for i,c in enumerate(c_val):
    centroids[i] = np.average(c, axis=0)

    print(f"C{i+1}'=",end="")
    for column in c.T:
      print(f"({'+'.join([str(x) for x in column])})/{len(column)}, ", end="")
    print(f"={centroids[i]}")
    print()

  sse = 0
  print(f"\nSSE=",end="")
  for i in range(k):
    for ci,vi,ii,c in [(centroids[i],c_val[i],clusters[i],i)]:
      for j in ii:
        print(f"d(V_{j},C_{c+1}')^2 + ", end="")
      sse += sum([d(v, ci)**2 for v in vi ])

  print(" = ",end="")
  print()

  for i in range(k):
    for ci,vi,ii,c in [(centroids[i],c_val[i],clusters[i],i)]:
      for v in vi:
        print(f"{d(v, ci):.3f}^2 + ", end="")
  print(f"= {sse:.3f}")

  for i in range(k):
    for ci,vi,ii,c in [(centroids[i],c_val[i],clusters[i],i)]:
      for v,j in zip(vi,ii):
        print(f"d(V_{j},C_{c+1})=√(", end="")
        for x,y in zip(v, ci):
          print(f"({x:.2f}-{y:.2f})^2+", end="")
        d2_=d(v, ci)
        print(f")={d2_:.3f}")

