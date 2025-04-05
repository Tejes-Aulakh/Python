def count_words(text):
    words = text.split()
    return len(words)

print("📝 Word Counter Tool")
user_input = input("Type a sentence: ")
word_count = count_words(user_input)

print(f"Your sentence has {word_count} words.")