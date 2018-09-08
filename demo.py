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


def main():
	print (" \n Hello World \n")
	print ("Beginning the Tweepy Test\n\n")

	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

	api = tweepy.API(auth)

	public_tweets = api.home_timeline()
	for tweet in public_tweets:
		print ("\n")
		print (tweet.text)


main()



