#Instructions
#In the code editor we've provided the lists for the first three rows.

#The fourth element in each list describes the number of ratings an app has received. Retrieve the fourth element from each list,
#and then find the average value of the retrieved numbers.

#1-Assign the fourth element from the list row_1 to a variable named ratings_1. Don't forget that the indexing starts at 0.
#2-Assign the fourth element from the list row_2 to a variable named ratings_2.
#3-Assign the fourth element from the list row_3 to a variable named ratings_3.
#4-Add the three numbers retrieved together and save the sum to a variable named total.
#5-Divide the sum (now saved in the variable total) by 3 to get the average number of ratings for the first three rows. Assign the result to a variable named average.

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]

ratings_1 = row_1[3]
ratings_2 = row_2[3]
ratings_3 = row_3[3]

total = ratings_1 + ratings_2 + ratings_3

average = total/3
