import re
import requests

# _____________________________________________________________
# Program that displays most starred language of your choice
# Languages Supported: Python, C, Objective C, C++, Rust, Java
#                      Swift, Javascript, Go, HTML and PHP
# _____________________________________________________________

# Storing the url of the API in url variable url with a length of 54 characters
url = 'https://api.github.com/search/repositories?q=language:'
# GitHub is currently on 3rd version of its API so we will use it
headers = {'Accept': 'application/vnd.github.v3+json'}
language = input("Please enter which language you want to lookup.\n")
request = str(language.lower())
objective_c = re.search(r'obj', request)

while len(url) < 55:
    if request == 'python':
        url += 'python&sort=stars'
    elif request == 'c++' or language == 'cpp':
        url += 'c++&sort=stars'
    elif request == 'rust':
        url += 'rust&sort=stars'
    elif request == 'javascript':
        url += 'javascript&sort=stars'
    elif request == 'go':
        url += 'go&sort=stars'
    elif request == 'java':
        url += 'java&sort=stars'
    elif request == 'typescript':
        url += 'typescript&sort=stars'
    elif objective_c:
        url += 'objective-c&sort=stars'
    elif request == 'c':
        url += 'c&sort=stars'
    elif request == 'swift':
        url += 'swift&sort=stars'
    elif request == 'html':
        url += 'html&sort=stars'
    elif request == 'php':
        url += 'php&sort=stars'
    else:
        print('Requested language is not supported, please try again.')
        break

git = requests.get(url, headers=headers)
print(f"Status code: {git.status_code}")

# Store API response in a variable
git_dict = git.json()

# Brief description about these repositories
git_dicts = git_dict['items']
print("\nOutput from GitHub API call:")
for repos in git_dicts:
    print(f"Name: {repos['name'].title()} || {repos['description']} ||"
          f" Stars: {repos['stargazers_count']}")
print("----------------------------------------------------------------\n"
      f"Total repositories for {request.title()} found: {git_dict['total_count']}\n"
      "----------------------------------------------------------------")
