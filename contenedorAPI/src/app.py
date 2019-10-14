from flask import Flask, request, jsonify
import pymysql
import json
import logging
import boto3
from botocore.exceptions import ClientError
import os
from flask_cors import CORS
from werkzeug import secure_filename

app = Flask(__name__)
CORS(app)

s3=boto3.resource('s3')
dirS3='https://201503925.s3.us-east-2.amazonaws.com/'
mensaje=""

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/api', methods = ['POST'])
def registro():
        global mensaje, s3
        db = pymysql.connect(host="172.17.0.2",port=3306,user="root",passwd="admin",db="flores")
        estado="Registrado"

        #Carga de Imagen
        f=request.files['file']
        f.save(secure_filename(f.filename))

        #obtener el nombre del archivo desde el request
        file_foto=f.filename

        #direccion del bucket mas foto
        # https://201503925.s3.us-east-2.amazonaws.com/fotografias+principales/foto.jpg
        direcS3=dirS3+file_foto

        nombre_picture= f.filename.replace('.png','')
        nombre_picture= nombre_picture.replace('.jpg','')
        nombre_picture= nombre_picture.replace('.jpeg','')

    
        #guardar imagen en el bucket 201503925

        s3 = boto3.client('s3')
        with open(file_foto, "rb") as f:
                s3.upload_fileobj(f, "201503925", file_foto,ExtraArgs={'ACL':'public-read'})

        #guardar en la base de datos el nombre y direccion en el bucket
        cursor = db.cursor()
        sql = "INSERT INTO FOTO(nombre,direccion) VALUES ('{0}','{1}')".format(nombre_picture,direcS3)
        try:
                cursor.execute(sql)
                db.commit()
        except:
                estado="Existio un error"
                db.rollback()
        db.close()
        return (estado)
        
@app.route('/seleccionar', methods = ['GET'])
def seleccionar():

        global mensaje, s3
        db = pymysql.connect(host="172.17.0.2",port=3306,user="root",passwd="admin",db="flores")
        #db = pymysql.connect("18.217.201.7:3306","mysql_db_docker","admin","flores")
        cursor=db.cursor()
        sql = "SELECT * FROM FOTO"
        cursor.execute(sql)
        resultado = cursor.fetchall()
        json_resp=[]
        #page_html="<br><br><br><br><br><br><br><br><br><br>"
        page_html="<table> <thead> <tr> <td>Nombre</td> <td>Fotografia</td> </tr> </thead> <tbody>"

        for row in resultado:
                c_flor = row[0]
                c_direccions3 = row[1]
                page_html+="<tr>"
                page_html+="<td> <h4>"+c_flor+"</h4> </td>"
                page_html+="<td> <img src=\""+c_direccions3+"\" height=\"100\" width=\"80\"> </td>"
                page_html+="</tr>"
                json_resp.append(dict(usuario=c_flor,s3dir=c_direccions3))
                print("user = {0}, direccion = {1}".format(c_flor,c_direccions3))
                pass

        page_html+=" </tbody> </table> "

        db.close()

        return page_html

if __name__ == "__main__":
    app.run(debug=1, port=3000, host='0.0.0.0')
