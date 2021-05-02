from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test Blog', 'Manuel')

        self.assertEqual('Manuel', b.author)
        self.assertEqual('Test Blog', b.title)
        self.assertListEqual([], b.posts)

    def test_multiple_repr(self):
        b = Blog('Test Blog', 'Manuel')
        b.posts = ['test']

        self.assertEqual("Test Blog by Manuel (1 post)", b.__repr__())

        b2 = Blog("my blog", 'Jordi')
        b2.posts = ['foo', 'bar']
        self.assertEqual("my blog by Jordi (2 posts)", b2.__repr__())
