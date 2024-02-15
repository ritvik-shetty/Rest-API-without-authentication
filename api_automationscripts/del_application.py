import requests

header={
    'Accept':'*/*'
}

response = requests.get("http://127.0.0.1:5000/list_employees", headers=header)
assert response.status_code==200 , f"expected response to have status code 200 but got {response.status_code}"

print("Initial GET Request and the Status Code is",response.status_code)
list=response.json()
for i in range(len(list)):
    print(list[i])



headDel={
    'Accept': '*/*'
}

responseDel= requests.delete("http://127.0.0.1:5000/remove_employee/7",headers=headDel)
assert responseDel.status_code==200 , f"expected response to have status code 200 but got {response.status_code}"
print("Deleted Successfull with response code",responseDel.status_code)



print("Data after delete")
response = requests.get("http://127.0.0.1:5000/list_employees", headers=header)
list=response.json()
for i in range(len(list)):
    print(list[i])
