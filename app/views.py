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

@app.route('/piles')
def piles():
  titles = {1: "can't do", 3: "can do with effort", 5: "mastered"}
  result = [get_pile_data(x, titles[x]) for x in (1,3,5)]
  return render_template('piles.html', data=result)

def get_pile_data(level, name):
  result = {'title':name, 'skills': []}
  query = models.Skill.query.filter(models.Skill.level==level)
  for skill in query:
    result['skills'].append(skill)
  return result