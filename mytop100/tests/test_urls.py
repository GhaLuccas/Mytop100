from django.test import SimpleTestCase
from django.urls import reverse , resolve
from api.views import MovieRetriveDeleteUpdate, MovieListCreateAPIView

class TestUrls(SimpleTestCase):
  
  def test_list_url(self):
    url = reverse('plural')
    self.assertEqual(resolve(url).func ,MovieListCreateAPIView)