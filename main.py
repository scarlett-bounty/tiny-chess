import json,os,urllib.request as u
U=os.environ['MAKEFUN_ENV_URL']
V=(0,100,320,330,500,900,0)
R='KKKKLMMGLJIKKKKOLLMPMMOQUUUUKKKKACEECGKLELMNEKNOELNOEKMNCGKKACEEGIIIIKLKILLMKKLMJLLMIKLMIKKKGIIIKKKLJKKKJKKKJKKKJKKKJKKKLMMMKKKKGIIJIKKKIKLLKKLLJKLLIKLLIKKKGIIJOQMKOOKKIGGGGEECECCAECCAECCAECCA'
W=[]
for r in zip(*[iter(R)]*4):W+=[(ord(c)-75)*5 for c in r+r[::-1]]
F=[(),(),(-33,-31,-18,-14,14,18,31,33),(-17,-15,15,17),(-16,-1,1,16),0,(-17,-16,-15,-1,1,15,16,17)]
F[5]=F[3]+F[4]
X=136
N=[0,10**5]
I=-10**9
def H(p,b):
 with u.urlopen(U+p,json.dumps(b).encode())as r:return json.load(r)
def Y(f):
 b=[0]*128;w=k=-1;u=f.split();s=112
 for h in u[0]:
  if h=='/':s-=24
  elif h.isdigit():s+=int(h)
  else:
   q='PNBRQK'.index(h.upper())+1
   if h.islower():q=-q
   b[s]=q
   if abs(q)==6:w,k=(s,k)if q>0 else(w,s)
   s+=1
 t=2*(u[1]=='w')-1
 v=sum((c in u[2])<<i for i,c in enumerate('KQkq'))
 p=-1 if u[3]=='-'else(int(u[3][1])-1)*16+ord(u[3][0])-97
 return b,t,v,p,w,k
def K(b,s,y):
 for z in(-15*y,-17*y):
  x=s+z
  if not x&X and b[x]==y:return 1
 for o,v,w in((F[2],2,0),(F[6],6,0),(F[3],3,1),(F[4],4,1)):
  for z in o:
   x=s+z
   while not x&X:
    q=b[x]
    if q:
     if q==v*y or w and q==5*y:return 1
     break
    if not w:break
    x+=z
 return 0
def P(d,s,o,t):
 d+=[(s,o,r)for r in((5,4,3,2)if(o>>4)==(7*t+7)>>1 else(0,))]
def G(b,t,c,e,p=0):
 d=[];a=d.append
 for s,q in enumerate(b):
  if s&X or not q or(q>0)!=(t>0):continue
  y=abs(q)
  if y==1:
   z=16*t;o=s+z
   if not o&X and not b[o]:
    if(o>>4)==(7*t+7)>>1:P(d,s,o,t)
    elif not p:
     a((s,o,0));w=s+2*z
     if(s>>4)==(7-5*t)//2 and not b[w]:a((s,w,0))
   for z in(z-1,z+1):
    o=s+z
    if o&X:continue
    if b[o]and(b[o]>0)!=(t>0):P(d,s,o,t)
    elif o==e:a((s,o,0))
  elif y in(2,6):
   for z in F[y]:
    o=s+z
    if not o&X and((not b[o]and not p)or(b[o]and(b[o]>0)!=(t>0))):a((s,o,0))
   if y==6 and not p:
    for f,w,i,r,k,j in((4,6,1,7,(5,6),(4,5,6)),(4,2,2,0,(3,2,1),(4,3,2)),(116,118,4,119,(117,118),(116,117,118)),(116,114,8,112,(115,114,113),(116,115,114))):
     if s==f and c&i and b[r]==4*t and all(not b[x]for x in k)and all(not K(b,x,-t)for x in j):a((f,w,0))
  else:
   for z in F[y]:
    o=s+z
    while not o&X and not b[o]:
     if not p:a((s,o,0))
     o+=z
    if not o&X and b[o]and(b[o]>0)!=(t>0):a((s,o,0))
 return d
def M(b,s,w):
 f,o,r=w;b=b[:];s=s[:];q=b[f]
 if abs(q)==1 and o==s[2] and b[o]==0:b[o-16*s[0]]=0
 b[o]=r*s[0]if r else q;b[f]=0
 if abs(q)==6:
  s[3+(s[0]<0)]=o
  if abs(o-f)==2:
   u=o+1 if o>f else o-2;v=o-1 if o>f else o+1;b[v]=b[u];b[u]=0
  s[1]&=~(3<<2*(s[0]<0))
 for x,v in((0,2),(7,1),(112,8),(119,4)):
  if f==x or o==x:s[1]&=~v
 s[2]=(f+o)//2 if abs(q)==1 and abs(o-f)==32 else-1
 s[0]=-s[0]
 return b,s
def L(b,s,p=0):
 return[w for w in G(b,s[0],s[1],s[2],p)if not K((c:=M(b,s,w))[0],c[1][3+(c[1][0]>0)],c[1][0])]
def E(b):
 s=0;z=y=0
 for q,p in enumerate(b):
  if q&X or not p:continue
  t=abs(p);i=(q>>4)*8+(q&7)
  if p<0:i^=56
  if t==6:
   if p>0:z=i
   else:y=i
   continue
  e=V[t]+W[(t-1)*64+i];s+=e if p>0 else-e
 s+=W[320+z]-W[320+y]
 return s
def O(d,b):
 return sorted(d,key=lambda w:-(V[abs(b[w[1]])]*10-V[abs(b[w[0]])])if b[w[1]]else 0)
def S(b,s,e,A,B):
 N[0]+=1
 if N[0]>=N[1]:return E(b)*s[0]
 if e<=0:
  t=E(b)*s[0]
  if t>=B:return B
  if t>A:A=t
  d=O(L(b,s,1),b)
 else:
  d=L(b,s)
  if not d:return-100000-e if K(b,s[3+(s[0]<0)],-s[0])else 0
  d=O(d,b)
 for j in d:
  r=-S(*M(b,s,j),e-1,-B,-A)
  if N[0]>=N[1]:return A
  if r>=B:return B
  if r>A:A=r
 return A
def B(f,l,x=10**5):
 D=lambda w:'%c%d%c%d%s'%((w[0]&7)+97,(w[0]>>4)+1,(w[1]&7)+97,(w[1]>>4)+1,'nbrq'[w[2]-2]if w[2]else'')
 b,t,cc,e,a,i=Y(f);s=[t,cc,e,a,i];N[1]=x
 d=[w for w in L(b,s)if D(w)in l];d=O(d,b);j=d[0];N[0]=0;v=1
 while N[0]<N[1]and v<32:
  h=j;r=A=I
  for w in d:
   p=-S(*M(b,s,w),v-1,I,-A)
   if N[0]>=N[1]:break
   if p>r:r=p;h=w
   if p>A:A=p
  else:j=h;v+=1
 return D(j)
def Z():
 while(g:=H('/game',{}))['status']!='done':
  while g['status']=='your_move':g=H('/move',{'game':g['game'],'move':B(g['fen'],g['legal_moves'])})
if __name__=='__main__':Z()
