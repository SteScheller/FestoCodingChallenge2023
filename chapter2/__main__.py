from pathlib import Path

from PIL import Image

from .puzzle1 import create_hammers, is_forgeable
from .puzzle2 import compute_task


p = Path(__file__).parent / "resources"
with open(p / "hammer_collection.txt") as f:
    hammer_collection = f.readlines()
hammers = create_hammers(hammer_collection)
with open(p / "21_keymaker_forge.txt") as f:
    possible_keys = f.readlines()
possible_keys = [k.strip() for k in possible_keys]
for k in possible_keys:
    if is_forgeable(hammers, k):
        key = k
        break
print(f"Puzzle 1: {key}")

first = compute_task("YXXXXYXY; XXXXXYXY; G; Q;")
second = compute_task("YXXXYXYX; YYYXXXXX; L; Q;")
print(f"Puzzle 2: {first + second}")

panel = Image.open(Path(__file__).parent / "resources/cipher_matrix.png")
plate1 = Image.open(Path(__file__).parent / "resources/plate_21.png")
# plate2 = Image.open(Path(__file__).parent / "resources/plate_22.png")
# plate3 = Image.open(Path(__file__).parent / "resources/plate_23.png")
panel.paste(plate1, mask=plate1)
# panel.paste(plate2, mask=plate2)
# panel.paste(plate3, mask=plate3)
panel.show()
