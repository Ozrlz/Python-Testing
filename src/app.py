MENU_PROMPT = """Enter "c" to create a blog, "l" to list blogs, "r" to read one, "p" to create a post, or "q" to quit alv """
blogs = dict() # Blog_name : Blog_object

def menu():
    # Show the available blogs
    # Catch the choice
    # Do something
    # Exit :v

    print_blogs()
    selection = input(MENU_PROMPT)

def print_blogs():
    # Print all blogs
    for key, blog in blogs.items():
        print ('- {}'.format(blog) )