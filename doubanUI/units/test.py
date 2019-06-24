from PIL import Image

def tt():

    infile = "../resource/1.jpg"
    outfile = "../resource/2.jpg"

    im = Image.open(infile)
    (x,y) = im.size
    x_s = 8000
    y_s = 6000

    print(x, y)
    print(x_s, int(y_s))









    out = im.resize((x_s,int(y_s)),Image.ANTIALIAS)
    out.save(outfile)



tt()
