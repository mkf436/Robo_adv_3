# Robo_adv_3

A solution for Mari Freitas' robo adv project: (https://github.com/mkf436/Robo_adv_3)

Issues requests to the alphavantage stock market api: (https://www.alphavantage.co/)


pre-reqs:
anaconda 3.7
python 3.7
pip

#installation

clone or download this repository: https://github.com/mkf436/Robo_adv_3 on your computer then navigate there from the command line:

enter into the command line:
cd robo-advisor-screencast

Use anaconda to create and activvate a new virtual envinronment. From inside the virutal environment, install package. 

##set up
before using or developing application, obtain an Alphavantage API key from https://www.alphavantage.co/support/#api-key (e.g. "abc123")

after obtaining an API key, create a new file in this repository called ".env", and update the contents of the ".env" file to specify your real API key

ALPHAVANTAGE_API_KEY="abc123"

##usage

run the recommendation script:

py
python app/robo_advisor.py

##license (license.md)