# Create a dictionary to store player names and their runs
runs = {
    "Virat": 645, "Rohit": 512, "Gill": 698, "Rahul": 435,
    "Hardik": 278, "Pant": 534, "Surya": 389, "Jadeja": 301,
    "Iyer": 455, "KL": 410
}

# Task 1: Check every player and print their name if they scored over 500
print("Players Scoring More Than 500 Runs:")
for player, score in runs.items():
    if score > 500:
        print(player)

# Task 2: Find the player with the highest (max) score
orange_cap_player = max(runs, key=runs.get)
print(f"\nOrange Cap Winner: {orange_cap_player} ({runs[orange_cap_player]})")

# Task 3: Find the player with the lowest (min) score
lowest_scorer = min(runs, key=runs.get)
print(f"Lowest Scorer: {lowest_scorer} ({runs[lowest_scorer]})")

# Task 4: Add up all the scores in the dictionary
total_runs = sum(runs.values())
print(f"Total Tournament Runs: {total_runs}")

# Task 5: Create a new list for players who scored less than 400
below_400 = [player for player, score in runs.items() if score < 400]
print(f"\nPlayers Scoring Below 400: {below_400}")

# Task 6: Count how many players have a score between 400 and 600
between_400_600 = len([p for p in runs.values() if 400 <= p <= 600])
print(f"Players Between 400 and 600 Runs: {between_400_600}")