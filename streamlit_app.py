import streamlit
import pandas

streamlit.title('My parents new healthy dinner')

streamlit.header('Breakfast Menu')

streamlit.text('🥣 Omega 3 & Bluberry oatmeal')

streamlit.text('🥗 Kale, Spinach & Rocket Smootie')

streamlit.text('🐔 Hard-Boiled Free-Range Egg')

streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruits_list = pandas.read.csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streatlit.dataframe(my_fruits_list)
