## HW 1
## SI 364 W18
## 1000 points

#################################

## List below here, in a comment/comments, the people you worked with on this assignment AND any resources you used to find code (50 point deduction for not doing so). If none, write "None".
# None


## [PROBLEM 1] - 150 points
## Below is code for one of the simplest possible Flask applications. Edit the code so that once you run this application locally and go to the URL 'http://localhost:5000/class', you see a page that says "Welcome to SI 364!"

from flask import Flask, request
import requests
import json
app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_to_you():
    return 'Hello!'
#PROBLEM 1
@app.route('/class')
def welcome():
    return 'Welcome to SI 364!'

# @app.route('/question4form')
# def lastq():
#     return "Last question!"

## [PROBLEM 2] - 250 points
## Edit the code chunk above again so that if you go to the URL 'http://localhost:5000/movie/<name-of-movie-here-one-word>'
# you see a big dictionary of data on the page. For example, if you go to the URL 'http://localhost:5000/movie/ratatouille', 
# you should see something like the data shown in the included file sample_ratatouille_data.txt, 
# which contains data about the animated movie Ratatouille. However, if you go to the url http://localhost:5000/movie/titanic, 
# you should get different data, and if you go to the url 'http://localhost:5000/movie/dsagdsgskfsl' for example, 
# you should see data on the page that looks like this:

# {
#  "resultCount":0,
#  "results": []
# }


## You should use the iTunes Search API to get that data.
## Docs for that API are here: https://affiliate.itunes.apple.com/resources/documentation/itunes-store-web-service-search-api/
## Of course, you'll also need the requests library and knowledge of how to make a request to a REST API for data.

## Run the app locally (repeatedly) and try these URLs out!

@app.route('/movie/<newthing>') # As long as the route and param name are the same, it's fine!
def get_movie_data(newthing):
    baseurl = "https://itunes.apple.com/search"
    params_diction = {}
    params_diction["term"] = newthing
    params_diction["media"] = "movie"
    resp = requests.get(baseurl,params=params_diction)
    text = resp.text
    python_obj = json.loads(text)
    album_titles = []
    print(python_obj)
    return resp.text



## [PROBLEM 3] - 250 points

## Edit the above Flask application code so that if you run the application locally and got to the URL http://localhost:5000/question, 
# you see a form that asks you to enter your favorite number.
## Once you enter a number and submit it to the form, you should then see a web page that says "Double your favorite number is <number>". 
# For example, if you enter 2 into the form, you should then see a page that says "Double your favorite number is 4". 
# Careful about types in your Python code!
## You can assume a user will always enter a number only.


@app.route('/question')
def enterData():
    s = """<!DOCTYPE html>
<html>
<body>
<form action="/result" method="POST">
  What is your favorite number?:<br>
  <input type="text" name="fav_num" value="2"> 
  <br>
  <input type="submit" value="Submit">
</form>
</body>
</html>"""
    return s

@app.route('/result', methods = ['POST', 'GET'])
def displayData():
    try:
        if request.method == 'POST':
            double_value = int(request.form["fav_num"]) * 2
            return "<h1>Double your favorite number is {}</h1>".format(double_value)
    except:
        return "Error occured! Please try again. "
 

## [PROBLEM 4] - 350 points

## Come up with your own interactive data exchange that you want to see happen dynamically in the Flask application, and build it into the above code for a Flask application, following a few requirements.

## You should create a form that appears at the route: http://localhost:5000/problem4form

## Submitting the form should result in your seeing the results of the form on the same page.

## What you do for this problem should:
# - not be an exact repeat of something you did in class
# - must include an HTML form with checkboxes and text entry
# - should, on submission of data to the HTML form, show new data that depends upon the data entered into the submission form and is readable by humans (more readable than e.g. the data you got in Problem 2 of this HW). The new data should be gathered via API request or BeautifulSoup.

# You should feel free to be creative and do something fun for you --
# And use this opportunity to make sure you understand these steps: if you think going slowly and carefully writing out steps for a simpler data transaction, like Problem 1, will help build your understanding, you should definitely try that!

# You can assume that a user will give you the type of input/response you expect in your form; you do not need to handle errors or user confusion. (e.g. if your form asks for a name, you can assume a user will type a reasonable name; if your form asks for a number, you can assume a user will type a reasonable number; if your form asks the user to select a checkbox, you can assume they will do that.)

# Points will be assigned for each specification in the problem.

# @app.route('/question4form')
# def last_question():
#     return "pls work"

@app.route('/lastquestion', methods = ['POST', 'GET'])
def article():
    s = """<!DOCTYPE html>
        <html>
        <body>
        <form method = "POST">
          <h1>Headlining Article Search</h1>
          What topic would you like to search top headlines for?<br>
          <input type="text" name="phrase">
          <br>
          Which category(s) would you like to search from?<br>
          <input type="checkbox" name="category", value = "business"> Business
          <br>
          <input type="checkbox" name="category", value = "entertainment"> Entertainment
          <br>
          <input type="checkbox" name="category", value = "general"> General
          <br>
          <input type="checkbox" name="category", value = "health"> Health
          <br>
          <input type="checkbox" name="category", value = "science"> Science
          <br>
          <input type="checkbox" name="category", value = "sports"> Sports
          <br>
          <input type="checkbox" name="category", value = "technology"> Technology
          <br>
          <input type="submit" value="Submit">
        </form>
        </body>
        </html>"""
    return s

    try:
        baseurl = ('https://newsapi.org/v2/top-headlines?'
       'apiKey=1947a0bcbb514ba28e1f51a4ee50cdab')
        params_diction = {'q':request.form['phrase'], 'category':request.form.getlist('category')}
        # params_diction["q"] = 'phrase'
        # params_diction["category"] = "category"
        resp = requests.get(baseurl,params=params_diction)
        text = resp.text
        python_obj = json.loads(text)
        album_titles = []
        print(python_obj)
        return resp.text
    except:
        return "Sorry, try again"


####
if __name__ == '__main__':
    app.run()

