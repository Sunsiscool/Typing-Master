import random

word_bank = [
    "mateo", "luis", "salma", "paolo", "elver", 
    "marifer", "paleta", "tiktok", "rudo", "mesa", 
    "silla", "computadora", "celular", "cabello", "ficha"
]

game_words = random.sample(word_bank, 15)

mistakes = 0
correct_count = 0

print("--- The Typing Testo---")

for target_word in game_words:
    print(f"\nType this exact word: {target_word}")
    user_typed = input("Here is Your entry: ")

    if user_typed == target_word:
        print("Correcto!")
        correct_count += 1
    else:
        print("Incorrecto!")
        mistakes += 1
    
    print(f"Current Mistakes: {mistakes}")

    total_words = len(game_words)
accuracy = (correct_count / total_words) * 100

print("\n--- Theeee Final Results ---")
print(f"Accuracy: {accuracy}%")
print(f"Total Mistakes: {mistakes}")