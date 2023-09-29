import operator


def evaluate(first, second, operation) -> str:
    operand_map = {"X": 0, "Y": 1}
    operation_map = {"R": operator.or_, "N": operator.and_}
    result = ""
    op = operation_map[operation.strip()]
    for a, b in zip(first.strip(), second.strip()):
        result += str(op(operand_map[a], operand_map[b]))
    return result


def compute_task(task: str) -> str:
    (a, b, op) = task.split(";")[:3]
    return evaluate(a, b, op)
