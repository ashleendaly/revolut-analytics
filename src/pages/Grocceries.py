import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df = st.session_state['df']

st.title('Grocery Spending Insights')

supermarkets = ['Tesco', 'Asda', 'Morrisons', 'Sainsbury', 'Waitrose', 'Aldi', 'Lidl', 'Iceland', 'Marks & Spencer', 'Superstore']

def groccery_data():
    df['Started Date'] = pd.to_datetime(df['Started Date'])
    filtered_df = df[df['Description'].str.contains('|'.join(supermarkets))]
    return filtered_df


df = groccery_data()

monthly_sum = df.groupby([pd.Grouper(key='Started Date', freq='M'), 'Description']).sum()['Amount'].abs()
st.write(monthly_sum)

total_monthly_sum = df.groupby(pd.Grouper(key='Started Date', freq='M')).sum()["Amount"].abs()
st.write(total_monthly_sum)

grouped_df = df.groupby(['Started Date', 'Description']).sum()['Amount'].abs()
pivoted_df = grouped_df.unstack('Description')

st.write(pivoted_df)

fig, ax = plt.subplots()
pivoted_df.plot(kind='bar', stacked=True, ax=ax)
ax.set_xlabel('Date')
ax.set_ylabel('Amount')
ax.set_title('Monthly Spending by Supermarket')

ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.xticks(rotation=45)

st.pyplot(fig)