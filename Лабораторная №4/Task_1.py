# TODO решите задачу
def task(file_path) -> float:
    import json
    with open(file_path) as f:
        data = json.load(f)
    result = 0
    for info in data:
        multi = float(info["score"] * info["weight"])
        result += multi
    return round(result, 3)


print(task("input.json"))







