def init(f):global ev;ev=f
def isf(x):
 return type(x[0])==int
def s(a,i):
 return[],a[1],[a[2][i]]
def mrg(s,d):
 return s+d[0][0],d[0][1],[x for e in d for x in e[2]]
def rws(x):
 l,*c=x[0];p=prd(c)
 return[(c,x[1],x[2][i*p:p*-~i])for i in range(l)]
def prd(a):
 x=1
 for y in a:x*=y
 return x
fna={}
def gg(a):
 def g(*fs):
  for f in fs:fna[f]=a
  return fs
 return g
mf,df,mm,dm=map(gg,[1,2,3,4])
add,sub,mul,idiv,fdiv,pow=df(
"+","-","*","//","/.","**")
mod  ,eq  ,neq ,gt,lt=df(
"/\\","==","-=",*"><")
gte,lte=df(">=","<=")
sign,absv,cnt,shap=mf(
"*.","*:","#","#.")
red,scan,fold,self,back=mm(
"/","\\","/:","_.","_:")
pms=[sign,absv]
pds=[add,sub,mul,idiv,fdiv,pow,
eq,neq,gt,lt]
def pm(f,tx,x):
 if f==absv:return 0,abs(x)
 if f==sign:return 0,(x>0)-(x<0)
def pd(f,tx,x,ty,y):
 if f==add:return 0,x+y
 if f==sub:return 0,x-y
 if f==mul:return 0,x*y
 if f==fdiv:return 0,x/y
 if f==idiv:return 0,x//y
 if f==mod:return 0,x%y
 if f==pow:return 0,x**y
 if f==eq:return 0,int(x==y)
 if f==neq:return 0,int(x!=y)
 if f==gt:return 0,int(x>y)
 if f==lt:return 0,int(x>y)
def mf(f,x):
 if f==cnt:return[],len(x)


def e2(f,x,y):
 sx,_,dx,sy,_,dy=x+y
 rx,ry,lx,ly=map(len,[
 sx,sy,dx,dy])
 m=min(rx,ry)
 if sx[:m]!=sy[:m]:0/0
 if rx<ry:return mrg(sy,[
  r(f,s(x,i*lx//ly),s(y,i))
  for i in range(ly)])
 return mrg(sx,[
  r(f,s(x,i),s(y,i*ly//lx))
  for i in range(lx)])
def rd(f,x,y):
 sx,tx,dx,sy,ty,dy=x+y
 if f[1]in pds:
  if sx!=[]or[]!=sy:
   return e2(f,x,y)
  t,v=pd(f[1],tx,dx[0],ty,dy[0])
  return[],t,[v]
def e1(f,x):
 return mrg(x[0],[r(f,s(x,i))
  for i in range(len(x[2]))])
def rm(f,x):
 sx,tx,dx=x
 if f[1]in pms:
  if[]!=sx:return e1(f,x)
  t,v=pm(f[1],tx,dx[0])
  return[],t,[v]
 return mf(f,x)
def r(f,*a):
 return[rm,rd][len(a)-1](f,*a)
