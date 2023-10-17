# Reddit-data-engineering-automation
This is an end-to-end Data Engineering project where I leverage Reddit API to get the top posts of the day from my favorite subreddits so that I don't have to go and look for it.  

## Purpose:
I wanted to automate the task of looking for diferent top posts from different sub-reddits so that I don't have to spend a lot of time on going through pages to pages, filtering through the best upvotes.

## Tools Used:
* Apache AirFlow (Schedule tasks and automate the workflow)
* Python (Main Programming language)
* Reddit API (API and web-scrapping)
* AWS for EC2 and bucket

## Output: 
It dumps the CSV file everyday to the S3 bucket at a scheduled time and the csv file in future will be converted or used to build a better GUI friendly frontend.
