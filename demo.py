####################################################################
##
##	Authors:		Peter Zorzonello
##	Last Update:	9/8/2018
##
##	Description:	Demo file to test out the Twitter API Tweepy
##
####################################################################

import tweepy
import globals_secret

#this is the consumer key and secret, needed to authenticate with Twitter
CONSUMER_KEY = globals_secret.CONSUMER_KEY
CONSUMER_SECRET = globals_secret.CONSUMER_SECRET
ACCESS_TOKEN = globals_secret.ACCESS_TOKEN
ACCESS_TOKEN_SECRET = globals_secret.ACCESS_TOKEN_SECRET


def getHandle():
	username = input("Enter a Twitter Handle: ")
	return username

def getUsersTweets(user, api):
	user_tweets = api.user_timeline(user)
	for tweet in user_tweets:
		print (tweet.text)
		print ("Tweet id: "+ str(tweet.id))
		print ("Tweet created_at: " + str(tweet.created_at) + "\n")



def printTweetsFromTimeLine(api):
	public_tweets = api.home_timeline()
	for tweet in public_tweets:
		print ("\n")
		print (tweet.text)

def main():
	print (" \n Hello World \n")
	print ("Beginning the Tweepy Test\n\n")

	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

	api = tweepy.API(auth)

	#printTweetsFromTimeLine(api)

	user = getHandle()
	print ("\n User: "+ user + "\n")
	getUsersTweets(user, api)

main()



