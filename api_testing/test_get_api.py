import unittest
import requests

class ApiTests(unittest.TestCase):
    BASE_URL = "http://127.0.0.1:5000/"

    
    expected_result={   
    "address": "BTM-bnglr",
    "city": "Banglore",
    "id": 1,
    "name": "Ram",
    "salary": "75000"
  }

    # Positive test case to get all employees 
    def test_valid_get_request(self):
        response = requests.get(f"{self.BASE_URL}/list_employees")

        self.assertEqual(response.status_code, 200)
        # Add more assertions based on your API response if needed
        print("Positive Test 1 completed - GET Request")
        print("The response code is 200 OK")
        print("--------------------------------------")

    # Positive test case to get specific employee
    def test_get_specific_employees(self):
        response= requests.get(f"{self.BASE_URL}/employee/1")
        self.assertEqual(response.status_code,200)
        
        for i in response.json():
            dict=i
        self.assertDictEqual(dict,self.expected_result)
        
        print("Positive Test 2 completed - GET Request")
        print("The response code is 200 OK")
        print("The result and expected result matches")
        print("--------------------------------------")

    

    # Positive test case to ensure the response is in JSON format
    def test_get_data_json_format(self):
        response = requests.get(self.BASE_URL+'/employee/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Content-Type'], 'application/json')

        print("Positive Test 3 completed - GET Request")
        print("The response code is 200 OK")
        print("The response is of correct content type")
        print("--------------------------------------")



    # Positive test case to ensure the API handles a large number of requests
    def test_get_data_multiple_requests(self):
        for _ in range(15):
            response = requests.get(self.BASE_URL+"/list_employees")
            self.assertEqual(response.status_code, 200)
        print("Positive Test 4 completed - GET Request")
        print("Handles multiple requests")
        print("The response code is 200 OK")   
        print("--------------------------------------")






    # Negative test case for non-existent data
    def test_get_nonexistent_data(self):
        response = requests.get(self.BASE_URL+'/employee/99999')
        self.assertEqual(response.status_code, 404)
        print("Negative Test 1 completed - GET Request")
        print("The response code is 401.")
        print("Data doesnt Exist")
        print("--------------------------------------")   

    # Negative test case for invalid request methods
    def test_invalid_method(self):
        response = requests.put(self.BASE_URL+"/update_employee/7")
        self.assertEqual(response.status_code, 415)
        print("Negative Test 2 completed - GET Request")
        print("The response code is 415")
        print("The requested method is invalid")
        print("--------------------------------------") 

    # Negative test case for proper handling of malformed URL
    def test_malformed_url(self):
        response = requests.get(self.BASE_URL+'/')
        self.assertEqual(response.status_code, 404)
        print("Negative Test 3 completed - GET Request")
        print("The response code is 404 Not Found.")
        print("The provided URL is not correct")
        print("--------------------------------------") 


if __name__ == '__main__':
    tester=ApiTests()
    tester.test_valid_get_request()
    tester.test_get_specific_employees()
    tester.test_get_data_json_format()
    tester.test_get_data_multiple_requests()


    tester.test_get_nonexistent_data()
    tester.test_invalid_method()
    tester.test_malformed_url()