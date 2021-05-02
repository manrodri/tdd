class Post(object):
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def json(self):
        return {
            "title": self.title,
            "content": self.content,
        }

    def __repr__(self):
        return f"post title: {self.title}. post content: {self.content}"
