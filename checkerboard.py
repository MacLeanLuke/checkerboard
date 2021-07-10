from flask import Flask, render_template  # Import Flask to allow us to create our app
from math import floor

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')  # I can have multiple routes stacked on top of each other.
@app.route('/<int:x>')
@app.route('/<int:x>/<int:y>')
def checkerboard(x=8,y=8):
    results = []
    for j in range(1,y+1):
        results_row = []
        for i in range(1, x+1):
            results_row.append(i+j)
        results.append(results_row)

    print(results)
    return render_template('index.html', table = results)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)  