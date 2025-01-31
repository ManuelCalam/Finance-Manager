from PIL import ImageTk, Image

def readImage(path, size):
    img = Image.open(path).resize(size)
    return ImageTk.PhotoImage(img)
