# Design Flyer Toolkit

Design more, resize less. A Python toolkit for flyers, mood boards and color palettes.

I built these tools to help a graphic designer friend who spends a lot of time on repetitive work.

## Tools

| File | What it does |
|---|---|
| `flyer_exporter.py` | Takes every flyer in the `input` folder, saves 5 sizes (social media and print) into `output`, and logs each export in `flyer_log.csv` |
| `inspiration.py` | Asks what kind of flyer you are designing and the mood, then opens Pinterest, Behance and Google Images searches |
| `moodboard.py` | Arranges the images in a `references` folder into one mood board |
| `palette.py` | Finds the 5 main colors in an image, prints them as hex codes and saves a palette strip |

## How to use

1. Install Python 3
2. Install the requirement: `pip install -r requirements.txt` (on Windows you can use `py -m pip install -r requirements.txt`)
3. Create the folders `input` and `references`
4. Run a tool, for example `py flyer_exporter.py`

## What I learned

This was my first Python project. I learned how to use pillow to resize images automatically, learning loops, how to work with folders in python, and how to automate repetitive design tasks using python to solve real problems for designers.

## Future ideas

- An image enhancer to improve photos in batches
- A template tool that fills in new names, dates and prices on a flyer
- A simple window with buttons, so no code is needed