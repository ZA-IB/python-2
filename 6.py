#Instructions
#1-Select the last three elements from row_1 using a list slicing syntax shortcut. Assign the output to a variable named last_3_fb.
#2-From row_5, select the list slice ['USD', 522012] using a list slicing syntax shortcut. Assign the output to a variable named minecraft_3_4.
#3-Print last_3_fb and minecraft_3_4 to see the results.


row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Fruit Ninja Classic', 1.99, 'USD', 698516, 4.5]
row_5 = ['Minecraft: Pocket Edition', 6.99, 'USD', 522012, 4.5]

last_3_fb = row_1[-3:]
minecraft_3_4 = row_5[2:4]
print(last_3_fb)
print(minecraft_3_4)
