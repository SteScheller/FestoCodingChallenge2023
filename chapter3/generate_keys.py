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

    from random import randrange

    (
        A,
        B,
        C,
        D,
    ) = (
        "A",
        "B",
        "C",
        "D",
    )
    BC, CB, DD, BD, CD, FE, AF, FA = "BC", "CB", "DD", "BD", "CD", "FE", "AF", "FA"

    rules = {A: [BC, CB], B: [DD, BD], C: [CD, FE], D: [AF, FA]}

    symbol = A
    key = [symbol]

    for i in range(iterations):
        # Select a random production rule
        symbol_rules = rules[symbol]
        rule_index = randrange(len(symbol_rules))
        rule = symbol_rules[rule_index]

        # Remove a random occurrence of the production symbol
        indices = [i for i, x in enumerate(key) if x == symbol]
        index_removal = randrange(len(indices))
        key.pop(index_removal)

        # Add the new symbols from the production rule to the key
        key += rule

        # Choose a valid random symbol from the key
        valid_symbols = [x for x in key if x in [A, B, C, D]]
        symbol_idx = randrange(len(valid_symbols))
        symbol = valid_symbols[symbol_idx]

    return "".join(key)


for i in range(3):
    print(generate_key())
    print(generate_key(16))
    print(generate_key(32))
