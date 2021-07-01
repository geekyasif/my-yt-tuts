import wikipedia

query = "Python (programming language)"
data = wikipedia.summary(query)
print(data)