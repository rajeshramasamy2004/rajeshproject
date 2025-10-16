import random
words = ["apple", "house", "train", "plant", "chair"]
word_to_guess = random.choice(words)
guessed_letters = []
incorrect_guesses = 0
max_guesses = 6
display_word = ["_" for _ in word_to_guess]

while incorrect_guesses < max_guesses and "_" in display_word:
    print("Word: ", " ".join(display_word))
    print("Guessed letters:", " ".join(guessed_letters))
    print(f"Incorrect guesses left: {max_guesses - incorrect_guesses}")
    
    guess = input("Guess a letter: ").lower()
    
    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single letter.")
        continue
    
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue
    
    guessed_letters.append(guess)
    
    if guess in word_to_guess:
        for i in range(len(word_to_guess)):
            if word_to_guess[i] == guess:
                display_word[i] = guess
        print("Good guess!")
    else:
        incorrect_guesses += 1
        print("Wrong guess.")

    print()

if "_" not in display_word:
    print("Congratulations! You guessed the word:", word_to_guess)
else:
    print("Out of guesses. The word was:", word_to_guess)