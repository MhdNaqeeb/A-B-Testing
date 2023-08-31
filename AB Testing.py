#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import datetime
from datetime import date, timedelta
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
pio.templates.default = "plotly_white"


# In[2]:


control_file_path = r"C:\Users\Mhd Naqeeb\Downloads\archive (8)\control_group.csv"
test_file_path = r"C:\Users\Mhd Naqeeb\Downloads\archive (8)\test_group.csv"

control_data = pd.read_csv(control_file_path, sep=";")
test_data = pd.read_csv(test_file_path, sep=";")


# In[3]:


print(control_data.head())


# In[4]:


print(test_data.head())


# Data Preparation
# The datasets have some errors in column names. Let’s give new column names before moving forward:

# In[5]:


control_data.columns = ["Campaign Name", "Date", "Amount Spent", 
                        "Number of Impressions", "Reach", "Website Clicks", 
                        "Searches Received", "Content Viewed", "Added to Cart",
                        "Purchases"]

test_data.columns = ["Campaign Name", "Date", "Amount Spent", 
                        "Number of Impressions", "Reach", "Website Clicks", 
                        "Searches Received", "Content Viewed", "Added to Cart",
                        "Purchases"]


# In[6]:


print(control_data.isnull().sum())


# In[7]:


print(test_data.isnull().sum())


# In[8]:


control_data["Number of Impressions"].fillna(value=control_data["Number of Impressions"].mean(), 
                                             inplace=True)
control_data["Reach"].fillna(value=control_data["Reach"].mean(), 
                             inplace=True)
control_data["Website Clicks"].fillna(value=control_data["Website Clicks"].mean(), 
                                      inplace=True)
control_data["Searches Received"].fillna(value=control_data["Searches Received"].mean(), 
                                         inplace=True)
control_data["Content Viewed"].fillna(value=control_data["Content Viewed"].mean(), 
                                      inplace=True)
control_data["Added to Cart"].fillna(value=control_data["Added to Cart"].mean(), 
                                     inplace=True)
control_data["Purchases"].fillna(value=control_data["Purchases"].mean(), 
                                 inplace=True)


# Now I will create a new dataset by merging both datasets:

# In[9]:


ab_data = control_data.merge(test_data, 
                             how="outer").sort_values(["Date"])
ab_data = ab_data.reset_index(drop=True)
print(ab_data.head())


# if the dataset has an equal number of samples about both campaigns:

# In[10]:


print(ab_data["Campaign Name"].value_counts())


# A/B testing to find the best marketing strategy.

# In[12]:


figure = px.scatter(data_frame=ab_data, 
                    x="Number of Impressions",
                    y="Amount Spent", 
                    size="Amount Spent", 
                    color="Campaign Name", 
                    trendline="ols",
                    color_discrete_map={"neon blue": "#00FFFF", "red": "#FF0000"})
figure.show()


# In[13]:


import plotly.graph_objects as go

label = ["Total Searches from Control Campaign", 
         "Total Searches from Test Campaign"]
counts = [sum(control_data["Searches Received"]), 
          sum(test_data["Searches Received"])]
colors = ['#ADD8E6', '#90EE90']  # Light blue and light green colors

fig = go.Figure(data=[go.Pie(labels=label, values=counts, marker=dict(colors=colors))])
fig.update_layout(title_text='Control Vs Test: Searches', scene=dict(aspectratio=dict(x=1, y=1, z=1)))
fig.update_traces(hoverinfo='label+percent', textinfo='value+label', 
                  textfont_size=20, pull=[0.05, 0.05])
fig.show()


# In[14]:


label = ["Website Clicks from Control Campaign", 
         "Website Clicks from Test Campaign"]
counts = [sum(control_data["Website Clicks"]), 
          sum(test_data["Website Clicks"])]
colors = ['#ADD8E6', '#90EE90']  # Light blue and light green colors

fig = go.Figure(data=[go.Pie(labels=label, values=counts, marker=dict(colors=colors))])
fig.update_layout(title_text='Control Vs Test: Website Clicks', scene=dict(aspectratio=dict(x=1, y=1, z=1)))
fig.update_traces(hoverinfo='label+percent', textinfo='value+label', 
                  textfont_size=20, pull=[0.05, 0.05])
fig.show()


