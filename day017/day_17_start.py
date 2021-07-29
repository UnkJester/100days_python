class User:
    def __init__(self, user_id=None, username=None):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

# user1 = User()
# user1.id = '001'
# user1.username = 'angela'

user1 = User('002', 'Jack')
print(user1.username)