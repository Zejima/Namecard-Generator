from PIL import Image,ImageDraw,ImageFont
import textwrap

im = Image.open('PersonaTextBox.png')

draw = ImageDraw.Draw(im)
image_width, image_height = im.size
font = ImageFont.truetype(font ="text/PROPAGANDASIGHTPERSONALUSE.ttf", size = int(image_height/3) )

text ="Aaron"
char_width, char_height = font.getsize('A')
chars_per_line = image_width//char_width
top_lines = textwrap.wrap(text, width = chars_per_line)

y = 10

for line in top_lines:
    line_width, line_height = font.getsize(line)
    x = (image_width- line_width)//2
    draw.text((x,140),line, fill = "white", font =font)
im.save(text+'.png')
im.show()
