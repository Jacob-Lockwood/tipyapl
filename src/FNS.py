def isf(x):
  return type(x[0])==int
def mrg(s,d):
  return s+d[0][0],d[0][1],[x for e in d for x in e[2]]
def rws(x):
  l,*c=x[0];p=prd(c)
  return[(c,x[1],x[2][i*p:p*-~i])for i in range(l)]
def prd(a):
  x=1
  for y in a:x*=y
  return x
pf=list("+-*")+["/.","/:","//","**","==","/=","gt","lt","ge","le"]
fs=pf+list("f,@r#[]")
def pm(f,t,x):
  if"+"==f[1]:return 0,x+1
  if"-"==f[1]:return 0,x-1
  if"*"==f[1]:return 0,(x>0)-(x<0)
def pd(f,tx,x,ty,y):
  if"+"==f[1]:return 0,x+y
  if"-"==f[1]:return 0,x-y
  if"*"==f[1]:return 0,x*y
  if"/."==f[1]:return 0,x/y
  if"/:"==f[1]:return 0,x%y
  if"//"==f[1]:return 0,x//y
  if"**"==f[1]:return 0,x**y
  if"=="==f[1]:return 0,int(x==y)
  if"/="==f[1]:return 0,int(x!=y)
def mf(f,x):
  s,t,d=x
  if","==f:return[prd(s)],t,d
  if"f"==f:return[1]+s,t,d
  if"@"==f:return[],t,d[:1]
  if"r"==f:
    if[]==s:return d,0,list(range(d[0]))
    o=[int(i/prd(d[j:]))%d[j]
       for i in range(prd(d))
       for j in range(s[0])]
    return d+s,0,o
  if"#"==f:return[len(s)],0,s
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
    return sy+sx[1:],tx,[z for i in dy for z in dx[i*c:-~i*c]]
    
  if"["==f:return x
  if"]"==f:return y
def un1(f,x):
  s,t,d=x
  if"#"==f:return d,0,list(range(prd(d)))
