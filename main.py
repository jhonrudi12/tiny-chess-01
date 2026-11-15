import json,os,urllib.request as u
D={'P':(-10,-20,-11,-9),'N':(-21,-19,-12,-8,8,12,19,21),'B':(-11,-9,9,11),'R':(-10,-1,1,10)};D['Q']=D['K']=D['R']+D['B']
V={'P':100,'N':320,'B':330,'R':500,'Q':900,'K':0}
Z="++++5555--/1,,-0+++/,*)+,--'++++$&''&)++'+--',-.'+-.'---&)++$&'')**++,,,)+++*+++++++)+++)+++)**+%##!%##!%##!%##!'%%#)'''//++/1-+!#%'%')+%)/1%)13%)13%)/1%%++!%%%"
G={};F={}
for L,a,b in zip('PNBRQK',(0,1,1,2,2,3),(0,1,1,2,2,4)):
 g=[0]*120;f=[0]*120
 for r in range(8):
  for c in range(8):
   i=r*10+c+21;w=c if c<4 else 7-c
   g[i]=V[L]+(ord(Z[a*32+r*4+w])-43)*5
   f[i]=V[L]+(ord(Z[b*32+r*4+w])-43)*5
 G[L]=g;F[L]=f
TT={};NC=[0];RB=[0]
def fen(f):
 p=f.split()
 b='         \n'*2+' '+''.join('.'*int(c) if c.isdigit() else c for c in p[0].replace('/','\n '))+'\n'+'         \n'*2
 m=e=h=0
 for i,q in enumerate(b):
  if q.isalpha():
   u=q.upper();s=1 if q.isupper() else -1;k=i if s>0 else 119-i;m+=s*G[u][k];e+=s*F[u][k];h+=V[u]//200
 w=('Q' in p[2],'K' in p[2]);v=('k' in p[2],'q' in p[2])
 t=(b,m,e,h,w,v)
 return(b[::-1].swapcase(),-m,-e,h,v,w) if p[1]=='b' else t
def mov(p,m):
 i,j,o=m;b=p[0];a=b[i];q=b[j]
 d=G[a][j]-G[a][i];e=F[a][j]-F[a][i];h=0
 if q in'pnbrqk':
  u=q.upper();d+=G[u][119-j];e+=F[u][119-j];h-=V[u]//200
 c=list(b);c[j]=a;c[i]='.'
 w,v=p[4],p[5]
 w=(w[0] and i!=91,w[1] and i!=98);v=(v[0] and j!=28,v[1] and j!=21)
 if a=='K':
  w=(0,0)
  if abs(j-i)==2:
   t2=(i+j)//2;r=91 if j<i else 98;d+=G['R'][t2]-G['R'][r];e+=F['R'][t2]-F['R'][r];c[r]='.';c[t2]='R'
 pm=a=='P' and 21<=j<=28
 if pm:
  d+=G[o][j]-G['P'][j];e+=F[o][j]-F['P'][j];h+=V[o]//200;c[j]=o
 return(''.join(c)[::-1].swapcase(),-(p[1]+d),-(p[2]+e),p[3]+h,v,w)
def atk(p,s,u):
 b=p[0]
 for ds,t in(((9,11) if u else (-9,-11),'P'),(D['N'],'N'),(D['K'],'K')):
  for d in ds:
   if b[s+d]==(t if u else t.lower()):return 1
 for d in D['K']:
  x=s+d
  while b[x]=='.':x+=d
  q=b[x]
  if q in'QqBbRr' and q.isupper()==u and(q in'Qq' or(q in'Bb')==(d in D['B'])):return 1
 return 0
def gen(p,c=0):
 b=p[0]
 for i,a in enumerate(b):
  if a not in'PNBRQK':continue
  for d in D[a]:
   j=i+d
   while 1:
    q=b[j]
    if q in' \nPNBRQKk':break
    if a=='P':
     if d%10==0:
      if q!='.' or c or d==-20 and(i<81 or b[i-10]!='.'):break
     elif q=='.':break
     yield (i,j,'Q' if 21<=j<=28 else '');break
    if q!='.' or not c:yield (i,j,'')
    if q!='.' or a in'NK':break
    j+=d;continue
 if not c:
  k=b.index('K')
  if not atk(p,k,0):
   if p[4][0] and b[91]=='R' and b[92:k]=='.'*(k-92) and not atk(p,k-1,0) and not atk(p,k-2,0):yield (k,k-2,'')
   if p[4][1] and b[98]=='R' and b[k+1:98]=='.'*(97-k) and not atk(p,k+1,0) and not atk(p,k+2,0):yield (k,k+2,'')
def leg(p,c=0):
 return [m for m in gen(p,c) if not atk(n:=mov(p,m),n[0].index('k'),1)]
def sc(p,m):
 q=p[0][m[1]]
 return V[q.upper()] if q in'pnbrqk' else 0
X=Exception
def ab(p,d,a,be,pl,rt=0):
 NC[0]+=1
 if NC[0]>6e4:raise X()
 ic=atk(p,p[0].index('K'),0)
 if d<=0:
  h=min(p[3],24);s=p[1]*h+p[2]*(24-h);st=int(s/24)
  if st>=be:return be
  if st>a:a=st
  ms=leg(p,not ic)
  if not ms:return -100000+pl if ic else a
  ms.sort(key=lambda m:sc(p,m),reverse=True)
  for m in ms:
   s=-ab(mov(p,m),0,-be,-a,pl+1)
   if s>=be:return be
   if s>a:a=s
  return a
 tm=TT.get((p,d))
 ms=leg(p)
 if not ms:return -100000+pl if ic else 0
 ms.sort(key=lambda m:9999 if m==tm else sc(p,m),reverse=True)
 bs=-10**9;bm=0;x=a
 for m in ms:
  s=-ab(mov(p,m),d-1,-be,-x,pl+1)
  if s>bs:
   bs=s;bm=m
   if rt:RB[0]=m
  if s>x:
   x=s
   if x>=be:break
 TT[(p,d)]=bm
 return bs
def root(p):
 NC[0]=0;TT.clear();RB[0]=0
 bs=0
 for d in range(1,65):
  try:s=ab(p,d,-10**9,10**9,0,1)
  except X:break
  if RB[0]:bs=RB[0]
 return bs
def uci(m,r=0):
 i,j,o=m
 if r:i,j=119-i,119-j
 return'%c%d%c%d%s'%((i-1)%10+97,10-i//10,(j-1)%10+97,10-j//10,o.lower())
U=os.getenv('MAKEFUN_ENV_URL')
def post(p,b):return json.load(u.urlopen(U+p,json.dumps(b).encode()))
while 1:
 g=post('/game',{})
 if g['status']=='done':break
 while g['status']=='your_move':
  f=g['fen'];m=root(fen(f))
  g=post('/move',{'game':g['game'],'move':uci(m,' b ' in f)})
