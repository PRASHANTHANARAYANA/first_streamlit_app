#import streamlit 

import streamlit 
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
import snowflake.connector

streamlit.header('Fruityvice Fruit Advice!')
try:
    fruit_choice = streamlit.text_input('What fruit would you like information about?')
    if not fruit_choice:
        streamlit.error("Please select a fruit to get information.")
    else:
        fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
        fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
        streamlit.dataframe(fruityvice_normalized)

except URLError as e:
        streamlit.error()




streamlit.stop()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("Select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.text("The fruit load contains:")
streamlit.dataframe(my_data_rows)

add_my_fruit=streamlit.text_input('What fruit would you like to add?','jackfruit')
streamlit.write('Thanks for adding ', add_my_fruit)

my_cur.execute("insert into FRUIT_LOAD_LIST values ('from streamlit')")

add_my_fruit=streamlit.text_input('What fruit would you like to add?','Orange')
streamlit.write('Thanks for adding ', add_my_fruit)
