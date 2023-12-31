import praw
import pandas as pd
from praw.models import MoreComments

# Initialize the Reddit instance
reddit_read_only = praw.Reddit(client_id="#", client_secret="#",
                               user_agent="#")


# Function to get subreddit information
def get_subreddit_info(subreddit_name):
    subreddit = reddit_read_only.subreddit(subreddit_name)
    print("Display Name:", subreddit.display_name)
    print("Title:", subreddit.title)
    print("Description:", subreddit.description)


# Function to print top 5 hot posts in a subreddit
def print_top_hot_posts(subreddit_name, limit=5):
    subreddit = reddit_read_only.subreddit(subreddit_name)
    for post in subreddit.hot(limit=limit):
        print(post.title)
        print()


# Function to scrape top posts of the current month and save to CSV
def scrape_and_save_top_posts(subreddit_name, time_filter="month", filename="Top Posts.csv"):
    subreddit = reddit_read_only.subreddit(subreddit_name)
    posts = subreddit.top(time_filter=time_filter)

    posts_dict = {"Title": [], "Post Text": [], "ID": [], "Score": [], "Total Comments": [], "Post URL": []}
    for post in posts:
        posts_dict["Title"].append(post.title)
        posts_dict["Post Text"].append(post.selftext)
        posts_dict["ID"].append(post.id)
        posts_dict["Score"].append(post.score)
        posts_dict["Total Comments"].append(post.num_comments)
        posts_dict["Post URL"].append(post.url)

    top_posts = pd.DataFrame(posts_dict)
    top_posts.to_csv(filename, index=False)
    return top_posts


# Function to scrape comments from a specific post and save to CSV
def scrape_and_save_comments(url, filename="Top Comments.csv"):
    submission = reddit_read_only.submission(url=url)
    post_comments = []
    for comment in submission.comments:
        if isinstance(comment, MoreComments):
            continue
        post_comments.append(comment.body)

    comments_df = pd.DataFrame(post_comments, columns=['Comments'])
    comments_df.to_csv(filename, index=False)
    return comments_df


# Executing functions
subreddit_name = "Eldenring"
get_subreddit_info(subreddit_name)
print_top_hot_posts(subreddit_name)
top_posts = scrape_and_save_top_posts(subreddit_name)
print("--\n")
print(top_posts)

url = "https://www.reddit.com/r/Eldenring/comments/18uodah/do_you_think_marika_loved_her_children/"
comments_df = scrape_and_save_comments(url)
print("\n--\n")
print(comments_df)
