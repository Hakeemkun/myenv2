from flask import Flask, render_template, redirect, request, url_for, session
import sqlite3
app2=Flask(__name__)


# getting the infos from the input and insert it in the database
@app2.route('/' , methods=['POST','GET'])
def homepage():
      if request.method == 'POST':
         db=sqlite3.connect('app.db')
         cr=db.cursor()
         cr.execute('create table if not exists skills (skill text , level integer)')
      
         skill=request.form["skill"]
         level=request.form["level"]
         cr.execute('SELECT * FROM skills WHERE skill=?', (skill,))
         skill_exists=cr.fetchone()
         if not skill_exists:
            cr.execute(f'insert into skills (skill,level)  values(?,?)',(skill,level))
            db.commit()
            db.close()
         return redirect(url_for('skills'))
      else:
         return render_template('home2.html')
#skills page

@app2.route('/skills')
def skills():
   #getting the data
   db=sqlite3.connect('app.db')
   cr=db.cursor()
   cr.execute('select skill from skills')
   skills=cr.fetchall()
   cr.execute('select level from skills')
   levels=cr.fetchall()
   #ziping the data
   ziped=zip(skills,levels)
   db.close()

   return render_template('skills.html',datalist=ziped,custom_css='skills')



#edit page

@app2.route('/edit', methods=['POST', 'GET'])
def edit():
    if request.method == 'POST':
        deleted = request.form["dt"]
      
        db = sqlite3.connect('app.db')
        cr = db.cursor()

        cr.execute(f'DELETE FROM skills WHERE skill="{deleted}"')
        db.commit()
        db.close()
        return redirect(url_for("skills"))
    else:
        return render_template('edit.html')




if  __name__=="__main__":
  app2.run()