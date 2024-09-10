'''from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Swetha"

if __name__ == ' __main__':
  app.run(host='0.0.0.0', debug=True)
  '''
from flask import Flask, render_template, jsonify

app = Flask(__name__)
JOBS = [
    {
        'id': 1,
        'title': 'DevOps Engineer',
        'location': 'Hyderabad, India',
        'salary': 'Rs. 14,00,000'
    },
    {
        'id': 2,
        'title': 'NLP Engineer',
        'location': 'New York, USA',
        'salary': '$140,000'
    },
    {
        'id': 3,
        'title': 'UI/UX Designer',
        'location': 'Berlin, Germany',
        
    },
    {
        'id': 4,
        'title': 'Cloud Architect',
        'location': 'London, UK',
        'salary': '£95,000'
    }
    
    
]


@app.route("/")
def hello():
    return render_template('home.html',
                          jobs=JOBS, company_name='Pravartak')
@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

   