from PIL import Image
#
#
name = input("which image? ")
img = Image.open(name) .convert("RGB")
img = img. resize((150, 150))
#
#
small = img.quantize(colors=5)
palette = small.getpalette()
#
#
total = small.width * small.height
#
swatches = []
#
#
print()
print("Main colors:")
for count, index in sorted(small.getcolors(), reverse=True):
    r = palette[index * 3]
    g = palette[index * 3 + 1]
    b = palette[index * 3 + 2]
    hex_code= f"#{r:02X}{g:02X}{b:02X}"
    percent = round(count / total * 100)  
    print(hex_code, "-", percent, "%")
    swatches.append((r, g, b))
    #
    #
SWATCH = 200
strip = Image.new("RGB", (SWATCH * len(swatches), SWATCH))
for position, color in enumerate(swatches):
    block = Image.new("RGB", (SWATCH, SWATCH), color)
    strip.paste(block, (position * SWATCH, 0))
strip.save("palette.png")
print("saved palette.png")



