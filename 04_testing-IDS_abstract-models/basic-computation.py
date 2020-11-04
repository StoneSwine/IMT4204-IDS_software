
#CHANGEME
tp=200
tn=700
fp=90
fn=10
n=tp+tn+fp+fn
tpr=tp/(tp+fn)
tnr=tn/(tn+fp)
fpr=fp/(fp+tn)
fnr=fn/(fn+tp)
pi=(tp+fn)/n
pa=(pi*tpr)+((1-pi)*fpr)
print(f"N   =𝑇𝑃 +𝑇𝑁 +𝐹𝑃 + 𝐹𝑁 ={tp}+{tn}+{fp}+{fn}={n}")
print(f"𝑇𝑃𝑅 =𝑃(𝐴|𝐼)=𝑇𝑃 /𝑇𝑃 +𝐹𝑁 ={tp}/{tp}+{fn}={tpr:.3f}")
print(f"𝑇𝑁𝑅 =𝑃(¬𝐴|¬𝐼)=𝑇𝑁 /𝑇𝑁 + 𝐹𝑃 ={tn}/{tn}+{fp}={tnr:.3f}")
print(f"𝐹𝑃𝑅 =𝑃(𝐴|¬𝐼)=𝐹𝑃 /𝐹𝑃 + 𝑇𝑁 ={fp}/{fp}+{tn}={fpr:.3f}")
print(f"𝐹𝑁𝑅 =𝑃(¬𝐴|𝐼)=𝐹𝑁 /𝐹𝑁 +𝑇𝑃 ={fn}/{fn}+{tp}={fnr:.3f}")
print(f"𝑃(𝐼)=𝑇𝑃 + 𝐹𝑁 /𝑁 ={tp}+{fn}/{n}={pi:.3f}")
print(f"𝑃(𝐴)=𝑃(𝐼)𝑃(𝐴|𝐼)+𝑃(¬𝐼)𝑃(𝐴|¬𝐼)={pi:.3f}*{tpr:.3f}+(1-{pi:.3f})*{fpr:.3f}={pa:.3f}")
print(f"𝑃𝑃𝑉 =𝑃(𝐼|𝐴)=𝑃(𝐼)𝑃(𝐴|𝐼)/𝑃(𝐴)=({pi:.3f}*{tpr:.3f})/{pa:.3f}={((pi*tpr)/pa):.3f}")
