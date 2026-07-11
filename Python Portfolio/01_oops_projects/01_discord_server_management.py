'''
You are creating your own Discord Server Manager.

Your program should store:

- Server Name
- Number of Members
- Number of Channels

The program should be able to:

• Add a new member.
• Remove a member.
• Create a new channel.
• Delete an existing channel.
• Display complete server information.

Rules:

- Members should never become negative.
- Channels should never become negative.
- Don't allow deleting the last remaining channel.

Challenge:

Think of at least 3 more useful features that a real Discord server should have and implement them

'''

class Discord_Server_Manager:

    members = []
    channels = []
    ban_list = []

    def __init__(self,server_name,number_of_members,number_of_channels,members_name,channel_names,banned_users):

        self.server_name =server_name
        self.number_of_members = number_of_members
        self.number_of_channels = number_of_channels
        self.member_name = members_name
        self.channel_name = channel_names
        self.banned_users = banned_users
        Discord_Server_Manager.members.extend(members_name)
        Discord_Server_Manager.channels.extend(channel_names)
        Discord_Server_Manager.ban_list.extend(banned_users)
    def add_member(self,user_name):

        print(f"{user_name} has been successfully Added to the server".title())
        self.number_of_members += 1
        self.member_name.append(user_name)
        Discord_Server_Manager.members.append(user_name)



    def remove_member(self,user_name):
        if self.number_of_members <= 1 :
            print(f"{user_name} can't be removed from the server... because last member can't leave the server".title())
        elif user_name not in self.member_name :
            print(f"{user_name} doesn't exist")
        else :
            print(f"{user_name} has been removed from the server".title())
            self.number_of_members -= 1
            self.member_name.remove(user_name)
            Discord_Server_Manager.members.remove(user_name)

    def create_channel(self,channel_name):
        print(f"{channel_name} has been created successfully".title())
        self.number_of_channels += 1
        self.channel_name.append(channel_name)
        Discord_Server_Manager.channels.append(channel_name)

    def delete_channel(self,channel_name):
        if self.number_of_channels <= 1 :
            print(f"{channel_name} can't be deleted as server should have at least 1 channel".title())

        elif channel_name not in self.channel_name :
            print(f"Channel {channel_name} doesn't exist")

        else :
            print(f"{channel_name} has been deleted ")
            self.number_of_channels -= 1
            self.channel_name.remove(channel_name)
            Discord_Server_Manager.channels.remove(channel_name)
    def give_role(self,role_name,user_name):
        roles = ["ADMIN","STAFF","CLOSE_FRIEND","MAIN_MEMBERS"]

        if role_name in roles and user_name in self.member_name:
            print(f"{user_name} has been appointed as {role_name}")
        else :
            print("Either user doesn't exist or the role")

    def ban(self,user_name):
        print(f"You have successfully banned {user_name}")
        self.banned_users.append(user_name)
        Discord_Server_Manager.ban_list.append(user_name)

    def unban(self,user_name):
        if user_name in self.banned_users:
            print(f"You have successfully Unbanned {user_name}")
            self.banned_users.remove(user_name)
            Discord_Server_Manager.ban_list.remove(user_name)
        else:
            print("User Doesn't exist")


    def display(self):
        print(f"Name of the server is {self.server_name}".title())
        print(f"Number of members in the server is {self.number_of_members}".title())
        print(f"Number of the channel this server has is {self.number_of_channels}".title())
        print(f"Name of the members in the server are {self.member_name}")
        print(f"Banned Players = {self.banned_users}")




manager = Discord_Server_Manager("Dhruv",5,3,["Harsh", "Shankar","Arya","Aditee","krishna"],["chill chat","annoucment","media"],["Aditee"])
manager.add_member("kai")
manager.give_role("ADMIN","Harsh")
manager.give_role("STAFF","Arya")
manager.display()
manager.ban("Shankar")
manager.display()
manager.unban("Shankar")
manager.remove_member("kai")
manager.create_channel("Complaint Area")
manager.display()
manager.delete_channel("Chill chat")
manager.display()