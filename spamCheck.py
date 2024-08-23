import re

def spamComment(comment):
    keywords = ["free", "buy now", "click here", "subscribe", "earn money", "lottery", "win big"]

    for keyword in keywords:
        if keyword.lower() in comment.lower():
            return True


    if re.search(r'([!?.]){5,}', comment):
        return True

    if comment.count('http') > 1:
        return True
    
    words = comment.split()
    count = {word: words.count(word) for word in words}
    if any(count > 5 for count in count.values()):
        return True

    return False

comment = input("Enter a comment to check for spam: ")

if spamComment(comment):
    print("The comment is likely spam.")
else:
    print("The comment is not spam.")
