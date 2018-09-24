from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #00FF00;
                padding: 20px;
                margin: 0 auto;
                width: 900px;
                font: 2em sans-serif;
                border-radius: 10px;
            }}
            label{{
                color: #006400;
            }}
            input{{
                font-size: 1.25em;
                color: #228B22;
            }}
            textarea {{
                margin: 10px 0;
                width: 900px;
                height: 240px;
                font: 1.5em sans-serif;
                color: #228B22;
            }}
            p.error {{
                color: red;
            }}
        </style>
    </head>
    <body>
        <!-- the form goes here -->
        <form method="POST">
            <p><label>Rotate by: <input id="rotations" type="text" name="rot" value="0" /></label></p>
            <textarea id="textarea" type="textarea" name="text" />{0}</textarea>
            <!-- <button type="submit" value="Submit Query"></button> -->
            <input type="submit" value="Time to Rotate" />
        </form>
    </body>
</html>    
"""
@app.route("/", methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    text = request.form['text']
    return form.format(rotate_string(text, rot))

@app.route("/")
def index():
    return form.format("")

app.run()