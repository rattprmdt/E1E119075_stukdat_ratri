# C-1.15

def are_distinct(data):
    count = 0
    for k in data:
        for j in range(1, len(data) - 1):
            if k == j:
                count += 1
                if count == 2:
                    return False
    return True


print(are_distinct(evens))
print(are_distinct(alpha))
