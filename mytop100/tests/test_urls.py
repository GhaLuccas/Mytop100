from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from movies.models import Movie
from movies.serializers import MovieSerializer


class MovieListCreateAPIView(TestCase):
  
    def setUp(self):
        self.url_plural = reverse('plural')
        self.movie1 = Movie.objects.create(title="Movie 1", director="Director 1", description="Description 1" , score=10)
        self.movie2 = Movie.objects.create(title="Movie 2", director="Director 2", description="Description 2" , score=10) 
    
    def test_url_list(self):
        response = self.client.get(self.url_plural )
        print(response.data)
        self.assertEqual(response.status_code, 200)
        
    def test_url_create(self):
      data = {"title": "New Movie", "director": "New Director", "description": "New Description" , "score": 10}
      response = self.client.post(self.url_plural , data)
      print(response.data)
      self.assertEqual(response.status_code , 201)
        
      
      
class MovieRetriveDeleteUpdate(TestCase):
  
  def setUp(self):
    self.movie = Movie.objects.create(title="Test Movie", director="Test Director", description="Test Description", score=10)
    self.url_singular  = reverse("singular" , kwargs={'movie_id':self.movie.id})
    
    
  def test_url_retrive(self):
      response = self.client.get(self.url_singular)
      print(response.data)
      self.assertEqual(response.status_code, 200)
      self.assertEqual(response.data['title'], "Test Movie")

      
    
    
