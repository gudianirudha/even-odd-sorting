sent='Anirudh'
find=input("Enter what you want to search")
pos=sent.find(find)
if pos > 0:
    print("found",pos)
else:
    print("Not found",pos)
