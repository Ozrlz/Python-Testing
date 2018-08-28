from blog import Blog
from post import Post

MENU_PROMPT = """Enter "c" to create a blog, "l" to list blogs, "r" to read one, "p" to create a post, or "q" to quit alv """
blogs = dict() # Blog_name : Blog_object

def menu():
    # Show the available blogs
    # Catch the choice
    # Do something
    # Exit :v

    print_blogs()
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'c':
            ask_create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            ask_read_blog()
        elif selection == 'p':
            ask_create_post()
        selection = input(MENU_PROMPT)


def print_blogs():
    # Print all blogs
    for key, blog in blogs.items():
        print ('- {}'.format(blog) )

def ask_create_blog():
    title = input('Enter the title')
    author = input('Enter the author')
    blogs[title] = Blog(title, author)

def ask_read_blog():
    title = input('Enter the title')
    blog = blogs.get(title)
    # print(blog.json() if blog else 'No blog were found')
    blog.print_posts()

def ask_create_post():
    title = input('Enter the title')
    blog = blogs.get(title)
    if blog:
        title = input('Enter the title')
        content = input('Enter the content')
        blog.create_post(title, content)
    else:
        print('Blog not found')
