from pathlib import Path

from PIL import Image

from .puzzle1 import find_ordered_key
from .puzzle2 import compute_task
from .puzzle3 import compute_state, State


p = Path(__file__).parent / "resources/01_keymaker_ordered.txt"
with open(p) as f:
    keys = f.readlines()
keys = [k.strip() for k in keys]
print(f"Puzzle 1: {find_ordered_key(keys)}")

first = compute_task("YXYY; YYXY; N; Q;")
second = compute_task("XYXX; XYYX; R; Q;")
print(f"Puzzle 2: {first + second}")

p = Path(__file__).parent / "resources/03_trap_logs.txt"
with open(p) as f:
    lines = f.readlines()
result = sum(
    [id_ for id_, log in enumerate(lines, 1) if compute_state(log) == State.safe]
)
print(f"Puzzle 3: {result}")

panel = Image.open(Path(__file__).parent / "resources/cipher_matrix.png")
plate1 = Image.open(Path(__file__).parent / "resources/plate_01.png")
plate2 = Image.open(Path(__file__).parent / "resources/plate_02.png")
plate3 = Image.open(Path(__file__).parent / "resources/plate_03.png")
panel.paste(plate1, mask=plate1)
panel.paste(plate2, mask=plate2)
panel.paste(plate3, mask=plate3)
panel.show()
