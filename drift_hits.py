
Tuesday, Thursday = {}, {}
times = ["7:00", "7:30", "8:00", "8:30", "9:00", "9:30", "10:00", "10:30", 
         "11:00", "11:30", "12:00", "12:30", "1:00", "1:30", "2:00", "2:30"]

player_list = ["Chun", "Ross", "Brian", "Sam", "George", "Oliver", "Tim", 
                "Alex", "Koong", "Noah", "Zander", "Nico", "James"]

#initially populate dictionaries where all players are available
for time in times:
    Tuesday[time] = player_list.copy()
    Thursday[time] = player_list.copy()

#function to populate a player's availability in players dict
    #removes availabilities given times (list)
    #player = player name (str)
    #day = which dict (insert dict)
    #times = list of unavailabilities (list of strings in 30 minute blocks where player is unavailable)
def populate(player, day, unavailabilities):
    for unavailable in unavailabilities:
        slot = day[unavailable]
        slot.remove(player)

#INSERT UNAVAILABILITIES ACCORDING TO PLAYER CLASSES IN 30-MINUTE BLOCKS
populate("Chun", Tuesday, ["1:00", "1:30", "2:00", "2:30"])
populate("Chun", Thursday, ["1:00", "1:30", "2:00", "2:30"])
populate("Ross", Tuesday, ["9:00", "9:30", "10:00"])
populate("Ross", Thursday, ["9:00", "9:30", "10:00"])
populate("Brian", Tuesday, ["1:00", "1:30", "2:00"])
populate("Brian", Thursday, ["1:00", "1:30", "2:00"])
populate("Sam", Tuesday, ["7:00"])
populate("Sam", Thursday, ["7:00"])
populate("George", Tuesday, ["1:00", "1:30", "2:00", "2:30"])
populate("George", Thursday, ["1:00", "1:30", "2:00", "2:30"])
populate("Oliver", Tuesday, ["7:00"])
populate("Oliver", Thursday, ["7:00"])
populate("Tim", Tuesday, ["1:00", "1:30", "2:00"])
populate("Tim", Thursday, ["2:30"])
populate("Alex", Tuesday, ["2:30"])
populate("Alex", Thursday, ["2:30"])
populate("Koong", Tuesday, ["2:30"])
populate("Koong", Thursday, ["2:30"])
populate("Noah", Tuesday, ["9:00", "9:30", "10:00", "10:30", "11:00", "11:30"])
populate("Noah", Thursday, ["9:00", "9:30", "10:00", "10:30", "11:00", "11:30"])
populate("Zander", Tuesday, ["1:00", "1:30", "2:00", "2:30"])
populate("Zander", Thursday, ["1:00", "1:30", "2:00", "2:30"])
populate("Nico", Tuesday, ["2:30"])
populate("Nico", Thursday, ["2:30"])
populate("James", Tuesday, [])
populate("James", Thursday, [])

print("TUESDAY AVAILABILITIES")
for i in times:
    print(i, ": ", Tuesday[i])

print("THURSDAY AVAILABILITIES")
for i in times:
    print(i, ": ", Thursday[i])