import praw
import re
import time

user_agent = ("BjarndPrinter 0.2")

r = praw.Reddit(user_agent = user_agent)

subreddit = r.get_subreddit("all")

already_done = set()
search_for = "dog"
while 1:
	print("Refreshing...")
	for submission in subreddit.get_hot(limit=100):
	    flat_comments = praw.helpers.flatten_tree(submission.comments)
	    for comment in flat_comments:
	    	if hasattr(comment, 'body'):
		    	if re.search(r"\b{}\b".format(search_for), str(comment.body), re.IGNORECASE) and comment.id not in already_done:
		    		with open('dump.txt', 'a') as f:
		    			f.write("URL: {} \nComment: {} \n-------------------------".format(comment.permalink, comment.body) + "\n")
		    		print("URL: {} \nComment: {} \n-------------------------".format(comment.permalink, comment.body))
		    		already_done.add(comment.id)
	print("Finished refresh cyle; 1 minute sleep")
	time.sleep(60)