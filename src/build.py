import base64,sys,os
HERE=os.path.dirname(os.path.abspath(__file__))
b=lambda f: base64.b64encode(open(os.path.join(HERE,'assets',f),'rb').read()).decode()
s=open(os.path.join(HERE,'app.src.html')).read()
for k,f in [('__AVI__','avi.webp'),('__F500__','fred500.woff2'),('__F700__','fred700.woff2'),('__FACE__','face.webp'),('__TOUCH__','touch.jpg'),('__FAV__','fav.png')]:
    assert k in s, k
    s=s.replace(k,b(f))
open(os.path.join(HERE,'..','index.html'),'w').write(s)
print('size KB', len(s)//1024)
