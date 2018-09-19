## HW 1
## SI 364 F18
## 1000 points

#################################

## List below here, in a comment/comments, the people you worked with on this assignment AND any resources you used to find code (50 point deduction for not doing so). If none, write "None".


## [PROBLEM 1] - 150 points
## Below is code for one of the simplest possible Flask applications. Edit the code so that once you run this application locally and go to the URL 'http://localhost:5000/class', you see a page that says "Welcome to SI 364!"

from flask import Flask, request
import requests
import json
app = Flask(__name__)
app.debug = True

@app.route('/class')
def welcome():
    return 'Welcome to SI 364!'


## [PROBLEM 2] - 250 points
## Edit the code chunk above again so that if you go to the URL 'http://localhost:5000/movie/<name-of-movie-here-one-word>' you see a big dictionary of data on the page. For example, if you go to the URL 'http://localhost:5000/movie/ratatouille', you should see something like the data shown in the included file sample_ratatouille_data.txt, which contains data about the animated movie Ratatouille. However, if you go to the url http://localhost:5000/movie/titanic, you should get different data, and if you go to the url 'http://localhost:5000/movie/dsagdsgskfsl' for example, you should see data on the page that looks like this:

# {
#  "resultCount":0,
#  "results": []
# }

@app.route('/movie/<nameofmoviehere>')
def moviename(nameofmoviehere):
    movies = requests.get("https://itunes.apple.com/search?term=" + nameofmoviehereoneword).text
    return movies

## You should use the iTunes Search API to get that data.
## Docs for that API are here: https://affiliate.itunes.apple.com/resources/documentation/itunes-store-web-service-search-api/
## Of course, you'll also need the requests library and knowledge of how to make a request to a REST API for data.

## Run the app locally (repeatedly) and try these URLs out!



## [PROBLEM 3] - 250 points

## Edit the above Flask application code so that if you run the application locally and got to the URL http://localhost:5000/question, you see a form that asks you to enter your favorite number.
## Once you enter a number and submit it to the form, you should then see a web page that says "Double your favorite number is <number>". For example, if you enter 2 into the form, you should then see a page that says "Double your favorite number is 4". Careful about types in your Python code!
## You can assume a user will always enter a number only.

@app.route('/question')
def favnum():
    formnumber= ''' <!DOCTYPE html>
    <html>
    <body>
    <form action="/result" method="post">
    <p>Enter your favorite number:</p>
    <input type='text' name='number'> <br><br>
    <input type='submit' value="Sumbit">
    </form>
    </body>
    </html>'''
    return formnumber


@app.route('/result', methods = ['POST','GET'])
def mynum():
    if request.method == "POST":
        s = int(request.form['number']) * int(request.form['number'])
        return "Double your favorite number is {}".format(s)


## [PROBLEM 4] - 350 points
@app.route('/problem4form', methods = ['GET'])
def choose_recipe():
	dessert = """<!DOCTYPE html>
<html>
<body>
<form name="myForm" action="/dessert_recipe" method="get">
<p>
Choose a dessert to find out recipes! <b> <br>
<input type="radio" name="choice" value="Cookie"> Cookie <br>
<input type="radio" name="choice" value="Ice Cream"> Ice Cream <br>
<input type="radio" name="choice" value="Brownie"> Brownie <br>
</p>
<p><input type=submit value=Submitt></p>
</form>
</form>
</body>
</html>"""
	return dessert

@app.route('/dessert_recipe', methods = ['GET'])
def recipes_data():
    result = request.args
    desserts= result.get('choice')

    base_url = "http://www.recipepuppy.com/api/?q="
    url = base_url + desserts
    dict = requests.get(url)
    json_data = dict.json()
    #print (json_data['results'])
    entries = []
    for entry in json_data['results']:
        title = entry['title']
        ingredients = entry['ingredients']
        entries.append(title)
        entries.append(ingredients)
    return str(entries)




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

if __name__ == '__main__':
    app.run()
