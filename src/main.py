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

