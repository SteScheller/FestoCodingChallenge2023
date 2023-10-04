import operator


def evaluate(first: str, second: str, operation: str) -> str:
    def convert(x: str):
        return int(x.replace("X", "0").replace("Y", "1"), 2)

    first = convert(first)
    second = convert(second)
    op = {"G": operator.add, "L": operator.sub}[operation.strip()]
    result = op(first, second) & 0xFF
    return f"{result:b}"


def compute_task(task: str) -> str:
    (a, b, op) = task.split(";")[:3]
    return evaluate(a, b, op)
