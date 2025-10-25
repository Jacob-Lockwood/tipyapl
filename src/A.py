from LANG import*

def dsp(x):
  if isf(x):return x
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
  print("\n".join(dsp(ex(i)[1])))
