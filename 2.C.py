def compare_strings(str1, str2):
    return str1.lower() == str2.lower()

# Test the function
string1 = "I like to drink water"
string2 = "I Like Too Drink Water"
result = compare_strings(string1, string2)
print(result)  # Output: True
