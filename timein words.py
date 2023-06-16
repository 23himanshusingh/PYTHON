def timeInWords(h, m):
    d=[[1,'one'],[2,'two'],[3,'three'],[4,'four'],[5,'five'],[6,'six'],[7,'seven'],[8,'eight'],[9,'nine'],[10,'ten'],[11,'eleven'],[12,'twelve'],[13,'thirteen'],[14,'fourteen'],[16,'sixteen'],[17,'seventeen'],[18,'eighteen'],[19,'nineteen']]
    d1=[[20,'twenty'],[30,'thirty'],[40,'forty'],[50,'fifty']]
    for i in range(len(d)):
        if d[i][0]==h and m==0:
            s=d[i][1]+" o' clock"
        elif d[i][0]==h and m==30:
            s='half past '+d[i][1]
        elif d[i][0]==h and m==15:
            s='quarter past '+d[i][1]
        elif d[i][0]==h and m>30 and 60-m==15:
            s='quarter to '+d[i+1][1]
        elif d[i][0]==h and m>30 and m!=45:
            diff=(60-m)
            if diff>0 and diff<10:
                for j in range(len(d)):
                    if d[j][0]==diff:
                        s1=d[j][1]
                if s1=='one':
                    s=s1+' minute to '+d[i+1][1]
                else:
                    s=s1+' minutes to '+d[i+1][1]
            elif diff>10 and diff<20:
                for j in range(len(d)):
                    if d[j][0]==diff:
                        s1=d[j][1] 
                s=s1+' minutes to '+d[i+1][1]
            else:
                q1=(diff//10)*10;q2=diff%10
                for j in range(len(d1)):
                    if d1[j][0]==q1:
                        s1=d1[j][1]
                if q2!=0:
                    for k in range(len(d)):
                        if d[k][0]==q2:
                            s2=d[k][1]
                    s=s1+' '+s2+' minutes to '+d[i+1][1]
                else:
                    s=s1+' minutes to '+d[i+1][1]
        elif d[i][0]==h and m<10 and m>0:
            for j in range(len(d)):
                if d[j][0]==m:
                    s1=d[j][1]
            if s1=='one':
                s=s1+' minute past '+d[i][1]
            else:
                q1=(m//10)*10;q2=m%10
                for j in range(len(d1)):
                    if d1[j][0]==q1:
                        s1=d1[j][1]
                if q2!=0:
                    for j in range(len(d)):
                        if d[j][0]==q2:
                            s2=d[j][1]
                    s=s1+' '+s2+' minutes past '+d[i+1][1]
                else:
                    s=s1+' minutes past '+d[i+1][1]
        elif d[i][0]==h and m<20 and m>10 and m!=15:
            for j in range(len(d)):
                if d[j][0]==m:
                    s1=d[j][1] 
            s=s1+' minutes past '+d[i][1]
        elif d[i][0]==h and m>20 and m<30:
            q1=(m//10)*10;q2=m%10
            for j in range(len(d1)):
                if d1[j][0]==q1:
                    s1=d1[j][1]
            if q2!=0:
                for j in range(len(d)):
                    if d[j][0]==q2:
                        s2=d[j][1]
                s=s1+' '+s2+' minutes past '+d[i][1]
            else:
                s=s1+' minutes past '+d[i][1] 
    return s
print(timeInWords(int(input()),int(input())))
            

