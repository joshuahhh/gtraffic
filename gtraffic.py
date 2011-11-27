import urllib, Image, ImageDraw, ImageFont, cStringIO, time

def im_from_url(url):
    data = urllib.urlopen(url).read()
    return Image.open(cStringIO.StringIO(data))

url_template = ("http://mt1.google.com/vt?hl=en&lyrs=m,traffic|" +
                "seconds_into_week:%i&x=%i&y=%i&z=10&style=15")
               # used to have "h@163315395" instead of "m"

t = 0
x = 163
y = 395
w = 3
h = 3

font_file = "/usr/share/fonts/truetype/msttcorefonts/Arial_Black.ttf"
font = ImageFont.truetype(font_file, 30)

d = 6
for subhour in range(0, 24*d):
    hour = float(subhour)/d
    t = 3600*(24+hour)
    
    out = Image.new('RGB', (256*w,256*h), color=(255,255,255))
                  # 'RGBA' for transparency

    for i in range(w):
        for j in range(h):
            im = im_from_url(url_template % (t, x+i, y+j))
            im = im.convert('RGBA')
            out.paste(im, (256*i, 256*j), im)
    
    draw = ImageDraw.Draw(out)
    label = "%02i:%02i" % (hour, (hour-int(hour))*60)
    print label
    (label_w, label_h) = draw.textsize(label, font=font)
    draw.text((0, (256*h-label_h)), label, font=font, fill=(0,0,0))

    out.save("out%07i.png" % t)
