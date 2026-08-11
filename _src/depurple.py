from PIL import Image, ImageSequence
src=Image.open("/Users/shuyuanshi/Documents/charizard/gmax.gif")
frames=[]; durations=[]
for fr in ImageSequence.Iterator(src):
    durations.append(fr.info.get("duration",30))
    im=fr.convert("RGBA"); px=im.load(); W,H=im.size
    for y in range(H):
        for x in range(W):
            r,g,b,a=px[x,y]
            if a>0 and b>g+15 and r>g+15:   # 洋红/紫家族 → 抠掉
                px[x,y]=(r,g,b,0)
    frames.append(im)
# 存为 RGBA 序列 png 供 magick 组装（保留 alpha 干净）
import os
os.makedirs("gmax_f",exist_ok=True)
for i,im in enumerate(frames):
    im.save(f"gmax_f/g{i:03d}.png")
# 同时写 durations
open("gmax_dur.txt","w").write(" ".join(str(d) for d in durations))
print("frames",len(frames),"first durations",durations[:5])
