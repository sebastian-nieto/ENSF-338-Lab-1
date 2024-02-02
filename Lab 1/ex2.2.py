def count_consonants(word):
    # Function to count the number of consonant letters in a word
    consonants = set("bcdfghjklmnpqrstvwxyz")
    return sum(1 for letter in word.lower() if letter in consonants)

def average_consonants_per_word(lines):
    # Function to calculate the average number of consonants per word in the lines
    total_consonants = 0
    total_words = 0
    counting_started = False

    for line in lines:
        # Start counting from the line containing "CHAPTER 1. Loomings."
        if "CHAPTER 1. Loomings." in line:
            counting_started = True

        if counting_started:
            words = line.split()
            total_consonants += sum(count_consonants(word) for word in words)
            total_words += len(words)

    if total_words == 0:
        return 0  # Avoid division by zero

    return total_consonants / total_words

if __name__ == "__main__":
    with open('pg2701.txt', 'r', encoding="UTF-8") as file:
        lines = file.readlines()
        lineArray = [line.strip() for line in lines]

        # Calculate and print the average number of consonants per word
        avg_consonants = average_consonants_per_word(lineArray)
        print(f"Average number of consonants per word from 'CHAPTER 1. Loomings.' onwards: {avg_consonants}")
