import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
from config import PAGE_CONFIG
from functions import *
import io


def main():

    st.set_page_config(**PAGE_CONFIG)
    st.title("📊 Preliminary EDA")

    # load the data
    df = pd.read_csv("../data/data_formatted.csv")

    # get categorical variables
    categ_var = df.select_dtypes(include="object").columns.tolist() + [
        "registration_year",
        "registration_month",
        "cylinders",
        "seats",
        "doors",
    ]

    with st.sidebar:

        # choose the variable
        variable = st.selectbox(
            label="Choose the variable", options=sorted(df.columns.to_list())
        )

        # optional: choose a hue
        hue_variable = st.selectbox(
            label="🎨 OPTIONAL: hue for color grouping",
            options=[None] + sorted(categ_var),
        )

        # for more fiters
        with st.expander("🧪 Advanced Filters", expanded=False):

            # Filter by emission label
            labels = df["emissions_label"].dropna().unique()
            selected_labels = st.multiselect(
                "Filter by Emissions Label",
                options=sorted(labels),
                placeholder="Select one or more",
            )

            # Filter by transmission
            transmissions = df["transmission"].dropna().unique()
            selected_transmissions = st.multiselect(
                "Filter by Transmission",
                options=sorted(transmissions),
                placeholder="Select one or more",
            )

            # Filter by body type
            bodies = df["body_type"].dropna().unique()
            selected_bodies = st.multiselect(
                "Filter by Body Type",
                options=sorted(bodies),
                placeholder="Select one or more",
            )

        # get a copy of the original df to be used as there might be more filters selected
        df_filtered = df.copy()

        if selected_labels:
            df_filtered = df_filtered[
                df_filtered["emissions_label"].isin(selected_labels)
            ]

        if selected_transmissions:
            df_filtered = df_filtered[
                df_filtered["transmission"].isin(selected_transmissions)
            ]

        if selected_bodies:
            df_filtered = df_filtered[df_filtered["body_type"].isin(selected_bodies)]

        st.markdown("# ")
        st.markdown("# ")
        st.markdown("")

        # download filtered data
        csv = df_filtered.to_csv(index=False)
        st.download_button(
            label="📥 Download filtered data as CSV",
            data=csv,
            file_name="filtered_data.csv",
            mime="text/csv",
        )

    # set the tabs
    tab1, tab2, tab3 = st.tabs(
        ["📉 Distributions", "📛 NaN's & Outliers", "✨ Correlations"]
    )

    # decide if the column contains numeric or categorical data
    # note that there are numeric variables that should be treated as categorical
    numeric_data = (
        df_filtered.drop(
            columns=["doors", "seats", "registration_month", "registration_year"]
        )
        .select_dtypes(include=np.number)
        .columns.tolist()
    )

    with tab1:

        st.markdown(f"# Distributions of {variable}")

        # in case we select advanced filters
        if (
            len(selected_labels) != 0
            or len(selected_transmissions) != 0
            or len(selected_bodies) != 0
        ):
            string = data_showing(
                selected_labels, selected_transmissions, selected_bodies
            )
            st.write(string)
        else:
            st.write("*Plotting all data")

        if variable in numeric_data:
            fig_hist, fig_scat, fig_box = plot_numeric_or_categ(
                df_filtered, variable, cat=0, hue=hue_variable
            )
            st.plotly_chart(fig_hist)

            st.divider()

            st.plotly_chart(fig_scat)

            st.divider()

            st.plotly_chart(fig_box)

            st.markdown("## Statistics")
            st.dataframe(statistics(df_filtered, variable))

        else:
            fig_bar = plot_numeric_or_categ(df_filtered, variable, cat=1)
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

                st.write(f"**{variable}** is a categorical variable.")
                st.title("-- %")
                st.write("of Outliers")

            st.plotly_chart(fig_out)

    with tab3:

        df_numeric = df.select_dtypes(include="number").drop(
            columns=["doors", "seats", "registration_month", "registration_year"]
        )

        # get the correlation matrix
        corr_matrix = df_numeric.corr()

        # variables to compare: allows to choose between all the numeric ones
        corr_variables = st.multiselect(
            label="Choose the variables to compare",
            options=sorted(df_numeric.columns.tolist()),
            default=None,
        )

        if len(corr_variables) < 2:
            st.warning("Choose 2 or more variables to compare")

        else:
            fig_corr = px.imshow(
                corr_matrix.loc[corr_variables, corr_variables],
                text_auto=True,
                aspect="auto",
                color_continuous_scale="RdBu",
                zmin=-1,
                zmax=1,
            )
            st.plotly_chart(fig_corr, use_container_width=True)


if __name__ == "__main__":
    main()
