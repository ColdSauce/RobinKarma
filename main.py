import time
import requests
import json

COMMENT_KARMA_MULTIPLYER = 1.0 
LINK_KARMA_MULTIPLYER = 0.8

def get_json_from_url(username):
	reddit_url = "http://www.reddit.com/user/{}/about.json".format(username.strip())
	user_agent = {'User-agent': 'Mozilla/5.0'}
	return requests.get(reddit_url, headers= user_agent).text

def main():
	final_total = -1
	final_username = ""
	final_link_karma = 0
	final_comment_karma = 0
	while 1:
		username = raw_input()
		if username == 'EOFEOF':
			break
		html_reddit = get_json_from_url(username)
		total = 0
		total = int(json.loads(html_reddit)['data']['link_karma']) * LINK_KARMA_MULTIPLYER
		total += int(json.loads(html_reddit)['data']['comment_karma']) * COMMENT_KARMA_MULTIPLYER
		if total > final_total:
			final_total = total
			final_username = username
		time.sleep(1)
	print "{} wins the karma contest! With a score of {}".format(final_username, final_total)




if __name__ == '__main__':
	main()