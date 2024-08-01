#Import required libraries
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio

pio.templates.default = "plotly_white"

#Read the dataset
data = pd.read_csv("../data/customer_acquisition_data.csv")
print(data.head())

#Exploratory Data Analysis

#Distribution of Acquisition cost
fig = px.histogram(data, x = "cost", nbins = 20,
                   labels={"cost": "Acquisition cost"}, title = "Distribution of Acquisition cost")

fig.show()

fig.write_image("../output/distribution_of_acquisition_cost.png")

#Distribution of Revenue
fig = px.histogram(data, x = "revenue", nbins = 20,
                   labels={"revenue": "Revenue"}, title = "Distribution of Revenue")

fig.show()

fig.write_image("../output/distribution_of_revenue.png")

#COMMENT: From both the distribution plots, we can observe that for 75% of customers, the customer acquisition cost (CAC) is under 10 units while for the remaining customers, the CAC was over 30 units.
# The revenue range 3500-3999 has the highest number of occurrences (110) suggesting most common revenue range and the range 500-999 and 4000-4499 have the lowest number of occurrences (72).
# The revenue ranges with higher frequencies (e.g., 1000-1499, 3500-3999) suggest that revenue is distributed somewhat centered around these ranges. However, there is no clear peak in the middle range.
# To increase revenue, the middle revenue ranges should be focused as those are more common and can help target marketing and sales strategies effectively.
# The lower and higher extremes might be areas to explore further to understand why they are less frequent.

#Most and Least profitable channels
cost_by_channel = data.groupby('channel')['cost'].mean().reset_index()

fig = px.bar(cost_by_channel,
            x = "channel",
            y = "cost",
            title = "Customer Acquisition Cost by Channel",
            labels = {"cost": "Acquisition cost", "channel": "Channel"})

fig.show()

fig.write_image("../output/customer_acquistion_cost_by_channel.png")

#COMMENT: Email Marketing has the lowest CAC at 5.25 (the most cost-effective channel for acquiring customers).
# Paid Advertising has the highest CAC at 30.45 (the most expensive channel for acquiring customers).
# If the organization's goal is to minimize CAC, more budget should be allocated to email marketing.
# However, if the budget is not a problem, strategies should be reassesed to reduce the high CAC for paid advertising.
# Because the email marketing is driving significant customer acquisition at a low cost, it could be a key area to expand.
# Evaluate Referral and Social Media channels to assess their performance and determine if their CAC can be reduced or if they offer any other strategic benefits.

#Most and Least effective channel at converting customers
conversion_by_channel = data.groupby('channel')['conversion_rate'].mean().reset_index()

fig = px.bar(conversion_by_channel,
            x = "channel",
            y = "conversion_rate",
            title = "Conversion Rate by Channel",
            labels = {"conversion_rate": "Conversion rate", "channel": "Channel"})

fig.show()

fig.write_image("../output/conversion_rate_by_channel.png")

#COMMENT: Highest to Lowest conversion rates channels are:
# Social Media (16.76%) > Referral (12.31%) > Email Marketing (4.38%) >Paid Advertising (1.63%)
# While the conversion rate for email marketing might be lower than referral and social media conversion rate, it is still moderately effective in the overall marketing strategy.
# The lowest conversion rate for Paid Advertising indicates that although it may attract a large number of leads, only few of these convert into customers.
# It is beneficial to invest more in referral programs and social media campaigns to further improve conversion rates.
# The conversion rate of email marketing can be improved by personalized content, better segmentation, and targeted campaigns.
# There is a need to reassess paid advertising strategy to improve its effectiveness.