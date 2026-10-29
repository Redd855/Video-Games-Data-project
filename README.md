# Video Game Sales Dashboard

## Purpose
The Video Game Sales Dashboard is an interactive web application built with Python and Streamlit. It allows users to explore historical video game sales data, view the number of games released over time, examine key statistics, and discover insights about video game sales. Users can filter the data by release year and download the filtered dataset as a CSV file.

## Dataset Used
This project uses the **Video Game Sales** dataset from Kaggle.

Dataset source: https://www.kaggle.com/datasets/gregorut/videogamesales

The dataset includes information about video game titles, platforms, release years, genres, publishers, and sales across different regions, including global sales. The dataset file used by the application is `vgsales.csv`.

## User Instructions

1. Open the dashboard using the provided Streamlit application link.
2. Use the release-year slider in the sidebar to select the years you want to explore.
3. Review the overview section to see key statistics for the selected period.
4. Explore the interactive chart to examine the number of video game records released per year.
5. Scroll to the data display section to view the filtered records.
6. Click the **Download Filtered Data as CSV** button to download the displayed data.
7. Review the insights section to learn more about the selected data.

Live Dashboard

Access the deployed application here:

https://video-games-data-project-msre2x8ysfqq8fgw3hbxrj.streamlit.app/

### Running the App Locally

To run the application on your computer:

1. Install Python.
2. Download or clone the project files.
3. Open a terminal in the project folder.
4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Start the application:

   ```bash
   streamlit run app.py
   ```

6. Open the local URL provided by Streamlit in your web browser.

Make sure `app.py`, `vgsales.csv`, and `requirements.txt` are in the appropriate project directory before running the application.
