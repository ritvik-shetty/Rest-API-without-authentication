import unittest
import requests

class ApiTests(unittest.TestCase):
    URL="http://127.0.0.1:5000/update_employee"
    VALID_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwNjUwOTU3OSwianRpIjoiZDM1NDcyYjEtMTdiNy00Nzc5LWEyMjAtY2E4ODY1ODZhYmNhIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Ik1pY2hhZWwiLCJuYmYiOjE3MDY1MDk1NzksImNzcmYiOiI0MjgyOTNmZi00MGE2LTQ5ZDYtYTNlOC1hMDg5ODljNmU0ZjUiLCJleHAiOjE3MDY1MTA0Nzl9.gpATfBKBYRjreH8wwOOMQcXOgteUrg9n1T-4O9XBKnE"
    INVALID_TOKEN = "invalid_token"

    data={        
        }

    data1={
       "address": "BTM_LAYOUT",
        "city": "Bangalore",
        "name": "rohit",
        "salary": "49000"
    }

    data2={
        "address": "Jmatar",
        "city": "Jaipur",
        "name": "Pranam",

    }

    data3={        
        "name": "Raj",
        "salary": "49000"}

    # Positive test case 1: Ensure successful PUT    
    def test_successful_put(self):
        headers = {
            "Authorization": f"Bearer {self.VALID_TOKEN}"
        }
        response = requests.put(self.URL+"/6", json=self.data1,headers=headers)
        self.assertEqual(response.status_code, 200)
        print("Positive Test 1 completed - PUT Request")
        print("The response code is 200 OK")
        print("--------------------------------------")


    # Negative test case 1: For Put with wrong token
    def test_put_invalid_token(self):
        headers = {
            "Authorization": f"Bearer {self.INVALID_TOKEN}"
        }
        response = requests.put(self.URL+"/9", json=self.data1,headers=headers)
        self.assertEqual(response.status_code, 422)
        print("Positive Test 1 completed - PUT Request")
        print("The response code is 422")
        print("--------------------------------------")


    # Negative test case 2: For non existing data
    def test_put_nonexisting_id(self):
        headers = {
            "Authorization": f"Bearer {self.VALID_TOKEN}"
        }
        response = requests.put(self.URL+"/9999999", json=self.data1)
        self.assertEqual(response.status_code, 401)
        print("Negative Test 2 completed - PUT Request")
        print("Put for non existing data")
        print("The response code is 401")
        print("--------------------------------------")


    # Negative test case 3: For missing parameters
    def test_missing_param(self):
        headers = {
            "Authorization": f"Bearer {self.VALID_TOKEN}"
        }
        response = requests.put(self.URL, json=self.data2,headers=headers)
        self.assertEqual(response.status_code, 404)
        print("Negative Test 3 completed - PUT Request")
        print("Passed missing parametes")
        print("The response code is 404")
        print("--------------------------------------")


    # Negative test case 4: For passing empty data
    def test_empty_put(self):
        headers = {
            "Authorization": f"Bearer {self.VALID_TOKEN}"
        }
        response = requests.put(self.URL+"/1", json=self.data, headers=headers)
        self.assertEqual(response.status_code, 400)
        print("Negative Test 4 completed - PUT Request")
        print("Passed Empty data")
        print("The response code is 400 BAD REQUEST")
        print("--------------------------------------")

if __name__ == '__main__':
    tester=ApiTests()
    tester.test_successful_put()

    tester.test_put_invalid_token()
    tester.test_put_nonexisting_id()
    tester.test_missing_param()
    tester.test_empty_put()