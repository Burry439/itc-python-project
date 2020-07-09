# 'requests' is a module installed using pip  
import requests
from pprint import pprint
from Classes.BasePost import BasePost

# our posts dictionary 
posts = {}

def get_posts():

        # make the request
        request = requests.get("https://jsonplaceholder.typicode.com/posts")

        # resolve the promise and get the data
        response = request.json()

        # for every post we got back from the request
        for post in response:

            # add a new entry to the posts dictionary with its key as the post id and set its value to a new BasePost class instance
            posts[post["id"]] = BasePost(post["userId"], post["id"], post["title"], post["body"])

            # print the posts values 
            pprint (vars(posts.get(post["id"])))

# call the method
get_posts()
