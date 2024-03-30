import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

def plot_premium_status_pie_chart(df):
    # Generate your Plotly figure
    fig = go.Figure(
        data=[
            go.Pie(
                labels=['Non-Premium', 'Premium'],
                values=df['is_premium'].value_counts().values.tolist(),
                insidetextfont=dict(color='black', size=18, family='Arial'),
            )
        ]
    )

    # Customize the layout of the figure
    fig.update_layout(
        title_text='LeetCode Problem Premium Status',
        title_font=dict(size=20, family='Arial', color='black'),
        title_x=0.25
    )

    # Further customize the traces
    fig.update_traces(
        textinfo='percent+label',
        hoverinfo='label+percent',
        textfont_size=15,
        pull=[0.1, 0],
        marker=dict(colors=['gold', 'mediumturquoise'], line=dict(color='#000000', width=2))
    )

    # Display the figure using Streamlit
    st.plotly_chart(fig)

def plot_difficulty_pie_chart(df):
    fig = go.Figure(
        data=[
            go.Pie(
                labels=df['difficulty'].value_counts().index.tolist(),
                values=df['difficulty'].value_counts().values.tolist(),
                insidetextfont=dict(color='black', size=18, family='Arial'),
            )
        ]
    )

    fig.update_layout(
        title_text='LeetCode Difficulty Level',
        title_font=dict(size=20, family='Arial', color='black'),
        title_x=0.33,
    )

    fig.update_traces(
        textinfo='percent+label',
        hoverinfo='label+percent',
        textfont_size=15,
        marker=dict(colors=['#FFD700', '#00CED1', '#FF8C00'], line=dict(color='#000000', width=2))
    )

    st.plotly_chart(fig)

def plot_top_tags_distribution(df):
    tag_counts = df['topic_tags'].str.split(', ').explode().value_counts(ascending=True)[-10:]
    tag_counts = tag_counts.reset_index()

    fig = px.bar(tag_counts, x='count', y='topic_tags',
                 orientation='h',
                 title='Top 10 Most Common Individual Topic Tags Distribution',
                 text_auto='.s'
    )

    fig.update_layout(
        title_text='Top 10 Most Common Individual Topic Tags Distribution',
        title_font=dict(size=20, family='Arial', color='black'),
        title_x=0.22,
        xaxis_title='Frequency',
        yaxis_title='Topic Tag',
    )

    fig.update_traces(marker_color='#FF8C00', marker_line_color='black',
                      marker_line_width=1, opacity=0.8)

    st.plotly_chart(fig)

def plot_premium_distribution(df):
    # Grouping and counting for Premium=True
    premium_true_data = df[df['is_premium'] == True].groupby('difficulty').size()

    # Grouping and counting for Premium=False
    premium_false_data = df[df['is_premium'] == False].groupby('difficulty').size()

    # Plotting side-by-side pie charts with hole
    fig = go.Figure()

    fig.add_trace(go.Pie(
        labels=premium_true_data.index,
        values=premium_true_data.values,
        domain=dict(x=[0, 0.45]),
        hole=0.4,
        insidetextfont=dict(color='black', size=18, family='Arial'),
    ))

    fig.add_trace(go.Pie(
        labels=premium_false_data.index,
        values=premium_false_data.values,
        domain=dict(x=[0.55, 1]),
        hole=0.4,
        name='Not Premium',
        insidetextfont=dict(color='black', size=18, family='Arial'),
    ))

    fig.update_traces(
        textinfo='percent+label',
        hoverinfo='label+percent',
        textfont_size=15,
        marker=dict(colors=['#FFD700', '#00CED1', '#FF8C00'], line=dict(color='#000000', width=2))
    )

    fig.update_layout(
        title_text='Distribution of Difficulty Level in Premium & Not Premium',
        title_font=dict(size=20, family='Arial', color='black'),
        title_x=0.22,
        annotations=[dict(text='Premium', x=0.169, y=0.5, font_size=18, showarrow=False, ),
                     dict(text='Not Premium', x=0.86, y=0.5, font_size=18, showarrow=False)],
        legend_title_text='Difficulty Level'
    )

    st.plotly_chart(fig)

def plot_acceptance_rate_box(df):
    # Assuming you have easy_data, medium_data, and hard_data defined
    easy_data = df[df['difficulty'] == 'Easy']['acceptance'].dropna()
    medium_data = df[df['difficulty'] == 'Medium']['acceptance'].dropna()
    hard_data = df[df['difficulty'] == 'Hard']['acceptance'].dropna()

    box_data = [easy_data, medium_data, hard_data]
    box_labels = ['Easy', 'Medium', 'Hard']
    colors = ['green', 'gold', 'red']

    fig = go.Figure()

    for i in range(len(box_data)):
        fig.add_trace(go.Box(y=box_data[i], name=box_labels[i], marker_color=colors[i]))

    fig.update_layout(
        title_text='Acceptance Rate Across Difficulty Levels',
        title_font=dict(size=20, family='Arial', color='black'),
        title_x=0.45,
        xaxis_title='Difficulty Level',
        yaxis_title='Acceptance Rate',
        legend_title_text='Difficulty Level'
    )

    st.plotly_chart(fig)

def plot_topic_tag_comparison(df):
    # Define the topic tags to compare
    topic_tags = ['Array', 'String', 'Hash Table', 'Dynamic Programming', 'Math', 'Sorting', 'Binary Search']

    # Initialize dictionaries to store counts for each difficulty level
    easy_counts = {}
    medium_counts = {}
    hard_counts = {}

    # Count occurrences of each tag for each difficulty level
    for tag in topic_tags:
        easy_counts[tag] = len(df[(df['difficulty'] == 'Easy') & (df['topic_tags'].str.contains(tag))])
        medium_counts[tag] = len(df[(df['difficulty'] == 'Medium') & (df['topic_tags'].str.contains(tag))])
        hard_counts[tag] = len(df[(df['difficulty'] == 'Hard') & (df['topic_tags'].str.contains(tag))])

    # Create a DataFrame for bar chart
    tag_comparison = pd.DataFrame({
        'Topic Tag': topic_tags,
        'Easy': list(easy_counts.values()),
        'Medium': list(medium_counts.values()),
        'Hard': list(hard_counts.values())
    })

    # Melt the DataFrame for easier plotting
    tag_comparison_melted = tag_comparison.melt(id_vars='Topic Tag', var_name='Difficulty', value_name='Count')

    # Plotting with specified colors
    fig = px.bar(tag_comparison_melted, y='Count', x='Topic Tag', color='Difficulty',
                 orientation='v', barmode='group',
                 title='Comparison of Top Topic Tags Across Difficulty Levels',
                 labels={'Count': 'Frequency', 'Topic Tag': 'Topic Tag'},
                 color_discrete_map={'Easy': 'green', 'Medium': 'gold', 'Hard': 'red'})

    fig.update_layout(
        title_font=dict(size=20, family='Arial', color='black'),
        title_x=0.45,
        yaxis_title='Frequency',
        xaxis_title='Topic Tag',
    )

    fig.update_traces(marker_line_color='black', marker_line_width=1, opacity=0.8)

    st.plotly_chart(fig)
