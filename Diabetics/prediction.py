import pickle

model=pickle.load(open('model.pkl','rb'))

# ans=model.predict([[5,130,78,30,26,30.2,0.988,29]])
# print(ans[0])
def fun(preg,glucose,bp,st,i,bmi,DPF,age):
    return model.predict([[preg,glucose,bp,st,i,bmi,DPF,age]])

print(fun(5,130,78,30,26,30.2,0.988,29))