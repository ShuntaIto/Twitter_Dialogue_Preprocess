# Twitter_Dialogue_Pre-process

## What's this?

This ipynb contains script to pre-process data collected by twitter_scraper(https://github.com/Marsan-Ma/twitter_scraper) for Seq2Seq.

I make this script for Japanese data, however, you can apply this script to any languages if you change regex patterns(r'hogehoge').

## How to use

###  load data

Twitter dialogue data collected by twitter_scraper are saved as text file(ex. hogehoge.txt).At first you have to load the data.
```py
raw_twitter_pairs = open('hogehoge.txt','r',encoding='utf-8')
twitter_pairs = raw_twitter_pairs.readlines()
```

###  import module

You have to import this module. I like to import it as tdp, original name is too long to use. 

```py
import twitter_dialogue_preprocess as tdp
```

###  pre-process

```py
twitter_preprocessed_data = tdp.pre_process(twitter_pairs)
```

### use ipynb

You can use twitter_preprocessing.ipynb on Jupyter instead of using module. If you want to change detail of the script, I recommend ipynb file.


##  Function
### delete_self_reply_pairs

This function removes self-reply pairs from data. They are not 'dialogue'.

### delete_hashtag_tweets_pairs

This function removes tweet-pairs from data if they contain inline hashtags(like #hogehoge).

Instagram culture influence twitter users and change their use of hashtag. Their sentences were very difficult for me to pre-process propely, so I decided to remove all tweets which contain inline hashtags.

### delete_hashtag_eos

This function removes hashtag at end of sequence from each tweet datum.

### delete_url

This function removes URL from each tweet datum.

### delete_username_sos

This function removes username(like @hogehoge) at start of sequence from each tweet datum.

Please use this function after using 'delete_self_reply_pairs'.

### delete_inline_username

This function removes inline username from each tweet datum.

Please use this function after using 'delete_username_sos'.

### delete_emoji

This function removes emoji(like 👌) from each tweet datum.

### delete_brackets

This function removes phrases in brackets(like 【hogehoge】,(´・ω・｀)).

### delete_blank

This function removes tweet-pairs from data if they contain blank tweet after using other functions.

### delete_line_feed_code

This function removes "line feed code", '\n', from each tweet datum.

### pairing

This function convert data to the list object of the list objects which store dialogue (query and response).

### pre_process

This function applies all functions to data.

```py
pre_process(twitter_data,pairing=False,save=False,save_name='twitter_preprocessed.pickle')
```

## License
MIT
