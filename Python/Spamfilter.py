from Processing import Processing
import re

def filter_spam(messages):

	messageslist = messages.split()

	for word in messageslist:
		if re.findall(word, messages) > 4:
			return False

	return True