def string_to_number_mapping(s: str) -> dict:
    result = {}

    for i in s:
        if i not in result.keys():
            result[i] = s.index(i)

    return result