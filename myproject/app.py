import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from flask import Flask,render_template,request
app=Flask(__name__)

@app.route('/')
def get_myfirst_post():
    return render_template("Project3.html")

@app.route('/contact', methods=['GET','POST'])
def contact():
    if request.method=="POST":
        data=request.form
        person_name=data["person_name"]
        account_name=data["account_name"]
        req_api="https://codeforces.com/api/user.rating?handle=" + account_name
        response=requests.get(req_api)
        data1=response.json()
        df=pd.DataFrame(data1['result'])
        y1=np.array(df['rank'])
        y1_plot=np.array(df['rank'])
        n=len(y1)
        y2=np.array(df['newRating'])
        y2_plot=np.array(df['newRating'])
        if(n>=10):
            y1=y1[n-11:n-1]
            y2=y2[n-11:n-1]      


        def linear_reg_coff(x,y):
            ux= np.mean(x);uy = np.mean(y)
            xdiff = x-ux
            ydiff = y-uy
            w_tem1 = xdiff*ydiff
            w_tem2 = xdiff*xdiff
            w1 = sum(w_tem1)/sum(w_tem2)
            w0 = uy -(w1)*(ux)
            return w1,w0

        def linear_reg(x,y,x_test):
            w1,w0  = linear_reg_coff(x,y)
            yout = w1*x_test+w0
            return int(yout)   

        def plotting_best_fit_line(x,y2):
            plt.plot(x,y2,color = 'r',label='your contest ranking')
            plt.scatter(x,y2)
            plt.xlabel("your given contests",fontsize = 10)
            plt.ylabel("corresponding rating  ->",fontsize= 10)
            plt.savefig('static/plot.png')
            # plt.show()
        
        x=np.array([i for i in range (1,len(y1)+1)])
        x_plot=np.array([i for i in range (1,len(y1_plot)+1)])
        pred_rank=linear_reg(x,y1,n+1)
        pred_rating=linear_reg(x,y2,n+1)
        plotting_best_fit_line(x_plot,y2_plot)

        return render_template("contact.html",name=person_name,rank=pred_rank,rating=pred_rating,number=n)




if __name__=="__main__":
    app.run(debug=True)