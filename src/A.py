from AFNS import mrg,rws,isf
from APRS import prs
from AFNS import init,r
def ev(x,*a):
 e=lambda X:ev(X,*a)
 if x==[[1]]:return a[0]
 if x==[[2]]:return a[1]
 if x[0]==0:
  return([],0,[x[1]])if type(x[1])==int else e(x[1])
 if type(x[0])==int:
  if type(x[1])==str:
   return r(x,*a)
  return ev(x[1],*a)
 if x[0][0]==0:
  if len(x)==1:return e(x[0])
  return mrg([len(x)],list(map(e,x)))
 if x[0][0]==1:
  return ev(x[0],e(x[1]))
 if x[0][0]==2:
  return ev(x[0],e(x[1]),e(x[2]))
 print("fall")
 print(x,a)
init(ev)
def dsp(x):
 if isf(x):return[str(x)]
 sx,tx,dx=x
 st=list(map(str,dx))
 if[]==sx:return st
 if len(sx)==1:
  return[" ".join(st)]
 if len(sx)==2:
  r,c=map(range,sx)
  cw=[max(len(st[i*sx[1]+j])
   for i in r)for j in c]
  return[" ".join(
  "{0:>{h}}".format(
  st[i*sx[1]+j],h=cw[j])
  for j in c)for i in r]
 a=list(map(dsp,rws(x)))
 if len(sx)%2==1:
  return[(-~len(sx)//2*" ")
  .join(r[i]for r in a)
  for i in range(len(a[0]))]
 sp=[" "*len(a[0][0])]*(len(sx)//2-1)
 o=[]
 for r in a:o+=sp+r
 return o[len(sp):]
while 1:
 i=input(" "*4)
 if""==i:break
 d=ev(prs(i))
 print("\n".join(dsp(d)))
