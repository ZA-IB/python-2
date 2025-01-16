#Instructions

#1-For Facebook, Instagram, and Minecraft: Pocket Edition, create lists that contain the name of the app (track_name),
#the rating count (rating_count_tot), and the user rating (user_rating). Remember, the first item in a list is at index 0.

#For Facebook, assign the list to a variable named fb_rating_data.
#For Instagram, assign the list to a variable named insta_rating_data.
#For Minecraft: Pocket Edition, assign the list to a variable named minecraft_rating_data.

#2-Use the data in fb_rating_data, insta_rating_data, 
#and minecraft_rating_data to find the average user rating for these three apps.

#Add the three user ratings (user_rating) together and save the sum as total_rating.
#Divide the total (total_rating) by 3 to get the average rating. Save it as average_rating.

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Fruit Ninja Classic', 1.99, 'USD', 698516, 4.5]
row_5 = ['Minecraft: Pocket Edition', 6.99, 'USD', 522012, 4.5]

fb_rating_data = [row_1[0] , row_1[3] , row_1[4]]
insta_rating_data = [row_2[0] , row_2[3] , row_2[4]]
minecraft_rating_data = [row_5[0] , row_5[3] , row_5[4]]

total_rating = fb_rating_data[2] + insta_rating_data[2] + minecraft_rating_data[2]

average_rating = total_rating / 3
