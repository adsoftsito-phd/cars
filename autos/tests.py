from django.test import TestCase

# Create your tests here.

from graphene_django.utils.testing import GraphQLTestCase
from mixer.backend.django import mixer
import graphene
import json

# Create your tests here.
from autos.schema import schema
from autos.models import Auto

AUTOS_QUERY = '''
 {
   autos {
     id
     descripcion
     modelo
     combustible
     transmision
   } 
 }
'''

class AutoTestCase(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema
    def setUp(self):
        self.auto1 = mixer.blend(Auto)
        self.auto2 = mixer.blend(Auto)
        self.auto3 = mixer.blend(Auto)

    def test_autos_query(self):
        response = self.query(
            AUTOS_QUERY,
        )
        content = json.loads(response.content)
        #print(content)
        self.assertResponseNoErrors(response)
        print ("query autos results ")
        print (content)
        assert len(content['data']['autos']) == 3
