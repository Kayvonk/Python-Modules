def print_scores(scores):
    print("\nCurrent Scores:")
    for player, score in scores.items():
        print(f"{player}: {score}")

def main():
    print("Welcome to the Scorekeeper!")
    players = []
    scores = {}

    num_players = int(input("How many players? "))
    for i in range(num_players):
        name = input(f"Enter name for player {i+1}: ")
        players.append(name)
        scores[name] = 0

    while True:
        print_scores(scores)
        player = input("Who scored? (type 'quit' to exit) ").strip()
        if player.lower() == 'quit':
            print("Final Scores:")
            print_scores(scores)
            print("Thanks for playing!")
            break
        if player not in players:
            print(f"Player '{player}' not found. Try again.")
            continue
        try:
            points = int(input("How many points scored? "))
            scores[player] += points
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
