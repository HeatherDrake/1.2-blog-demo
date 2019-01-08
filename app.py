# say_this="hello there"
# print(say_this)
# more_stuff = 2
# print(more_stuff)
#
# cats = ["fluffy", "lion", "tommy"]
# favorite_numbers = [3, 6, 9 ]
#
# print(cats)
# print (cats[1])


import  os

from flask import Flask
from flask import request

app = Flask(__name__)
@app.route("/")
def hello():
    post_name = request.args.get("post")

    counter_file_name = "{}_likes.txt".format(post_name)
    print(counter_file_name)

        (counter_file = open ( counter_file_name, "r")
         post_count =counter_file.reas()
         if not post_count:
         new_count =1 + int(post_count)
         print(new_count)
         if os.path.exisits(counter_file_name):
             counter_file = open (counter_file_name, "r")
         else:
             counter_file = open (counter_file_name, "r")
             post_count = counter_file_read)
         if not post_count:
             post_count =0
        new_count = 1 + int(post_count)
        print(new_count)





    #print("hello world")

    index_file = open("index.html", "r")
    my_html = index_file.read()
    #print(my_html)
    index_file.close()
    return my_html


    return "hello world"

