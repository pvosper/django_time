from django.test import TestCase
from timeapp.models import Event


class EventTestCase(TestCase):

    def test_string_representation(self):
        expected = "This is a Title"
        p1 = Event(title=expected)
        actual = str(p1)
        self.assertEqual(expected, actual)
