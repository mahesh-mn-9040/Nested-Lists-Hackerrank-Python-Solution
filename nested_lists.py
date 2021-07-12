n=int(input())
res=[]
grade=[]
for i in range(n):
    name=input()
    marks=float(input())
    res.append([name,marks])
    grade.append(marks)
grade=sorted(set(grade)) ########store list of sorted unique elements   
#print(grade[1])
m=grade[1]
s=[]
for i in res:
        if m==i[1]:
            s.append(i[0])
final=sorted(s)
for _ in final:
    print(_)
