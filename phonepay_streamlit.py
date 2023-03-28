#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from sqlalchemy import create_engine
import pandas as pd
import json
from PIL import Image
import streamlit as st
import pymysql
import sqlalchemy
import plotly.express as px
import plotly.graph_objects as go


st.set_page_config(page_title='PhonePay India Dashboards', layout='wide')
image=Image.open("C:/Users/shakt/OneDrive/Desktop/Phonepay/phone-pay-image.jpg")
st.title('&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;**PhonePay India Dashboard**')
st.image(image)



dash=st.button('PhonePay Dashboard')
if dash:
    st.sidebar.header('**INDIA**')
    add_selectbox = st.sidebar.selectbox(
        "**Select an option**",
        ("user","transaction",)
    )

    col1,col2=st.sidebar.columns(2)

    if add_selectbox=='user' or 'transaction':
        with col1:
            year=st.selectbox('**Select an option**',(2018,2019,2020,2021,2022))
            if year==2018:
                quarter=st.selectbox('Select an option',('Q1(Jan-March)','Q2(Apr-June)','Q3(July-Sep)','Q4(Oct-Dec)'))
            elif year==2019:
                quarter=st.selectbox('Select an option',('Q1(Jan-March)','Q2(Apr-June)','Q3(July-Sep)','Q4(Oct-Dec)'))
            elif year==2020:
                quarter=st.selectbox('Select an option',('Q1(Jan-March)','Q2(Apr-June)','Q3(July-Sep)','Q4(Oct-Dec)'))
            elif year==2021:
                quarter=st.selectbox('Select an option',('Q1(Jan-March)','Q2(Apr-June)','Q3(July-Sep)','Q4(Oct-Dec)'))
            elif year==2022:
                quarter=st.selectbox('Select an option',('Q1(Jan-March)','Q2(Apr-June)','Q3(July-Sep)','Q4(Oct-Dec)'))

    types=st.sidebar.selectbox("**Select an option**",('Aggregation','Top_list'))

    #***************************************************************************************************************************
    host='localhost'
    user='root'
    password='365616'
    port=3306
    database='phonepay'

    engine =sqlalchemy.create_engine(f"mysql://{user}:{password}@{host}:{port}/{database}")
    connection=engine.connect()

    table_name = "aggregated_transaction"
    df_agg_trans = pd.read_sql_table(table_name, connection)

    table_name = "aggregated_users"
    df_agg_users = pd.read_sql_table(table_name, connection)

    table_name = "map_transactions"
    df_map_trans = pd.read_sql_table(table_name, connection)

    table_name = "map_users"
    df_map_users = pd.read_sql_table(table_name, connection)


    table_name = "top_transactions"
    df_top_trans = pd.read_sql_table(table_name, connection)

    table_name = "top_users"
    df_top_users = pd.read_sql_table(table_name, connection)



    #*************************************************************************************************************************

    if add_selectbox == 'user':
        if year == 2018:
            if quarter == 'Q1(Jan-March)':
                if types == 'Aggregation':
                    filtered_df = df_agg_users[(df_agg_users['Year'] == 2018) & (df_agg_users['Quarter'] == 1)]


                    fig1=px.bar(filtered_df,x='Device_Brands',y='Counts',hover_name='State',color='State',range_y=(0,13000000))
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='Device_Brands',values='Counts')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['State','Device_Brands'],values='Counts',color='State')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)


                elif types == 'Top_list':
                    col,col1=st.columns(2)
                    with col:
                        tts=st.button('Top 10 State')
                        if tts:
                            filtered_df = df_top_users[(df_top_users['Year'] == 2018) & (df_top_users['Quarter'] == 1)]
                            state_counts=filtered_df.groupby('State').agg({'Registered_user':'sum'})
                            sorted_counts=state_counts.sort_values('Registered_user',ascending=False)
                            top_ten_states=sorted_counts.head(10)
                            st.dataframe(top_ten_states)

                            fig = px.bar(top_ten_states, x=top_ten_states.index, y='Registered_user', labels={'x':'State', 'Registered_user':'Registered Users'})
                            st.plotly_chart(fig)

                            fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='Registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)
                    with col1:
                        ttp=st.button('Top 10 Pincodes')
                        if ttp:
                            filtered_df = df_top_users[(df_top_users['Year'] == 2018) & (df_top_users['Quarter'] == 1)]
                            pin_counts=filtered_df.groupby('Pincode').agg({'Registered_user':'sum'})
                            sort_counts=pin_counts.sort_values('Registered_user',ascending=False)
                            top_ten_pin=sort_counts.head(10)
                            st.dataframe(top_ten_pin)


                            fig1 = px.pie(top_ten_pin, names=top_ten_pin.index, values='Registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)

                            fig2=go.Figure(go.Pie(labels=top_ten_pin.index,values=top_ten_pin['Registered_user'],hole=0.5))
                            st.plotly_chart(fig2)


            elif quarter == 'Q2(Apr-June)':
                if types == 'Aggregation':
                    filtered_df = df_agg_users[(df_agg_users['Year'] == 2018) & (df_agg_users['Quarter'] == 2)]


                    fig1=px.bar(filtered_df,x='Device_Brands',y='Counts',hover_name='State',color='State',range_y=(0,13000000))
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='Device_Brands',values='Counts')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['State','Device_Brands'],values='Counts',color='State')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                elif types == 'Top_list':
                    col,col1=st.columns(2)
                    with col:
                        tts=st.button('Top 10 State')
                        if tts:
                            filtered_df = df_top_users[(df_top_users['Year'] == 2018) & (df_top_users['Quarter'] == 2)]
                            state_counts=filtered_df.groupby('State').agg({'Registered_user':'sum'})
                            sorted_counts=state_counts.sort_values('Registered_user',ascending=False)
                            top_ten_states=sorted_counts.head(10)
                            st.dataframe(top_ten_states)

                            fig = px.bar(top_ten_states, x=top_ten_states.index, y='Registered_user', labels={'x':'State', 'Registered_user':'Registered Users'})
                            st.plotly_chart(fig)

                            fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='Registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)
                    with col1:
                        ttp=st.button('Top 10 Pincodes')
                        if ttp:
                            filtered_df = df_top_users[(df_top_users['Year'] == 2018) & (df_top_users['Quarter'] == 2)]
                            pin_counts=filtered_df.groupby('Pincode').agg({'Registered_user':'sum'})
                            sort_counts=pin_counts.sort_values('Registered_user',ascending=False)
                            top_ten_pin=sort_counts.head(10)
                            st.dataframe(top_ten_pin)


                            fig1 = px.pie(top_ten_pin, names=top_ten_pin.index, values='Registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)

                            fig2=go.Figure(go.Pie(labels=top_ten_pin.index,values=top_ten_pin['Registered_user'],hole=0.5))
                            st.plotly_chart(fig2)


            elif quarter == 'Q3(July-Sep)':
                if types == 'Aggregation':
                    filtered_df = df_agg_users[(df_agg_users['Year'] == 2018) & (df_agg_users['Quarter'] == 3)]


                    fig1=px.bar(filtered_df,x='Device_Brands',y='Counts',hover_name='State',color='State',range_y=(0,13000000))
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)

                    fig3 = px.pie(filtered_df,names='Device_Brands',values='Counts')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['State','Device_Brands'],values='Counts',color='State')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)
                    st.write('Output for user, year=2018, quarter=Q2, and type=Aggregation')
                elif types == 'Top_list':
                    col,col1=st.columns(2)
                    with col:
                        tts=st.button('Top 10 State')
                        if tts:
                            filtered_df = df_top_users[(df_top_users['Year'] == 2018) & (df_top_users['Quarter'] == 3)]
                            state_counts=filtered_df.groupby('State').agg({'Registered_user':'sum'})
                            sorted_counts=state_counts.sort_values('Registered_user',ascending=False)
                            top_ten_states=sorted_counts.head(10)
                            st.dataframe(top_ten_states)

                            fig = px.bar(top_ten_states, x=top_ten_states.index, y='Registered_user', labels={'x':'State', 'Registered_user':'Registered Users'})
                            st.plotly_chart(fig)

                            fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='Registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)
                    with col1:
                        ttp=st.button('Top 10 Pincodes')
                        if ttp:
                            filtered_df = df_top_users[(df_top_users['Year'] == 2018) & (df_top_users['Quarter'] == 3)]
                            pin_counts=filtered_df.groupby('Pincode').agg({'Registered_user':'sum'})
                            sort_counts=pin_counts.sort_values('Registered_user',ascending=False)
                            top_ten_pin=sort_counts.head(10)
                            st.dataframe(top_ten_pin)


                            fig1 = px.pie(top_ten_pin, names=top_ten_pin.index, values='Registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)

                            fig2=go.Figure(go.Pie(labels=top_ten_pin.index,values=top_ten_pin['Registered_user'],hole=0.5))
                            st.plotly_chart(fig2)

            elif quarter == 'Q4(Oct-Dec)':
                if types == 'Aggregation':
                    filtered_df = df_agg_users[(df_agg_users['Year'] == 2018) & (df_agg_users['Quarter'] == 4)]


                    fig1=px.bar(filtered_df,x='Device_Brands',y='Counts',hover_name='State',color='State',range_y=(0,13000000))
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='Device_Brands',values='Counts')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['State','Device_Brands'],values='Counts',color='State')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                elif types == 'Top_list':
                    col,col1=st.columns(2)
                    with col:
                        tts=st.button('Top 10 State')
                        if tts:
                            filtered_df = df_top_users[(df_top_users['Year'] == 2018) & (df_top_users['Quarter'] == 4)]
                            state_counts=filtered_df.groupby('State').agg({'Registered_user':'sum'})
                            sorted_counts=state_counts.sort_values('Registered_user',ascending=False)
                            top_ten_states=sorted_counts.head(10)
                            st.dataframe(top_ten_states)

                            fig = px.bar(top_ten_states, x=top_ten_states.index, y='Registered_user', labels={'x':'State', 'Registered_user':'Registered Users'})
                            st.plotly_chart(fig)

                            fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='Registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)
                    with col1:
                        ttp=st.button('Top 10 Pincodes')
                        if ttp:
                            filtered_df = df_top_users[(df_top_users['Year'] == 2018) & (df_top_users['Quarter'] == 4)]
                            pin_counts=filtered_df.groupby('Pincode').agg({'Registered_user':'sum'})
                            sort_counts=pin_counts.sort_values('Registered_user',ascending=False)
                            top_ten_pin=sort_counts.head(10)
                            st.dataframe(top_ten_pin)


                            fig1 = px.pie(top_ten_pin, names=top_ten_pin.index, values='Registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)

                            fig2=go.Figure(go.Pie(labels=top_ten_pin.index,values=top_ten_pin['Registered_user'],hole=0.5))
                            st.plotly_chart(fig2)

        if year == 2019:
            if quarter == 'Q1(Jan-March)':
                if types == 'Aggregation':
                    filtered_df = df_agg_users[(df_agg_users['Year'] == 2019) & (df_agg_users['Quarter'] == 1)]


                    fig1=px.bar(filtered_df,x='Device_Brands',y='Counts',hover_name='State',color='State',range_y=(0,13000000))
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='Device_Brands',values='Counts')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['State','Device_Brands'],values='Counts',color='State')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                elif types == 'Top_list':
                    col,col1=st.columns(2)
                    with col:
                        tts=st.button('Top 10 State')
                        if tts:
                            filtered_df = df_top_users[(df_top_users['Year'] == 2019) & (df_top_users['Quarter'] == 1)]
                            state_counts=filtered_df.groupby('State').agg({'Registered_user':'sum'})
                            sorted_counts=state_counts.sort_values('Registered_user',ascending=False)
                            top_ten_states=sorted_counts.head(10)
                            st.dataframe(top_ten_states)

                            fig = px.bar(top_ten_states, x=top_ten_states.index, y='Registered_user', labels={'x':'State', 'Registered_user':'Registered Users'})
                            st.plotly_chart(fig)

                            fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='Registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)
                    with col1:
                        ttp=st.button('Top 10 Pincodes')
                        if ttp:
                            filtered_df = df_top_users[(df_top_users['Year'] == 2018) & (df_top_users['Quarter'] == 1)]
                            pin_counts=filtered_df.groupby('Pincode').agg({'Registered_user':'sum'})
                            sort_counts=pin_counts.sort_values('Registered_user',ascending=False)
                            top_ten_pin=sort_counts.head(10)
                            st.dataframe(top_ten_pin)


                            fig1 = px.pie(top_ten_pin, names=top_ten_pin.index, values='Registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)

                            fig2=go.Figure(go.Pie(labels=top_ten_pin.index,values=top_ten_pin['Registered_user'],hole=0.5))
                            st.plotly_chart(fig2)

            elif quarter == 'Q2(Apr-June)':
                if types == 'Aggregation':
                    filtered_df = df_agg_users[(df_agg_users['Year'] == 2019) & (df_agg_users['Quarter'] == 2)]


                    fig1=px.bar(filtered_df,x='Device_Brands',y='Counts',hover_name='State',color='State',range_y=(0,13000000))
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='Device_Brands',values='Counts')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['State','Device_Brands'],values='Counts',color='State')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)
                elif types == 'Top_list':
                    col,col1=st.columns(2)
                    with col:
                        tts=st.button('Top 10 State')
                        if tts:
                            filtered_df = df_top_users[(df_top_users['Year'] == 2019) & (df_top_users['Quarter'] == 2)]
                            state_counts=filtered_df.groupby('State').agg({'Registered_user':'sum'})
                            sorted_counts=state_counts.sort_values('Registered_user',ascending=False)
                            top_ten_states=sorted_counts.head(10)
                            st.dataframe(top_ten_states)

                            fig = px.bar(top_ten_states, x=top_ten_states.index, y='Registered_user', labels={'x':'State', 'Registered_user':'Registered Users'})
                            st.plotly_chart(fig)

                            fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='Registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)
                    with col1:
                        ttp=st.button('Top 10 Pincodes')
                        if ttp:
                            filtered_df = df_top_users[(df_top_users['Year'] == 2018) & (df_top_users['Quarter'] == 2)]
                            pin_counts=filtered_df.groupby('Pincode').agg({'Registered_user':'sum'})
                            sort_counts=pin_counts.sort_values('Registered_user',ascending=False)
                            top_ten_pin=sort_counts.head(10)
                            st.dataframe(top_ten_pin)


                            fig1 = px.pie(top_ten_pin, names=top_ten_pin.index, values='Registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)

                            fig2=go.Figure(go.Pie(labels=top_ten_pin.index,values=top_ten_pin['Registered_user'],hole=0.5))
                            st.plotly_chart(fig2)

            elif quarter == 'Q3(July-Sep)':
                if types == 'Aggregation':
                    filtered_df = df_agg_users[(df_agg_users['Year'] == 2019) & (df_agg_users['Quarter'] ==3)]


                    fig1=px.bar(filtered_df,x='Device_Brands',y='Counts',hover_name='State',color='State',range_y=(0,13000000))
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='Device_Brands',values='Counts')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['State','Device_Brands'],values='Counts',color='State')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)
                elif types == 'Top_list':
                    col,col1=st.columns(2)
                    with col:
                        tts=st.button('Top 10 State')
                        if tts:
                            filtered_df = df_top_users[(df_top_users['Year'] == 2019) & (df_top_users['Quarter'] == 3)]
                            state_counts=filtered_df.groupby('State').agg({'Registered_user':'sum'})
                            sorted_counts=state_counts.sort_values('Registered_user',ascending=False)
                            top_ten_states=sorted_counts.head(10)
                            st.dataframe(top_ten_states)

                            fig = px.bar(top_ten_states, x=top_ten_states.index, y='Registered_user', labels={'x':'State', 'Registered_user':'Registered Users'})
                            st.plotly_chart(fig)

                            fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='Registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)
                    with col1:
                        ttp=st.button('Top 10 Pincodes')
                        if ttp:
                            filtered_df = df_top_users[(df_top_users['Year'] == 2018) & (df_top_users['Quarter'] == 3)]
                            pin_counts=filtered_df.groupby('Pincode').agg({'Registered_user':'sum'})
                            sort_counts=pin_counts.sort_values('Registered_user',ascending=False)
                            top_ten_pin=sort_counts.head(10)
                            st.dataframe(top_ten_pin)


                            fig1 = px.pie(top_ten_pin, names=top_ten_pin.index, values='Registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)

                            fig2=go.Figure(go.Pie(labels=top_ten_pin.index,values=top_ten_pin['Registered_user'],hole=0.5))
                            st.plotly_chart(fig2)

            elif quarter == 'Q4(Oct-Dec)':
                if types == 'Aggregation':
                    filtered_df = df_agg_users[(df_agg_users['Year'] == 2019) & (df_agg_users['Quarter'] == 4)]


                    fig1=px.bar(filtered_df,x='Device_Brands',y='Counts',hover_name='State',color='State',range_y=(0,13000000))
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='Device_Brands',values='Counts')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['State','Device_Brands'],values='Counts',color='State')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)
                elif types == 'Top_list':
                    col,col1=st.columns(2)
                    with col:
                        tts=st.button('Top 10 State')
                        if tts:
                            filtered_df = df_top_users[(df_top_users['Year'] == 2019) & (df_top_users['Quarter'] == 4)]
                            state_counts=filtered_df.groupby('State').agg({'Registered_user':'sum'})
                            sorted_counts=state_counts.sort_values('Registered_user',ascending=False)
                            top_ten_states=sorted_counts.head(10)
                            st.dataframe(top_ten_states)

                            fig = px.bar(top_ten_states, x=top_ten_states.index, y='Registered_user', labels={'x':'State', 'Registered_user':'Registered Users'})
                            st.plotly_chart(fig)

                            fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='Registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)
                    with col1:
                        ttp=st.button('Top 10 Pincodes')
                        if ttp:
                            filtered_df = df_top_users[(df_top_users['Year'] == 2018) & (df_top_users['Quarter'] == 4)]
                            pin_counts=filtered_df.groupby('Pincode').agg({'Registered_user':'sum'})
                            sort_counts=pin_counts.sort_values('Registered_user',ascending=False)
                            top_ten_pin=sort_counts.head(10)
                            st.dataframe(top_ten_pin)


                            fig1 = px.pie(top_ten_pin, names=top_ten_pin.index, values='Registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)

                            fig2=go.Figure(go.Pie(labels=top_ten_pin.index,values=top_ten_pin['Registered_user'],hole=0.5))
                            st.plotly_chart(fig2)


        if year == 2020:
            if quarter == 'Q1(Jan-March)':
                if types == 'Aggregation':
                    filtered_df = df_agg_users[(df_agg_users['Year'] == 2020) & (df_agg_users['Quarter'] == 1)]


                    fig1=px.bar(filtered_df,x='Device_Brands',y='Counts',hover_name='State',color='State',range_y=(0,13000000))
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='Device_Brands',values='Counts')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['State','Device_Brands'],values='Counts',color='State')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                elif types == 'Top_list':
                    col,col1=st.columns(2)
                    with col:
                        tts=st.button('Top 10 State')
                        if tts:
                            filtered_df = df_top_users[(df_top_users['Year'] == 2020) & (df_top_users['Quarter'] == 1)]
                            state_counts=filtered_df.groupby('State').agg({'Registered_user':'sum'})
                            sorted_counts=state_counts.sort_values('Registered_user',ascending=False)
                            top_ten_states=sorted_counts.head(10)
                            st.dataframe(top_ten_states)

                            fig = px.bar(top_ten_states, x=top_ten_states.index, y='Registered_user', labels={'x':'State', 'Registered_user':'Registered Users'})
                            st.plotly_chart(fig)

                            fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='Registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)
                    with col1:
                        ttp=st.button('Top 10 Pincodes')
                        if ttp:
                            filtered_df = df_top_users[(df_top_users['Year'] == 2018) & (df_top_users['Quarter'] == 1)]
                            pin_counts=filtered_df.groupby('Pincode').agg({'Registered_user':'sum'})
                            sort_counts=pin_counts.sort_values('Registered_user',ascending=False)
                            top_ten_pin=sort_counts.head(10)
                            st.dataframe(top_ten_pin)


                            fig1 = px.pie(top_ten_pin, names=top_ten_pin.index, values='Registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)

                            fig2=go.Figure(go.Pie(labels=top_ten_pin.index,values=top_ten_pin['Registered_user'],hole=0.5))
                            st.plotly_chart(fig2)

            elif quarter == 'Q2(Apr-June)':
                if types == 'Aggregation':
                    filtered_df = df_agg_users[(df_agg_users['Year'] == 2020) & (df_agg_users['Quarter'] == 2)]

                    fig1=px.bar(filtered_df,x='Device_Brands',y='Counts',hover_name='State',color='State',range_y=(0,13000000))
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)

                    fig3 = px.pie(filtered_df,names='Device_Brands',values='Counts')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['State','Device_Brands'],values='Counts',color='State')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)
                elif types == 'Top_list':
                    col,col1=st.columns(2)
                    with col:
                        tts=st.button('Top 10 State')
                        if tts:
                            filtered_df = df_top_users[(df_top_users['Year'] == 2020) & (df_top_users['Quarter'] == 2)]
                            state_counts=filtered_df.groupby('State').agg({'Registered_user':'sum'})
                            sorted_counts=state_counts.sort_values('Registered_user',ascending=False)
                            top_ten_states=sorted_counts.head(10)
                            st.dataframe(top_ten_states)

                            fig = px.bar(top_ten_states, x=top_ten_states.index, y='Registered_user', labels={'x':'State', 'Registered_user':'Registered Users'})
                            st.plotly_chart(fig)

                            fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='Registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)
                    with col1:
                        ttp=st.button('Top 10 Pincodes')
                        if ttp:
                            filtered_df = df_top_users[(df_top_users['Year'] == 2018) & (df_top_users['Quarter'] == 2)]
                            pin_counts=filtered_df.groupby('Pincode').agg({'Registered_user':'sum'})
                            sort_counts=pin_counts.sort_values('Registered_user',ascending=False)
                            top_ten_pin=sort_counts.head(10)
                            st.dataframe(top_ten_pin)


                            fig1 = px.pie(top_ten_pin, names=top_ten_pin.index, values='Registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)

                            fig2=go.Figure(go.Pie(labels=top_ten_pin.index,values=top_ten_pin['Registered_user'],hole=0.5))
                            st.plotly_chart(fig2)

            elif quarter == 'Q3(July-Sep)':
                if types == 'Aggregation':
                    filtered_df = df_agg_users[(df_agg_users['Year'] == 2020) & (df_agg_users['Quarter'] == 3)]


                    fig1=px.bar(filtered_df,x='Device_Brands',y='Counts',hover_name='State',color='State',range_y=(0,13000000))
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='Device_Brands',values='Counts')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['State','Device_Brands'],values='Counts',color='State')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)
                elif types == 'Top_list':
                    col,col1=st.columns(2)
                    with col:
                        tts=st.button('Top 10 State')
                        if tts:
                            filtered_df = df_top_users[(df_top_users['Year'] == 2020) & (df_top_users['Quarter'] == 3)]
                            state_counts=filtered_df.groupby('State').agg({'Registered_user':'sum'})
                            sorted_counts=state_counts.sort_values('Registered_user',ascending=False)
                            top_ten_states=sorted_counts.head(10)
                            st.dataframe(top_ten_states)

                            fig = px.bar(top_ten_states, x=top_ten_states.index, y='Registered_user', labels={'x':'State', 'Registered_user':'Registered Users'})
                            st.plotly_chart(fig)

                            fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='Registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)
                    with col1:
                        ttp=st.button('Top 10 Pincodes')
                        if ttp:
                            filtered_df = df_top_users[(df_top_users['Year'] == 2018) & (df_top_users['Quarter'] == 3)]
                            pin_counts=filtered_df.groupby('Pincode').agg({'Registered_user':'sum'})
                            sort_counts=pin_counts.sort_values('Registered_user',ascending=False)
                            top_ten_pin=sort_counts.head(10)
                            st.dataframe(top_ten_pin)


                            fig1 = px.pie(top_ten_pin, names=top_ten_pin.index, values='Registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)

                            fig2=go.Figure(go.Pie(labels=top_ten_pin.index,values=top_ten_pin['Registered_user'],hole=0.5))
                            st.plotly_chart(fig2)

            elif quarter == 'Q4(Oct-Dec)':
                if types == 'Aggregation':
                    filtered_df = df_agg_users[(df_agg_users['Year'] == 2020) & (df_agg_users['Quarter'] == 4)]


                    fig1=px.bar(filtered_df,x='Device_Brands',y='Counts',hover_name='State',color='State',range_y=(0,13000000))
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='Device_Brands',values='Counts')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['State','Device_Brands'],values='Counts',color='State')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)
                elif types == 'Top_list':
                    col,col1=st.columns(2)
                    with col:
                        tts=st.button('Top 10 State')
                        if tts:
                            filtered_df = df_top_users[(df_top_users['Year'] == 2020) & (df_top_users['Quarter'] == 4)]
                            state_counts=filtered_df.groupby('State').agg({'Registered_user':'sum'})
                            sorted_counts=state_counts.sort_values('Registered_user',ascending=False)
                            top_ten_states=sorted_counts.head(10)
                            st.dataframe(top_ten_states)

                            fig = px.bar(top_ten_states, x=top_ten_states.index, y='Registered_user', labels={'x':'State', 'Registered_user':'Registered Users'})
                            st.plotly_chart(fig)

                            fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='Registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)
                    with col1:
                        ttp=st.button('Top 10 Pincodes')
                        if ttp:
                            filtered_df = df_top_users[(df_top_users['Year'] == 2018) & (df_top_users['Quarter'] == 4)]
                            pin_counts=filtered_df.groupby('Pincode').agg({'Registered_user':'sum'})
                            sort_counts=pin_counts.sort_values('Registered_user',ascending=False)
                            top_ten_pin=sort_counts.head(10)
                            st.dataframe(top_ten_pin)


                            fig1 = px.pie(top_ten_pin, names=top_ten_pin.index, values='Registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)

                            fig2=go.Figure(go.Pie(labels=top_ten_pin.index,values=top_ten_pin['Registered_user'],hole=0.5))
                            st.plotly_chart(fig2)

        if year == 2021:
            if quarter == 'Q1(Jan-March)':
                if types == 'Aggregation':
                    filtered_df = df_agg_users[(df_agg_users['Year'] == 2021) & (df_agg_users['Quarter'] == 1)]


                    fig1=px.bar(filtered_df,x='Device_Brands',y='Counts',hover_name='State',color='State',range_y=(0,13000000))
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='Device_Brands',values='Counts')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['State','Device_Brands'],values='Counts',color='State')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)
                elif types == 'Top_list':
                    col,col1=st.columns(2)
                    with col:
                        tts=st.button('Top 10 State')
                        if tts:
                            filtered_df = df_top_users[(df_top_users['Year'] == 2021) & (df_top_users['Quarter'] == 1)]
                            state_counts=filtered_df.groupby('State').agg({'Registered_user':'sum'})
                            sorted_counts=state_counts.sort_values('Registered_user',ascending=False)
                            top_ten_states=sorted_counts.head(10)
                            st.dataframe(top_ten_states)

                            fig = px.bar(top_ten_states, x=top_ten_states.index, y='Registered_user', labels={'x':'State', 'Registered_user':'Registered Users'})
                            st.plotly_chart(fig)

                            fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='Registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)
                    with col1:
                        ttp=st.button('Top 10 Pincodes')
                        if ttp:
                            filtered_df = df_top_users[(df_top_users['Year'] == 2018) & (df_top_users['Quarter'] == 1)]
                            pin_counts=filtered_df.groupby('Pincode').agg({'Registered_user':'sum'})
                            sort_counts=pin_counts.sort_values('Registered_user',ascending=False)
                            top_ten_pin=sort_counts.head(10)
                            st.dataframe(top_ten_pin)


                            fig1 = px.pie(top_ten_pin, names=top_ten_pin.index, values='Registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)

                            fig2=go.Figure(go.Pie(labels=top_ten_pin.index,values=top_ten_pin['Registered_user'],hole=0.5))
                            st.plotly_chart(fig2)

            elif quarter == 'Q2(Apr-June)':
                if types == 'Aggregation':
                    filtered_df = df_agg_users[(df_agg_users['Year'] == 2021) & (df_agg_users['Quarter'] == 2)]


                    fig1=px.bar(filtered_df,x='Device_Brands',y='Counts',hover_name='State',color='State',range_y=(0,13000000))
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='Device_Brands',values='Counts')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['State','Device_Brands'],values='Counts',color='State')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)
                elif types == 'Top_list':
                    col,col1=st.columns(2)
                    with col:
                        tts=st.button('Top 10 State')
                        if tts:
                            filtered_df = df_top_users[(df_top_users['Year'] == 2021) & (df_top_users['Quarter'] == 2)]
                            state_counts=filtered_df.groupby('State').agg({'Registered_user':'sum'})
                            sorted_counts=state_counts.sort_values('Registered_user',ascending=False)
                            top_ten_states=sorted_counts.head(10)
                            st.dataframe(top_ten_states)

                            fig = px.bar(top_ten_states, x=top_ten_states.index, y='Registered_user', labels={'x':'State', 'Registered_user':'Registered Users'})
                            st.plotly_chart(fig)

                            fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='Registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)
                    with col1:
                        ttp=st.button('Top 10 Pincodes')
                        if ttp:
                            filtered_df = df_top_users[(df_top_users['Year'] == 2018) & (df_top_users['Quarter'] == 2)]
                            pin_counts=filtered_df.groupby('Pincode').agg({'Registered_user':'sum'})
                            sort_counts=pin_counts.sort_values('Registered_user',ascending=False)
                            top_ten_pin=sort_counts.head(10)
                            st.dataframe(top_ten_pin)


                            fig1 = px.pie(top_ten_pin, names=top_ten_pin.index, values='Registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)

                            fig2=go.Figure(go.Pie(labels=top_ten_pin.index,values=top_ten_pin['Registered_user'],hole=0.5))
                            st.plotly_chart(fig2)

            elif quarter == 'Q3(July-Sep)':
                if types == 'Aggregation':
                    filtered_df = df_agg_users[(df_agg_users['Year'] == 2021) & (df_agg_users['Quarter'] == 3)]


                    fig1=px.bar(filtered_df,x='Device_Brands',y='Counts',hover_name='State',color='State',range_y=(0,13000000))
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='Device_Brands',values='Counts')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['State','Device_Brands'],values='Counts',color='State')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)
                elif types == 'Top_list':
                    col,col1=st.columns(2)
                    with col:
                        tts=st.button('Top 10 State')
                        if tts:
                            filtered_df = df_top_users[(df_top_users['Year'] == 2021) & (df_top_users['Quarter'] == 3)]
                            state_counts=filtered_df.groupby('State').agg({'Registered_user':'sum'})
                            sorted_counts=state_counts.sort_values('Registered_user',ascending=False)
                            top_ten_states=sorted_counts.head(10)
                            st.dataframe(top_ten_states)

                            fig = px.bar(top_ten_states, x=top_ten_states.index, y='Registered_user', labels={'x':'State', 'Registered_user':'Registered Users'})
                            st.plotly_chart(fig)

                            fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='Registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)
                    with col1:
                        ttp=st.button('Top 10 Pincodes')
                        if ttp:
                            filtered_df = df_top_users[(df_top_users['Year'] == 2018) & (df_top_users['Quarter'] == 3)]
                            pin_counts=filtered_df.groupby('Pincode').agg({'Registered_user':'sum'})
                            sort_counts=pin_counts.sort_values('Registered_user',ascending=False)
                            top_ten_pin=sort_counts.head(10)
                            st.dataframe(top_ten_pin)


                            fig1 = px.pie(top_ten_pin, names=top_ten_pin.index, values='Registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)

                            fig2=go.Figure(go.Pie(labels=top_ten_pin.index,values=top_ten_pin['Registered_user'],hole=0.5))
                            st.plotly_chart(fig2)

            elif quarter == 'Q4(Oct-Dec)':
                if types == 'Aggregation':
                    filtered_df = df_agg_users[(df_agg_users['Year'] == 2021) & (df_agg_users['Quarter'] == 4)]


                    fig1=px.bar(filtered_df,x='Device_Brands',y='Counts',hover_name='State',color='State',range_y=(0,13000000))
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='Device_Brands',values='Counts')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['State','Device_Brands'],values='Counts',color='State')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)
                elif types == 'Top_list':
                    col,col1=st.columns(2)
                    with col:
                        tts=st.button('Top 10 State')
                        if tts:
                            filtered_df = df_top_users[(df_top_users['Year'] == 2021) & (df_top_users['Quarter'] == 4)]
                            state_counts=filtered_df.groupby('State').agg({'Registered_user':'sum'})
                            sorted_counts=state_counts.sort_values('Registered_user',ascending=False)
                            top_ten_states=sorted_counts.head(10)
                            st.dataframe(top_ten_states)

                            fig = px.bar(top_ten_states, x=top_ten_states.index, y='Registered_user', labels={'x':'State', 'Registered_user':'Registered Users'})
                            st.plotly_chart(fig)

                            fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='Registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)
                    with col1:
                        ttp=st.button('Top 10 Pincodes')
                        if ttp:
                            filtered_df = df_top_users[(df_top_users['Year'] == 2018) & (df_top_users['Quarter'] == 4)]
                            pin_counts=filtered_df.groupby('Pincode').agg({'Registered_user':'sum'})
                            sort_counts=pin_counts.sort_values('Registered_user',ascending=False)
                            top_ten_pin=sort_counts.head(10)
                            st.dataframe(top_ten_pin)


                            fig1 = px.pie(top_ten_pin, names=top_ten_pin.index, values='Registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)

                            fig2=go.Figure(go.Pie(labels=top_ten_pin.index,values=top_ten_pin['Registered_user'],hole=0.5))
                            st.plotly_chart(fig2)

        if year == 2022:
            if quarter == 'Q1(Jan-March)':
                if types == 'Aggregation':
                    filtered_df = df_agg_users[(df_agg_users['Year'] == 2022) & (df_agg_users['Quarter'] == 1)]


                    fig1=px.bar(filtered_df,x='Device_Brands',y='Counts',hover_name='State',color='State',range_y=(0,13000000))
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='Device_Brands',values='Counts')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['State','Device_Brands'],values='Counts',color='State')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)
                elif types == 'Top_list':
                    col,col1=st.columns(2)
                    with col:
                        tts=st.button('Top 10 State')
                        if tts:
                            filtered_df = df_top_users[(df_top_users['Year'] == 2022) & (df_top_users['Quarter'] == 1)]
                            state_counts=filtered_df.groupby('State').agg({'Registered_user':'sum'})
                            sorted_counts=state_counts.sort_values('Registered_user',ascending=False)
                            top_ten_states=sorted_counts.head(10)
                            st.dataframe(top_ten_states)

                            fig = px.bar(top_ten_states, x=top_ten_states.index, y='Registered_user', labels={'x':'State', 'Registered_user':'Registered Users'})
                            st.plotly_chart(fig)

                            fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='Registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)
                    with col1:
                        ttp=st.button('Top 10 Pincodes')
                        if ttp:
                            filtered_df = df_top_users[(df_top_users['Year'] == 2018) & (df_top_users['Quarter'] == 1)]
                            pin_counts=filtered_df.groupby('Pincode').agg({'Registered_user':'sum'})
                            sort_counts=pin_counts.sort_values('Registered_user',ascending=False)
                            top_ten_pin=sort_counts.head(10)
                            st.dataframe(top_ten_pin)


                            fig1 = px.pie(top_ten_pin, names=top_ten_pin.index, values='Registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)

                            fig2=go.Figure(go.Pie(labels=top_ten_pin.index,values=top_ten_pin['Registered_user'],hole=0.5))
                            st.plotly_chart(fig2)

            elif quarter == 'Q2(Apr-June)':
                if types == 'Aggregation':
                    filtered_df = df_agg_users[(df_agg_users['Year'] == 2022) & (df_agg_users['Quarter'] == 2)]


                    fig1=px.bar(filtered_df,x='Device_Brands',y='Counts',hover_name='State',color='State',range_y=(0,13000000))
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='Device_Brands',values='Counts')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['State','Device_Brands'],values='Counts',color='State')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)
                elif types == 'Top_list':
                    col,col1=st.columns(2)
                    with col:
                        tts=st.button('Top 10 State')
                        if tts:
                            filtered_df = df_top_users[(df_top_users['Year'] == 2022) & (df_top_users['Quarter'] == 2)]
                            state_counts=filtered_df.groupby('State').agg({'Registered_user':'sum'})
                            sorted_counts=state_counts.sort_values('Registered_user',ascending=False)
                            top_ten_states=sorted_counts.head(10)
                            st.dataframe(top_ten_states)

                            fig = px.bar(top_ten_states, x=top_ten_states.index, y='Registered_user', labels={'x':'State', 'Registered_user':'Registered Users'})
                            st.plotly_chart(fig)

                            fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='Registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)
                    with col1:
                        ttp=st.button('Top 10 Pincodes')
                        if ttp:
                            filtered_df = df_top_users[(df_top_users['Year'] == 2018) & (df_top_users['Quarter'] == 2)]
                            pin_counts=filtered_df.groupby('Pincode').agg({'Registered_user':'sum'})
                            sort_counts=pin_counts.sort_values('Registered_user',ascending=False)
                            top_ten_pin=sort_counts.head(10)
                            st.dataframe(top_ten_pin)


                            fig1 = px.pie(top_ten_pin, names=top_ten_pin.index, values='Registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)

                            fig2=go.Figure(go.Pie(labels=top_ten_pin.index,values=top_ten_pin['Registered_user'],hole=0.5))
                            st.plotly_chart(fig2)

            elif quarter == 'Q3(July-Sep)':
                if types == 'Aggregation':
                    filtered_df = df_agg_users[(df_agg_users['Year'] == 2022) & (df_agg_users['Quarter'] == 3)]


                    fig1=px.bar(filtered_df,x='Device_Brands',y='Counts',hover_name='State',color='State',range_y=(0,13000000))
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='Device_Brands',values='Counts')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['State','Device_Brands'],values='Counts',color='State')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)
                elif types == 'Top_list':
                    col,col1=st.columns(2)
                    with col:
                        tts=st.button('Top 10 State')
                        if tts:
                            filtered_df = df_top_users[(df_top_users['Year'] == 2022) & (df_top_users['Quarter'] == 3)]
                            state_counts=filtered_df.groupby('State').agg({'Registered_user':'sum'})
                            sorted_counts=state_counts.sort_values('Registered_user',ascending=False)
                            top_ten_states=sorted_counts.head(10)
                            st.dataframe(top_ten_states)

                            fig = px.bar(top_ten_states, x=top_ten_states.index, y='Registered_user', labels={'x':'State', 'Registered_user':'Registered Users'})
                            st.plotly_chart(fig)

                            fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='Registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)
                    with col1:
                        ttp=st.button('Top 10 Pincodes')
                        if ttp:
                            filtered_df = df_top_users[(df_top_users['Year'] == 2018) & (df_top_users['Quarter'] == 3)]
                            pin_counts=filtered_df.groupby('Pincode').agg({'Registered_user':'sum'})
                            sort_counts=pin_counts.sort_values('Registered_user',ascending=False)
                            top_ten_pin=sort_counts.head(10)
                            st.dataframe(top_ten_pin)


                            fig1 = px.pie(top_ten_pin, names=top_ten_pin.index, values='Registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)

                            fig2=go.Figure(go.Pie(labels=top_ten_pin.index,values=top_ten_pin['Registered_user'],hole=0.5))
                            st.plotly_chart(fig2)

            elif quarter == 'Q4(Oct-Dec)':
                if types == 'Aggregation':
                    filtered_df = df_agg_users[(df_agg_users['Year'] == 2022) & (df_agg_users['Quarter'] == 1)]


                    fig1=px.bar(filtered_df,x='Device_Brands',y='Counts',hover_name='State',color='State',range_y=(0,13000000))
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='Device_Brands',values='Counts')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['State','Device_Brands'],values='Counts',color='State')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)
                elif types == 'Top_list':
                    col,col1=st.columns(2)
                    with col:
                        tts=st.button('Top 10 State')
                        if tts:
                            filtered_df = df_top_users[(df_top_users['Year'] == 2022) & (df_top_users['Quarter'] == 4)]
                            state_counts=filtered_df.groupby('State').agg({'Registered_user':'sum'})
                            sorted_counts=state_counts.sort_values('Registered_user',ascending=False)
                            top_ten_states=sorted_counts.head(10)
                            st.dataframe(top_ten_states)

                            fig = px.bar(top_ten_states, x=top_ten_states.index, y='Registered_user', labels={'x':'State', 'Registered_user':'Registered Users'})
                            st.plotly_chart(fig)

                            fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='Registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)
                    with col1:
                        ttp=st.button('Top 10 Pincodes')
                        if ttp:
                            filtered_df = df_top_users[(df_top_users['Year'] == 2018) & (df_top_users['Quarter'] == 4)]
                            pin_counts=filtered_df.groupby('Pincode').agg({'Registered_user':'sum'})
                            sort_counts=pin_counts.sort_values('Registered_user',ascending=False)
                            top_ten_pin=sort_counts.head(10)
                            st.dataframe(top_ten_pin)


                            fig1 = px.pie(top_ten_pin, names=top_ten_pin.index, values='Registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)

                            fig2=go.Figure(go.Pie(labels=top_ten_pin.index,values=top_ten_pin['Registered_user'],hole=0.5))
                            st.plotly_chart(fig2)



    if add_selectbox == 'transaction':
        if year == 2018:
            if quarter == 'Q1(Jan-March)':
                if types == 'Aggregation':
                    filtered_df=df_agg_trans[(df_agg_trans['Year']==2018)&(df_agg_trans['Quarter']==1)]

                    fig1=px.bar(filtered_df,x='Transaction_type',y='Transaction_count',hover_name='Transaction_amount',color='State',range_y=(0,1000000),animation_frame='State')
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='Transaction_type',values='Transaction_count')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['State','Transaction_type'],values='Transaction_count',color='State')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                elif types == 'Top_list':
                    filtered_df=df_agg_trans[(df_agg_trans['Year']==2018)&(df_agg_trans['Quarter']==1)]     
                    state_counts=filtered_df.groupby('State').agg({'Transaction_count':'sum','Transaction_amount':'sum'})
                    sorted_counts=state_counts.sort_values('Transaction_count',ascending=False)
                    top_ten_states=sorted_counts.head(10)
                    st.dataframe(top_ten_states)
                    fig = px.bar(top_ten_states, x=top_ten_states.index, y='Transaction_count', labels={'x':'State', 'y':'Registered Users'})
                    st.plotly_chart(fig)

                    fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='Transaction_amount')
                    fig1.update_traces(textposition='outside')
                    st.plotly_chart(fig1)



            elif quarter == 'Q2(Apr-June)':
                if types == 'Aggregation':
                    filtered_df=df_agg_trans[(df_agg_trans['Year']==2018)&(df_agg_trans['Quarter']==2)]

                    fig1=px.bar(filtered_df,x='Transaction_type',y='Transaction_count',hover_name='Transaction_amount',color='State',range_y=(0,1000000),animation_frame='State')
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='Transaction_type',values='Transaction_count')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['State','Transaction_type'],values='Transaction_count',color='State')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                elif types == 'Top_list':
                    filtered_df=df_agg_trans[(df_agg_trans['Year']==2018)&(df_agg_trans['Quarter']==2)]     
                    state_counts=filtered_df.groupby('State').agg({'Transaction_count':'sum','Transaction_amount':'sum'})
                    sorted_counts=state_counts.sort_values('Transaction_count',ascending=False)
                    top_ten_states=sorted_counts.head(10)
                    st.dataframe(top_ten_states)
                    fig = px.bar(top_ten_states, x=top_ten_states.index, y='Transaction_count', labels={'x':'State', 'y':'Registered Users'})
                    st.plotly_chart(fig)

                    fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='Transaction_amount')
                    fig1.update_traces(textposition='outside')
                    st.plotly_chart(fig1)

            elif quarter == 'Q3(July-Sep)':
                if types == 'Aggregation':
                    filtered_df=df_agg_trans[(df_agg_trans['Year']==2018)&(df_agg_trans['Quarter']==3)]

                    fig1=px.bar(filtered_df,x='Transaction_type',y='Transaction_count',hover_name='Transaction_amount',color='State',range_y=(0,1000000),animation_frame='State')
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='Transaction_type',values='Transaction_count')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['State','Transaction_type'],values='Transaction_count',color='State')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)
                elif types == 'Top_list':
                    filtered_df=df_agg_trans[(df_agg_trans['Year']==2018)&(df_agg_trans['Quarter']==3)]     
                    state_counts=filtered_df.groupby('State').agg({'Transaction_count':'sum','Transaction_amount':'sum'})
                    sorted_counts=state_counts.sort_values('Transaction_count',ascending=False)
                    top_ten_states=sorted_counts.head(10)
                    st.dataframe(top_ten_states)
                    fig = px.bar(top_ten_states, x=top_ten_states.index, y='Transaction_count', labels={'x':'State', 'y':'Registered Users'})
                    st.plotly_chart(fig)

                    fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='Transaction_amount')
                    fig1.update_traces(textposition='outside')
                    st.plotly_chart(fig1)

            elif quarter == 'Q4(Oct-Dec)':
                if types == 'Aggregation':
                    filtered_df=df_agg_trans[(df_agg_trans['Year']==2018)&(df_agg_trans['Quarter']==4)]

                    fig1=px.bar(filtered_df,x='Transaction_type',y='Transaction_count',hover_name='Transaction_amount',color='State',range_y=(0,1000000),animation_frame='State')
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='Transaction_type',values='Transaction_count')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['State','Transaction_type'],values='Transaction_count',color='State')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)
                elif types == 'Top_list':
                    filtered_df=df_agg_trans[(df_agg_trans['Year']==2018)&(df_agg_trans['Quarter']==4)]     
                    state_counts=filtered_df.groupby('State').agg({'Transaction_count':'sum','Transaction_amount':'sum'})
                    sorted_counts=state_counts.sort_values('Transaction_count',ascending=False)
                    top_ten_states=sorted_counts.head(10)
                    st.dataframe(top_ten_states)
                    fig = px.bar(top_ten_states, x=top_ten_states.index, y='Transaction_count', labels={'x':'State', 'y':'Registered Users'})
                    st.plotly_chart(fig)

                    fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='Transaction_amount')
                    fig1.update_traces(textposition='outside')
                    st.plotly_chart(fig1)

        if year == 2019:
            if quarter == 'Q1(Jan-March)':
                if types == 'Aggregation':
                    filtered_df=df_agg_trans[(df_agg_trans['Year']==2019)&(df_agg_trans['Quarter']==1)]

                    fig1=px.bar(filtered_df,x='Transaction_type',y='Transaction_count',hover_name='Transaction_amount',color='State',range_y=(0,1000000),animation_frame='State')
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='Transaction_type',values='Transaction_count')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['State','Transaction_type'],values='Transaction_count',color='State')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)
                elif types == 'Top_list':
                    filtered_df=df_agg_trans[(df_agg_trans['Year']==2019)&(df_agg_trans['Quarter']==1)]     
                    state_counts=filtered_df.groupby('State').agg({'Transaction_count':'sum','Transaction_amount':'sum'})
                    sorted_counts=state_counts.sort_values('Transaction_count',ascending=False)
                    top_ten_states=sorted_counts.head(10)
                    st.dataframe(top_ten_states)
                    fig = px.bar(top_ten_states, x=top_ten_states.index, y='Transaction_count', labels={'x':'State', 'y':'Registered Users'})
                    st.plotly_chart(fig)

                    fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='Transaction_amount')
                    fig1.update_traces(textposition='outside')
                    st.plotly_chart(fig1)

            elif quarter == 'Q2(Apr-June)':
                if types == 'Aggregation':
                    filtered_df=df_agg_trans[(df_agg_trans['Year']==2019)&(df_agg_trans['Quarter']==2)]

                    fig1=px.bar(filtered_df,x='Transaction_type',y='Transaction_count',hover_name='Transaction_amount',color='State',range_y=(0,1000000),animation_frame='State')
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='Transaction_type',values='Transaction_count')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['State','Transaction_type'],values='Transaction_count',color='State')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)
                elif types == 'Top_list':
                    filtered_df=df_agg_trans[(df_agg_trans['Year']==2019)&(df_agg_trans['Quarter']==2)]     
                    state_counts=filtered_df.groupby('State').agg({'Transaction_count':'sum','Transaction_amount':'sum'})
                    sorted_counts=state_counts.sort_values('Transaction_count',ascending=False)
                    top_ten_states=sorted_counts.head(10)
                    st.dataframe(top_ten_states)
                    fig = px.bar(top_ten_states, x=top_ten_states.index, y='Transaction_count', labels={'x':'State', 'y':'Registered Users'})
                    st.plotly_chart(fig)

                    fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='Transaction_amount')
                    fig1.update_traces(textposition='outside')
                    st.plotly_chart(fig1)

            elif quarter == 'Q3(July-Sep)':
                if types == 'Aggregation':
                    filtered_df=df_agg_trans[(df_agg_trans['Year']==2019)&(df_agg_trans['Quarter']==3)]

                    fig1=px.bar(filtered_df,x='Transaction_type',y='Transaction_count',hover_name='Transaction_amount',color='State',range_y=(0,1000000),animation_frame='State')
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='Transaction_type',values='Transaction_count')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['State','Transaction_type'],values='Transaction_count',color='State')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)
                elif types == 'Top_list':
                    filtered_df=df_agg_trans[(df_agg_trans['Year']==2019)&(df_agg_trans['Quarter']==3)]     
                    state_counts=filtered_df.groupby('State').agg({'Transaction_count':'sum','Transaction_amount':'sum'})
                    sorted_counts=state_counts.sort_values('Transaction_count',ascending=False)
                    top_ten_states=sorted_counts.head(10)
                    st.dataframe(top_ten_states)
                    fig = px.bar(top_ten_states, x=top_ten_states.index, y='Transaction_count', labels={'x':'State', 'y':'Registered Users'})
                    st.plotly_chart(fig)

                    fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='Transaction_amount')
                    fig1.update_traces(textposition='outside')
                    st.plotly_chart(fig1)

            elif quarter == 'Q4(Oct-Dec)':
                if types == 'Aggregation':
                    filtered_df=df_agg_trans[(df_agg_trans['Year']==2019)&(df_agg_trans['Quarter']==4)]

                    fig1=px.bar(filtered_df,x='Transaction_type',y='Transaction_count',hover_name='Transaction_amount',color='State',range_y=(0,1000000),animation_frame='State')
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='Transaction_type',values='Transaction_count')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['State','Transaction_type'],values='Transaction_count',color='State')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)
                elif types == 'Top_list':
                    filtered_df=df_agg_trans[(df_agg_trans['Year']==2019)&(df_agg_trans['Quarter']==4)]     
                    state_counts=filtered_df.groupby('State').agg({'Transaction_count':'sum','Transaction_amount':'sum'})
                    sorted_counts=state_counts.sort_values('Transaction_count',ascending=False)
                    top_ten_states=sorted_counts.head(10)
                    st.dataframe(top_ten_states)
                    fig = px.bar(top_ten_states, x=top_ten_states.index, y='Transaction_count', labels={'x':'State', 'y':'Registered Users'})
                    st.plotly_chart(fig)

                    fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='Transaction_amount')
                    fig1.update_traces(textposition='outside')
                    st.plotly_chart(fig1)


        if year == 2020:
            if quarter == 'Q1(Jan-March)':
                if types == 'Aggregation':
                    filtered_df=df_agg_trans[(df_agg_trans['Year']==2020)&(df_agg_trans['Quarter']==1)]

                    fig1=px.bar(filtered_df,x='Transaction_type',y='Transaction_count',hover_name='Transaction_amount',color='State',range_y=(0,1000000),animation_frame='State')
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='Transaction_type',values='Transaction_count')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['State','Transaction_type'],values='Transaction_count',color='State')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)
                elif types == 'Top_list':
                    filtered_df=df_agg_trans[(df_agg_trans['Year']==2020)&(df_agg_trans['Quarter']==1)]     
                    state_counts=filtered_df.groupby('State').agg({'Transaction_count':'sum','Transaction_amount':'sum'})
                    sorted_counts=state_counts.sort_values('Transaction_count',ascending=False)
                    top_ten_states=sorted_counts.head(10)
                    st.dataframe(top_ten_states)
                    fig = px.bar(top_ten_states, x=top_ten_states.index, y='Transaction_count', labels={'x':'State', 'y':'Registered Users'})
                    st.plotly_chart(fig)

                    fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='Transaction_amount')
                    fig1.update_traces(textposition='outside')
                    st.plotly_chart(fig1)

            elif quarter == 'Q2(Apr-June)':
                if types == 'Aggregation':
                    filtered_df=df_agg_trans[(df_agg_trans['Year']==2020)&(df_agg_trans['Quarter']==2)]

                    fig1=px.bar(filtered_df,x='Transaction_type',y='Transaction_count',hover_name='Transaction_amount',color='State',range_y=(0,1000000),animation_frame='State')
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='Transaction_type',values='Transaction_count')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['State','Transaction_type'],values='Transaction_count',color='State')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)
                elif types == 'Top_list':
                    filtered_df=df_agg_trans[(df_agg_trans['Year']==2020)&(df_agg_trans['Quarter']==2)]     
                    state_counts=filtered_df.groupby('State').agg({'Transaction_count':'sum','Transaction_amount':'sum'})
                    sorted_counts=state_counts.sort_values('Transaction_count',ascending=False)
                    top_ten_states=sorted_counts.head(10)
                    st.dataframe(top_ten_states)
                    fig = px.bar(top_ten_states, x=top_ten_states.index, y='Transaction_count', labels={'x':'State', 'y':'Registered Users'})
                    st.plotly_chart(fig)

                    fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='Transaction_amount')
                    fig1.update_traces(textposition='outside')
                    st.plotly_chart(fig1)

            elif quarter == 'Q3(July-Sep)':
                if types == 'Aggregation':
                    filtered_df=df_agg_trans[(df_agg_trans['Year']==2020)&(df_agg_trans['Quarter']==3)]

                    fig1=px.bar(filtered_df,x='Transaction_type',y='Transaction_count',hover_name='Transaction_amount',color='State',range_y=(0,1000000),animation_frame='State')
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='Transaction_type',values='Transaction_count')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['State','Transaction_type'],values='Transaction_count',color='State')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)
                elif types == 'Top_list':
                    filtered_df=df_agg_trans[(df_agg_trans['Year']==2020)&(df_agg_trans['Quarter']==3)]     
                    state_counts=filtered_df.groupby('State').agg({'Transaction_count':'sum','Transaction_amount':'sum'})
                    sorted_counts=state_counts.sort_values('Transaction_count',ascending=False)
                    top_ten_states=sorted_counts.head(10)
                    st.dataframe(top_ten_states)
                    fig = px.bar(top_ten_states, x=top_ten_states.index, y='Transaction_count', labels={'x':'State', 'y':'Registered Users'})
                    st.plotly_chart(fig)

                    fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='Transaction_amount')
                    fig1.update_traces(textposition='outside')
                    st.plotly_chart(fig1)

            elif quarter == 'Q4(Oct-Dec)':
                if types == 'Aggregation':
                    filtered_df=df_agg_trans[(df_agg_trans['Year']==2020)&(df_agg_trans['Quarter']==4)]

                    fig1=px.bar(filtered_df,x='Transaction_type',y='Transaction_count',hover_name='Transaction_amount',color='State',range_y=(0,1000000),animation_frame='State')
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='Transaction_type',values='Transaction_count')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['State','Transaction_type'],values='Transaction_count',color='State')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)
                elif types == 'Top_list':
                    filtered_df=df_agg_trans[(df_agg_trans['Year']==2020)&(df_agg_trans['Quarter']==4)]     
                    state_counts=filtered_df.groupby('State').agg({'Transaction_count':'sum','Transaction_amount':'sum'})
                    sorted_counts=state_counts.sort_values('Transaction_count',ascending=False)
                    top_ten_states=sorted_counts.head(10)
                    st.dataframe(top_ten_states)
                    fig = px.bar(top_ten_states, x=top_ten_states.index, y='Transaction_count', labels={'x':'State', 'y':'Registered Users'})
                    st.plotly_chart(fig)

                    fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='Transaction_amount')
                    fig1.update_traces(textposition='outside')
                    st.plotly_chart(fig1)

        if year == 2021:
            if quarter == 'Q1(Jan-March)':
                if types == 'Aggregation':
                    filtered_df=df_agg_trans[(df_agg_trans['Year']==2021)&(df_agg_trans['Quarter']==1)]

                    fig1=px.bar(filtered_df,x='Transaction_type',y='Transaction_count',hover_name='Transaction_amount',color='State',range_y=(0,1000000),animation_frame='State')
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='Transaction_type',values='Transaction_count')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['State','Transaction_type'],values='Transaction_count',color='State')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)
                elif types == 'Top_list':
                    filtered_df=df_agg_trans[(df_agg_trans['Year']==2021)&(df_agg_trans['Quarter']==1)]     
                    state_counts=filtered_df.groupby('State').agg({'Transaction_count':'sum','Transaction_amount':'sum'})
                    sorted_counts=state_counts.sort_values('Transaction_count',ascending=False)
                    top_ten_states=sorted_counts.head(10)
                    st.dataframe(top_ten_states)
                    fig = px.bar(top_ten_states, x=top_ten_states.index, y='Transaction_count', labels={'x':'State', 'y':'Registered Users'})
                    st.plotly_chart(fig)

                    fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='Transaction_amount')
                    fig1.update_traces(textposition='outside')
                    st.plotly_chart(fig1)

            elif quarter == 'Q2(Apr-June)':
                if types == 'Aggregation':
                    filtered_df=df_agg_trans[(df_agg_trans['Year']==2021)&(df_agg_trans['Quarter']==2)]

                    fig1=px.bar(filtered_df,x='Transaction_type',y='Transaction_count',hover_name='Transaction_amount',color='State',range_y=(0,1000000),animation_frame='State')
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='Transaction_type',values='Transaction_count')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['State','Transaction_type'],values='Transaction_count',color='State')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)
                elif types == 'Top_list':
                    filtered_df=df_agg_trans[(df_agg_trans['Year']==2021)&(df_agg_trans['Quarter']==2)]     
                    state_counts=filtered_df.groupby('State').agg({'Transaction_count':'sum','Transaction_amount':'sum'})
                    sorted_counts=state_counts.sort_values('Transaction_count',ascending=False)
                    top_ten_states=sorted_counts.head(10)
                    st.dataframe(top_ten_states)
                    fig = px.bar(top_ten_states, x=top_ten_states.index, y='Transaction_count', labels={'x':'State', 'y':'Registered Users'})
                    st.plotly_chart(fig)

                    fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='Transaction_amount')
                    fig1.update_traces(textposition='outside')
                    st.plotly_chart(fig1)

            elif quarter == 'Q3(July-Sep)':
                if types == 'Aggregation':
                    filtered_df=df_agg_trans[(df_agg_trans['Year']==2021)&(df_agg_trans['Quarter']==3)]

                    fig1=px.bar(filtered_df,x='Transaction_type',y='Transaction_count',hover_name='Transaction_amount',color='State',range_y=(0,1000000),animation_frame='State')
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='Transaction_type',values='Transaction_count')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['State','Transaction_type'],values='Transaction_count',color='State')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)
                elif types == 'Top_list':
                    filtered_df=df_agg_trans[(df_agg_trans['Year']==2021)&(df_agg_trans['Quarter']==3)]     
                    state_counts=filtered_df.groupby('State').agg({'Transaction_count':'sum','Transaction_amount':'sum'})
                    sorted_counts=state_counts.sort_values('Transaction_count',ascending=False)
                    top_ten_states=sorted_counts.head(10)
                    st.dataframe(top_ten_states)
                    fig = px.bar(top_ten_states, x=top_ten_states.index, y='Transaction_count', labels={'x':'State', 'y':'Registered Users'})
                    st.plotly_chart(fig)

                    fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='Transaction_amount')
                    fig1.update_traces(textposition='outside')
                    st.plotly_chart(fig1)

            elif quarter == 'Q4(Oct-Dec)':
                if types == 'Aggregation':
                    filtered_df=df_agg_trans[(df_agg_trans['Year']==2021)&(df_agg_trans['Quarter']==4)]

                    fig1=px.bar(filtered_df,x='Transaction_type',y='Transaction_count',hover_name='Transaction_amount',color='State',range_y=(0,1000000),animation_frame='State')
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='Transaction_type',values='Transaction_count')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['State','Transaction_type'],values='Transaction_count',color='State')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)
                elif types == 'Top_list':
                    filtered_df=df_agg_trans[(df_agg_trans['Year']==2021)&(df_agg_trans['Quarter']==4)]     
                    state_counts=filtered_df.groupby('State').agg({'Transaction_count':'sum','Transaction_amount':'sum'})
                    sorted_counts=state_counts.sort_values('Transaction_count',ascending=False)
                    top_ten_states=sorted_counts.head(10)
                    st.dataframe(top_ten_states)
                    fig = px.bar(top_ten_states, x=top_ten_states.index, y='Transaction_count', labels={'x':'State', 'y':'Registered Users'})
                    st.plotly_chart(fig)

                    fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='Transaction_amount')
                    fig1.update_traces(textposition='outside')
                    st.plotly_chart(fig1)

        if year == 2022:
            if quarter == 'Q1(Jan-March)':
                if types == 'Aggregation':
                    filtered_df=df_agg_trans[(df_agg_trans['Year']==2022)&(df_agg_trans['Quarter']==1)]

                    fig1=px.bar(filtered_df,x='Transaction_type',y='Transaction_count',hover_name='Transaction_amount',color='State',range_y=(0,1000000),animation_frame='State')
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='Transaction_type',values='Transaction_count')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['State','Transaction_type'],values='Transaction_count',color='State')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)
                elif types == 'Top_list':
                    filtered_df=df_agg_trans[(df_agg_trans['Year']==2022)&(df_agg_trans['Quarter']==1)]     
                    state_counts=filtered_df.groupby('State').agg({'Transaction_count':'sum','Transaction_amount':'sum'})
                    sorted_counts=state_counts.sort_values('Transaction_count',ascending=False)
                    top_ten_states=sorted_counts.head(10)
                    st.dataframe(top_ten_states)
                    fig = px.bar(top_ten_states, x=top_ten_states.index, y='Transaction_count', labels={'x':'State', 'y':'Registered Users'})
                    st.plotly_chart(fig)

                    fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='Transaction_amount')
                    fig1.update_traces(textposition='outside')
                    st.plotly_chart(fig1)

            elif quarter == 'Q2(Apr-June)':
                if types == 'Aggregation':
                    filtered_df=df_agg_trans[(df_agg_trans['Year']==2022)&(df_agg_trans['Quarter']==2)]

                    fig1=px.bar(filtered_df,x='Transaction_type',y='Transaction_count',hover_name='Transaction_amount',color='State',range_y=(0,1000000),animation_frame='State')
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='Transaction_type',values='Transaction_count')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['State','Transaction_type'],values='Transaction_count',color='State')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)
                elif types == 'Top_list':
                    filtered_df=df_agg_trans[(df_agg_trans['Year']==2022)&(df_agg_trans['Quarter']==2)]     
                    state_counts=filtered_df.groupby('State').agg({'Transaction_count':'sum','Transaction_amount':'sum'})
                    sorted_counts=state_counts.sort_values('Transaction_count',ascending=False)
                    top_ten_states=sorted_counts.head(10)
                    st.dataframe(top_ten_states)
                    fig = px.bar(top_ten_states, x=top_ten_states.index, y='Transaction_count', labels={'x':'State', 'y':'Registered Users'})
                    st.plotly_chart(fig)

                    fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='Transaction_amount')
                    fig1.update_traces(textposition='outside')
                    st.plotly_chart(fig1)

            elif quarter == 'Q3(July-Sep)':
                if types == 'Aggregation':
                    filtered_df=df_agg_trans[(df_agg_trans['Year']==2022)&(df_agg_trans['Quarter']==3)]

                    fig1=px.bar(filtered_df,x='Transaction_type',y='Transaction_count',hover_name='Transaction_amount',color='State',range_y=(0,1000000),animation_frame='State')
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='Transaction_type',values='Transaction_count')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['State','Transaction_type'],values='Transaction_count',color='State')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)
                elif types == 'Top_list':
                    filtered_df=df_agg_trans[(df_agg_trans['Year']==2022)&(df_agg_trans['Quarter']==3)]     
                    state_counts=filtered_df.groupby('State').agg({'Transaction_count':'sum','Transaction_amount':'sum'})
                    sorted_counts=state_counts.sort_values('Transaction_count',ascending=False)
                    top_ten_states=sorted_counts.head(10)
                    st.dataframe(top_ten_states)
                    fig = px.bar(top_ten_states, x=top_ten_states.index, y='Transaction_count', labels={'x':'State', 'y':'Registered Users'})
                    st.plotly_chart(fig)

                    fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='Transaction_amount')
                    fig1.update_traces(textposition='outside')
                    st.plotly_chart(fig1)

            elif quarter == 'Q4(Oct-Dec)':
                if types == 'Aggregation':
                    filtered_df=df_agg_trans[(df_agg_trans['Year']==2022)&(df_agg_trans['Quarter']==4)]

                    fig1=px.bar(filtered_df,x='Transaction_type',y='Transaction_count',hover_name='Transaction_amount',color='State',range_y=(0,1000000),animation_frame='State')
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='Transaction_type',values='Transaction_count')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['State','Transaction_type'],values='Transaction_count',color='State')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)
                elif types == 'Top_list':
                    filtered_df=df_agg_trans[(df_agg_trans['Year']==2022)&(df_agg_trans['Quarter']==4)]     
                    state_counts=filtered_df.groupby('State').agg({'Transaction_count':'sum','Transaction_amount':'sum'})
                    sorted_counts=state_counts.sort_values('Transaction_count',ascending=False)
                    top_ten_states=sorted_counts.head(10)
                    st.dataframe(top_ten_states)
                    fig = px.bar(top_ten_states, x=top_ten_states.index, y='Transaction_count', labels={'x':'State', 'y':'Registered Users'})
                    st.plotly_chart(fig)

                    fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='Transaction_amount')
                    fig1.update_traces(textposition='outside')
                    st.plotly_chart(fig1)

#------------------------------------------------------------------------------------------------------------



