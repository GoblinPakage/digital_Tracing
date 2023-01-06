from reqData.decoration import exectionTime_decoration

@exectionTime_decoration
def Count_Word_UsingDict(text):
    counts = dict()
    words = text.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

@exectionTime_decoration
def Count_Word_UsingCounterfunc(text):
    words = text.split()
    counts = []
    for word in words:
        counts.append(words.count(word))
    return counts
