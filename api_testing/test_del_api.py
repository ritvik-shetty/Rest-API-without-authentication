import unittest
import requests

class ApiTests(unittest.TestCase):
    URL="http://127.0.0.1:5000/remove_employee"

    # Positive test case to delete an employee
    def test_delete_existing_item(self):
        response=requests.delete(self.URL+'/7')
        self.assertEqual(response.status_code,200)
        
        print("Positive test 1 completed- DELETE Request")
        print("The response code is 200 OK")
        print("-----------------------------------------")



    # Negative test case to delete an employee
    def test_delete_with_improper_token(self):
        response=requests.delete(self.URL+'/10')
        self.assertEqual(response.status_code,404)
        
        print("Negative test 1 completed- DELETE Request")
        print("The response code is 404")
        print("-----------------------------------------")    

    
    # Negative test case for non-existent data
    def test_delete_non_existent_item(self):
        response=requests.delete(self.URL+'/99999')
        self.assertEqual(response.status_code,404)
        
        print("Negative test 2 completed- DELETE Request")
        print("The response code is 404")
        print("-----------------------------------------")


        # Negative test case for invalid request methods
    def test_invalid_method(self):
        response = requests.put(self.URL)
        self.assertEqual(response.status_code, 404)
        print("Negative Test 2 completed - DELETE Request")
        print("The response code is 404 ")
        print("The requested method is invalid")
        print("--------------------------------------") 

if __name__ == '__main__':
    tester=ApiTests()
    tester.test_delete_existing_item()


    tester.test_delete_with_improper_token()
    tester.test_delete_non_existent_item()
    tester.test_invalid_method()