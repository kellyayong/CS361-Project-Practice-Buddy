# Author: Kelly Yong


if __name__ == "__main__":
    # Home  - Title
    title = """
____________  ___  _____ _____ _____ _____  _____  ______ _   _______________   __
| ___ \ ___ \/ _ \/  __ \_   _|_   _/  __ \|  ___| | ___ \ | | |  _  \  _  \ \ / /
| |_/ / |_/ / /_\ \ /  \/ | |   | | | /  \/| |__   | |_/ / | | | | | | | | |\ V /
|  __/|    /|  _  | |     | |   | | | |    |  __|  | ___ \ | | | | | | | | | \ /
| |   | |\ \| | | | \__/\ | |  _| |_| \__/\| |___  | |_/ / |_| | |/ /| |/ /  | |
\_|   \_| \_\_| |_/\____/ \_/  \___/ \____/\____/  \____/ \___/|___/ |___/   \_/
"""

    subtitle = "Are you practicing your instrument? Log your sessions here."

    # Display Title & Subtitle
    print(f"{title}\n{subtitle}\n")

    # Home Page Options
    home_options = {
        1: "Add new practice session",
        2: "Search for sessions",
        3: "View all past practice sessions",
        4: "Edit session",
        5: "Delete session",
        6: "Exit"
    }
