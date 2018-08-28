POST_TEMPLATE = '''
--- {} ---

{}

'''

class Post(object):

    def __init__(self, title, content):
        self.title = title
        self.content = content
    def json(self):
        return {
            'title': self.title,
            'content': self.content,
        }

    def print_post(self):
        print(POST_TEMPLATE.format(self.title, self.content))