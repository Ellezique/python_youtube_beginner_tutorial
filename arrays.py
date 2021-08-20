friends = ["Kevin", "Evan", "Jim", "April", "Marcus"]
lucky_numbers = [4, 8, 15,16, 23, 42]


print (friends)
print (friends[1])
print (friends[-1])
print (friends[1:3])

#modify array
friends[0] ="Atoine"
print(friends)

friends.sort()
print(friends)
friends.reverse()
print(friends)

friends.extend(lucky_numbers)
print(friends)

friends.append("Lucky")
print(friends)

friends.insert(1, "Kelly")
print(friends)

friends.pop()
print(friends)

# Is an element in the list, and if so, at what index
print(friends.index("Evan"))

friends2 = friends.copy()
print(friends2)


friends.clear()
print(friends)