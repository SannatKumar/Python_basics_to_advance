# how to count and display likes

#likes = []
#likes = ["Mika"]
#likes = ["Andrei", "Sandra"]
#likes = ["Paula", "Petra", "Kunal"]
likes = ["Ziva", "Radha", "Uttam", "Sanjeeta", "Usman"]

String = likes.copy()

def likes():
    if not String:
        print("Noone likes this")
    elif len(String) == 1:
        print(String[0], "likes this")
    elif len(String) == 2:
        print(String[0],"and",String[1], " like this" )
    elif len(String) == 3:
        print(String[0]+", "+String[1] +" and ",String[2], "like this" )
    else:
        count = len(String)
        print(String[0]+", "+String[1] +" and ",count-2, " others like this" )

likes()

