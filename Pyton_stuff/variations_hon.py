import itertools

# Define the pattern and the possible characters for replacement
pattern = '*E*UL*OR'
replacement_chars = "UORESLP".split() + list('FQVXZ')  # All characters that can replace '*'

V1 = "ABDOMEN" + "A****EN" + "*******"
V2 = "CITYFUL" + "*******" + "*I*****"
V3 = "GAWKISH" + "*A*KIS*" + "*I*****"
V4 = "INSPEAK" + "INS*EAK" + "*I*****"
V5 = "SINKAGE" + "S**KA*E" + "*IN****"

Z1 = "AIN****" + "AIN****"
Z1 = "EIN****"
Z1 = "KIN****"
AA = "KIN*AA*"
EE = "KIN*EEE"
SS = "KIN**S*"
KK = "KINK**K"

c1 = "KINSERA"


# Create a set to store unique variations
variations = set()

# Generate all combinations of 3 characters from the available replacement characters
# ensuring both G and T are included in every combination
for additional_char in replacement_chars:
    for combo in itertools.permutations([additional_char, "A","E","K","S"], 5):  # Select 3 characters including G and T
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