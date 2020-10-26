import pytest
import requests
import unittest
import os

baseUrl = "https://binaryjazz.us/wp-json/genrenator/" #Seperating base url from the rest as servers may change. Alternatively, we can as well capture this from run time terminal using sys
version = {"default": "v1"} #Passing the version of the api as param as we may maintain different versions, in order to test all versions without modifying much in the existing tests. Any new version in test we simply have to append
endpoint =  {"genre": "/genre", "story": "/story"} #the number of end points may increase based on different types of stories, so keeping this as a hash, so any new will not modify existing
outputPath = os.getcwd()
def api(url):
    api.response = requests.get(url)
    print (api.response.headers["Date"])

class Tests(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print ("Setting up data")

    def test_should_not_throw_error_when_length_is_not_provided(self): #Checking if the story length has not been provided, whether server throws 500
        api(baseUrl + version["default"] + endpoint["story"])
        self.assertNotEqual(api.response.status_code,500)


    def test_length_must_be_none(self): #Testing if 0 length is passed it  does not capture it from 1
        api(baseUrl + version["default"] + endpoint["story"] + "/0")
        self.assertNotEqual(api.response.status_code,500)
        self.assertEqual(api.response.status_code,200)
        self.assertEqual(len(api.response.json()),0)

    def test_must_be_returned_when_passed_length(self): #Testing if valid length is passed, server returns the same number of stories
        api(baseUrl + version["default"] + endpoint["story"] + "/3")
        self.assertNotEqual(api.response.status_code,500)
        self.assertEqual(api.response.status_code,200)
        self.assertNotEqual(len(api.response.json()),0)
        self.assertEqual(len(api.response.json()),3)
        
    def test_should_throw_notfound_incorrecturl(self): #Testing is server throwing 500 on incorrect url. Alternatively we could check if redirect is implemented with is_redirect
        api(baseUrl + "v2" + endpoint["story"] + "/3")
        self.assertEqual(api.response.status_code,404)
        self.assertNotEqual(api.response.status_code,500)
        self.assertEqual(api.response.json()['message'],"No route was found matching the URL and request method")

    def test_should_throw_notfound_additional_query_appended(self): #Testing server throwing 500 if appending another query to a valid query
        api(baseUrl + version["default"] + endpoint["story"] + "/3" + "/3")
        self.assertEqual(api.response.status_code,404)
        self.assertNotEqual(api.response.status_code,500)
        self.assertEqual(api.response.json()['message'],"No route was found matching the URL and request method")

    def test_date_mustbe_returned_in_GMT_in_headers(self): #Asserted if the time default is returned in GMT unless query passed
        api(baseUrl + version["default"] + endpoint["story"] + "/3")
        self.assertTrue(api.response.headers["Date"])
        self.assertTrue("GMT" in api.response.headers["Date"])
    
    def test_cookies_must_be_returned(self): #Asserting if cookies is greater than 0
        api(baseUrl + version["default"] + endpoint["story"] + "/3")
        self.assertNotEqual(len(api.response.headers["Set-cookie"]),0)
        self.assertGreater(len(api.response.headers["Set-cookie"]),0)


    @classmethod
    def tearDownClass(self): #Any revert to the environment or preparing the report
        print("Reverting back ") 
