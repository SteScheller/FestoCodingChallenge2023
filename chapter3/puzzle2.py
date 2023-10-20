import operator


def evaluate(first: str, second: str, operation: str, format_: str) -> str:
    def manipulate_inputs(first, second):
        first = first[0:2] + first[3] + first[2] + first[4:]
        second = second[0:1] + second[2] + second[1] + second[3:]
        return first, second

    def convert(x: str):
        return int(x.replace("X", "0").replace("Y", "1"), 2)

    def operatorM(x: int, y: int):
        result = x
        if y == 1:
            result = x >> 1
            if x % 2:
                result += 128
        elif y == 128:
            result = x << 1
            if x >= 128:
                result += 1
        return result

    first, second = manipulate_inputs(first, second)
    first = convert(first)
    second = convert(second)
    op = {
        "G": operator.add,
        "L": operator.sub,
        "W": operator.mul,
        "P": lambda x, y: round(operator.truediv(x, y)),
        "M": operatorM,
    }[operation.strip()]
    result = op(first, second) & 0xFF
    if format_ == "E":
        result = f"{result}"
    elif format_ == "Q":
        result = f"{result:b}"
    elif format_ == "F":
        result = f"{result:x}"

    return result


def compute_task(task: str) -> str:
    (a, b, op, format_) = [x.strip() for x in task.split(";")[:4]]
    return evaluate(a, b, op, format_)
