def solution(digits):
    max_number = 0 
    for i in range(len(digits) -4):
        current_number = int(digits[i : i + 5])
        max_number = max(max_number, current_number)
        return max_number