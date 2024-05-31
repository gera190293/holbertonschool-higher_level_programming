#!/usr/bin/python3

"""Module for RESTful API exercises"""
import requests
import csv

url = "https://jsonplaceholder.typicode.com/posts"

def fetch_and_print_posts():
    """Function that fetches all post from JSONPlaceholder"""
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        data = response.json()
        
        for post in data:
            print(post['title'])
    else:
        print("Error retrieving posts")

def fetch_and_save_posts():
    """Function that fetches all post from JSONPlaceholder and saves them into a CSV file"""
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        data = response.json()
        fieldnames = ['id', 'title', 'body']
        posts_list = []

        for post in data:
            post_dict = {
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            }
            posts_list.append(post_dict)

        with open('posts.csv', mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(posts_list)
        print("File saved successfully as posts.csv")
    else:
        print("Failed to retrieve posts")

fetch_and_save_posts()
