#lets open the demo file

followingList = [line.rstrip('\n') for line in open("accountsifollow.txt")]
print(followingList)

#Now demo1 list
followersList = [line.rstrip('\n') for line in open("accountsfme.txt")]
print(followersList)
print("UNFOLLOWERS")
for unfollowers in followingList:
    if not unfollowers in followersList:
        print(unfollowers)
