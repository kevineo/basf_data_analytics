import streamlit as st
import plotly_express as px
import pandas as pd


.
st.set_page_config(page_title='DA-Demo Employee Dashboard',
                   page_icon=":desktop_computer:", #https://www.webfx.com/tools/emoji-cheat-sheet/
                   layout="wide")




df = pd.read_excel(
    io='sample_data/Employee Sample Data.xlsx',
    engine='openpyxl',
    sheet_name='Data'
)

# print(df)

# # build the sidebar

st.sidebar.header("Filter By:")

dept = st.sidebar.multiselect(
    "Department:",
    options=df['Department'].unique(),
    default=df['Department'].unique()
)

jobtitle = st.sidebar.multiselect(
    "Job Title:",
    options=df['JobTitle'].unique(),
    default=df['JobTitle'].unique()
)

gender = st.sidebar.multiselect(
    "Gender:",
    options=df['Gender'].unique(),
    default=df['Gender'].unique()
)

age = st.sidebar.multiselect(
    "Age:",
    options=df['Age'].unique(),
    default=df['Age'].unique()
)

df_selection = df.query(
    "Department== @dept & Gender == @gender & Age == @age"
)    


# st.dataframe(df_selection)

# mainpage

st.title(":desktop_computer: My HR Dashboard")
st.markdown("##")

# top KPIs
avg_age= round(df_selection['Age'].mean())
avg_bonus = round(df_selection['Bonus'].mean(),2)*100
total_wages = int(df_selection['AnnualSalary'].sum())

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Total Annual Wages:")
    st.subheader(f"USD {total_wages:,}")

with middle_column:
    st.subheader("Average Bonus Given:")
    st.subheader(f"{avg_bonus}%")

with right_column:
    st.subheader("Average Employee Age:")
    st.subheader(f"{avg_age}")


# bar charts
group_by_city = (
    df_selection.groupby(by=["City"]).count()
)

# st.dataframe(group_by_city)
fig_employee_city = px.bar(
    group_by_city,
    x="EEID",
    y=group_by_city.index,
    orientation="h",
    title="<b> Employees by City </b>",
    color_discrete_sequence=["#0083B8"] * len(group_by_city),
    template="plotly_white"
)

st.plotly_chart(fig_employee_city)

group_by_country = (
    df_selection.groupby(by=["Country"]).count()
)

fig_employee_country = px.bar(
    group_by_country,
    x="EEID",
    y=group_by_country.index,
    orientation="h",
    title="<b> Employees by Country </b>",
    color_discrete_sequence=["#952323"] * len(group_by_country),
    template="plotly_white"
)

st.plotly_chart(fig_employee_country)