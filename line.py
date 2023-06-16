delvout=[]
delvin=[]
vout=[0.0322,0.94111,1.88,2.81,3.74,4.53,4.66,4.70,4.72,4.73]
vin=[0.03435,1.006,2.007,3.003,4.009,5.005,6.006,7.002,8.003,8.99]
for i in range(len(vout)-1):
    diffout=vout[i+1]-vout[i]
    diffout=round(diffout,3)
    delvout.append(diffout)
print('delvout',delvout)
for j in range(len(vin)-1):
    diffin=vin[j+1]-vin[j]
    diffin=round(diffin,3)
    delvin.append(diffin)
print('delvin',delvin)
percent=[]
for k in range(9):
    ans=round((delvout[k]/delvin[k]),3)
    percent.append(ans)
print('percent line regulation',percent)



VFL=[1.09,1.31,2.26,2.98,3.64,4.22]
per=[]
for i in range(6):
    k=((4.741/VFL[i])-1)*100
    k=round(k,3)
    per.append(k)
pernew=[]
for i in range(6):
    per[i]=str(per[i])
    pernew.append(per[i])
print(" ".join(pernew))
print("kl")



