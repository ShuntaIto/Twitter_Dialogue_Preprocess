# Twitter_Dialogue_Preprocess

## What's this?

This ipynb contains script to pre-process data collected by twitter_scraper(https://github.com/Marsan-Ma/twitter_scraper).

## How to use

You have to build Jupyter environment.

Open twitter_preprocessing.ipynb on Jupyter, change the filename at 'load data' to your data and Run all cells.

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

### pre_process

This function applies all functions to data.

## License
MIT
