import os

def merge_files():
    folder_path = "games_data"
    output_file = "Top_Multiplayer_PC_Games_Dataset.csv"

    with open(output_file, "w", encoding="utf-8") as outfile:
        # CSV Header
        outfile.write("Game,Content\n")

        for filename in os.listdir(folder_path):
            if filename.endswith(".txt"):
                file_path = os.path.join(folder_path, filename)

                with open(file_path, "r", encoding="utf-8") as infile:
                    content = infile.read()

                    content = content.replace("\n", " ").replace(",", " ")

                    game_name = filename.replace(".txt", "")

                    outfile.write(f"{game_name},{content}\n")

    print("Master Dataset Created Successfully!")

if __name__ == "__main__":
    merge_files()