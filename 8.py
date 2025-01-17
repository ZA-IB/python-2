#Instructions
#1-In the code editor, we've already stored the five rows as lists in separate variables. Group the five lists together in a list of lists. Assign the resulting list of lists to a variable named app_data_set.
#2-Calculate the average rating of the apps by retrieving the right data points from the app_data_set list of lists.
#-The rating is the last element of each row. You'll need to add up the ratings and then divide by the number of rows.
#-Assign the result to a variable named avg_rating.


row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Fruit Ninja Classic', 1.99, 'USD', 698516, 4.5]
row_5 = ['Minecraft: Pocket Edition', 6.99, 'USD', 522012, 4.5]

app_data_set = [row_1, row_2, row_3, row_4, row_5]

avg_rating = app_data_set[0][-1] + app_data_set[1][-1] + app_data_set[2][-1] + app_data_set[3][-1] + app_data_set[4][-1]
avg_rating = avg_rating/5
print(avg_rating)
