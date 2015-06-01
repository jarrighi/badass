from app import app, db, models
from flask import render_template

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/skills')
def skills():
  result = []
  query = models.Skill.query.all()
  for skill in query:
    result.append(skill)
  return render_template('skills.html', skills=result)
