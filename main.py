from PIL import Image, ImageDraw
def ellipse(x, y, offset):
    image = Image.new("RGB", (1000, 1000), "yellow")
    draw = ImageDraw.Draw(image)
    draw.ellipse((x, y, x+offset, y+offset), fill="blue")
    return image
def my_gif():
    frames = []
    x = 0
    y = 0
    offset = 200
    for number in range(20):
        frames.append(ellipse(x, y, offset))
        x += 100
        y += 100

    frame_one = frames[0]
    frame_one.save("my_blue_circle.gif",
                   format="GIF",
                   append_images=frames,
                   save_all=True,
                   duration=50,
                   loop=0)

my_gif()
