
import streamlit
import pandas as pd

streamlit.title("New Healthy Diner")

streamlit.header("π²Breakfast Favorites")
streamlit.text("π₯ Omega 3 and Bluberry Oatmeal")
streamlit.text("π₯ Banana Pancakes")
streamlit.text("π₯ Hashbrown pancakes")
streamlit.text("π₯ Avacado Toast")

streamlit.header('ππ₯­ Build Your Own Fruit Smoothie π₯π')
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# streamlit.dataframe(my_fruit_list)

my_fruit_list = my_fruit_list.set_index('Fruit')

# Lets put a pick list here so they can pick the fruit they want to include
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

fruits_to_show = my_fruit_list.loc[fruits_selected]

# disply the table on the page
streamlit.dataframe(fruits_to_show)

