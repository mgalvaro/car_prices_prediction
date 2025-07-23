import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st


def plot_numeric_or_categ(df, variable, cat, target="price", hue=None):
    """Plots a histogram, a boxplot and a scatterplot for numerical variables
    and a barplot for categorical variables distribution"""

    # for numerical values
    if cat == 0:
        fig_hist = px.histogram(
            df,
            x=variable,
            nbins=50,
            title=f"Histogram: distribution of {variable}",
            color=hue,
        )
        fig_scat = px.scatter(
            df,
            x=variable,
            y=target,
            title=f"Scatterplot of {variable} vs. {target}",
            color=hue,
        )
        fig_box = px.box(df, x=variable, title=f"Boxplot of {variable}", color=hue)
        return fig_hist, fig_scat, fig_box

    # categorigal values
    else:
        # sort out the standard categorical values and those categorical values which come in a numerical format
        if variable not in [
            "doors",
            "seats",
            "registration_month",
            "registration_year",
        ]:
            fig_bar = px.bar(
                df,
                x=variable,
                title=f"Distribution of {variable}",
                category_orders={variable: df[variable].value_counts().index.tolist()},
            )
        else:
            fig_bar = px.bar(
                df.groupby(variable).agg(count=(variable, "count")).reset_index(),
                x=variable,
                y="count",
                title=f"Distribution of {variable}",
            )
        return fig_bar


def plot_nans_outliers(data, x, y, nans_or_out, clr):

    fig = px.bar(
        data,
        x=x,
        y=y,
        title=f"Global Distribution of {nans_or_out}",
        color_discrete_sequence=[clr],
    )

    fig.update_layout(xaxis_tickangle=310)

    return fig


def count_nans(df):
    """Returns a df with the total number of NaNs for each variable and it's percentage"""

    # create a df to store the column name and the NaNs %
    nan_count = pd.DataFrame(columns=["parameter", "Total nans", "nans %"])

    for col in df.columns:

        total_nans = df[col].isna().sum()
        temp_row = [
            col,
            total_nans,
            round(df[col].isna().sum() / (df.shape[0]) * 100, 2),
        ]

        nan_count.loc[len(nan_count)] = temp_row

    nan_count = nan_count.sort_values(by="nans %", ascending=False).reset_index(
        drop=True
    )

    fig_nans = plot_nans_outliers(
        nan_count, x="parameter", y="nans %", nans_or_out="NaNs", clr="#F50808"
    )

    fig_nans.update_layout(xaxis_tickangle=310)

    return nan_count, fig_nans


def outliers_tukey(df, k=1.5):

    numeric_data = (
        df.select_dtypes(include=np.number)
        .drop(
            columns=[
                "doors",
                "seats",
                "registration_month",
                "registration_year",
            ]
        )
        .columns.to_list()
    )

    df_outliers = pd.DataFrame(columns=["parameter", "normal_data", "outliers_%"])

    for col in numeric_data:
        q1 = np.nanquantile(df[col], q=0.25)
        q3 = np.nanquantile(df[col], q=0.75)

        ric = q3 - q1
        lim_inf = q1 - k * ric
        lim_sup = q3 + k * ric

        normal_data = df[df[col].between(lim_inf, lim_sup)].shape[0]
        total_outliers = df.shape[0] - normal_data
        per_outliers = round(total_outliers / df.shape[0] * 100, 2)

        df_outliers.loc[len(df_outliers)] = [col, total_outliers, per_outliers]

    df_outliers = df_outliers.sort_values(by="outliers_%", ascending=False).reset_index(
        drop=True
    )

    fig_out = plot_nans_outliers(
        df_outliers,
        x="parameter",
        y="outliers_%",
        nans_or_out="Outliers",
        clr="#2FE088",
    )

    return df_outliers, fig_out


def statistics(df, column):
    mean = df[column].mean()
    median = df[column].median()
    q1 = df[column].quantile(0.25)
    q3 = df[column].quantile(0.75)
    iqr = q3 - q1
    std = df[column].std()
    min_val = df[column].min()
    max_val = df[column].max()

    summary_df = pd.DataFrame(
        {
            "statistic": ["mean", "median", "Q1", "Q3", "IQR", "std", "min", "max"],
            "value": [mean, median, q1, q3, iqr, std, min_val, max_val],
        }
    )

    return summary_df


def data_showing(emiss, transm, body):

    show_dict = {
        "Emission Labels": emiss,
        "Transmission Types": transm,
        "Body Types": body,
    }

    string = "*Plotting data for: "

    for k, v in show_dict.items():
        if len(v) != 0:
            string += f"{k}: {v} || "

    return string
