from flask import render_template,url_for,redirect,flash
from Diabetics import app
from Diabetics.forms import data

import pickle

model=pickle.load(open('model.pkl','rb'))

def fun(preg,glucose,bp,st,i,bmi,DPF,age):
    return model.predict([[preg,glucose,bp,st,i,bmi,DPF,age]])

@app.route('/',methods=['GET','POST'])
@app.route('/home',methods=['GET','POST'])
def home():
    form=data()
    if form.validate_on_submit():
        if form.preg.data == None:
            preg=0
        else:
            preg=form.preg.data
        if form.glucose.data == None:
            glucose=0
        else:
            glucose=form.glucose.data
        if form.bp.data == None:
            bp = 0
        else:
            bp = form.bp.data
        if form.st.data == None:
            st = 0
        else:
            st = form.st.data
        if form.i.data == None:
            i = 0
        else:
            i = form.i.data
        if form.bmi.data == None:
            bmi = 0
        else:
            bmi = form.bmi.data
        if form.DPF.data == None:
            DPF = 0
        else:
            DPF = form.DPF.data
        if form.age.data == None:
            age=0
        else:
            age=form.age.data
        pred=fun(preg,glucose,bp,st,i,bmi,DPF,age)
        final=pred[0]
        if final==0:
            return render_template('ans.html',ans='NO')
        else:
            return render_template('ans.html',ans='YES')

    return render_template('home.html',title='Register',form=form)
    return render_template('home.html',form=form)