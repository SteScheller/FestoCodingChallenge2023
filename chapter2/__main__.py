from pathlib import Path

from PIL import Image

from chapter1.puzzle1 import create_hammers

# from .puzzle2 import compute_task

p = Path(__file__).parent / "resources"
with open(p / "hammer_collection.txt") as f:
    hammers = f.readlines()
# with open(p / "11_keymaker_recipe.txt") as f:
#    recipes = f.readlines()
# hammers = create_hammers(hammers)
# for r in recipes:
#    key = forge_key(hammers, r)
#    if key is not None:
#        break
# print(f"Puzzle 1: {key}")


panel = Image.open(Path(__file__).parent / "resources/cipher_matrix.png")
# plate1 = Image.open(Path(__file__).parent / "resources/plate_21.png")
# plate2 = Image.open(Path(__file__).parent / "resources/plate_22.png")
# plate3 = Image.open(Path(__file__).parent / "resources/plate_23.png")
# panel.paste(plate1, mask=plate1)
# panel.paste(plate2, mask=plate2)
# panel.paste(plate3, mask=plate3)
panel.show()
