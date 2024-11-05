import itertools

# Define the pattern and the possible characters for replacement
pattern = '**A**R*S*'
replacement_chars = ["A","R","S","H"] + list('CDEFIJKLMNPQVWXYZ')  # All characters that can replace '*'

# Create a set to store unique variations
variations = set()

# Generate all combinations of 3 characters from the available replacement characters
# ensuring both G and T are included in every combination
for additional_char in replacement_chars:
    for combo in itertools.permutations([additional_char, "A","R","S","H"], 5):  # Select 3 characters including G and T
        temp_pattern = list(pattern)
        rep_index = 0
        for i in range(len(temp_pattern)):
            if temp_pattern[i] == '*':
                temp_pattern[i] = combo[rep_index]
                rep_index += 1
        variations.add(''.join(temp_pattern))

# Output the results
#for i, variation in enumerate(sorted(variations)):
#    print(f"Variation {i + 1}: {variation}")
print("Variations: ", variations)