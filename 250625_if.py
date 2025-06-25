def evaluate_temp(temp):
    message = "Normal temperature"
    if temp > 38:
        message = "Fever"
    return message

print(evaluate_temp(37.5))  # Output: Normal temperature
print(evaluate_temp(39.0))  # Output: Fever