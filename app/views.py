from app import app, db, models
from flask import render_template, request, redirect, url_for

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

@app.route('/add_skill', methods=['POST'])
def add_skill():
  title = request.form['skill_name']
  description = request.form['skill_description']
  level = int(request.form['skill_level'])

  skill_obj = models.Skill(title, description, level)
  db.session.add(skill_obj)
  db.session.commit()
  return redirect(url_for('skills'))