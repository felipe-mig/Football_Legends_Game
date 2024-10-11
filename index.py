# IMPORTS
## art
from art import logo
from art import playerlogo
from art import vs
from art import gameover
## Import the database from game_data.py
from game_data import data
## Select random data
import random


def format_data(player):
    """Takes the player data and returns the printable format"""
        # - This will go into the dictionary <-- Our database, and pull out the value under the key 'name', and save it to the variable 'player_name'.
        # - ATTENTION: Make sure that you don't have any typos in your keys here, because remember they need to match these precisely in order for it to not error out. So, is better to copy and and paste key from the database.
    player_name = player["name"]
    player_description = player["description"]
    player_country = player["country"]
    player_scores = player["scores_in_national_team"]
        # - Once that we've got all of these pieces of data, we can now print the final version.
        # - And instead of printing the final outcome we are going to return it as the output. So now we can call that function ahead.
    print("\n")
    return f"\033[38;5;255mName: \033[38;5;255m{player_name} \nAbout: {player_description}\nCountry: {player_country}\n" #Goals: {player_scores}


# Function to display the name of the player and the goals once the user types the wrong answer
def player_name_for_game_over_info(player):
    """Takes the player data but only the name"""
    player_name_two = player["name"]
    return f"{player_name_two}"


# This function is to check if the player chose the correct answer
def check_answer(user_guess, player_a_scores, player_b_scores):
    """Takes the user's guess and the 'scores_in_national_team' counts and returns if they got it right"""
    # - Use if statement to check if user is correct.
    if player_a_scores > player_b_scores:
        # Long way to do this:
            # if user_guess == "a":
            #     return True
            # else:
            #     return False
        # Short version:
        return guess == "a"
    else:
        return guess == "b"
    # ↑ Now basically the code says, if A has more scores, and they guessed A, then return True. If B has more scores, and they guessed B, then return True, and if the opposite happens, then return False.


# GAME STARTS
print(f"\033[38;5;227m{logo}\033[0m")
print("\033[38;5;255mINTRUCTIONS")
print("------------------------------------------------------------------------------------------------------------------------------------")
print("-Welcome to Football Legends!")
print("-Your football knowledge is going to be tested by answering which legends have more goals in their national teams. Good luck and enjoy!")
print("-Notice that the info of the players are current as of \033[38;5;11mOctober 11, 2024.\033[0m")
print("\033[38;5;255m------------------------------------------------------------------------------------------------------------------------------------")
# Clear the screen
print("\n" * 2)
 # - score keeping step 2
score = 0
# Create a flag for repeating the game meanwhile they are guessing correctly
game_should_continue = True

# While loop to repeat the game meanwhile they are guessing correctly
while game_should_continue:
    # Generate a random player from the game data
        # - Select random data
    player_a = random.choice(data)
    player_b = random.choice(data)
        # - This is to check and make sure that player_a is different from player_b. If they are equal we make sure that player_b is regenerated.
    if player_a == player_b:
        player_b = random.choice(data)

        # - now we can call that function down here, and we can pass in each player in turn. So we're going to call format_data, and we're going to pass in the player_a for this first line, and then we are going to do the same for player_b.
    print(f"\033[38;5;117m▌PLAYER A▐\033[0m\n\n{format_data(player_a)}")
    print(vs)
    print(f"\033[38;5;196m▌PLAYER B▐\033[0m\n\n{format_data(player_b)}")

    # Ask user to a guess
    print("\n" * 2)
    guess= input("-Who scored more goals with the national team, \033[38;5;117mPLAYER A\033[0m \033[38;5;255mor \033[38;5;196mPLAYER B\033[0m \033[38;5;255m? \n-Type \033[38;5;117m'A'\033[0m \033[38;5;255mor \033[38;5;196m'B'\033[0m\033[38;5;255m:\n\n ").lower()


    # Check if user is correct.
        # - Get scores count of each account
        # - pass the key 'scores_in_national_team' into the 'player_a_scores_in_national_team_count' and 'player_b_scores_in_national_team_count'
    player_a_scores_in_national_team_count = player_a["scores_in_national_team"]
    player_b_scores_in_national_team_count = player_b["scores_in_national_team"]

     # - Here is where we check if the user typed the correct answer by calling the function 'check_answer()' and passing its parameters into the new 'is_correct' variable that we need to create.
    is_correct = check_answer(guess, player_a_scores_in_national_team_count, player_b_scores_in_national_team_count)

    # USER ANSWER CORRECTLY
    # Give user feedback on their guess
        # - score keeping step 1
    if is_correct:
        # - as we play on, and if they get it correct, then the score should be incremented by one each time
        score += 1
        # - info about the correct answer
        print("\n" * 3)
        print(f"-That's'correct mate!\n")
        print("\033[38;5;3m───────────────────────────────\033[0m") 
        print(f"\033[38;5;255m{player_name_for_game_over_info(player_a)} goals → {player_a_scores_in_national_team_count}")
        print(f"{player_name_for_game_over_info(player_b)} goals → {player_b_scores_in_national_team_count}")
        print("\033[38;5;3m───────────────────────────────\033[0m") 
        print(f"\n\033[38;5;220m«\033[0m \033[38;5;255mCurrent score: [ {score} ]\033[0m \033[38;5;220m»\033[0m")
        print("\n")
    else:
        # GAME OVER inforamation
        print(f"\n-Sorry mate, that's wrong...\n")
        # - # - info about the correct answer
        print("───────────────────────────────")
        print(f"{player_name_for_game_over_info(player_a)} goals → {player_a_scores_in_national_team_count}")
        print(f"{player_name_for_game_over_info(player_b)} goals → {player_b_scores_in_national_team_count}")
        print("───────────────────────────────")
        # print(f"~GAME OVER~\n")
        print(gameover)
        print(playerlogo)
        print(f"\n\033[38;5;220m«\033[0m \033[38;5;255mFinal score: [ {score} ]\033[0m \033[38;5;220m»\033[0m")
        print("\n" * 2)
        print("\033[38;5;255m© 2024 Felipe Iglesias Garcia")
        print("\n" * 2)
        
        # - this is the point where we're going to change 'game_should_continue' to False, so the game ends after GAME OVER and final score are printed
        game_should_continue = False


