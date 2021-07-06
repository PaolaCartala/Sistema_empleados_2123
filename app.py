from flask import Flask
from flask import render_template
from flaskext.mysql import MySQL

app = Flask(__name__) # instanciamos flask

mysql = MySQL()
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'sistema2123'
mysql.init_app(app)



@app.route('/') # routeamos
def index():
    sql = "INSERT INTO `empleados` (`id`, `nombre`, `correo`, `foto`) VALUES (NULL, 'Venus', 'venusperradeatenas@gmail.com', 'fotodevenus.jpg');" # consulta
    conn = mysql.connect() 
    cursor = conn.cursor() # crea el cursor
    cursor.execute(sql) # ejecuta
    conn.commit() # hace commit

    return render_template('empleados/index.html')

if __name__ == '__main__':
    app.run(debug=True)
