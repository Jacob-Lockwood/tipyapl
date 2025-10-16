def isf(x):
  return type(x[0])==int
def mrg(s,d):
  return s+d[0][0],d[0][1],[x for e in d for x in e[2]]
def prd(a):
  x=1
  for y in a:x*=y
  return x
pf="+-"
def pm(f,t,x):
  if"+"==f[1]:return 0,x+1
  if"-"==f[1]:return 0,x-1
def pd(f,tx,x,ty,y):
  if"+"==f[1]:return 0,x+y
  if"-"==f[1]:return 0,x-y
def mf(f,x):
  s,t,d=x
  if","==f:return[prd(s)],t,d
  if"f"==f:return[1]+s,t,d
  if"@"==f:return[],t,d[:1]
  if"r"==f:return d,0,list(range(d[0]))
def df(f,x,y):
  sx,tx,dx,sy,ty,dy=x+y
  if","==f:
    if tx!=ty:0/0
    if sx==[]and[]==sy:
      return[2],tx,dx+dy
    rx,ry=len(sx),len(sy)
    if sx[1:]==sy[1:]:return[prd(sx[:1])+prd(sy[:1])]+sx[1:],tx,dx+dy
    if sx[rx-ry:]==sy:
      return[sx[0]+1]+sx[1:],tx,dx+dy*prd(sx[1:rx-ry])
    if sy[ry-rx:]==sx:
      return[sy[0]+1]+sy[1:],tx,dx*prd(sy[1:ry-rx])+dy
  if"@"==f:
    c=prd(sx[1:])
    return sy,tx,[z for i in dy for z in dx[i*c:-~i*c]]
  if"["==f:return x
  if"]"==f:return y
