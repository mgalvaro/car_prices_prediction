import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
from config import PAGE_CONFIG
from functions import *


def main():

    st.set_page_config(**PAGE_CONFIG)
    st.title("📊 Preliminary EDA")

    # load the data
    df = pd.read_csv("../data/data_formatted.csv")

    # choose the variable
    variable = st.selectbox(
        label="Choose the variable", options=sorted(df.columns.to_list())
    )

    # set the tabs
    tab1, tab2 = st.tabs(["📉 Distributions", "📛 NaN's & Outliers"])

    # decide if the column contains numeric or categorical data
    # note that there are numeric variables that should be treated as categorical
    numeric_data = (
        df.drop(columns=["doors", "seats", "registration_month", "registration_year"])
        .select_dtypes(include=np.number)
        .columns.tolist()
    )

    with tab1:

        st.markdown(f"# Distributions of {variable}")

        if variable in numeric_data:
            fig_hist, fig_scat, fig_box = plot_numeric_or_categ(df, variable, cat=0)
            st.plotly_chart(fig_hist)

            st.divider()

            col1, col2 = st.columns(2)

            with col1:
                st.plotly_chart(fig_scat)
            with col2:
                st.plotly_chart(fig_box)
                st.dataframe(statistics(df, variable))

        else:
            fig_bar = plot_numeric_or_categ(df, variable, cat=1)
            st.plotly_chart(fig_bar)

    with tab2:

        st.markdown(f"# Distribution of Missing Values and Outliers in **{variable}**")

        df_nans, fig_nans = count_nans(df)
        df_out, fig_out = outliers_tukey(df)

        col1, col2 = st.columns(2)

        with col1:

            tot_nans = df_nans[df_nans["parameter"] == variable].iloc[0, 1]
            per_nans = df_nans[df_nans["parameter"] == variable].iloc[0, 2]

            st.write(f"**{variable}** has {tot_nans} missing values, which means:")
            st.title(f"{per_nans} %")
            st.write("of NaN's")

            st.plotly_chart(fig_nans)

        with col2:

            try:

                tot_out = df_out[df_out["parameter"] == variable].iloc[0, 1]
                per_out = df_out[df_out["parameter"] == variable].iloc[0, 2]

                st.write(
                    f"**{variable}** has {tot_out} outliers (Tukey's Fence criterion), which means:"
                )
                st.title(f"{per_out} %")
                st.write("of Outliers")

            except:

                st.write(f"**{variable}** is a categorical variable. No outliers here.")
                st.title("-- %")
                st.write("of Outliers")

            st.plotly_chart(fig_out)


if __name__ == "__main__":
    main()
