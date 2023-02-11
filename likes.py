names = ["Alex", "Jacob", "Mark", "Max"]
likes = len(names)

if likes ==0:
    print ("no one likes this")
elif likes == 1:
    print(names[0], "likes this")
elif likes == 2:
    print(names[0], "and", names[1], "likes this")
elif likes ==3:
    print(names[0], ",", names[1], "and", names[2], " likes this")
else:
    print (names[0],"," ,names[1], "and" ,(likes-2) ,"others likes this")


'''
def likes(names):
    likes = len(names)
    
    if likes == 0:
        return "no one likes this"
    elif likes == 1:
        return  names[0] +" likes this"
    elif likes == 2:
        return names[0]+ " and " +names[1]+ " like this"
    elif likes ==3:
        return names[0]+ ", " +names[1]+ " and " +names[2]+ " like this"
    else:
         return names[0]+", " +names[1]+ " and " +str(likes-2)+ " others like this"

'''
    
    