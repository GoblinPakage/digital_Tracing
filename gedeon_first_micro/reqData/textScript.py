from reqData.decoration import exectionTime_decoration
import collections

@exectionTime_decoration
def Count_Word_UsingDict(text):
    count = {}
    list_of_words = text.split()
    for word in list_of_words:
        count[word] = count.get(word, 0) + 1
    return 'ok'

@exectionTime_decoration
def Count_Word_UsingCounterfunc(text):
    return collections.Counter(text)
