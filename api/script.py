from flask import Flask,request,render_template
from flaskext.mysql import MySQL
mysql=MySQL()

app=Flask(__name__)
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']='15352113'
app.config['MYSQL_DATABASE_DB']='reviews'
app.config['MYSQL_DATABASE_host']='localhost'
mysql.init_app(app)



@app.route('/',methods=['GET','POST'])
def get_data():
  if request.method=='POST':
    comments=request.form['commenties']
    connection = mysql.get_db()
    cursor = connection.cursor()
    query="INSERT INTO opinions(comment) VALUES(%s)"
    cursor.execute(query,(comments))
    connection.commit()
  return render_template("sample.html")

if __name__=='__main__':
    app.run(debug=True)

