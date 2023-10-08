from pathlib import Path

from PIL import Image

from .puzzle1 import create_hammers, forge_key
from .puzzle2 import compute_task
from .puzzle3 import parse_config, is_activated

p = Path(__file__).parent / "resources"
with open(p / "hammer_collection.txt") as f:
    hammers = f.readlines()
with open(p / "11_keymaker_recipe.txt") as f:
    recipes = f.readlines()
hammers = create_hammers(hammers)
for r in recipes:
    key = forge_key(hammers, r)
    if key is not None:
        break
print(f"Puzzle 1: {key}")

first = compute_task("YXXXXYXY; XXXXXYXY; G; Q;")
second = compute_task("YXXXYXYX; YYYXXXXX; L; Q;")
print(f"Puzzle 2: {first + second}")

with open(p / "13_trap_balance.txt") as f:
    configs = f.readlines()
safe_trap_ids = list()
for c in configs:
    id_, left, right = parse_config(c)
    if not is_activated(left, right):
        safe_trap_ids.append(id_)
print(f"Puzzle 3: {sum(safe_trap_ids)}")

panel = Image.open(Path(__file__).parent / "resources/cipher_matrix.png")
plate1 = Image.open(Path(__file__).parent / "resources/plate_11.png")
plate2 = Image.open(Path(__file__).parent / "resources/plate_12.png")
plate3 = Image.open(Path(__file__).parent / "resources/plate_13.png")
panel.paste(plate1, mask=plate1)
panel.paste(plate2, mask=plate2)
panel.paste(plate3, mask=plate3)
panel.show()
