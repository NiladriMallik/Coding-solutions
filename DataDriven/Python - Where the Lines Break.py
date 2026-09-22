def tokenize(line: str) -> list:
    result = [r for r in line.split() if r]
    return result