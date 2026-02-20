import random

word_bank = [
    "mateo", "luis", "salma", "paolo", "elver", 
    "marifer", "paleta", "tiktok", "rudo", "mesa", 
    "silla", "computadora", "celular", "cabello", "ficha"
]

game_words = random.sample(word_bank, 15)

user_mistakes = 0
correct_entries = 0
total_words = len(game_words)

print("--- The Typing Test Assignment ---")
print("Type each word as it appears try not to mistype")

for current_word in game_words:
    print(f"\nWord to type: {current_word}")
    user_input = input("Your answer: ")

    if user_input == current_word:
        print("Correct!")
        correct_entries += 1
    else:
        print("Incorrect!")
        user_mistakes += 1
    
    print(f"Mistakes count: {user_mistakes}")

accuracy = (correct_entries / total_words) * 100

print("-" * 30)
print("Test is Done")
print(f"Your Total Mistakes: {user_mistakes}")
print(f"Your Accuracy: {accuracy}%")