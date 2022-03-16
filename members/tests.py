from django.test import TestCase
from .models import *


class ProfileTestCase(TestCase):
    def setUp(self):
        Profile.objects.create(user="josh", profile_pic="media/default2_GJAt4l6.png", caption="Josh a test")
        Profile.objects.create(user="bob", profile_pic="media/default2_GJAt4l6.png", caption="Bob a test")

    def test_animals_can_speak(self):
        pro1 = Profile.objects.get(user="josh")
        pro2 = Profile.objects.get(name="bob")
        self.assertEqual(pro1.caption, 'Josh a test')
        self.assertEqual(pro2.caption, 'Bob a test')



