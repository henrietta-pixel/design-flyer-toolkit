"""
Flyer exporter (step1)

drop finished flyers into the "input" folder, run this script, and it will:
1. Make a copy of each flyer in every size you need (social media + print)
2. Save the copies in the "output" folder
3. write a record of everything it made in "flyer_log.csv"

your original files are NEVER changed. The script only reads them.
"""

import csv
from datetime import datetime
from pathlib import Path

from PIL import Image, ImageOps
#
SIZES = {
    "status_story": (1080,1920),       #whatsapp status / instagram & facebook story
    "instagram_post": (1080,1350),     #instagram potrait post
    "square_post": (1080, 1080),       #square post
    "print_A4": (2480, 3508),          #A4 print at 300 DPI
    "print_A5": (1748, 2480),          #A5 print at 300 DPI
}
IMAGE_TYPES = {".jpg", ".jpeg", ".png", ".webp"}
OUTPUT_FOLDER = Path("output")
OUTPUT_FOLDER.mkdir(exist_ok=True)
#
for file in Path("input").iterdir():
#
    print(file.name)
OUTPUT_FOLDER = Path("output")
OUTPUT_FOLDER.mkdir(exist_ok=True)
#
for file in Path("input").iterdir():
    if file.suffix.lower() not in IMAGE_TYPES:
        continue
    img = Image.open(file)
    for size_name, size in SIZES.items():
        result= ImageOps.pad(img, size, color="black")
        result.save(OUTPUT_FOLDER / f"{file.stem}_{size_name}.jpg")
        print("saved", file.name, size_name) 
        with open("flyer_log.csv", "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M"), file.name, size_name])
