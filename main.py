import json,os,urllib.request
U=os.environ["MAKEFUN_ENV_URL"]
def H(p,b):return json.load(urllib.request.urlopen(U+p,json.dumps(b).encode()))
P="KKKKLMMGLJIKKKKOLLMPMMOQUUUUKKKKACEECGKLELMNEKNOELNOEKMNCGKKACEEGIIIIKLKILLMKKLMJLLMIKLMIKKKGIIIKKKLJKKKJKKKJKKKJKKKJKKKLMMMKKKKGIIJIKLKILLLKKLLJKLLIKLLIKKKGIIJOQMKOOKKIGGGGEECECCAECCAECCAECCA"
W=(0,100,320,330,500,900,0);A=(-33,-31,-18,-14,14,18,31,33);D=(-17,-15,15,17);F=(-16,-1,1,16);C=D+F;N=[0];O=[ord(c)-75 for c in P]
def u(m):return"%c%d%c%d%s"%((m[0]&7)+97,(m[0]>>4)+1,(m[1]&7)+97,(m[1]>>4)+1,"nbrq"[m[2]-2]if m[2] else"")
def Y(z):
 b=[0]*128;q=z.split();w=k=-1;s=112;f=0
 for ch in q[0]:
  if ch=="/":s-=16;f=0
  elif ch.isdigit():f+=int(ch)
  else:
   sq=s+f;p="PNBRQK".index(ch.upper())+1
   if ch.islower():p=-p
   b[sq]=p
   if p==6:w=sq
   if p==-6:k=sq
   f+=1
 t=1 if q[1]=="w"else-1;c=sum(1<<i for i,ch in enumerate("KQkq")if ch in q[2]);e=-1
 if q[3]!="-":e=int(q[3][1])*16+ord(q[3][0])-113
 return b,t,c,e,w,k
def T(b,s,y):
 for o,p in((A,2),(C,6),((-15*y,-17*y),1)):
  for d in o:
   t=s+d
   if not t&0x88 and b[t]==p*y:return 1
 for o,p in((D,3),(F,4)):
  for d in o:
   t=s+d
   while not t&0x88 and not b[t]:t+=d
   if not t&0x88 and b[t]in(p*y,5*y):return 1
 return 0
def G(b,s,z=False):
 p=[];t=s[0]
 for q in range(128):
  if q&0x88:continue
  pc=b[q]
  if pc==0 or(pc>0)!=(t>0):continue
  v=abs(pc)
  if v==1:
   d=16*t;o=q+d
   if not o&0x88 and b[o]==0:
    if(o>>4)==(7 if t>0 else 0):p.extend((q,o,r)for r in(5,4,3,2))
    elif not z:
     p.append((q,o,0));w=q+2*d
     if(q>>4)==(1 if t>0 else 6)and b[w]==0:p.append((q,w,0))
   for o in(d-1,d+1):
    u=q+o
    if u&0x88:continue
    if b[u]!=0 and(b[u]>0)!=(t>0):
     if(u>>4)==(7 if t>0 else 0):p.extend((q,u,r)for r in(5,4,3,2))
     else:p.append((q,u,0))
    elif u==s[2]:p.append((q,u,0))
  elif v==2 or v==6:
   for o in A if v==2 else C:
    u=q+o
    if u&0x88:continue
    if b[u]==0 and not z or b[u]and(b[u]>0)!=(t>0):p.append((q,u,0))
   if v==6 and not z:
    for d in(1,-1):
     bit=1<<(d<0)+(t<0)*2
     if s[1]&bit and b[q+d]==0 and b[q+2*d]==0 and not(d<0 and b[q+3*d])and b[q+3*d-(d<0)]==4*t and not T(b,q,-t)and not T(b,q+d,-t)and not T(b,q+2*d,-t):p.append((q,q+2*d,0))
  else:
   o=D if v==3 else F if v==4 else D+F
   for e in o:
    u=q+e
    while not u&0x88:
     x=b[u]
     if x and(x>0)!=(t>0):p.append((q,u,0))
     if x:break
     if not z:p.append((q,u,0))
     u+=e
 o=[]
 for m in p:
  n,w=M(b,s,m);k=w[3+(s[0]<0)]
  if not T(n,k,-s[0]):o.append(m)
 o.sort(key=lambda m:-(W[abs(b[m[1]])]*10-W[abs(b[m[0]])])if b[m[1]] else 0)
 return o
def M(b,s,m):
 f,t,p=m;n=b[:];o=s[:];pc=n[f]
 if abs(pc)==1 and t==o[2] and n[t]==0:n[t-16*o[0]]=0
 n[t]=p*o[0]or pc;n[f]=0
 if abs(pc)==6:
  o[3+(o[0]<0)]=t;o[1]&=~3 if o[0]>0 else~12
  if abs(t-f)==2:d=(t>f)*2-1;r=3*d-(d<0);n[f+d]=n[f+r];n[f+r]=0
 for q,v in((0,2),(7,1),(112,8),(119,4)):
  if f==q or t==q:o[1]&=~v
 o[2]=(f+t)//2 if abs(pc)==1 and abs(t-f)==32 else-1
 o[0]=-o[0];return n,o
def E(b):
 s=0
 for q in range(128):
  if q&0x88:continue
  p=b[q]
  if not p:continue
  t=abs(p);r=q>>4 if p>0 else 7-(q>>4);f=q&7;f=7-f if f>3 else f
  v=W[t]+O[(t-1)*32+r*4+f]*5
  s+=v if p>0 else-v
 return s
def S(b,s,d,a,be,x=100000):
 N[0]+=1
 if N[0]>=x:return E(b)*s[0]
 k=s[3+(s[0]<0)];c=T(b,k,-s[0])
 if d==0 and not c:
  st=E(b)*s[0]
  if st>=be:return be
  if st>a:a=st
 ms=G(b,s,d==0 and not c)
 if not ms:
  if c:return-100000-d
  if d==0:return a
  return 0
 for m in ms:
  n,o=M(b,s,m);sc=-S(n,o,max(d-1,0),-be,-a,x)
  if N[0]>=x:return a
  if sc>=be:return be
  if sc>a:a=sc
 return a
def B(f,z,x=100000):
 b,t,c,e,w,k=Y(f);s=[t,c,e,w,k];N[0]=0
 ms=[m for m in G(b,s)if u(m)in z];best=ms[0];d=1
 while 1:
  cb=best;al=-10**9
  for m in ms:
   n,o=M(b,s,m);sc=-S(n,o,d-1,-10**9,-al,x)
   if N[0]>=x:break
   if sc>al:al=sc;cb=m
  if N[0]>=x:break
  best=cb;d+=1
  if d>32:break
 return u(best)
if __name__=="__main__":
 while 1:
  g=H("/game",{})
  if g["status"]=="done":break
  if g["status"]=="your_move":g=H("/move",{"game":g["game"],"move":B(g["fen"],g["legal_moves"])})
