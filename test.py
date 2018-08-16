from sys import argv
from commitTelegramBot import CommitTelegramBot

if __name__ == '__main__':
	bot = CommitTelegramBot(argv[1], argv[2], argv[3], argv[4])
	print("today's commit count total : %s" % bot.count_total())
	bot.handler()
