from PIL import Image, ImageSequence, ImageDraw, ImageFont
import math
src=Image.open("n_sleep.gif")
frames=[]; durs=[]
for fr in ImageSequence.Iterator(src):
    frames.append(fr.convert("RGBA")); durs.append(fr.info.get("duration",40))
N=len(frames)
# 字体
fp=None
for cand in ["/System/Library/Fonts/Supplemental/Arial Bold.ttf","/System/Library/Fonts/Supplemental/Arial.ttf"]:
    try: ImageFont.truetype(cand,20); fp=cand; break
    except: pass
def zimg(size, alpha):
    f=ImageFont.truetype(fp,size)
    pad=size
    im=Image.new("RGBA",(pad*2,pad*2),(0,0,0,0)); d=ImageDraw.Draw(im)
    # 描边白字蓝边，像睡眠气泡
    for ox,oy in [(-2,0),(2,0),(0,-2),(0,2),(-1,-1),(1,1),(-1,1),(1,-1)]:
        d.text((pad+ox,pad+oy),"Z",font=f,fill=(40,80,160,alpha))
    d.text((pad,pad),"Z",font=f,fill=(255,255,255,alpha))
    return im.crop(im.getbbox())
# 三个 Z：固定锚点(右上)，循环上升+淡入淡出，错相位形成 z-z-z 节奏
anchors=[(132,86,18),(150,62,24),(170,34,32)]  # x,y,size
cycle=N  # 整段为一循环
out=[]
for i in range(N):
    base=frames[i].copy()
    t=i/cycle
    for k,(ax,ay,sz) in enumerate(anchors):
        ph=(t*1.0 + k*0.18)%1.0          # 相位错开
        rise=int(10*ph)                  # 缓缓上升
        # 透明度：先淡入后淡出
        a=math.sin(ph*math.pi)
        alpha=int(235*max(0,a))
        if alpha<8: continue
        z=zimg(sz,255)
        # 单独乘 alpha
        za=z.split()[3].point(lambda p:int(p*alpha/255)); z.putalpha(za)
        base.alpha_composite(z,(ax-z.width//2, ay-rise-z.height//2))
    out.append(base)
out[0].save("n_sleeping.gif",save_all=True,append_images=out[1:],duration=durs,loop=0,disposal=2,transparency=0)
print("sleeping frames",len(out),"font",fp)
