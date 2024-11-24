# rocketchat-bulkuser-create
This python script let you create bulk user using rocketchat Rest API.


Step 1)  You have to get your User ID and Auth Token from your rocketchat instance. to do that, you need to get admin privilege acces in rocketchat. 
after that, you go to Progile >> Personal Access Tokens >> Add 

the output should be like this image below:

![Screenshot 2024-11-24 164116](https://github.com/user-attachments/assets/e028aafa-b1c7-486c-811e-ee7fb3081c47)

IMPORTANT! > DO NOT SAVE THIS INFO ON ROCKETCHAT SAVE MESSAGE OR ANY OTHER UNTRUSTED PLACES! ATTACKERS WITH THIS INFO CAN EASILY ACCESS YOUR ROCKETCHAT INFORMATION. 


Step 2) Replace your rocketchat URL and Token and User ID in the placeholders in python script. the naming is obvious. if you are here, you know where you should put it.

Step 3) Place the username of the users in username.txt file and their Full name in names.txt file. 

IMPORTANT!!!!! >> The order of the usernames and names should be equal. for example if in the first line of username.txt is m.afshar, the first line of names.txt should be mohammad afshar. if it does not match, user WILL create but with wrong name :)
so if you want to evoid renaming more than hundred users, pay attention!
ALSO the number of usernames and names should be equal as well. 

Step 3) Run the script using this command >> 

python3 bulkuser-rocketchat.py
