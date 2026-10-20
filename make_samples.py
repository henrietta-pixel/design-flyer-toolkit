from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

Path("samples").mkdir(exist_ok=True)

flyers = [
    ("USER TESTING", "Saturday, 14th October", "#1b4332", "#d8f3dc"),
    ("USER TESTING", "Friday October , 20th ", "#3c096c", "#e0aaff"),
    ("USER TESTING", "Sunday, 22nd October", "#7f1d1d", "#fecaca"),
]

big = ImageFont.load_default(size=70)
small = ImageFont.load_default(size=40)

for number, (title, date, bg, fg) in enumerate(flyers, start=1):
    img = Image.new("RGB", (810, 1012), bg)
    draw = ImageDraw.Draw(img)
    draw.rectangle((60, 60, 750, 952), outline=fg, width=6)
    draw.text((405, 440), title, font=big, fill=fg, anchor="mm")
    draw.text((405, 560), date, font=small, fill=fg, anchor="mm")
    img.save(f"samples/sample_flyer_{number}.jpg")
print("Made 3 sample flyers in the samples folder")