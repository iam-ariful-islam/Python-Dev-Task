from gensim import corpora, models


def text_summarize(text):
    # Tokenize the text and create a dictionary
    words = text.split()
    dictionary = corpora.Dictionary([words])

    # Create a bag of words representation
    bow = [dictionary.doc2bow(words)]

    # summarization 5% text from full text
    x = int((len(text)*5)/100)

    # Create an LSA model
    lsa = models.LsiModel(bow, id2word=dictionary, num_topics=x)
    topics = lsa.show_topics(num_topics=x, num_words=x, log=False, formatted=False)

    # Use the top words to generate new text
    generated_text = ''
    for topic in topics:
        topic_words = [word for word, _ in topic[1]]
        topic_sentence = " ".join(topic_words)
        generated_text += topic_sentence + ' '
        
    return generated_text