# I chose to use tabulate as my 3rd party library and datetime will help me put dates for each game
from tabulate import tabulate
from datetime import date, datetime

log = "nfc_log.txt"

def nfc_teams():

    # PSEUDOCODE:
    # Make a list that holds each NFC team
    # Each team will have:
        # Team name
        # Their next game (date, time, and opponent)
        # Their previous games (list of previous games with scores)
    # Show list to user

    # These games did not happen. I used these stats for the purpose of the project.
    # I did not add every NFC team and their stats as there are 17 different teams to look through.
        teams = [
        {
            "name": "Detroit Lions",
            "next_game": {
                "date": date(2024, 10, 13),
                "time": "4:25 PM",
                "opponent": "Dallas Cowboys"
            },
            "games": [
                {"week": 1,
                 "opponent": "Los Angeles Rams",
                 "team_score": 26,
                 "opponent_score": 20},

                {"week": 2,
                 "opponent": "Tampa Bay Buccaneers",
                 "team_score": 16,
                 "opponent_score": 20},

                {"week": 3,
                 "opponent": "Arizona Cardinals",
                 "team_score": 20,
                 "opponent_score": 13},

                {"week": 4,
                 "opponent": "Seattle Seahawks",
                 "team_score": 42,
                 "opponent_score": 29},
            ]
        },

        {
            "name": "Dallas Cowboys",
            "next_game": {
                "date": date(2024, 10, 6),
                "time": "8:20 PM",
                "opponent": "Pittsburgh Steelers"
            },
            "games": [
                {"week": 1,
                 "opponent": "Cleveland Browns",
                 "team_score": 33,
                 "opponent_score": 17},

                {"week": 2,
                 "opponent": "New Orleans Saints",
                 "team_score": 19,
                 "opponent_score": 44},

                {"week": 3,
                 "opponent": "Baltimore Ravens",
                 "team_score": 25,
                 "opponent_score": 28},

                {"week": 4,
                 "opponent": "New York Giants",
                 "team_score": 20,
                 "opponent_score": 15},
            ]
        },

        {
            "name": "Green Bay Packers",
            "next_game": {
                "date": date(2024, 10, 6),
                "time": "1:25 PM",
                "opponent": "Los Angeles Rams"
            },
            "games": [
                {"week": 1,
                 "opponent": "Philadelphia Eagles",
                 "team_score": 29,
                 "opponent_score": 34},

                {"week": 2,
                 "opponent": "Indianapolis Colts",
                 "team_score": 16,
                 "opponent_score": 10},

                {"week": 3,
                 "opponent": "Tennessee Titans",
                 "team_score": 30,
                 "opponent_score": 14},

                {"week": 4,
                 "opponent": "Minnesota Vikings",
                 "team_score": 29,
                 "opponent_score": 31},
            ]
        },

        {
            "name": "San Francisco 49ers",
            "next_game": {
                "date": date(2024, 10, 6),
                "time": "1:05 PM",
                "opponent": "Arizona Cardinals"
            },
            "games": [
                {"week": 1,
                 "opponent": "New York Jets",
                 "team_score": 32,
                 "opponent_score": 19},

                {"week": 2,
                 "opponent": "Minnesota Vikings",
                 "team_score": 17,
                 "opponent_score": 23},

                {"week": 3,
                 "opponent": "Los Angeles Rams",
                 "team_score": 24,
                 "opponent_score": 27},

                {"week": 4,
                 "opponent": "New England Patriots",
                 "team_score": 30,
                 "opponent_score": 13},
            ]
        },
        ]
        return teams

def load_log():
    
    # PSEUDOCODE:
    # try to open a previously created log file
    # if it exists, read all lines and return them to user
    
    # AI was used to help with "FileNotFoundError"
    try:
        with open(log, "r", encoding="utf-8") as f:
            lines = f.readlines()
            return lines
    except FileNotFoundError:
        print("Unfortunately, no previous log was found!")
        print("We will create another one for you!")
        return []


