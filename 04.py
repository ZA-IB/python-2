#Instructions
#The last element in each list shows the average user rating of each application.

#Retrieve the user ratings (user_rating) for the first three rows, and then find the average value of all the ratings retrieved.

#1-Assign the last element from the list row_1 to a variable named rating_1. Try to use negative indexing.
#2-Assign the last element from the list row_2 to a variable named rating_2.
#3-Assign the last element from the list row_3 to a variable named rating_3.
#4-Add the three ratings together, and save the sum to a variable named total_rating.
#5-Divide the total by 3 to get the average rating. Assign the result to a variable named average_rating.

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]

rating_1 = row_1[4]
rating_2 = row_2[4]
rating_3 = row_3[4]

total_rating = rating_1 + rating_2 + rating_3

average_rating = total_rating / 3
