# Manual implementation (with validation and default handling)

from operator import itemgetter

def sort_dicts_safe(data, key, reverse=False, default=None):
    """
    Sort a list of dictionaries by a given key.
    - Handles missing keys by using `default`.
    - Validates input types.
    """
    if not isinstance(data, list):
        raise TypeError("data must be a list of dictionaries")
    # Normalize entries to ensure comparability
    def key_fn(d):
        if not isinstance(d, dict):
            raise TypeError("each item must be a dict")
        return d.get(key, default)
    # Use stable sort
    return sorted(data, key=key_fn, reverse=reverse)

# Example usage:
if __name__ == "__main__":
    items = [
        {"id": 1, "priority": 10},
        {"id": 2},  # missing priority
        {"id": 3, "priority": 7},
    ]
    print(sort_dicts_safe(items, "priority", default=0))
