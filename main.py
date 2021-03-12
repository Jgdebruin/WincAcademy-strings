# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

'''UEFA Euro 1988 Final - Soccermatch Report
By: Jamie de Bruin'''

# Players who scored
player_1 = 'Ruud Gullit'
player_2 = 'Marco van Basten'

# In which minute the goals were made
goal_1 = 32
goal_2 = 54

# Who scored when
scorers = player_1 + ' = ' + str(goal_1) + ', ' + player_2 + ' = ' + str(goal_2)
# print(scorers)

# Same as the above, but now formated in a f-string
report = f'{player_1} scored in the {goal_1}nd minute\n{player_2} scored in the {goal_2}th minute'
# print(report)

player = player_1

# Slicing the string and keeping the first name
first_name = player[0:4]
# print(first_name)

# Lettercount last name
last_name_len = len(player[5:])
# print(last_name_len)

# Shorting the name
name_short = f'{player[0:1]}. {player[5:]}'
# print(name_short)

# Make crowd chant
chant = (f'{player[0:4]}! ' * len(player[0:4])).rstrip()
# print(chant)

# Check if chant != ends with a spacecharacter
if chant.endswith(' ') != True:
    good_chant = True
else:
    good_chant = False
print(good_chant)

# vraag: inequality operator toepassen werkt niet