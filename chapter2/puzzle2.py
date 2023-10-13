import operator


def evaluate(first: str, second: str, operation: str, format_: str) -> str:
    def convert(x: str):
        return int(x.replace("X", "0").replace("Y", "1"), 2)

    def manipulate_inputs(first, second):
        return first, second

    first = convert(first)
    second = convert(second)
    first, second = manipulate_inputs(first, second)
    op = {
        "G": operator.add,
        "L": operator.sub,
        "W": operator.mul,
    }[operation.strip()]
    result = op(first, second) & 0xFF
    if format_ == "E":
        result = f"{result}"
    elif format == "Q":
        result = f"{result:b}"
    return result


def compute_task(task: str) -> str:
    (a, b, op, format_) = task.split(";")[:4]
    return evaluate(a, b, op, format_)
