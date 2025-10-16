from FNS import*
dg="0123456789"
mm=".\\"
dm="o"
def p(s,**a):
  x,r,n,i,d=s[0],s[1:],"",1,1
  if x in dg:
    while s!=""and s[0]in dg:
      n+=s[0];s=s[1:]
    return s,([],0,[int(n)])
  elif"("==x:
    s,e=ex(r);return s[1:],e
  elif"{"==x:
    while i<len(s)and d>0:
      d+=(s[i]=="{")-(s[i]=="}");i+=1
    return s[i:],(3,s[1:i-1])
  elif"'"==x:return r,x
  elif x!=x.lower():return r,a[x]
  return r,(0,x)
# 0=f,1=mm,2=dm,3=dfn
def mx(s,**a):
  if s[0]in mm:
    x=s[0]
    s,f=mx(s[1:])
    return s,(1,x,f)
  s,l=p(s,**a)
  if""!=s and s[0]in dm:
    x=s[0]
    s,r=mx(s[1:])
    return s,(2,x,l,r)
  return s,l
def ex(s,**a):
  s,x=mx(s,**a)
  while""!=s and")"!=s[0]:
    s,o=mx(s,**a)
    f=[]
    while isf(o):
      f.append(o)
      if""==s or")"==s[0]:break
      s,o=mx(s,**a)
    for t in f[:-1]:x=rm(t,x)
    if isf(o):x=rm(o,x)
    else:x=rd(f[-1],x,o)
  return s,x
def e1(f,x):
  d=[rm(f,([],x[1],[z]))for z in x[2]]
  return(x[0],d[0][1],[x[2][0]for x in d])
def rm(f,x):
  if f[0]==3:return ex(f[1],X=x)[1]
  sx,tx,dx=x
  if f[1]in pf:
    if[]!=sx:return e1(f,x)
    t,r=pm(f,tx,dx[0])
    return[],t,[r]
  if f[0]==0:return mf(f[1],x)
  if f[0]==1:
    if"."==f[1]:return e1(f,x)
    if"\\"==f[1]:
      o=([],tx,dx[:1])
      for d in dx[1:]:o=rd(f[2],o,([],tx,[d]))
      return o
def e2(f,x,y):
  sx,tx,dx,sy,ty,dy=x+y
  if sx==sy:
    return mrg(sx,[rd(f,([],tx,[dx[i]]),([],ty,[dy[i]]))for i in range(len(dx))])
  if[]==sx:
    return mrg(sy,[rd(f,x,([],ty,[z]))for z in dy])
  elif[]==sy:
    return mrg(sx,[rd(f,([],tx,[z]),y)for z in dx])
  elif sx==sy[:len(sx)]:
    g=len(dy)/len(dx)
def rd(f,x,y):
  if f[0]==3:return ex(f[1],X=x,Y=y)[1]
  sx,tx,dx,sy,ty,dy=x+y
  if f[1]in pf:
    if sx!=[]or[]!=sy:
      return e2(f,x,y)
    t,v=pd(f,tx,dx[0],ty,dy[0])
    return[],t,[v]
  if f[0]==0:return df(f[1],x,y)
  elif f[0]==2:
    if"o"==f[1]:return rd(f[2],rm(f[3],x),rm(f[3],y))
