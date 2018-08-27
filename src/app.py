blogs = dict() # Blog_name : Blog_object

def menu():
    # Show the available blogs
    # Catch the choice
    # Do something
    # Exit :v

    print_blogs()

def print_blogs():
    # Print all blogs
    for key, blog in blogs.items():
        print ('- {}'.format(blog) )