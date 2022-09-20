# Note all lines without starting # is a part of running code: 

import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError


streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Menu')

streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')

streamlit.text('🥗  Kale , Spinach & Bucket Smoothie')

streamlit.text('🐔 Hard-Boiled Free-Range Egg')

streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Choose the Fruit Name Column as the Index
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
# streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
# streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

# lets put a pick list here so they can pick the fruit they want to include
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
# streamlit.dataframe(my_fruit_list)
streamlit.dataframe(fruits_to_show)

# we need to bring in anotherPython Package liberary : This one is called request
# import requests
# but before this Adding
# New section to dispaly  fruitvice api response

streamlit.header('Fruitvice Fruit Advise!')

#  Add a Text Entry Box and Send the Input to Fruityvice as Part of the API Call

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
 
# Above is the latest renwed code 
----------------------------------------------------------------------------------

#    output it the screen as a table

#-----------------------------------------------------------------------------------------


# now getting package

#   import requests
#   fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#   streamlit.text(fruityvice_response.json())

# above code lines completed and ran suxccefully  so  commenting out so that it would not run with the subsequent code   

# Let's Get the Fruityvice Data Looking a Little Nicer
#    import requests
#    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#    streamlit.text(fruityvice_response.json())  # just write the data to  the screen

# take the jason version of the respinse and normalize it 
#    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#    output it the screen as a table
#    streamlit.dataframe(fruityvice_normalized)

# above code lines completed and ran suxccefully  so  commenting out so that it would not run with the subsequent code   


# Let's removed the line of raw JSON, and separate the base URL from the fruit name (which will make it easier to use a variable there).
#   import requests
#   fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
# take the jason version of the respinse and normalize it 
#   fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output it the screen as a table
#   streamlit.dataframe(fruityvice_normalized)

# above code lines completed and ran suxccefully  so  commenting out so that it would not run with the subsequent code   


#  Add a Text Entry Box and Send the Input to Fruityvice as Part of the API Call

#  fruit_choice = streamlit.text_input('What fruit would you like information about?', 'Kiwi')
#  streamlit.write('The user entered', fruit_choice)

# import request
#   fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

#  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#    output it the screen as a table
#  streamlit.dataframe(fruityvice_normalized)
#
# Commenting out above 


#  -------------------------------------------------
# Put All the Import Commands Together, At the Top 
# ---------------------------------------------------




# don't run anything past here while we troubleshoot
streamlit.stop()


#   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#   my_cur = my_cnx.cursor()
#   my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
#   my_data_row = my_cur.fetchone()
#   streamlit.text("Hello from Snowflake:")
#   streamlit.text(my_data_row)

# above executed succefully .

# commenting out , so that can run the following code only 

# Let's Query Some Data, Instead

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")

# following line will fatch only one row
#  my_data_row = my_cur.fetchone()   

#  Lets get all the rows
my_data_rows = my_cur.fetchall()

# streamlit.text("The fruit load list contains:")
# replacing above line with following to make things look little nicer 
streamlit.header("The fruit load list contains:")

streamlit.dataframe(my_data_rows)

# above executed succefully .


#  Add a Second Text Entry Box: 
#  Allow the end user to add a fruite to  the list:

add_my_fruit = streamlit.text_input('What fruit would you like to add?', 'jackfruit')
streamlit.write('Thanks for adding', add_my_fruit)

# this will not work correctly , but jsu go with it for  now :
my_cur.execute("insert into fruit_load_list values ('from streamlit')")
