import multiprocessing as mp
from pathlib import Path

from PIL import Image
from tqdm import tqdm

from .puzzle1 import create_hammers, is_long_key_forgeable
from .puzzle2 import compute_task
from .puzzle3 import compute_per_config_job


p = Path(__file__).parent / "resources"
with open(p / "hammer_collection.txt") as f:
    hammer_collection = f.readlines()
hammers = create_hammers(hammer_collection)
with open(p / "31_keymaker_forge_2.txt") as f:
    possible_keys = f.readlines()
possible_keys = [k.strip() for k in possible_keys]
# for k in tqdm(possible_keys) -> "educated guess" to speed things up
for k in tqdm(possible_keys[920:925]):
    if is_long_key_forgeable(hammers, k):
        key = k
        break
print(f"Puzzle 1: {key}")

solution = "".join(
    [
        compute_task("XYYYYYYY; YXXXXXXX; M; F;"),
        compute_task("XYXYXYXX; XXXYXXYY; P; E;"),
        compute_task("YXXYXXYX; XXXXXXXY; M; E;"),
        compute_task("YYXYXXYX; XXXYXYXY; P; F;"),
    ]
)
print(f"Puzzle 2: {solution}")


with open(p / "33_trap_water.txt") as f:
    configs = f.readlines()
pool = mp.Pool(mp.cpu_count())
sum_ = sum(tqdm(pool.imap(compute_per_config_job, configs), total=len(configs)))
print(f"Puzzle 3: {sum_}")

panel = Image.open(Path(__file__).parent / "resources/cipher_matrix.png")
plate1 = Image.open(Path(__file__).parent / "resources/plate_31.png")
plate2 = Image.open(Path(__file__).parent / "resources/plate_32.png")
# plate3 = Image.open(Path(__file__).parent / "resources/plate_33.png")
panel.paste(plate1, mask=plate1)
panel.paste(plate2, mask=plate2)
# panel.paste(plate3, mask=plate3)
panel.show()