# In[15]:


label = ["Content Viewed from Control Campaign", 
         "Content Viewed from Test Campaign"]
counts = [sum(control_data["Content Viewed"]), 
          sum(test_data["Content Viewed"])]
colors = ['#ADD8E6', '#90EE90']  

fig = go.Figure(data=[go.Pie(labels=label, values=counts, marker=dict(colors=colors))])
fig.update_layout(title_text='Control Vs Test: Content Viewed', scene=dict(aspectratio=dict(x=1, y=1, z=1)))
fig.update_traces(hoverinfo='label+percent', textinfo='value+label', 
                  textfont_size=20, pull=[0.05, 0.05])
fig.show()


# The audience of the control campaign viewed more content than the test campaign. Although there is not much difference, as the website clicks of the control campaign were low, its engagement on the website is higher than the test campaign.

# In[16]:


#Now let’s have a look at the number of products added to the cart from both campaigns:
import plotly.graph_objects as go

label = ["Products Added to Cart from Control Campaign", 
         "Products Added to Cart from Test Campaign"]
counts = [sum(control_data["Added to Cart"]), 
          sum(test_data["Added to Cart"])]
colors = ['#ADD8E6', '#90EE90'] 

fig = go.Figure(data=[go.Pie(labels=label, values=counts, marker=dict(colors=colors))])
fig.update_layout(title_text='Control Vs Test: Added to Cart', scene=dict(aspectratio=dict(x=1, y=1, z=1)))
fig.update_traces(hoverinfo='label+percent', textinfo='value+label', 
                  textfont_size=20, pull=[0.05, 0.05])
fig.show()


# In[17]:


label = ["Amount Spent in Control Campaign", 
         "Amount Spent in Test Campaign"]
counts = [sum(control_data["Amount Spent"]), 
          sum(test_data["Amount Spent"])]
colors = ['#ADD8E6', '#90EE90'] 

fig = go.Figure(data=[go.Pie(labels=label, values=counts, marker=dict(colors=colors))])
fig.update_layout(title_text='Control Vs Test: Amount Spent', scene=dict(aspectratio=dict(x=1, y=1, z=1)))
fig.update_traces(hoverinfo='label+percent', textinfo='value+label', 
                  textfont_size=20, pull=[0.05, 0.05])
fig.show()


# In[26]:


#purchases made by both comapny
label = ["Purchases Made by Control Campaign", 
         "Purchases Made by Test Campaign"]
counts = [sum(control_data["Purchases"]), 
          sum(test_data["Purchases"])]
colors = ['#ADD8E6', '#90EE90']  

fig = go.Figure(data=[go.Pie(labels=label, values=counts, marker=dict(colors=colors))])
fig.update_layout(title_text='Control Vs Test: Purchases', scene=dict(aspectratio=dict(x=1, y=1, z=1)))
fig.update_traces(hoverinfo='percent', textinfo='value', 
                  textfont_size=20, pull=[0.05, 0.05])
fig.show()


# In[28]:


figure = px.scatter(data_frame=ab_data, 
                    x="Added to Cart",
                    y="Content Viewed", 
                    size="Added to Cart", 
                    color="Campaign Name", 
                    trendline="ols",
                    color_discrete_map={"neon blue": "blue", "Red": "red"})
figure.show()


# Again, the control campaign wins! Now let’s have a look at the relationship between the number of products added to the cart and the number of sales from both campaigns:

# In[29]:


figure = px.scatter(data_frame=ab_data, 
                    x="Purchases",
                    y="Added to Cart", 
                    size="Purchases", 
                    color="Campaign Name", 
                    trendline="ols",
                    color_discrete_map={"neon blue": "blue", "Red": "red"})
figure.show()


# Although the control campaign resulted in more sales and more products in the cart, the conversation rate of the test campaign is higher.

# ##   Conclusion

# From the above A/B tests, we found that the control campaign resulted in more sales and engagement from the visitors. More products were viewed from the control campaign, resulting in more products in the cart and more sales. But the conversation rate of products in the cart is higher in the test campaign. The test campaign resulted in more sales according to the products viewed and added to the cart. And the control campaign results in more sales overall. So, the Test campaign can be used to market a specific product to a specific audience, and the Control campaign can be used to market multiple products to a wider audience.
