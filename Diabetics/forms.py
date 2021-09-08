from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField,PasswordField,SubmitField,FloatField

class data(FlaskForm):
    preg=IntegerField('Pregnancies')
    glucose=IntegerField('Glucose')
    bp=IntegerField('Blood Pressure')
    st=IntegerField('Skin Thickness')
    i=IntegerField('Insulin')
    bmi=FloatField('BMI')
    DPF=FloatField('Diabetes Pedigree Function')
    age=IntegerField('Age')
    submit = SubmitField('Check')

