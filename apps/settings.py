import streamlit as st
import sqlite3


def app():
    st.title("Settings")       
    
    #Connect to Main Database 
    mainDB = sqlite3.connect('mainDB')
    #Create cursor to interact with Database
    mainDBcursor = mainDB.cursor()
    
    #Get all Sub Agents Listed within Sub Agents Table
    mainDBcursor.execute("select * from subagents")
    result = mainDBcursor.fetchall();
    
    
    #Form to add New Sub Agents to Database
    with st.form("addSubAgent", clear_on_submit=True):
        st.subheader('Add Sub Agent')
        newAgencyName = st.text_input("Add Agency Name", "", placeholder="Agency Name")
        newAgencyTier = st.text_input("Add Agency Tier", "", placeholder="Base")
        newRocketCode = st.text_input("Add Rocket Code", "", placeholder="RocketCode000")
        newAonCode = st.text_input("Add Aon Code", "", placeholder="0000")
        newBeyondCode = st.text_input("Add Beyond Code", "", placeholder="000000")
        newNeptuneCode = st.text_input("Add Neptune Code", "", placeholder="FL0000")
        newPalomarCode = st.text_input("Add Palomar Code", "", placeholder="PSIC-0000-0")
        newSterlingCode = st.text_input("Add Sterling Code", "", placeholder="00000")
        newWrightCode = st.text_input("Add Wright Code", "", placeholder='000000')
        
        submitted = st.form_submit_button("Submit")
        
        #When submitted add New Agent to Database
        if submitted:
            #Insert New Sub Agent into DataBase
            mainDBcursor.execute("insert into subagents(agency_name, tier, rocket_code, aon_code, beyond_code, neptune_code, palomar_code, sterling_code, wright_code) values(?, ?, ?, ?, ?, ?, ?, ?, ?)", (newAgencyName, newAgencyTier, newRocketCode, int(newAonCode), int(newBeyondCode), newNeptuneCode, newPalomarCode, int(newSterlingCode), int(newWrightCode)))
            #Alert box that new agent was added to DataBase
            st.success("Successfully added new Sub Agent!")
    
    #Save Changes made to Database        
    mainDB.commit()
