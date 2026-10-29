import streamlit as st
import pandas as pd
import plotly.express as px

# ============================================
# 1. PAGE TITLE
# ============================================

st.set_page_config(
    page_title="Video Game Sales Dashboard",
    layout="wide"
)

st.title("Video Game Sales Dashboard")
st.subheader("By: Daniel Hernandez")

st.write(
    """
    Welcome to the Video Game Sales Dashboard!

    This application explores historical video game sales data.
    You can examine the number of games released each year,
    explore the dataset, and discover patterns in the video
    game industry.
    """
)

st.divider()

# ============================================
# 2. LOAD DATASET
# ============================================

df = pd.read_csv("vgsales.csv")

# Convert Year to numeric values
df["Year"] = pd.to_numeric(df["Year"], errors="coerce")

# ============================================
# 3. SIDEBAR FILTER
# ============================================

st.sidebar.header("Dashboard Filters")

st.sidebar.write(
    "Use the filter below to explore games released "
    "during a specific period."
)

valid_years = df["Year"].dropna()

min_year = int(valid_years.min())
max_year = int(valid_years.max())

year_range = st.sidebar.slider(
    "Select release year range",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year)
)

# Filter dataset by year
filtered_df = df[
    df["Year"].between(year_range[0], year_range[1])
].copy()

# ============================================
# 4. OVERVIEW SECTION
# ============================================

st.header("1. Overview")

st.write(
    """
    The Overview section provides a summary of the dataset.

    The information below changes when you select a different
    release-year range using the sidebar.
    """
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Games",
        f"{len(filtered_df):,}"
    )

with col2:
    st.metric(
        "Total Global Sales",
        f"{filtered_df['Global_Sales'].sum():,.2f} million"
    )

with col3:
    st.metric(
        "Number of Genres",
        filtered_df["Genre"].nunique()
    )

st.caption(
    "Global sales are reported in millions of units in the source dataset."
)

st.divider()

# ============================================
# 5. VIDEO GAMES RELEASED PER YEAR
# ============================================

st.header("2. Video Games Released Per Year")

st.write(
    """
    This chart shows the number of video game records associated
    with each release year.

    It helps us identify periods when more games were released
    and examine how the volume of game releases changed over time.
    """
)

# Count games released each year
games_per_year = (
    filtered_df.dropna(subset=["Year"])
    .groupby("Year")
    .size()
    .reset_index(name="Number of Games")
)

games_per_year = games_per_year.sort_values("Year")

if not games_per_year.empty:

    # Create interactive bar chart
    fig = px.bar(
        games_per_year,
        x="Year",
        y="Number of Games",
        title="Number of Video Games Released Per Year",
        labels={
            "Year": "Release Year",
            "Number of Games": "Number of Games Released"
        },
        hover_data={
            "Number of Games": True
        }
    )

    fig.update_layout(
        xaxis_title="Release Year",
        yaxis_title="Number of Games Released",
        showlegend=False
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # Identify the year with the most records
    peak_year = games_per_year.loc[
        games_per_year["Number of Games"].idxmax()
    ]

    st.write(
        f"**Observation:** The highest number of game records "
        f"in the selected period occurred in {int(peak_year['Year'])}, "
        f"with {int(peak_year['Number of Games'])} games."
    )

else:
    st.warning(
        "No games with valid release years were found "
        "in the selected range."
    )

st.caption(
    "Note: This chart counts records in the dataset, not necessarily "
    "every video game released worldwide. Records with missing "
    "release years are excluded."
)

st.divider()

# ============================================
# 6. DATA DISPLAY SECTION
# ============================================

st.header("3. Data Display")

st.write(
    """
    This section allows you to inspect the underlying dataset.

    Each row represents a game record, with information such as
    the game title, platform, release year, genre, publisher,
    and regional sales estimates.
    """
)

st.write(
    f"Showing **{len(filtered_df):,}** records "
    f"for release years {year_range[0]}–{year_range[1]}."
)

st.dataframe(
    filtered_df,
    use_container_width=True,
    hide_index=True
)

# Download filtered data
csv_data = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Filtered Data as CSV",
    data=csv_data,
    file_name="filtered_video_game_sales.csv",
    mime="text/csv"
)

st.divider()

# ============================================
# 7. INSIGHTS SECTION
# ============================================

st.header("4. Insights")

st.write(
    """
    This section highlights some basic findings from the
    selected data. These statistics help summarize the
    dataset and identify patterns worth investigating.
    """
)

if not filtered_df.empty:

    # Most represented genre
    genre_counts = filtered_df["Genre"].value_counts()

    if not genre_counts.empty:
        top_genre = genre_counts.index[0]
        top_genre_count = genre_counts.iloc[0]

        st.subheader("Most Represented Genre")

        st.write(
            f"The genre with the most game records in the selected "
            f"period is **{top_genre}**, with "
            f"**{top_genre_count:,} games**."
        )

    # Highest global sales
    sales_df = filtered_df.dropna(subset=["Global_Sales"])

    if not sales_df.empty:
        best_game = sales_df.loc[
            sales_df["Global_Sales"].idxmax()
        ]

        st.subheader("Highest-Selling Game in the Dataset Selection")

        st.write(
            f"**Game:** {best_game['Name']}"
        )

        st.write(
            f"**Platform:** {best_game['Platform']}"
        )

        st.write(
            f"**Global sales:** "
            f"{best_game['Global_Sales']:.2f} million units"
        )

    st.info(
        "Interpret these findings carefully. The dataset contains "
        "historical sales estimates and may have missing values. "
        "These observations describe the available records and do "
        "not establish why a particular game or genre was successful."
    )

else:
    st.warning(
        "There are no records available for the current selection."
    )

st.divider()

# ============================================
# 8. ABOUT THE DATASET
# ============================================

st.header("5. About the Dataset")

st.write(
    """
    The Video Game Sales dataset contains historical information
    about video game titles, platforms, release years, genres,
    publishers, and estimated sales across different regions.

    It is useful for exploring release patterns and comparing
    game sales across the video game industry.
    """
)

st.markdown(
    "Dataset source: "
    "[Video Game Sales on Kaggle]"
    "(https://www.kaggle.com/datasets/gregorut/videogamesales)"
)

st.caption(
    "Developed using Python, Streamlit, Pandas, and Plotly."
)