last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

gradebook = [["physics",98], ["calculus",97],["poetry",85], ["history",88]]
gradebook.append(["computer science",100])
gradebook.append(["visual arts",93])
gradebook[5][1] += 5 #adding score of 5 to visual arts

#removing score from poetry class
gradebook[2].remove(85)
gradebook[2].append("Pass")
print(gradebook,'\n')

full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)
