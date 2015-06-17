How To Replace Yourself With A Bot
==================================

Procedure
---------
1. Review what a twitter bot is
2. Create a low-tech bot
3. Cover a basic bot script/system
4. Break into groups/teams to work on bots




#What is a twitter bot?

* Automated posts on the Twitter microblogging service.
* Yes - some are spam to entice clicks. Others post @replies or automatically retweet in response to tweets that include a certain word or phrase. 
* 24% of tweets that are on Twitter? source: [Mashable](http://mashable.com/2009/08/06/twitter-bots/)
* new art form
* internet as poetry
* experimental, weird, community

### Bot styles

Chatbot, datamining, markov chains, visual generation, text generation, mashup/text remixing, scheduled tweets, response bots...

#Some Twitter bots

* [All bots by Darius Kazemi](https://twitter.com/tinysubversions/lists/darius-kazemi-s-bots/members)
* [Big Ben](https://twitter.com/big_ben_clock) by Jonathan Marchant
* [Alicia Winderland](http://twitter.com/aliciawnderland) by Lee Tusman
* [story of glitch](https://twitter.com/storyofglitch) by thricedotted
* [Pentametron](https://twitter.com/pentametron/) by Rhanjit Bhatnagar
* [Deleuze and Guattari](https://twitter.com/DeleuzeGuattari)
* [GreatArtBot](https://twitter.com/greatartbot) by Anthony Prestia
* [Babelling Borges](https://twitter.com/BabellingBorges)
* [Two Headlines](https://twitter.com/TwoHeadlines) by Darius Kazemi
* [Everyword](http://twitter.com/everyword) by Allison Parrish
* [Stealth Mountain](https://twitter.com/StealthMountain) by Jason Eppink
* [Your Title Sucks/The Answer Is No](https://twitter.com/YourTitleSucks) by Jason Eppink

## Bot Approaches / Low Tech v. High Tech

# Low Tech
* Start With a Concept
* Find/write/develop your text
* You type out your tweets in advance.
* You use a scheduler like [Hootsuite](http://hootsuite.com), [Buffer](http://buffer.com) or [Botize](http://botize.com). Or a simple script/program like [IFTTT](https://ifttt.com).

# High Tech

* Using cronjobs
* cron is a daemon, meaning it starts once and stays dormant until it is needed (a web server is also a daemon. it waits for a user to type in the url to load.)

## Register a new twitter name/handle

* Note: You can make many accounts under same email address if you use YourEmail+NewTwitterHandle@gmail.com for example (you can do this while using private browse so you can have mulitple accounts open at once)
* Verify via email after making new account

## Register a new app on twitter & get access tokens/keys

* Go to [https://apps.twitter.com/](https://apps.twitter.com/)
  * You need to register a phone number (arrrgh) if not already done. Must be unique!
* Create new app
* Go to Keys and Access Tokens tab
* Access Level should be: Read and write
* At bottom of page click the button to generate access tokens

## Getting started With twitter in Python

* We'll be installing [tweepy](https://github.com/tweepy/tweepy) to access twitter in Python
* Open the command line/terminal shell and run this in Bash

Linux

```sudo apt-get install python-pip```

OR

Mac

```
sudo easy_install pip #if not already installed
pip install virtualenv
pip install tweepy
```

# Create your python bot

* Example script such as scriptname.py
* Add your access tokens and keys
* Test it in your terminal with ```python scriptname.py```

# Sign up on digital ocean

* DigitalOcean is a virtual private server
* You create droplets aka virtual (cloud) servers
* Sign up for an Ubuntu server
* You will be emailed an ip address, etc, prompted to change emails
* Log in

# Login via ssh

Steps are [here](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-14-04)

# Connect to your server via ssh

Steps are [here](https://www.digitalocean.com/community/tutorials/how-to-connect-to-your-droplet-with-ssh)

# Upload Your Script

* You can upload to your server with ```scp```

```scp <path/to/file/on/your/computer> <username>@<hostname>:<destination path>```

for example

```scp /Users/2sman/Documents/code/github\ projects/Gamelan_Ebooks/gamelan* admin@45.55.87.237:~```

# Re-install what you need on remote

## Getting started With twitter in Python

* We'll be installing [tweepy](https://github.com/tweepy/tweepy) to access twitter in Python
* Install pip on digitalocean server to root

```
apt-get update
sudo apt-get install python-pip
pip install tweepy
```

# Create a cronjob

* first you need to add cron

```sudo apt-get install cron```

* Run ```crontab -e``` and you may have to select nano (2) as your editor
* Add to bottom ```0 * * * * python script.py``` to have it run once an hour








### Additional things/links

* [Corpora](https://github.com/dariusk/corpora) available to use
* 