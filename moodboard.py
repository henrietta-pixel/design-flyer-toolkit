from pathlib import Path 
from PIL import Image, ImageOps
#
IMAGE_TYPES = {".jpg", ".jpeg", ".png", ".webp"}
#
images = []
for file in Path("references").iterdir():
    if file.suffix.lower() not in IMAGE_TYPES:
        continue
    images.append(Image.open(file))
#
print(len(images),  "images found")
if len(images)== 0:
    print("No Images found. put some pictures in the 'references' folder first.")
    raise SystemExit
TITLE_W, TITLE_H = 400, 400
GAP = 20
COLUMNS = 3
ROWS = (len(images) + COLUMNS - 1) // COLUMNS
BACKGROUND = "#7FFFD4"
#
board_width = COLUMNS* TITLE_W + (COLUMNS + 1) * GAP
board_height = ROWS* TITLE_H + (ROWS + 1) * GAP
#
board = Image.new("RGB",    (board_width, board_height), BACKGROUND)
#
for index, image in enumerate(images):
    column = index % COLUMNS
    row = index // COLUMNS
    x = GAP + column * (TITLE_W + GAP)
    Y = GAP + row * (TITLE_H + GAP)
    title = ImageOps.pad(image.convert("RGB"), (TITLE_W, TITLE_H),  color=BACKGROUND)
    board.paste(title, (x, Y))
#
board.save("moodboard.png")