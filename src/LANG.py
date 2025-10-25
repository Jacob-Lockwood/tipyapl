from MOD import*
dg="0123456789"
vrs={"A":([],0,[100])}
def p(s,**a):
  x,r,n,i,d=s[0],s[1:],"",1,1
  if x in dg:
    while s!=""and s[0]in dg:
      n+=s[0];s=s[1:]
    return s,([],0,[int(n)])
  if s[:2]in fs:
    return s[2:],(0,s[:2])
  if s[0]in fs:
    return r,(0,x)
  elif"("==x:
    s,e=ex(r,**a)
    return s[1:],e
  elif"{"==x:
    while i<len(s)and d>0:
      d+=(s[i]=="{")-(s[i]=="}");i+=1
    return s[i:],(3,s[1:i-1])
  elif"'"==x:return r,x
  elif x!=x.lower():
    if x in a:return r,a[x]
    return r,vrs[x]
  elif"=:"==s[:2]:return s[3:],(4,s[2])
  elif'"'==x:
    s,f=mx(r)
    if isf(f):
      return s,([],1,[f])
    return s,f[2][0]
# 0=f,1=mm,2=dm,3=dfn,4=assign
def mx(s,**a):
  while" "==s[0]:s=s[1:]
  if s[:2]in mm:
    x=s[:2]
    s,f=mx(s[2:],**a)
    return s,(1,x,f)
  if s[0]in mm and s[:2]not in fs:
    x=s[0]
    s,f=mx(s[1:],**a)
    if("_",[])==(x,f[0]):return s,([],0,[-f[2][0]])
    return s,(1,x,f)
  s,l=p(s,**a)
  if s[:2]in dm:
    x=s[:2]
    s,r=mx(s[2:],**a)
    return s,(2,x,l,r)
  if s[:1]in dm:
    x=s[0]
    s,r=mx(s[1:],**a)
    return s,(2,x,l,r)
  return s,l
def ex(s,**a):
  if":="==s[1:3]:
    n=s[0];s,x=ex(s[3:],**a)
    vrs[n]=x
    return s,x
  s,x=mx(s,**a)
  f=[]
  while""!=s and")"!=s[0]:
    if isf(x):
      f.append(x);x=a["X"]
    s,o=mx(s,**a)
    while isf(o):
      f.append(o)
      if""==s or")"==s[0]:break
      s,o=mx(s,**a)
    for t in f[:-1]:
      if t[0]==4:vrs[t[1]]=x
      else:x=rm(ex,t,x)
    if"'"==o:
      s,r=mx(s,**a)
      if"Y"not in a:o=rm(ex,r,a["X"])
      else:o=rd(ex,r,a["X"],a["Y"])
    if o[0]==4:vrs[o[1]]=x
    elif isf(o):x=rm(ex,o,x)
    else:x=rd(ex,f[-1],x,o)
    f=[]
  for t in f:x=rm(ex,t,x)
  return s,x
