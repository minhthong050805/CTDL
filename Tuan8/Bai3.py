def count_frequency(arr):
    freq = {}
    for item in arr:
        freq[item] = freq.get(item, 0) + 1
    return freq


data = ['a', 'b', 'a', 'c', 'a']
result = count_frequency(data)
print(f"Mang: {data}")
print(f"Tan suat: {result}")
