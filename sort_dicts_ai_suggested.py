# AI-suggested implementation (concise)

def sort_dicts(data, key, reverse=False):
    """
    Sort a list of dictionaries by a given key.
    Example: sort_dicts(list_of_dicts, 'priority')
    """
    return sorted(data, key=lambda d: d.get(key), reverse=reverse)

# Example usage:
if __name__ == "__main__":
    items = [
        {"id": 1, "priority": 10},
        {"id": 2, "priority": 5},
        {"id": 3, "priority": 7},
    ]
    print(sort_dicts(items, "priority"))
