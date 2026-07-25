import os
import subprocess
import sys
import requests

def get_github_info():
    username = input("Enter GitHub username: ")
    url = f"https://api.github.com/users/{username}"
    headers = {
        "Accept": "application/vnd.github.v3+json"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        
        print(f"\nAccount Info: {data.get('login')}")
        print("-" * 40)
        print(f"Name: {data.get('name')}")
        print(f"Company: {data.get('company')}")
        print(f"Blog/Website: {data.get('blog')}")
        print(f"Location: {data.get('location')}")
        print(f"Email: {data.get('email')}")
        print(f"Bio: {data.get('bio')}")
        print(f"Public Repositories: {data.get('public_repos')}")
        print(f"Public Gists: {data.get('public_gists')}")
        print(f"Followers: {data.get('followers')}")
        print(f"Following: {data.get('following')}")
        print(f"Profile URL: {data.get('html_url')}")
        print(f"Created At: {data.get('created_at')}")
        print(f"Updated At: {data.get('updated_at')}")
        
        script_path = os.path.abspath(__file__)
        subprocess.run(["osascript", "-e", f'tell application "Terminal" to do script "python3 {script_path}"'])
    elif response.status_code == 404:
        print("User not found.")
    else:
        print(f"Error occurred: {response.status_code}")

if __name__ == "__main__":
    get_github_info()