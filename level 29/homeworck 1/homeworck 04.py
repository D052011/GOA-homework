letters = ["ა", "ბ", "გ", "დ", "ე", "ვ", "ზ", "თ"]

print(", ".join(letters[:3]))

print(", ".join(letters[3:6]))

print(", ".join(letters[6:]))


letters2 = ["თ", "ზ", "ვ", "ე", "დ", "გ", "ბ", "ა"]

reversed_letters2 = ", ".join(letters2[::-1])
print(reversed_letters2)