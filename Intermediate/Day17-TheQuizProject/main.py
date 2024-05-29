class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user1 = User("001", "Ye")
user2 = User("002", "Min")

user1.follow(user2)
print(f"User1 follower: {user1.followers}")
print(f"User1 following: {user1.following}")
print(f"User2 follower: {user2.followers}")
print(f"User2 following: {user2.following}")
