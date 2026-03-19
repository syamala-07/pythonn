def count_items(data):
    count = {}
    for item in data:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1
    return count
print(count_items("aba"))