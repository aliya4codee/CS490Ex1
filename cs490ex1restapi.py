import requests
import json

# my information
student_info = {
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

# Make sure section is correct
if student_info["section"] not in ["101", "103"]:
    print("Error: Section must be either 101 or 103")
    exit()

# API endpoint
url = "https://student-info-api.netlify.app/.netlify/functions/submit_student_info"
headers = {"Content-Type": "application/json"}

print("Choose an action:")
print("1. Submit (POST)")
print("2. Retrieve (GET)")
print("3. Update (PUT)")
print("4. Delete (DELETE)")
choice = input("Enter your choice (1-4): ")

if choice == "1":
    response = requests.post(url, headers=headers, data=json.dumps(student_info))
elif choice == "2":
    get_url = f"{url}?UCID={student_info['UCID']}&section={student_info['section']}"
    response = requests.get(get_url)
elif choice == "3":
    student_info["favorite_cartoon"] = "SpongeBob"
    response = requests.put(url, headers=headers, data=json.dumps(student_info))
elif choice == "4":
    delete_url = f"{url}?UCID={student_info['UCID']}&section={student_info['section']}"
    response = requests.delete(delete_url)
else:
    print("Invalid choice")
    exit()

# Check the response
if response.status_code == 200:
    print("Success!")
    print("Response:", response.text)
else:
    print("Failed with status code:", response.status_code)
    print("Response:", response.text)