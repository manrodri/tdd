from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):

    def test_create_post(self):
        b = Blog('Manuel', 'Test Blog')
        b.create_post('post title', 'blah blah blah')

        self.assertEqual(1, len(b.posts))
        self.assertEqual('post title', b.posts[0].title)
        self.assertEqual('blah blah blah', b.posts[0].content)

        b.create_post('second post', 'foo')
        self.assertEqual(2, len(b.posts))
        self.assertEqual('second post', b.posts[1].title)
        self.assertEqual('foo', b.posts[1].content)

    def test_json(self):
        b = Blog('Manuel', 'Test Blog')
        b.create_post('foo', 'bar')

        expected = {
            'title': "Test Blog",
            "author": "Manuel",
            "posts": [
                {
                    "title": 'foo',
                    "content": "bar"
                }
            ]
        }

        self.assertEqual('Test Blog', b.json()['title'])
        self.assertEqual("Manuel", b.json()['author'])

        self.assertEqual(1, len(b.json()["posts"]))
        self.assertEqual('foo', b.json()['posts'][0].title)
        self.assertEqual('bar', b.json()['posts'][0].content)


        # self.assertDictEqual(expected, b.json())





