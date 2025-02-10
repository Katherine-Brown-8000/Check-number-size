data = [39, 41, 47, 58, 65, 37, 37, 49, 56, 59, 62, 36, 48, 52, 64, 29, 44, 47, 49, 52, 53, 54, 72, 50, 50]

def check_size(data):
    count = 0
    for num in data:
        if 37.5 <= num and num <= 62.5:
            count += 1
    return count

print(check_size(data))
