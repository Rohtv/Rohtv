
from pymongo.mongo_client import MongoClient
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Reminder App", page_icon=":bell:", layout="centered")


uri = st.secrets["MONGO_CONNECTION_STRING"]

# create a new client and connect to the server
client = MongoClient(uri)

try:
    client.admin.command('ping')
    print ("Pinged your deployment.you succesfully connected to MongoDB !")
except Exception as e:
    print (e)


db = client['powers']
col = db['ability']

def signupPage():
     st.title("signup")
     username = st.text_input("Username", key="svusername")
     password = st.text_input("Password", type="password", key="password")
     a= st.number_input("Age", min_value=18, max_value=100, step=1, key="age")
     p = st.number_input("Phone", min_value=91, max_value=9999999999, key="phone")
     m= st.text_input("Email", key="mail")  

    
     newdetails = {
            "username": username,
            "password": password,
            "age": a,
            "phone": p,
            "mail": m
     }
          
     
     if st.button("Signup"):
         if username in col.distinct("username"):
             st.error("Username already exists")
         else:
             col.insert_one(newdetails)
             st.success("Successfully registered! You may now Login with your credentials")

            
def loginPage():
     st.title("login")
     username = st.text_input("Username", key="lvusername")
     email = st.text_input("Email", key="svemail")
     password = st.text_input("Password", type="password", key="lvpassword")
     if st.button("Login"):
         if username in col.distinct("username"):
             if password in col.distinct("password"):
                 st.success("Logged in as {}".format(username))
                 st.balloons()  
             else:
                 st.error("Incorrect username or password")
         else:
             st.error("Incorrect username or password")



def main():

    with st.sidebar:
        selected = option_menu(None, ["Login", "SignUp"])

    if selected == "Login":
        loginPage()
    elif selected == "SignUp":
        signupPage()


if __name__ == "__main__":
    main() 
