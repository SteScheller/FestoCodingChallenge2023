from pathlib import Path

from PIL import Image

# from .puzzle1 import create_hammers, find_forgable_keys
from .puzzle2 import compute_task

# from .puzzle3 import parse_config, can_be_balanced


# p = Path(__file__).parent / "resources"
# with open(p / "hammer_collection.txt") as f:
#     hammer_collection = f.readlines()
# hammers = create_hammers(hammer_collection)
# with open(p / "31_keymaker_forge_2.txt") as f:
#     keys = f.readlines()
# keys = [k.strip() for k in keys]
# key = find_forgable_keys(hammers, keys)[0]
# print(f"Puzzle 1: {key}")

solution = "".join(
    [
        compute_task("XYYYYYYY; YXXXXXXX; M; F;"),
        compute_task("XYXYXYXX; XXXYXXYY; P; E;"),
        compute_task("YXXYXXYX; XXXXXXXY; M; E;"),
        compute_task("YYXYXXYX; XXXYXYXY; P; F;"),
    ]
)
print(f"Puzzle 2: {solution}")

# with open(p / "23_trap_right_side.txt") as f:
#     configs = f.readlines()
# safe_trap_ids = list()
# for c in configs:
#     id_, left, right = parse_config(c)
#     if can_be_balanced(left, right):
#         safe_trap_ids.append(id_)
# print(f"Puzzle 3: {sum(safe_trap_ids)}")

panel = Image.open(Path(__file__).parent / "resources/cipher_matrix.png")
# plate1 = Image.open(Path(__file__).parent / "resources/plate_31.png")
plate2 = Image.open(Path(__file__).parent / "resources/plate_32.png")
# plate3 = Image.open(Path(__file__).parent / "resources/plate_33.png")
# panel.paste(plate1, mask=plate1)
panel.paste(plate2, mask=plate2)
# panel.paste(plate3, mask=plate3)
panel.show()
