import sys


def get_player_decision(prompt_text: str, valid_choices: dict[str, str]) -> str:
    """
    Ask the player for input until a valid choice is provided.
    valid_choices maps accepted input to a normalized key.
    """
    while True:
        player_input = input(prompt_text).strip().lower()
        if player_input in valid_choices:
            return valid_choices[player_input]
        print("Please choose one of the available options.")


def start_adventure() -> str:
    print("\nWelcome to the Ancient Treasure Adventure!")
    print("You are an explorer searching for a legendary treasure hidden in an ancient land.")
    print("Make your choices carefully and enjoy the journey.\n")

    player_name = input("What is your name, explorer? ").strip()
    if not player_name:
        player_name = "Explorer"

    print(f"\nHello, {player_name}! Your quest begins now.\n")
    return player_name


def forest_path(player_name: str) -> bool:
    print("You walk into a dense forest filled with sunlight and strange sounds.")
    forest_choice = get_player_decision(
        "Do you want to follow the river or climb a tall tree? (river/tree): ",
        {"river": "river", "tree": "tree"},
    )

    if forest_choice == "river":
        print(
            "\nYou follow the river downstream. A friendly traveler appears and offers you help."
        )
        help_choice = get_player_decision(
            "Do you accept the traveler's help or continue alone? (help/alone): ",
            {"help": "help", "alone": "alone"},
        )

        if help_choice == "help":
            print(
                "\nThe traveler shares a secret map and guides you to a hidden clearing."
            )
            print("In the clearing you discover the legendary treasure chest!")
            print("Congratulations, you found the treasure!\n")
            return True
        print(
            "\nYou continue alone and lose your path in the dense forest. After hours of wandering, the adventure ends."
        )
        return False

    print(
        "\nYou climb the tree and spot a faint path leading deeper into the woods."
    )
    tree_choice = get_player_decision(
        "Do you take the faint path or return to the forest entrance? (path/return): ",
        {"path": "path", "return": "return"},
    )

    if tree_choice == "path":
        print(
            "\nThe faint path leads you to a hidden waterfall with a cave entrance behind it."
        )
        print("You carefully step through and find a shining treasure chest!")
        print("Congratulations, you found the treasure!\n")
        return True

    print(
        "\nYou return to the entrance but the forest is now too confusing."
    )
    print("You are forced to stop your quest and try again later.")
    return False


def cave_path(player_name: str) -> bool:
    print("You enter a mysterious cave where your footsteps echo loudly.")
    cave_choice = get_player_decision(
        "Do you light a torch or proceed in the dark? (torch/dark): ",
        {"torch": "torch", "dark": "dark"},
    )

    if cave_choice == "torch":
        print(
            "\nThe torch lights the cave walls and reveals ancient symbols."
        )
        print(
            "You follow the markings and discover a hidden chamber full of treasure!"
        )
        print("Congratulations, you found the treasure!\n")
        return True

    print(
        "\nYou move in the dark and suddenly stumble into a deep pit."
    )
    print("You cannot find a safe way out, and the adventure ends here.")
    return False


def offer_restart() -> bool:
    restart_choice = get_player_decision(
        "Would you like to play again? (yes/no): ",
        {"yes": "yes", "y": "yes", "no": "no", "n": "no"},
    )
    return restart_choice == "yes"


def play_adventure_game() -> None:
    print("Adventure Game - Ancient Treasure Quest")

    while True:
        player_name = start_adventure()

        first_choice = get_player_decision(
            "Do you explore the forest or enter the cave? (forest/cave): ",
            {"forest": "forest", "cave": "cave"},
        )

        if first_choice == "forest":
            success = forest_path(player_name)
        else:
            success = cave_path(player_name)

        if success:
            print(f"Well done, {player_name}! Your adventure was a success.")
        else:
            print(f"Sorry, {player_name}. This attempt did not find the treasure.")

        if not offer_restart():
            print("\nThank you for playing the Ancient Treasure Adventure!")
            break

    sys.exit(0)


if __name__ == "__main__":
    play_adventure_game()
