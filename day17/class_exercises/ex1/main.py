# main.py
""" I added some extra features to the class out of curiosity."""


class User():
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.name = str()
        self.follower_count = 0
        self.following = 0
        self.followers = []

    def follow(self, user):
        user.follower_count += 1
        user.followers.append(self)
        self.following += 1

    def print_followers(self):
        if not self.followers == []:
            print(f"{self.username} is being followed by:")
            for follower in self.followers:
                print(f"{follower.username}")
        else:
            print("You don't have any followers")
        return


user_1 = User("001", "ebdsaleh")
user_2 = User("002", "jack")
user_1.follow(user_2)
print(f"{user_1.username} has {user_1.follower_count} followers.")
print(f"{user_1.username} is following {user_1.following} user(s).")
print(f"{user_2.username} has {user_2.follower_count} followers.")
print(f"{user_2.username} is following {user_2.following} user(s).")
user_2.print_followers()
