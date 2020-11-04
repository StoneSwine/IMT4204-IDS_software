import numpy as np
import math
np.set_printoptions(precision=2)

# CHANGEME:
fv = np.loadtxt(open("data/probability_table.csv", "rb"), delimiter=",", dtype='float')
iterations=1

c1=int(input("C1: "))
c2=int(input("C2: "))
k=2 # pls no change
cluster_1=[c1]
cluster_2=[c2]
cntroid_1 = fv[c1-1]
cntroid_2 = fv[c2-1]
def d(x, y):
  return math.sqrt(sum([(xi-yi)**2 for xi, yi in zip(x, y)]))

for _ in range(iterations):
  print("Input feature vector to the iteration")
  for i,arr in enumerate(fv):
    if i not in [c1, c2]:
      print(f"V_{i+1}={arr}")
  print("Input centroids")
  print(f"C_1={cntroid_1}")
  print(f"C_2={cntroid_2}")
  print()
  for i,arr in enumerate(fv):
    i=i+1
    if i not in [c1, c2]:
      print(f"d(V_{i},C_{c1})=√(", end="")
      for x,y in zip(arr, cntroid_1):
        print(f"({x}-{y})^2+", end="")
      d1_=d(arr, cntroid_1)
      print(f")={d1_:.3f}")

      print(f"d(V_{i},C_{c2})=√(", end="")
      for x,y in zip(arr, cntroid_2):
        print(f"({x}-{y})^2+", end="")
      d2_=d(arr, cntroid_2)
      print(f")={d2_:.3f}")

      if d1_ < d2_:
        cluster_1.append(i)
        print(f"V_{i} ==> V_{c1}\n")
      else:
        cluster_2.append(i)
        print(f"V_{i} ==> V_{c2}\n")
  
  c1_p = np.array([fv[i-1] for i in cluster_1])
  c2_p = np.array([fv[i-1] for i in cluster_2])

  print("Cluster 1:")
  for i,arr in zip(cluster_1, c1_p):
    print(f"V_{i}={arr}")
  print()

  print("Cluster 2:")
  for i,arr in zip(cluster_2, c2_p):
    print(f"V_{i}={arr}")
  print()

  cntroid_1=np.average(c1_p, axis=0)
  cntroid_2=np.average(c2_p, axis=0)
  print("New centroids: (average of the clusters)")
  
  print("C1'=",end="")
  for column in c1_p.T:
    print(f"({' '.join([str(x) for x in column])})/{len(column)}, ", end="")
  print(f"={cntroid_1}")
  
  print("C2'=",end="")
  for column in c2_p.T:
    print(f"({' '.join([str(x) for x in column])})/{len(column)}, ", end="")
  print(f"={cntroid_2}")
  
  sse = 0
  print(f"\nSSE=",end="")
  for ci,vi,ii,c in [(cntroid_1,c1_p,cluster_1,1), (cntroid_2, c2_p,cluster_2,2)]:
    for i in ii:
      print(f"d(V_{i},C_{c}')^2 + ", end="")
    sse += sum([d(v, ci)**2 for v in vi ])
  print(" = ",end="")

  for ci,vi,ii,c in [(cntroid_1,c1_p,cluster_1,1), (cntroid_2, c2_p,cluster_2,2)]:
    for v in vi:
      print(f"{d(v, ci):.3f}^2 + ", end="")
  print(f"= {sse:.3f}")

  for ci,vi,ii,c in [(cntroid_1,c1_p,cluster_1,1), (cntroid_2, c2_p,cluster_2,2)]:
    for v,i in zip(vi,ii):
      print(f"d(V_{i},C_{c})=√(", end="")
      for x,y in zip(v, ci):
        print(f"({x:.2f}-{y:.2f})^2+", end="")
      d2_=d(v, ci)
      print(f")={d2_:.3f}")
