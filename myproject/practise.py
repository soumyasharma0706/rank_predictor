import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
response=requests.get("https://codeforces.com/api/user.rating?handle=soumya07062003")
try:
    response.raise_for_status()  # Check if the request was successful
    data = response.json()
    print(data)
except requests.exceptions.HTTPError as errh:
    print ("HTTP Error:", errh)
except requests.exceptions.ConnectionError as errc:
    print ("Error Connecting:", errc)
except requests.exceptions.Timeout as errt:
    print ("Timeout Error:", errt)
except requests.exceptions.RequestException as err:
    print ("Error:", err)
# df=pd.DataFrame(b['result'])
# y=(np.array(df['newRating']))
# n=len(y)
# print(y)
# if (n>=5):
#     y=y[n-6:n-1]
# print(y)

# def pearson_correlation(x,y):
#     mean_x = sum(x)/float(len(x))
#     mean_y = sum(y)/float(len(y))
#     # Subtracting mean from the individual elements
#     sub_x = [i-mean_x for i in x]
#     sub_y = [i-mean_y for i in y]
#     # covariance for x and y
#     numerator = sum([sub_x[i]*sub_y[i] for i in range(len(sub_x))])
#     # Standard Deviation of x and y
#     std_deviation_x = sum([sub_x[i]**2.0 for i in range(len(sub_x))])
#     std_deviation_y = sum([sub_y[i]**2.0 for i in range(len(sub_y))])
#     # squaring by 0.5 to find the square root
#     denominator = (std_deviation_x*std_deviation_y)**0.5 
#     cor = numerator/denominator
#     return cor

# def linear_reg_coff(x,y):
#     ux= np.mean(x);uy = np.mean(y)
#     xdiff = x-ux
#     ydiff = y-uy
#     w_tem1 = xdiff*ydiff
#     w_tem2 = xdiff*xdiff
#     w1 = sum(w_tem1)/sum(w_tem2)
#     w0 = uy -(w1)*(ux)
#     return w1,w0

# def linear_reg(x,y,x_test):
#     w1,w0  = linear_reg_coff(x,y)
#     yout = w1*x_test+w0
#     return int(yout)   

# def plotting_best_fit_line(x,y,col_name):
#     w1,w0 = linear_reg_coff(x,y)
#     y_reg = w1*x +w0
#     plt.plot(x,y_reg,color = 'r')
#     plt.scatter(x,y)
#     plt.xlabel(col_name,fontsize = 30)
#     plt.ylabel("Rings",fontsize= 30)
#     plt.grid(True)
#     plt.title("BEST FIT LINE ON SCATTER PLOT ->",fontsize =40)
#     plt.show()

# x=[i for i in range(1,len(y)+1)]
# print(x)
# b=linear_reg(x,y,8)
# print(b)

