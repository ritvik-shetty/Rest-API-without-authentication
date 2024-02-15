import requests

header={
    'Accept':'*/*'
}
response= requests.get("http://127.0.0.1:5000/list_employees", headers=header)

assert response.status_code==200 , f"expected response to have status code 200 but got {response.status_code}"

print("The program has run successfully and the Status Code is",response.status_code)

list=response.json()
for i in range(len(list)):
    print(list[i])
