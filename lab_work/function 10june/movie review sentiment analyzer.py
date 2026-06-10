# List of movie reviews to be processed
reviews = [
    "excellent movie", "average story", "excellent acting", 
    "poor direction", "excellent visuals", "poor screenplay", 
    "good music", "excellent climax", "average performance", 
    "good cinematography"
]

# Function to count the occurrences of specific sentiment keywords
def count_sentiments(reviews):
    # Initialize a dictionary to store counts for each category
    counts = {"Excellent": 0, "Good": 0, "Average": 0, "Poor": 0}
    for review in reviews:
        # Increment the count if the keyword exists in the review string
        if "excellent" in review: counts["Excellent"] += 1
        elif "good" in review: counts["Good"] += 1
        elif "average" in review: counts["Average"] += 1
        elif "poor" in review: counts["Poor"] += 1
    
    # Display the results formatted as per the sample output
    for sentiment, count in counts.items():
        print(f"{sentiment} Reviews: {count}")

# Function to find the single word that appears most frequently across all reviews
def most_common_word(reviews):
    words = []
    # Break each review into individual words and add them to a master list
    for review in reviews:
        words.extend(review.split())
    
    # Identify the word with the highest frequency count in the list
    common = max(set(words), key=words.count)
    print(f"\nMost Common Word:\n{common}")

# Function to identify and return the review with the most characters
def longest_review(reviews):
    # Find the string with the maximum length in the reviews list
    longest = max(reviews, key=len)
    print(f"\nLongest Review:\n{longest}")

# Function to filter and print all reviews that contain a specific search term
def reviews_with_keyword(reviews, keyword):
    print(f"\nReviews containing '{keyword}':")
    for review in reviews:
        # Check if the keyword is a substring of the current review
        if keyword in review:
            print(review)

# Execution of the functions to match sample output
count_sentiments(reviews)
most_common_word(reviews)
longest_review(reviews)
reviews_with_keyword(reviews, "excellent")