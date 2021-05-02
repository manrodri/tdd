from unittest import TestCase
from unittest.mock import patch

import app
from blog import Blog


class AppTest(TestCase):
    def setUp(self) -> None:
        b = Blog('Test', 'Test Blog')
        app.blogs = {'Test': b}

    def test_print_blogs(self):
        # patch takes a module.function as parameter
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('- Test by Test Blog (0 posts)')

    def test_menu_calls_print_function(self):
        with patch('app.print_blogs') as mocked_print_blogs:
            with patch('builtins.input', return_value='q'):
                app.menu()
                mocked_print_blogs.assert_called()

    def test_menu_calls_ask_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('c', 'q')
            with patch('app.ask_create_blog') as mocked_ask_create_blog:
                app.menu()
                mocked_ask_create_blog.assert_called()

    def test_menu_ask_print_blogs_option(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('l', 'q')
            with patch('app.print_blogs') as mocked_print_blogs:
                app.menu()
                mocked_print_blogs.assert_called()

    def test_menu_prints_prompt(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.return_value = "q"
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)

    def test_menu_ask_read_blog_called(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('r', 'q')
            with patch('app.ask_read_blog') as mocked_read_blog:
                app.menu()
                mocked_read_blog.assert_called()

    def test_menu_ask_craete_post_called(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('p', 'q')
            with patch('app.ask_create_post') as mocked_create_post:
                app.menu()
                mocked_create_post.assert_called()

    def test_ask_create_blog_asks_user_for_blog_title(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', "Test Author")
            app.ask_create_blog()
            self.assertIsNotNone(app.blogs.get('Test'))

    def test_ask_read_blog(self):
        # blog with no posts
        with patch('builtins.input', return_value='Test'):
            with patch('builtins.print') as mokced_print:
                app.ask_read_blog()
                mokced_print.assert_not_called()

        # blog with posts
        app.blogs['Test'].create_post('Test post', 'Test Content')
        with patch('builtins.input', return_value='Test'):
            with patch('builtins.print') as mokced_print:
                app.ask_read_blog()
                mokced_print. \
                    assert_called_once_with(app.POST_TEMPLATE.format(
                    app.blogs['Test'].posts[0].title, app.blogs['Test'].posts[0].content))

    def test_ask_create_blog(self):


        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', "Test Title", "Test Content")
            app.ask_create_post()

            self.assertEqual('Test Title', app.blogs['Test'].posts[0].title)
            self.assertTrue('Test Content' == app.blogs['Test'].posts[0].content)
