# PageSpeedAPI
A python wrapper around PageSpeedAPI to get the aggregated performance score and opportunities for each specified url

# Steps to run: 

1. Install the requirements and then make a file urls.xls specifying the url, mode (desktop or mobile) and client name
2. Get a free API key from Google 
3. Run fetch_details.py enter the key in the command line and then the script genarates a csv for each specified url with score and opportunities. 

Sample urls.xls included

# Requirements : 

Pythonn 3.x

Run the following commands  
1. pip install xlwt
2. pip install xlrd
3. pip install requests
