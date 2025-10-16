from LANG import*

def dsp(x):
  if isf(x):return x
  sx,tx,dx=x
  st=list(map(str,dx))
  if[]==sx:return st[0]
  if len(sx)==1:
    return" ".join(st)
  if len(sx)==2:
    r,c=map(range,sx)
    cw=[max(len(st[i*sx[1]+j])
        for i in r)for j in c]
    return"\n".join(" ".join(
      "{0:>{h}}".format(
      st[i*sx[1]+j],h=cw[j])
      for j in c)for i in r)
while 1:
  i=input(" "*4)
  if""==i:break
  print(dsp(ex(i)[1]))
