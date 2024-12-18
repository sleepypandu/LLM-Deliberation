import subprocess

games = ["base", "base_7players", "base_rewritten", "game1", "game2", "game3"]
params = dict(zip(games, [(6,5)]*6))
params["base_7players"] = (7,6)

def get_command(window_size, game, round_num):
    exp_name = game + "_test"
    if game not in games:
        return "Sorry, that game is unavailable. Please try again with one of " + ", ".join(games)
    command = ["python", "main.py", "--exp_name", exp_name, "--agents_num", str(params[game][0]), 
               "--issues_num", str(params[game][1]), "--window_size", window_size, "--game_dir", 
               "./games_descriptions/"+game,"--rounds_num", round_num]
    return command

play_again = True

while play_again:
    game = input("What game would you like to play? Choices: " + ", ".join(games) +". ")
    window_size = input("Window size? ")
    round_num = input("How many rounds should we do? ")
    # Command as a list of strings (recommended)
    command = get_command(window_size, game, round_num)
    print(command)
    print(" ".join(command))
    if type(command) is str:
        continue
    # Run the command and capture output
    result = subprocess.run(command, capture_output=True, text=True)
    # Print the output
    # print(result.stdout)
    # print("Error Output:", result.stderr)

    # # Check if there was an error
    # if result.returncode != 0:
    #     print(f"Command failed with return code: {result.returncode}")
    again = input("Play Again? ")
    play_again = True if again[0].lower() == "y" else False