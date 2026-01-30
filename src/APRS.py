from AFNS import fna
def t():
 global s
 x=s[0];s.remove(x);return x
def d(s):
 x,dg="","0123456789"
 while s[0]in dg:x+=t()
 return x
def n(s):
 r=d(s)
 if r:return 0,(
  float(r+t()+d(s))if"."==s[0]
  else int(r))
def st(s):
 if'"'!=s[0]:return
 o=t()
 while'"'!=s[0]:
  x=t();o+=x
  if"\\"==x:o+=t()
 if'"'!=s[0]:0/0
 return 0,eval(o+t())
def prm(s):
 k="".join(s[:2])
 if k in fna:
  return[fna[k],t()+t()]
 if s[0]in fna:
  return[fna[s[0]],t()]
def par(s):
 if"("!=s[0]:return
 t();x=ex(s)
 if")"!=t():0/0
 return x
def ex(s):
 m=["e"]
 while["EOF"]!=s:
  while" "==s[0]:t()
  x=(prm(s)or n(s)or st(s)
    or par(s))
  if x==None:break
  m.append(x)
 return m
def rd(e):
 if"e"!=e[0]:return e
 e=list(map(rd,e[1:]))
 a=+(e[0][0]>0)
 n=s=[[1]]if a else[e.pop(0)]
 for x in e:
  if x[0]==0:s.append(x)
  elif n[0][0]==2 and[]==n[2]:
   a=max(a,x[0])
   n[2]=[x,[[1]]]if x[0]else x
  else:
   s=[];n=[x,n]+[s]*(x[0]==2)
 return[a,n]
def prs(str):
 global s;s=list(str)+["EOF"]
 return rd(ex(s))