def word_count(d):
    count={}
    for i in d:
        count[i]=d.count(i)
    return count
print(word_count("scavn"))
