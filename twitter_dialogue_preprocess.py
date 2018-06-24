import re
import emoji
import pickle

def delete_self_reply_pairs(twitter_data):
    dialogue_tweets = []
    for i in range(1,len(twitter_data),2):
        if re.match('@',twitter_data[i])!=None:
            dialogue_tweets.append(twitter_data[i-1])
            dialogue_tweets.append(twitter_data[i])
    return dialogue_tweets

def delete_hashtag_tweets_pairs(twitter_data):
    hashtag = r'[#＃]([\w一-龠ぁ-んァ-ヴーａ-ｚ]+( |　))'
    dialogue_tweets = []
    for i in range(0,len(twitter_data),2):
        if re.search(hashtag,twitter_data[i])==None and re.search(hashtag,twitter_data[i+1])==None:
            dialogue_tweets.append(twitter_data[i])
            dialogue_tweets.append(twitter_data[i+1])
        else:
            pass
    return dialogue_tweets

def delete_hashtag_eos(twitter_data):
    hashtag = r'[#＃]([\w一-龠ぁ-んァ-ヴーａ-ｚ]+$)'
    dialogue_tweets = []
    for ele in twitter_data:
        ele_hashtag_deleted = re.sub(hashtag,'',ele)
        dialogue_tweets.append(ele_hashtag_deleted)
    return dialogue_tweets

def delete_url(twitter_data):
    url = r'(https?|ftp)(:\/\/[-_\.!~*\'()a-zA-Z0-9;\/?:\@&=\+\$,%#]+)'
    dialogue_tweets = []
    for ele in twitter_data:
        ele_url_deleted = re.sub(url,'',ele)
        dialogue_tweets.append(ele_url_deleted)
    return dialogue_tweets

def delete_username_sos(twitter_data):
    username = r'@([a-zA-Z0-9_…]+ )'
    dialogue_tweets = []
    for ele in twitter_data:
        ele_username_deleted = re.sub(username,'',ele)
        dialogue_tweets.append(ele_username_deleted)
    return dialogue_tweets

def delete_inline_username(twitter_data):
    username = r'@([a-zA-Z0-9_…]+)'
    dialogue_tweets = []
    for ele in twitter_data:
        ele_username_deleted = re.sub(username,'',ele)
        dialogue_tweets.append(ele_username_deleted)
    return dialogue_tweets

def delete_emoji(twitter_data):
    dialogue_tweets = []
    for ele in twitter_data:
        ele_emoji_deleted = ''.join(char for char in ele if char not in emoji.UNICODE_EMOJI)
        dialogue_tweets.append(ele_emoji_deleted)
    return dialogue_tweets

def delete_brackets(twitter_data):
    brackets = []
    brackets.append(r'【(.+)】')
    brackets.append(r'《(.+)》')
    brackets.append(r'\((.+)\)')
    brackets.append(r'（(.+)）')
    dialogue_tweets = []
    for ele in twitter_data:
        for bracket in brackets:
            ele = re.sub(bracket,'',ele)
        dialogue_tweets.append(ele)
    return dialogue_tweets

def delete_blank(twitter_data):
    space = r'\s+'
    dialogue_tweets = []
    for i in range(0,len(twitter_data),2):
        if twitter_data[i]=='' or twitter_data[i+1]=='':
            pass
        elif re.match(space,twitter_data[i])!=None or re.match(space,twitter_data[i+1])!=None:
            pass
        else:
            dialogue_tweets.append(twitter_data[i])
            dialogue_tweets.append(twitter_data[i+1])
    return dialogue_tweets

def delete_line_feed_code(twitter_data):
    dialogue_tweets = []
    for ele in twitter_data:
        ele_code_deleted = re.sub('\n','',ele)
        dialogue_tweets.append(ele_code_deleted)
    return dialogue_tweets

def pairing(twitter_data):
    pairing_data = []
    for i in range(0,len(twitter_data),2):
        pair = []
        pair.append(twitter_data[i])
        pair.append(twitter_data[i+1])
        pairing_data.append(pair)
    return pairing_data

def pre_process(twitter_data,pairing=False,save=False,save_name='twitter_preprocessed.pickle'):    
    try:
        data = delete_line_feed_code(delete_blank(delete_brackets(delete_emoji(delete_inline_username(delete_username_sos(delete_url(delete_hashtag_eos(delete_hashtag_tweets_pairs(delete_self_reply_pairs(twitter_data))))))))))
        num_rawdata = int(len(twitter_data)/2)
        num_processed_data = int(len(data)/2)
        yield_rate = num_processed_data/num_rawdata
        print('The Number of Raw Data: '+str(num_rawdata))
        print('The Number of Pre-processed Data: '+str(num_processed_data))
        print('Yield Rate: '+str(yield_rate))
        if(pairing):
            data = pairing(data)
        if(save):
            save_file = open(save_name,'wb') 
            pickle.dump(data,save_file)
            save_file.close
        return data
    except:
        import traceback
        print('pre-processing is failed')
        traceback.print_exc()
        return None