import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import streamlit as st

# Define the bin size and start year
bin_size = st.slider('Bin Size', 2, 10, 3)
start_year = st.slider('Start Year', 1950, 2020, 1986)

df = pd.read_csv('combined_tables.csv')
df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
df = df.dropna(subset=['Year'])
df['Year'] = df['Year'].astype(int)
df = df[df['Year'] >= start_year]
df['Period'] = df['Year'].apply(lambda x: f"{(x // bin_size) * bin_size}-{(x // bin_size) * bin_size + bin_size - 1}")
df['PeriodMidpoint'] = df['Year'].apply(lambda x: (x // bin_size) * bin_size + bin_size // 2)
period_counts = df['PeriodMidpoint'].value_counts().sort_index()
period_counts_df = period_counts.reset_index()
period_counts_df.columns = ['PeriodMidpoint', 'Count']

# Create scatter plot using Plotly
fig = px.scatter(period_counts_df, x='PeriodMidpoint', y='Count', 
                 title='New Programming Languages over Time',)

# Fit a 2nd-order polynomial to the data
x = period_counts_df['PeriodMidpoint']
y = period_counts_df['Count']
coefficients = np.polyfit(x, y, 2)
poly_func = np.poly1d(coefficients)

# Generate values for the trendline
x_vals = np.linspace(min(x), max(x), 100)
y_vals = poly_func(x_vals)

# Add the trendline to the figure
fig.add_trace(go.Scatter(x=x_vals, y=y_vals, mode='lines', name='Trendline',
                         line=dict(color='grey', dash='dash'), opacity=0.6))

# Customize x-axis to show PeriodMidpoint as year ranges
fig.update_layout(
    xaxis_title="Year",
    xaxis_tickvals=period_counts_df['PeriodMidpoint'],
    xaxis_ticktext=[f"{int(midpoint - bin_size // 2)}-{int(midpoint + bin_size // 2 - 1)}" 
                    for midpoint in period_counts_df['PeriodMidpoint']]
)

# Display the plot using Streamlit
st.plotly_chart(fig, use_container_width=True)
st.caption('Data Source: Wikipedia Timeline of programming languages')