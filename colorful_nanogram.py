from flask import Flask, render_template, request, session, redirect
from flask_session import Session
import numpy as np
app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route('/')
def homepage():
  

    return render_template('main_page.html')





@app.route('/show_picture')
def show_picture_picture():
        
        size = request.args.get('size')
        colors = request.args.get('colors')
        size_s = [int(string) for string in size.split(',')]
        colors = [int(string) for string in colors.split(',')]
        pix_to_color = number_to_color(colors)
        
        return render_template('show_picture.html',size_s = size_s, pix_to_color = pix_to_color)



@app.route('/simple_picture')
def simple_picture():
        size_s = [2,3]
        pixs_s = [0,1,2,3,4,5]
        pix_to_color = []
        pix_to_color = number_to_color (pixs_s)
           


        return render_template('simple_picture.html', size_s = size_s, pix_to_color = pix_to_color)

@app.route('/chess_picture')
def chess_picture():
        size_s = [8,8]
        pixs_s = [0,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,1,
                    0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,1,0,
                    1,0,1,0,1,0]
        pix_to_color = number_to_color (pixs_s)
            
        return render_template('chess_picture.html', size_s = size_s, pix_to_color = pix_to_color)

@app.route('/special_picture')
def special_picture():
        size_s = [10,10]
        pixs_s =  [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 2, 2, 0, 0, 0, 0, 2, 2, 0,
    2, 2, 2, 2, 0, 0, 2, 2, 2, 2,
    2, 2, 5, 5, 2, 2, 5, 5, 2, 2,
    2, 2, 5, 5, 5, 5, 5, 5, 2, 2,
    0, 2, 2, 5, 5, 5, 5, 2, 2, 0,
    0, 0, 2, 2, 5, 5, 2, 2, 0, 0,
    0, 0, 0, 2, 2, 2, 2, 0, 0, 0,
    0, 0, 0, 0, 2, 2, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        pix_to_color = number_to_color (pixs_s)

        return render_template('special_picture.html', size_s = size_s, pix_to_color = pix_to_color)



def number_to_color (numbers):
    colors =[]
    for j in numbers:
            if j == 0:
                colors.append('white')
            if j == 1:
                colors.append('black')
            if j == 2:
                colors.append('red')
            if j == 3:
                colors.append('green')
            if j == 4:
                colors.append('blue')
            if j == 5:
                colors.append('purple')
    return colors


if __name__ == "__main__":
    app.run(debug=True)