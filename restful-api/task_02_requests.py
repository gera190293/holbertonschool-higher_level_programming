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
        print("Error to retrieve post")

def fetch_and_save_posts():
    """Function that fetches all post from JSONPlaceholder"""
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        data = response.json()
        names = ['id', 'title', 'body']
        post_dic = []

        for post in data:
            post_dic = {
            'id': post['id'], 'title': post['title'], 'body': post['body']
            }
            post_dic.append(post_dic)

        with open('post_dic.csv', mode= 'w', newline='', encoding='utf-8') as f:
            wr = csv.DictWriter(post_dic, fieldnames=names)
            wr.writeheader()
            wr.writerow(post_dic)
        print("File save susessfull")
    else:
        print("Fail to retrieve post")
