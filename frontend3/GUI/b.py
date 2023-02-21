from PIL import Image

array1 = [[0.48, 0.4,  0.56, 0.32, 0.52],
 [0.36, 0.56, 0.56, 0.68, 0.56],
 [0.32, 0.72, 0.88, 0.44, 0.56],
 [0.56, 0.64, 0.76, 0.52, 0.48],
 [0.32, 0.88, 0.56, 0.52, 0.4 ]]

width1 = 5
height1 = 5

im = Image.new('L', (width1, height1))
pix = im.load()
for y in range(height1):
    for x in range(width1):
        pix[x, y] = int(array1[y][x] * 255.9999)

im = im.resize((width1 * 10, height1 * 10), resample=Image.NEAREST)
im.save(r'c:\temp\temp.png')

