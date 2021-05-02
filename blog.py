from post import Post


class Blog:
    def __init__(self, title, author):
        self.author = author
        self.title = title
        self.posts = []

    def __repr__(self):
        return f"{self.title} by {self.author} " \
               f"({str(len(self.posts))} post{'s' if len(self.posts )!=1 else ''})"

    def create_post(self, title, content):
        self.posts.append(Post(title, content))

    def json(self):
        return {
            'title': self.title,
            'author': self.author,
            'posts': [post for post in self.posts]
        }
