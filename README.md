# sentimental
Fintech Project 2 - Analysis Of Crypto Pricing and Ukraine War Twitter Sentiment  

## Project Overview
An analysis of Twitter Data based on Ukraine and crypto queries. This data was cleaned, and then run through sentiment analysis, looking for relationships between crypto prices and twitter sentiment on war/crypto topics.  

[Presentation slides](media/preso.pdf)  

See [installation guide](#installation-guide) below for specifics on setting up your environment.

---

## Data Collection And Preparation
TBD  

## Approach Taken  



## Results  


## Technologies And Modules Used  

This proect uses [python 3.7](https://docs.python.org/3.7/) and the following modules:  

- [time](https://docs.python.org/3.7/library/time.html?highlight=time#module-time)
- [datetime](https://docs.python.org/3.7/library/datetime.html#module-datetime)
- [re](https://docs.python.org/3.7/library/re.html?highlight=re#module-re)
- [pandas](https://pypi.org/project/pandas/)
- [numpy](https://pypi.org/project/numpy/)
- [wordcloud](https://pypi.org/project/wordcloud/)
- [nltk](https://github.com/nltk/nltk)
- [json](https://docs.python.org/3/library/json.html)
- [folium](https://pypi.org/project/folium/)
- [requests](https://docs.python-requests.org/en/latest/)
- [pysentimiento](https://github.com/pysentimiento/pysentimiento)
- [rfc3339](https://pypi.org/project/rfc3339/)
- [tqdm](https://pypi.org/project/tqdm/)
- [iso8601](https://pypi.org/project/iso8601/)


See [installation guide](#installation-guide) below for specifics on setting up your environment.

---


## Installation Guide

You will need Python 3.7 for this application to run. An easy way to install python 3.7 is to download and install [Anaconda](https://www.anaconda.com/products/individual). After installing anaconda, open a terminal/command-prompt, and setup a python 3.7 environment, and then activate it like so:

```
# creating a python 3.7 environment
# name can be any friendly name to refer to your environment, eg 'dev'
conda create --name dev python=3.7 anaconda

# activating the environment
conda activate dev
```

Next, use [pip](https://pypi.org/project/pip/) to install the required modules from the [list above](#Technologies-And-Modules)


```
# instaling required modules
$ pip install pandas
$ pip install numpy
$ etc...
```
You are now ready to run the program!

---

## Usage Notes

**NOTE** Twitter API Usage  
You must sign up for a Twitter API key in order to authenticate and fetch twitter data.  
See [config_example](./config_example.py) for how to stage your Twitter API [Bearer Token](https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens)  

[WordCloud](./wordcloud_viz.ipynb)  Generates a wordcloud visual from query data. Based on [folium](https://pypi.org/project/folium/) library.  


## Contributors

[Peter Morales](https://github.com/pmm09c)  
[Shivangi Gupta](https://github.com/shivangiuw)   
[Jaime Aranda](https://github.com/Aranda80)  
[David Lopez](https://github.com/sububer)  

---

## License

MIT