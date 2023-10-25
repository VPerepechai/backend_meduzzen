import json

from rest_framework import status
from rest_framework.test import APITestCase

# from .models import User

class userProfileTestCase(APITestCase):
    
    def test_create_user(self):
        """
        Ensure we can create a new user.
        """
        # create a new user making a post request to djoser endpoint
        data = {
            "username": "Miderg",
            "email": "epdetcdfghcxgai@gmail.com",
            "password": "sdgdfhdhddfh325d",
            "re_password": "sdgdfhdhddfh325d",
        }
        response=self.client.post('/auth/users/',data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
