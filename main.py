import requests
import json
import os
import dotenv
from time import sleep
from pathlib import Path
dotenv.load_dotenv(".env")

base_url = "https://rebrickable.com/api/v3/"
def api_info():
    api_key = os.getenv("API_KEY")
    headers = {
        "Authorization": f"key {api_key}"
    }
    return(headers)

def fetch_api_data(url, headers):
    try:
        # Make the GET request
        print(url)
        response = requests.get(url, headers=headers)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"Error: API request failed with status code {response.status_code}")
            print(response.json()) # Print error details if available
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the API call: {e}")

def elementprint(data):
    print("------------------------")
    print("part #:", data["part"]["part_num"])
    print("part name:", data["part"]["name"])
    print("color:", data["color"]["id"])
    print("RB color:", data["color"]["name"])
    print("Lego Color:", data["color"]["external_ids"]["LEGO"]["ext_descrs"][0][0])
    print("img url:", data["part"]["part_img_url"])
    print("------------------------")
def partprint(data):
    print("------------------------")
    print("part #:", data["part_num"])
    print("part name:", data["name"])
    print("img url:", data["part_img_url"])   
    print("------------------------") 
def partcolorprint(data,part_num,color_id):
    print("------------------------")
    print("part #:", part_num)
    print("color id:", color_id)
    print("elements:", data["elements"])
    print("img url:", data["part_img_url"])
    print("------------------------")
def partcolorsprint(data,part_num):
    #print("------------------------")
    print("part #:", part_num)
    print("color_id:", data["color_id"])
    print("color name:", data["color_name"])
    print("elements:", data["elements"])
    print("img url:", data["part_img_url"])
    print("------------------------")

def read_json_file(filename):
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
    return data

def fetch_data(choice, endpoint):
    my_file = Path(choice)
    if my_file.is_file():
        data = read_json_file(choice)
        print("Read data from existing file.")
        return(data)
        #print("Read data from existing file.")
    else:
        headers = api_info()
        url = f"{base_url}{endpoint}"
        data = fetch_api_data(url, headers)
        if data == None:
            print("Invalid part number or error fetching data.")
            exit()
        with open(choice, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        return(data)
        print("Fetched data from API and saved to file.")

def menuinput(choice):

    if choice == '1':
        element_id = input("Enter element id: ")
        filename = f'output/element-{element_id}.json'
        endpoint = f"lego/elements/{element_id}/"
        
        elementprint(fetch_data(filename, endpoint))

    elif choice == '2':
        part_num = input("Enter part_num: ")
        filename = f'output/part_num-{part_num}.json'
        endpoint = f"lego/parts/{part_num}/"
        
        partprint(fetch_data(filename, endpoint))
        #call parts function
    elif choice == '3':
        part_num = input("Enter part_num: ")
        color_id = input("Enter color id: ")
        filename = f'output/part_num-{part_num}-{color_id}.json'
        endpoint = f"lego/parts/{part_num}/colors/{color_id}"
        
        partcolorprint(fetch_data(filename, endpoint),part_num,color_id)
    elif choice == '4':
        part_num = input("Enter part_num: ")
        filename = f'output/part_num-{part_num}-colors.json'
        endpoint = f"lego/parts/{part_num}/colors/"
        data = fetch_data(filename, endpoint)
        for line in data["results"]:
            sleep(0.1)
            partcolorsprint(line,part_num)
    elif choice == '5':
        exit()
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
        exit()

def userinput():
    userinput = input(f'''
Lego Part Menu:
1. Enter an element id
2. Enter a part_num
3. Enter a part_num and color_id to see info about that specific part in that color
4. Enter a part_num to see all available colors for that part
5. Exit
Please choose (1-5): ''')
    menuinput(userinput)
    #return userinput
def waitmenu():
    if input("Press Enter to return to menu..."):
        return

while True:
    choice = userinput()
    waitmenu()

#action = menuinput(choice)

