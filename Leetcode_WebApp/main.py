import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from recommender_system import recommender_system
from analytics import *
from pathlib import Path

current_directory = Path(__file__).resolve().parent
csv_file_path = current_directory / "preprocessed_data.csv"

def main_page():
    st.title('LeetCode: Navigator and Recommender System')
    st.write('Please select an option from the sidebar to get started.')
    
def recommender_system_ui():
    st.title('Hybrid Recommender System')
    problem_id = st.number_input('Enter a Problem ID:', min_value=1, value=1, step=1)
    results_df = recommender_system(problem_id) 

    def get_difficulty_color(difficulty):
        if difficulty == 'Easy':
            return '#4CAF50'  # Green
        elif difficulty == 'Medium':
            return '#FF9800'  # Orange
        else:
            return '#F44336'  # Red

    if not results_df.empty:
        for index, row in results_df.iterrows():
            difficulty_color = get_difficulty_color(row['difficulty'])
            card_html = f'''
            <div style="border-radius: 10px; padding: 20px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); margin-bottom: 20px;">
                <h2 style="color: {difficulty_color}; font-size: 20px;">{row['title']}</h2>
                <p style="margin-top: -10px; margin-bottom: 10px;">Difficulty: <span style="color: {difficulty_color}; font-weight: bold;">{row['difficulty']}</span></p>
                <p style="margin-top: -10px; margin-bottom: 10px;">Topic Tags: {row['topic_tags']}</p>
                <a href="{row['problem_URL']}" target="_blank" style="text-decoration: none; color: #0078ff; font-size: 14px;">View Problem</a>
            </div>
            '''
            st.markdown(card_html, unsafe_allow_html=True)
    else:
        st.write("No recommendations found.")


def analytics_ui():
    st.title('LeetCode Analytics Dashboard')
    df = pd.read_csv(csv_file_path)

    # Select box options
    options = ['All', 'Premium Status Pie Chart', 'Difficulty Pie Chart',
               'Top Tags Distribution', 'Premium Distribution', 
               'Acceptance Rate Box', 'Topic Tag Comparison']
    
    # User selection
    selected_option = st.selectbox('Select Plot', options)

    if selected_option == 'All':
        st.subheader('LeetCode Problem Premium Status')
        plot_premium_status_pie_chart(df)
        st.subheader('LeetCode Difficulty Level')
        plot_difficulty_pie_chart(df)
        st.subheader('Top 10 Most Common Individual Topic Tags Distribution')
        plot_top_tags_distribution(df)
        st.subheader('Distribution of Difficulty Level in Premium & Not Premium')
        plot_premium_distribution(df)
        st.subheader('Acceptance Rate Across Difficulty Levels')
        plot_acceptance_rate_box(df)
        st.subheader('Comparison of Top Topic Tags Across Difficulty Levels')
        plot_topic_tag_comparison(df)
    elif selected_option == 'Premium Status Pie Chart':
        st.subheader('LeetCode Problem Premium Status')
        plot_premium_status_pie_chart(df)
    elif selected_option == 'Difficulty Pie Chart':
        st.subheader('LeetCode Difficulty Level')
        plot_difficulty_pie_chart(df)
    elif selected_option == 'Top Tags Distribution':
        st.subheader('Top 10 Most Common Individual Topic Tags Distribution')
        plot_top_tags_distribution(df)
    elif selected_option == 'Premium Distribution':
        st.subheader('Distribution of Difficulty Level in Premium & Not Premium')
        plot_premium_distribution(df)
    elif selected_option == 'Acceptance Rate Box':
        st.subheader('Acceptance Rate Across Difficulty Levels')
        plot_acceptance_rate_box(df)
    elif selected_option == 'Topic Tag Comparison':
        st.subheader('Comparison of Top Topic Tags Across Difficulty Levels')
        plot_topic_tag_comparison(df)

# Sidebar navigation
st.sidebar.title('Navigation')
option = st.sidebar.radio('Go to', ('Home', 'Recommender System', 'Analytics'))

if option == 'Home':
    main_page()
elif option == 'Recommender System':
    recommender_system_ui()
elif option == 'Analytics':
    analytics_ui()
