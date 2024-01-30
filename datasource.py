import requests
import json
# constants
service_name = "<Your_Azure_AI_search_service_name>" #
api_version = "2023-10-01-Preview"
admin_key = "<Your_Azure_AI_search_admin_key>"
MySQLServerName = "<Your_MySQL_Server_Name>"
DatabaseName = "<The_Databse_name_from_the_MySQL_server>"
UserName = "<The_Admin_Username_which_was_set_while_creating_the_MySQL_server>"
Password = "<<The_Password_which_was_set_while_creating_the_MySQL_server>"
TableName = "<>"

# setting url and api version
url = f"https://{service_name}.search.windows.net/datasources?api-version={api_version}"
# setting header
headers = {
    "Content-Type":"application/json",
    "api-key":admin_key
}
# Request Body
data = {
    "name": "<Name_of_the_datasource>",
    "description": "a simple description",
    "type":"mysql",
    "credentials": {
        "connectionString":
            f"Server={MySQLServerName}.MySQL.database.azure.com; Port=3306; Database={DatabaseName}; Uid={UserName}; Pwd={Password}; SslMode=Preferred;"           
    },
    "container":{
        "name":f"{TableName}",
        "query":"select * from Employees;"
    }
}
# send the request
request = requests.post(url=url, headers=headers, data=json.dumps(data))

# print the response (just to check the response)
print(request.json())