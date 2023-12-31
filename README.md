# Reddit-Web-Scraping

The provided script is a comprehensive Python program designed to interact with Reddit using the PRAW (Python Reddit API Wrapper) library. For this specific code, it focuses on the subreddit "Eldenring" but is structured to be easily adaptable for other subreddits. The script is divided into distinct functions, each with a clear purpose:

Initializing Reddit Instance: The script starts by setting up a read-only Reddit instance with specified credentials. This is a prerequisite for all subsequent operations involving Reddit API interactions.

Subreddit Information Retrieval: get_subreddit_info function fetches and prints basic details about the specified subreddit, including its display name, title, and description.

Fetching and Displaying Hot Posts: print_top_hot_posts accesses the top hot posts from the subreddit. It's set to retrieve the top 5 posts but can be adjusted with the limit parameter.

Scraping Top Posts: The scrape_and_save_top_posts function scrapes the top posts within a specified time filter (default is the current month) from the subreddit. It extracts key information like the title, text, ID, score, total comments, and post URL. This data is then stored in a pandas DataFrame and saved as a CSV file named "Top Posts.csv".

Scraping Comments from a Specific Post: scrape_and_save_comments targets a specific Reddit post using its URL. It gathers all top-level comments (excluding nested replies) and compiles them into a DataFrame, which is then saved as "Top Comments.csv".

Execution: The script executes these functions in sequence, showcasing the subreddit information, printing top hot posts, scraping top posts of the current month, and finally scraping comments from a specific post.
