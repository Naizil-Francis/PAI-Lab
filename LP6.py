from fuzzywuzzy import fuzz

def fuzzy_union(set1, set2):
    union_result = max(set1, set2, key=lambda x: max(x))
    return union_result

def fuzzy_intersection(set1, set2):
    intersection_result = min(set1, set2, key=lambda x: max(x))
    return intersection_result

# Example fuzzy sets
set_a = {'a': 0.8, 'b': 0.6, 'c': 0.4, 'd': 0.2, 'e': 0.1}
set_b = {'a': 0.7, 'b': 0.5, 'c': 0.3, 'f': 0.9, 'g': 0.4}

# Calculate Union and Intersection
union_result = fuzzy_union(set_a, set_b)
intersection_result = fuzzy_intersection(set_a, set_b)

# Print results
print("Fuzzy Set A:", set_a)
print("Fuzzy Set B:", set_b)
print("Union:", union_result)
print("Intersection:", intersection_result)
