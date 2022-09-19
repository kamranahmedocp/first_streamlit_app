import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Menu')

streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')

streamlit.text('🥗  Kale , Spinach & Bucket Smoothie')

streamlit.text('🐔 Hard-Boiled Free-Range Egg')

streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas

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

# but before this Adding New section to dispaly  fruitvice api response
streamlit.header('Fruitvice Fruit Advise!')

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
#    import requests
#    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
# take the jason version of the respinse and normalize it 
#    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output it the screen as a table
#    streamlit.dataframe(fruityvice_normalized)

# above code lines completed and ran suxccefully  so  commenting out so that it would not run with the subsequent code   


#  Add a Text Entry Box and Send the Input to Fruityvice as Part of the API Call


import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
# take the jason version of the respinse and normalize it 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output it the screen as a table
streamlit.dataframe(fruityvice_normalized)









