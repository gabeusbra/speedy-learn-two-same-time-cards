from PIL import Image, ImageTk

size = (42, 42)
img = Image.open(r"images/soundBig.png")
sound42x42 = img.resize(size, resample= Image.BILINEAR)
sound42x42.save("images/sound42x42.png")

img = Image.open(r"images/sound42x42.png")
