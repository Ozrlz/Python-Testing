from post import Post

class Blog(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.posts = list()

    def __repr__(self):
        return '{} by {} ({} posts)'.format(self.title, self.author, len(self.posts))
    
    def create_post(self, title, content):
        self.posts.append(Post(title, content))

    def json(self):
        return {
            'title': self.title,
            'author': self.author,
            'posts': [post.json() for post in self.posts],
        }
    
    def print_posts(self):
        for post in self.posts:
            post.print_post()