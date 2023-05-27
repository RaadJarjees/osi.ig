

def user_info(usrname):
    url = f"https://example.com/api/user/{usrname}"  # Replace 'example.com' with the actual API endpoint
    resp = requests.get(url)

    if resp.status_code == 200:
        resp_js = resp.text
        try:
            js = json.loads(resp_js)
            # Process the JSON data here
            print(js)  # Example: Print the JSON data
        except json.JSONDecodeError as e:
            print("Error decoding JSON:", e)
    else:
        print("Error:", resp.status_code)









	






	
