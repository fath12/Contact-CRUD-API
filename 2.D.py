def extract_word(input_string):
    words = input_string.split()
    for word in words:
        if word.lower() == "sushi":
            return word

# Test the function
string1 = "One of the recommended food from japan is Sushi"
string2 = "Indonesian doesn't eat Sushi"

output1 = extract_word(string1)
output2 = extract_word(string2)

print(output1)  # Output: "Sushi"
print(output2)  # Output: "Sushi"
