from balinese_textpreprocessor import TextPreprocessor

# file for testing TextPreprocessor class
obj = TextPreprocessor()
text = "I Lutung ajake I Kakua ngalih amah-amahan diumah Gubernur N.I.C.A. Ditu lantas ia ajaka dadua mulung nyuh. Pekak-pekak ane nepukin ento lantas ngebug I Lutung ajak I Kakua 35 kali. Adepe buin Rp. 35.0900"
sentence = "I Lutung ajake I Kakua ngalih amah-amahan diumah Gubernur N.I.C.A."

# 1. Test word tokenization function
print('Test function 1: balinese_word_tokenization')
print(obj.balinese_word_tokenize(sentence))

# 1. Test word tokenization function
print('Test function 1: balinese_sentences_segmentation')
print(obj.balinese_sentences_segmentation(text))
