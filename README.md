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

## To Reuse this Repo:
* Reddit-key-pair.pem is empty right now. You have to create a key-pair to replace this file. I removed the value in this file for security reasons
* For API access, you have to get API access Key and Secrets, I have replaced my values with ######### in this case. You can get your API access information and replace the ########
