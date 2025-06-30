text = input()
length = int(input())

if ("gold" in text) and len(text) >= length:
    print("A goldfish!")
elif ("gold" in text) or len(text) >= length:
    print("Only one thing!")
else:
    print("Either it's not a fish, or it's not a golden one.")