import random


def generate_key(iterations: int = 8) -> str:
    """
    1. A -> BC
    2. A -> CB
    3. B -> DD
    4. B -> BD
    5. C -> CD
    6. C -> FE
    7. D -> AF
    8. D -> FA
    """

    A, B, C, D = "A", "B", "C", "D"
    BC, CB, DD, BD, CD, FE, AF, FA = "BC", "CB", "DD", "BD", "CD", "FE", "AF", "FA"

    rules = {A: [BC, CB], B: [DD, BD], C: [CD, FE], D: [AF, FA]}

    symbol = A
    key = [symbol]

    for _ in range(iterations):
        # Select a random production rule
        rule = random.choice(rules[symbol])

        # Remove a random occurrence of the production symbol
        index_removal = random.choice([i for i, x in enumerate(key) if x == symbol])

        # Add the new symbols from the production rule to the key
        key = key[:index_removal] + [sym for sym in rule] + key[index_removal + 1 :]

        # Choose a valid random symbol from the key
        valid_symbols = [x for x in key if x in [A, B, C, D]]
        symbol = random.choice(valid_symbols)

    return "".join(key)


for length in (8, 16, 32):
    for _ in range(5):
        print(generate_key(length))
