import requests

header={
    'Accept':'*/*'
}

response= requests.get("http://127.0.0.1:5000/list_employees", headers=header)

print("Before Update")
list=response.json()
for i in range(len(list)):
    print(list[i])



headerPut={
    'Accept':'*/*',
    'Content-Type': 'application/json'
}

putPayload={
        "address": "Kadri",
        "city": "Mangalore",
        "name": "Manoj",
        "salary": "99999"
}

responsePut= requests.put("http://127.0.0.1:5000/update_employee/5",headers=headerPut,json=putPayload)



print("After Update")
response= requests.get("http://127.0.0.1:5000/list_employees", headers=header)
list=response.json()
for i in range(len(list)):
    print(list[i])


assert responsePut.status_code == 200 , f"expected response to have status code 200 but got {response.status_code}"

print("The program has run successfully and the Status Code is",response.status_code)