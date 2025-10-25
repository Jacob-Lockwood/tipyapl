from FNS import*
mm=list("/\\_")+["].","[."]
dm=["o","]:","[:"]
def rm(ex,f,x):
  def e1(f,x):
    d=[rm(ex,f,([],x[1],[z]))for z in x[2]]
    return(x[0],d[0][1],[x[2][0]for x in d])
  if f[0]==3:return ex(f[1],X=x)[1]
  sx,tx,dx=x
  if f[1]in pf:
    if[]!=sx:return e1(f,x)
    t,r=pm(f,tx,dx[0])
    return[],t,[r]
  if f[0]==0:return mf(f[1],x)
  if f[0]==1:
    if"/"==f[1]:
      o,*r=rws(x)
      for d in r:o=rd(ex,f[2],o,d)
      return o
    if"\\"==f[1]:
      o,*r=rws(x);a=[o]
      for d in r:
        o=rd(ex,f[2],o,d)
        a.append(o)
      return mrg(sx[:1],a)
    if"_"==f[1]:
      if f[2][0]==0:
        return un1(f[2][1],x)
def rd(ex,f,x,y):
  def e2(f,x,y):
    sx,tx,dx,sy,ty,dy=x+y
    if sx==sy:
      return mrg(sx,[rd(ex,f,([],tx,[dx[i]]),([],ty,[dy[i]]))for i in range(len(dx))])
    if[]==sx:
      return mrg(sy,[rd(ex,f,x,([],ty,[z]))for z in dy])
    elif[]==sy:
      return mrg(sx,[rd(ex,f,([],tx,[z]),y)for z in dx])
    elif sx==sy[:len(sx)]:
      g=len(dy)/len(dx)
  if f[0]==3:return ex(f[1],X=x,Y=y)[1]
  sx,tx,dx,sy,ty,dy=x+y
  if f[1]in pf:
    if sx!=[]or[]!=sy:
      return e2(f,x,y)
    t,v=pd(f,tx,dx[0],ty,dy[0])
    return[],t,[v]
  if f[0]==0:return df(f[1],x,y)
  if f[0]==1:
    if"[."==f[1]:return rm(ex,f[2],x)
    if"]."==f[1]:return rm(ex,f[2],y)
  elif f[0]==2:
    if"o"==f[1]:return rd(ex,f[2],rm(ex,f[3],x),rm(ex,f[3],y))
    # if"]:"==f[1]:return 

# \{X+Y*(Y*)}
# \{+Y*'].*}
# (X+Y)*(Y*)
# +]:*     = {X+Y*}
# +]]*[[*  = {X+Y*(X*Y)}
# {+Y*'*}
