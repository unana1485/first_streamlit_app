
import streamlit
import pandas as pd

streamlit.title("New Healthy Diner")

streamlit.header("🍲Breakfast Favorites")
streamlit.text("🥞 Omega 3 and Bluberry Oatmeal")
streamlit.text("🥞 Banana Pancakes")
streamlit.text("🥚 Hashbrown pancakes")
streamlit.text("🥑 Avacado Toast")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# streamlit.dataframe(my_fruit_list)

my_fruit_list = my_fruit_list.set_index('Fruit')

# Lets put a pick list here so they can pick the fruit they want to include
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

# disply the table on the page
streamlit.dataframe(my_fruit_list)

