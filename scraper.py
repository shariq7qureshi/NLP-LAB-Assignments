import wikipediaapi
import wikipedia
import os

def is_actual_game(page):
    try:
        categories = page.categories.keys()
        for cat in categories:
            if "video game" in cat.lower():
                return True
    except:
        pass
    return False


def get_game_data():
    wiki = wikipediaapi.Wikipedia(
        user_agent="Shariq7qureshi_Bot/1.0 (contact: shariqnadeemqureshi@gmail.com)",
        language="en",
    )

    os.makedirs("games_data", exist_ok=True)

    queries = [
        "multiplayer video games",
        "online games",
        "fps games",
        "battle royale games",
        "steam games",
        "popular pc games",
        "esports games"
    ]

    all_titles = set()

    for q in queries:
        try:
            results = wikipedia.search(q, results=50)
            for r in results:
                all_titles.add(r)
        except:
            pass

    print("Total collected titles:", len(all_titles))

    count = 0

    for title in all_titles:
        try:
            page = wiki.page(title)

            if page.exists() and is_actual_game(page) and len(page.text) > 1000:

                filename = title.replace(" ", "_").replace("/", "_")

                with open(f"games_data/{filename}.txt", "w", encoding="utf-8") as f:
                    f.write(page.text)

                print("Saved:", title)
                count += 1

            else:
                print("Skipped (not a game):", title)

        except Exception as e:
            print("Error:", title)

    print(f"\nDone! {count} REAL game files saved")


if __name__ == "__main__":
    get_game_data()