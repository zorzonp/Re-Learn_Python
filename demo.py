####################################################################
##
##	Authors:		Peter Zorzonello
##	Last Update:	9/8/2018
##
##	Description:	Demo file to test out the Twitter API Tweepy
##
####################################################################

import tweepy

#this is the consumer key and secret, needed to authenticate with Twitter
CONSUMER_KEY = "O0FbWZf9VbNKom7LM0UvZJLst"
CONSUMER_SECRET = "s3nL8fORzmqjlTKQfvhlpsC8wGwXwGUard06gPJXaFmrunsEMN"
ACCESS_TOKEN = "804969750-yn7Yl2fKXcQzRLeTDGMYbPpdtbpfQb2ky31R114Z"
ACCESS_TOKEN_SECRET = "ZDb2nMfYIQ1I0TbK8HQFzCsUHKsjPuxdSPwx03k0mBvgJ"


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



