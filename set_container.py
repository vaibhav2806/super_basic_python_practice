s = input("ENTER A STRING :")
words = [word for word in s.split(" ")]
print (" ".join(sorted(list(set(words)))))


#set container is used to remove duplicate data from words 