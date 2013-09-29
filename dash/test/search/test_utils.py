from django.test import TestCase

from music.models import MusicProfile
from users.models import User

class SearchTestCase(TestCase):

    def setUp(self):

        u = User.objects.create(username='joe')
        MusicProfile.objects.create(user=u, zipcode='80516')

    def test_find_one(self):

        user = do_find('80516')

        self.assertEquals(user.count(), 1)
        self.assertEquals(user[0].username, 'joe')

    def test_find_two(self):

        u = User.objects.create(username='jane')
        MusicProfile.objects.create(user=u, zipcode='80516')

        users = do_find('80516')

        self.assertEquals(users.count(), 2)
        self.assertContainss(users, 'joe')

        u = User.objects.create(username='bob')
        MusicProfile.objects.create(user=u, zipcode='51104')

        users = do_find('80516')

        self.assertEquals(users.count(), 2)
        self.assertNotContainss(users, 'joe')
