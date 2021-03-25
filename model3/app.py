from flask import Flask,render_template,request,redirect
from model3.models import Produk
import pymysql

application = Flask(__name__)

@application.route('/')
def index():
    DATABASE = pymysql.connect('localhost','root','rikimaru14','latihan')
    cursor = DATABASE.cursor()
    cursor.execute('select * from produk')
    data = cursor.fetchall()
    container = []
    for i in range(len(data)):
        kode = data[i][0]
        nama = data[i][1]
        harga = data[i][2]
        model = Produk(kode,nama,harga)
        container.append(model)
    DATABASE.commit()
    cursor.close()
    DATABASE.close()
    return render_template('index.html',container=container)

@application.route('/tambah', methods = ['GET','POST'])
def tambah():
    if request.method == 'POST':
        kode = request.form['kode']
        nama = request.form['nama']
        harga = request.form['harga']
        model = Produk(kode,nama,harga)
        model.tambah()
        return redirect('http://127.0.0.1:5000')
    else:
        return render_template('tambah_form.html')

@application.route('/ubah/<int:id>',methods = ['GET','POST'])
def ubah(id):
    model = Produk()
    model.load(id)
    if request.method == 'POST':
        kode = request.form['kode']
        nama = request.form['nama']
        harga = request.form['harga']
        model.setKode(kode)
        model.setNama(nama)
        model.setHarga(harga)
        model.ubah()
        return redirect('http://127.0.0.1:5000')
    else:
        return render_template('ubah_form.html',model = model)

@application.route('/hapus/<int:id>',methods = ['GET','POST'])
def hapus(id):
    model = Produk()
    model.load(id)
    model.hapus()
    return redirect('http://127.0.0.1:5000')


if __name__ == '__main__':
    application.run(debug = True)