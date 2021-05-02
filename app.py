from blog import Blog
from post import Post

MENU_PROMPT = \
    'Enter "c" to create a blog, "l" to list blogs, "r" to read one, "p"  to create a post, or "q" to quit'

POST_TEMPLATE = ''''
--- {} ---

{}

'''

blogs = dict()  # blog_name: Blog object


def menu():
    # show the user the available blogs
    # let the user select an option
    # do something with the choice
    # exit

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
    print("Thank you for using the app. Bye.")


def print_blogs():
    for k, blog in blogs.items():
        print(f"- {blog}")


def ask_create_blog():
    title = input("Please enter blog title: ")
    user_name = input("Please enter your name: ")
    blogs[title] = Blog(title, user_name)


def ask_read_blog():
    blog_title = input('Please enter the title of the blog you\' like to read')
    print_posts(blogs[blog_title])


def print_posts(blog):
    for post in blog.posts:
        print_post(post)


def print_post(post):
    print(POST_TEMPLATE.format(post.title, post.content))


def ask_create_post():
    blog_title = input("Enter the blog title you want to write a post in: ")
    title = input('Enter your post title: ')
    content = input('Enter your post content: ')

    # deal with exceptions necessary
    blogs[blog_title].create_post(title, content)
