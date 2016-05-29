import praw
import time

RIGHT_USERNAME=""
WRONG_USERNAME=""
PASSWORD=""
r = praw.Reddit("Mentions checker by /u/Pandemic21")
r.login(WRONG_USERNAME,PASSWORD,disable_warning="True")

while 1:
	messages = r.get_unread()
	for message in messages:
		body = "[Context here](https://www.reddit.com" + message.context + ")\n\n" + message.body
		r.send_message(RIGHT_USERNAME, message.subject, body)
		message.mark_as_read()
	sleep(300)
