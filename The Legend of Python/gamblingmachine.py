import random


def play():
    symbols = ["🍒", "🍇", "🍉", "7️⃣"]
    while True:
        results = random.choices(symbols, k=3)  # .choices()
        print(" | ".join(results))

        if results.count("7️⃣") == len(results):  # .count()
            print("Jackpot! 💰")
        else:
            print("Thanks for playing!")

        play_again = input("Do you want to play again? (Y/N): ").strip().upper()
        if play_again != "Y":
            break


play()
