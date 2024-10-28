from django.test import TestCase 
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from movies.models import Movie
from movies.serializers import MovieSerializer


class MovieListCreateAPITest (APITestCase):
  
    def setUp(self):
        self.url_plural = reverse('plural')
        self.movie1 = Movie.objects.create(title="Movie 1", director="Director 1", description="Description 1" , score=10)
        self.movie2 = Movie.objects.create(title="Movie 2", director="Director 2", description="Description 2" , score=10) 
    
    def test_url_list(self):
        response = self.client.get(self.url_plural )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_url_create(self):
      data = {"title": "Teste New Movie", "director": "New Director", "description": "New Description" , "score": 10}
      response = self.client.post(self.url_plural , data ,format='json')
      self.assertEqual(response.status_code , status.HTTP_201_CREATED)
      self.assertEqual(Movie.objects.count(), 3) 
      self.assertEqual(Movie.objects.last().title, "Teste New Movie")
      
    # Invalidate data tests
    
    def test_invalid_create_url(self):
      data = {"director": "New Director", "description": "New Description" , "score": 10}
      response = self.client.post(self.url_plural , data , format='json')
      self.assertEqual(response.status_code , status.HTTP_404_BAD_REQUEST)
        
      
      
class MovieRetrieveDeleteUpdateTest(APITestCase):
  
  def setUp(self):
    self.movie = Movie.objects.create(title="Test Movie", director="Test Director", description="Test Description", score=10)
    self.url_singular  = reverse("singular" , kwargs={'movie_id':self.movie.id})
    self.invalid_id = reverse('singular', kwargs={"movie_d":999})
    self.invalid_data = { "director": "Update Director", "description": "Update Description" , "score": 10}
    
    
  def test_url_retrive(self):
      response = self.client.get(self.url_singular)
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertEqual(response.data['title'], "Test Movie")
      
  def test_url_put(self):
      data = {"title": "Update Movie", "director": "Update Director", "description": "Update Description" , "score": 10}
      response = self.client.put(self.url_singular,data , format='json')
      self.assertEqual(response.status_code , status.HTTP_200_OK)
      self.movie.refresh_from_db()
      self.assertEqual(self.movie.title, "Update Movie")

      
  def test_url_delete(self):
    response = self.client.delete(self.url_singular)
    self.assertEqual(response.status_code , status.HTTP_204_NO_CONTENT)
    movie_exists = Movie.objects.filter(id=self.movie.id).exists()
    self.assertFalse(movie_exists)
    
  # Invalid data tests
  
  def test_invalid_put_url(self):
    response = self.client.put(self.invalid_id,self.invalid_data , format='json')
    self.assertEqual(response.status_code , status.HTTP_404_NOT_FOUND)
    
  
  
  def test_invalid_retrive_url(self):
    response = self.client.get(self.invalid_id)
    self.assertEqual(response.status_code , status.HTTP_404_NOT_FOUND)
    
    
  def test_invalid_delete_url(self):
    response = self.client.delete(self.invalid_id)
    self.assertEqual(response.status_code , status.HTTP_404_NOT_FOUND)    
  
      
  

    

      



    
