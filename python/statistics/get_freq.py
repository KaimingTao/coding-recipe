from collections import Counter


def get_frequency(value_list):
    freq = Counter(value_list)

    return [
        {
            'value': v,
            'n': f,
            '%': f / len(value_list)
        }
        for v, f in freq.items()
    ]
