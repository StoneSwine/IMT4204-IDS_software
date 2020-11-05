import numpy as np
import math
old = [0.2, 0.3, 0.2, 0.1, 0.2]
n = [0.5]
w = int(input("width(𝜇): "))
old_mean = np.average(old, axis=0)
old_stddev = math.sqrt((1/(len(old)-1))*(sum([(x-old_mean)**2 for x in old])))

print(f"𝜇=", end="")
print(f"({'+'.join([str(x) for x in old])})/{len(old)}", end="")
print(f"={old_mean}")
print(f"𝜎=√( {1}/{len(old)-1 }(", end="")
for i in old:
    print(f"({i}-{old_mean})^2 + ", end="")
print(f"=\n\t", end="")
for i in old:
    print(f"({i-old_mean:.2f})^2 + ", end="")
print(f"))={old_stddev:.3f}")

print(f"max(0,𝜇-{w}𝜎) to min(1,𝜇+{w}𝜎)")
print(f"max(0,{old_mean:.3f}-{w}*{old_stddev:.3f}) to min(1,{old_mean:.3f}+{w}*{old_stddev:.3f})", end="")
print(
    f" = {max([0,(old_mean-(w*old_stddev))]):.3f} to {min([1,(old_mean+(w*old_stddev))]):.3f}")

for i in n:
    if float(max([0, (old_mean-(w*old_stddev))])) >= float(i) <= float(min([1, (old_mean+(w*old_stddev))])):
        print(f"the new measurement ({i}) is considered normal")
    else:
        print(f"the new measurement ({i}) is not normal")
