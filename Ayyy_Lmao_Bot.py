import praw
import time

r = praw.Reddit(user_agent = "Ayyy Lmao Bot by Cory /u/belly_on_wheels")
r.login()

words_to_match = ["ayyy", "ayy", "ayyyy", "ayyyyy", "ay"]
cache = []

def run_bot():
	print ("Grabbing Subreddit...")
	subreddit = r.get_subreddit("test")
	print("Grabbing Coments...")
	comments = subreddit.get_comments(limit=25)
	for comment in comments:
		comment_text = comment.body.lower()
		is_match = any(string in comment_text for string in words_to_match)
		if comment.id not in cache and is_match:
			print ("Match Found! Comment ID:" + comment.id)
			comment.reply('lmao')
			print ("Reply Succesful")
			cache.append(comment.id)
	print ("Comment Loop Finished.  Time to Sleep.")

while True:
	run_bot()
	time.sleep(10)