
#import sys
#sys.path.append('C:/Users/adith/Documents/ipl_app/team_app/bowling')


import streamlit as st

import pickle
from bowler1 import Bowler
import numpy as np
import pandas as pd



with open('bowling1.pkl', 'rb') as f:
    bow = pickle.load(f)


#result1=bow.calculateb('TA Boult',[1,2,3],["RHB"],[2023])
#print(result1['wickets'])

def main():
    # Title of the app
    st.title("IPL: Team Bowling Stats")
    # Input for PlayerName
    player_names = bow.players
    # Input for PlayerName (dropdown)
   
    player_name = st.selectbox("Select Team Name", player_names)
    phases = st.multiselect("Select Phases ", ["Powerplay", "Middle1","Middle2","Slog"])
    # Input for Bowling type (dropdown)
    batting_type = st.multiselect("Select Batting Type(s)", ["LHB", "RHB"])
    # Input for Season (slider)
    start_year = 2016
    end_year = 2023
    selected_years = st.slider("Select Seasons", start_year, end_year, (start_year, end_year))
    ph1={'Powerplay':1,'Middle1':2,'Middle2':3,'Slog':4}
    
    overs=[ph1[phases[i]] for i in range(len(phases))]
    batting_type=[batting_type[i] for i in range(len(batting_type))]
    Season=[i for i in range(selected_years[0],selected_years[1]+1)]
    
    
    # Display the selected inputs
    
    if st.button('Submit'):
        
        
        #st.write("Selected Player Name:", player_name)
        #st.write("Selected Bowling Type:", type(bowling_type[0]))  # Corrected indentation
        #st.write("Selected Phases:", len(phases))          
        #st.write("Selected Seasons:", selected_years[0], "to", selected_years[1])
        result1=bow.calculateb(player_name,overs,batting_type,Season)
        result2=bow.overall()
        result3=bow.combined()

        st.write("Overall (All phases and batting types ):")
        st.dataframe(result2)
        
        st.write("Combined (Given phases and bowling types ):")
        st.dataframe(result3)
        
        
        st.write("Phase wise breakdown:")
        st.dataframe(result1)
        
    
    
if __name__=='__main__':
    main()
