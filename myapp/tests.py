from django.test import TestCase
from myapp.models import Event, Guest
# Create your tests here.
class ModelTest(TestCase):
    def setUp(self):
        Event.objects.create(id=1,
                             name='小米12发布会',
                             status=True,
                             limit=500,
                             address='环球中心',
                             start_time='2021-12-08 19:00:00')
        Guest.objects.create(id=1,
                             event_id=1,
                             realname='andy',
                             phone='1802212121',
                             email='andy@mail.com',
                             sign=True)

    def test_event_modles(self):
        result = Event.objects.get(name="小米12发布会")
        self.assertEqual(result.address, "环球中心")
        self.assertTrue(result.status)

    def test_guest_models(self):
        result = Guest.objects.get(phone='1802212121')
        self.assertEqual(result.realname, "andy")
        self.assertTrue(result.sign)


