import requests
import json

# Collect user information
data = {
    "UCID": "AHL25", 
    "first_name": "Aliya",  
    "last_name": "Laliwala",  
    "github_username": "aliya4codee",  
    "discord_username": "aliya.159",  
    "favorite_cartoon": "Spongebob",
    "favorite_language": "Python",
    "movie_or_game_or_book": "The Alchemist",
    "section": "101" 
}

# Validate section before sending
if data["section"] not in ["101", "103"]:
    print("Error: Section must be either '101' or '103'.")
    exit(1)

# API endpoint
url = "https://student-info-api.netlify.app/.netlify/functions/submit_student_info"

# Headers
headers = {
    "Content-Type": "application/json"
}

try:
    # Send POST request
    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    # Check response
    if response.status_code == 200:
        print("Success! Your information was submitted.")
        print("Server Response:", response.json())
    else:
        print(f"Failed to submit data. Status code: {response.status_code}")
        print("Response:", response.text)

except requests.exceptions.RequestException as e:
    print("An error occurred while sending the request:", e)