def save_log(team_name, choice_type_text):
   
    #PSEUDOCODE:
    # open the log file
    # write the line to the file
        with open(log, "a", encoding="utf-8") as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_line = f"{timestamp} Team: {team_name} Choice: {choice_type_text}\n"
            f.write(log_line)

def int_option(prompt, min, max):
    
    # PSEUDOCODE:
    # loop forever
        # ask the user for input
        # try to change to integer
            # if fail, show error message and continue
        # if number is not a choice, print error message
    while True:
        user_choice = input(prompt).strip()

        if user_choice == "":
            print("You must choose one of the choices given above! Try again!")
            continue

        try:
            number = int(user_choice)
        except ValueError:
            print("You must enter a whole number! Try again!")
            continue

        if number < min or number > max:
            print(f"Please enter a number between {min} and {max}.")
            continue

        return number


def y_n_choice(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("y", "yes"):
            return True
        elif answer in ("n", "no"):
            return False
        else:
            print("Please answer with 'y' or 'n'.")

def team_menu(teams):
    
    #PSEUDOCODE:
    # sort the list of teams alphabetically by name
    #  print a numbered menu
    sorted_teams = sorted(teams, key=lambda t: t["name"])

    menu = {}
    print("\nTeams you can choose from: ")
    for index, team in enumerate(sorted_teams, start=1):
        print(f"{index}. {team['name']}")
        menu[index] = team

    print("0. Quit program")
    return menu


def show_game(team):
    #PSEUDOCODE:
    # format the date using strftime
    # print the opponent, date, and time
    next_game = team["next_game"]
    game_date = next_game["date"]
    date_str = game_date.strftime("%A, %B %d, %Y")

    print("Upcoming Game")
    print(f"Team: {team['name']}")
    print(f"Opponent: {next_game['opponent']}")
    print(f"Date: {date_str}")
    print(f"Time: {next_game['time']}")

def team_stats(team):
    #PSEUDOCODE:
    # get the list of games from the team list
    # for each game show opponent, date and game stats
    # use tabulate to print a table
    games = team["games"]
    rows = []

    for game in games:
        score_str = f"{game['team_score']} - {game['opponent_score']}"
        rows.append([game["week"], game["opponent"], score_str])

    print("\n--- Game Scores ---")
    # Used tabulate to make a table
    # AI was used to help learn tabulate
    print(tabulate(rows, headers=["Week", "Opponent", "Score"], tablefmt="github"))

def main():
    #PSEUDOCODE:
    # load previous log file if there is one
    # load the team stats
    # loop:
        # show the team menu
        # ask the user to choose a team by choosing a number assigned to that team
        # ask the user whether they want:
            #1. next game
            #2. previous games / stats
        # show the stats
        # put the user's choice in a file
        # ask if the user wants to look up another team
         #   if not, break
    print("Welcome to the Juliens NFC stat program!")
    print("You can look up the next game or previous game results for the following NFC teams.")

    previous_use = load_log()
    if previous_use:
        print(f"You have used this program {len(previous_use)} times to look up a team!")
    else:
        print("We've noticed this is your first time using this program. Welcome!")

    teams = nfc_teams()

    while True:
        menu = team_menu(teams)
        max_choice = len(menu)

        team_number = int_option(
            f"Choose a team by number (1-4): ",
            0,
            max_choice
        )

        if team_number == 0:
            print("Thank you for using the Juliens NFC stat program. Come back soon!")
            break

        chosen_team = menu[team_number]
        print(f"You chose: {chosen_team['name']}")

        print("What information would you like?")
        print("1. Next game (date, time, opponent)")
        print("2. Team stats (previous games and scores)")

        stat_choice = int_option("Enter 1 or 2: ", 1, 2)

        if stat_choice == 1:
            show_game(chosen_team)
            choice_text = "Next Game"
        else:
            team_stats(chosen_team)
            choice_text = "Team Stats (Previous Games)"

        # Log the user choice
        save_log(chosen_team["name"], choice_text)

        # Ask if they want to see another
        again = y_n_choice("Would you like to look up another team? (y/n): ")
        if not again:
            print("Thank you for using the Juliens NFC program. Come back soon!")
            break

if __name__ == "__main__":
    main()