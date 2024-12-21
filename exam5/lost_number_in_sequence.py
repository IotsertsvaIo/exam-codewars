def find_deleted_number(arr, mixed_arr):
    missing = sum(arr) - sum(mixed_arr)
    return missing if missing != 0 else 0