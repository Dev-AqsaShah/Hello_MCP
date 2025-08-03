<<<<<<< HEAD
import requests

url = "http://localhost:8000/mcp/stream"

headers = {
    "Accept": "application/json,text/event-stream",
}

body = {
    "jsonrpc": "2.0",
   "method": "tools/list",
   "id": 1,
   "params": {},
}

response = requests.post(url, headers=headers, json=body)

for line in response.iter_lines():
    if line:
        print(line)
=======
import requests

url = "http://localhost:8000/mcp/stream"

headers = {
    "Accept": "application/json,text/event-stream",
}

body = {
    "jsonrpc": "2.0",
   "method": "tools/list",
   "id": 1,
   "params": {},
}

response = requests.post(url, headers=headers, json=body)

for line in response.iter_lines():
    if line:
        print(line)
>>>>>>> 4f6dd5f6b17a327b85d755eef9df4c91a34893dc
