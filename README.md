# Rebrickable API via Python
Calls Rebrickable API and show various information. Written in Python.
This script uses the Rebrickable API to look up info about Lego part numbers and element IDs. 
It stores/caches the results in .JSON files in the same format as the API response.

---

## Info
Element ID (element_id) is the designation for a specific Lego part and color combination.
Part Number (part_num) is the designation for a part with no color indication.
color_id is the numeric designation for a color

---

## Examples
If you don't have an API key you can use these examples. I have included cached JSON files for the following examples:

+ element_id = 4119698
+ part_num = 3001
+ color_id 10


---

## Uses the following libraries
+ import requests
+ import json
+ import os
+ import dotenv
+ from time import sleep
+ from pathlib import Path

---

## Instructions
Put your API key into .env file in the same directory as the main Python file.
API_KEY = "[apikeyhere]"

Run in command line and choose a menu selection and enter what you want to look up.

---

## Links

[Rebrickable API info](https://rebrickable.com/api/v3/docs/)

