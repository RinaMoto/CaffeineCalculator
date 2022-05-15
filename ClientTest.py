import requests

PORT_NUM = 3000
ENDPOINT = f"http://127.0.0.1:{PORT_NUM}/max"
headers = {'Content-type': 'application/json'}

# Normal call with all 4 parameters
response = requests.post(ENDPOINT, json={'weight': 155.9, 'weight_units': 'lbs',
                                   'content': 130.7, 'content_units': 'mg'},
                                   headers=headers)
res = response.json()
if response.status_code != 200:
  print(res['message'])
else:
  print(res['maxServings'])

# Normal call with all 4 parameters (will still work if floats are strings)
response = requests.post(ENDPOINT, json={'weight': '155.9', 'weight_units': 'lbs',
                                   'content': '130.7', 'content_units': 'mg'},
                                   headers=headers)
res = response.json()
if response.status_code != 200:
  print(res['message'])
else:
  print(res['maxServings'])

# Call with missing param
response = requests.post(ENDPOINT, json={'weight': 150, 'weight_units': 'lbs',
                                   'content': 125},
                                   headers=headers)
res = response.json()
if response.status_code != 200:
  print(res['message'])
else:
  print(res['maxServings'])

# Call with wrong type
response = requests.post(ENDPOINT, json={'weight': 150, 'weight_units': 'lbs',
                                   'content': 'error', 'content_units': 'mg'},
                                   headers=headers)
res = response.json()
if response.status_code != 200:
  print(res['message'])
else:
  print(res['maxServings'])

# Call with undefined units
response = requests.post(ENDPOINT, json={'weight': 150, 'weight_units': 'lbs',
                                   'content': '125', 'content_units': 'm^3'},
                                   headers=headers)
res = response.json()
if response.status_code != 200:
  print(res['message'])
else:
  print(res['maxServings'])
