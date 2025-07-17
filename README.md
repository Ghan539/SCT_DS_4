# SCT_DS_4
analyzing and visualizing US traffic accident data (March 2023) using Pandas, Seaborn, and Matplotlib.
# US Accident Data Analysis (March 2023)

This project analyzes and visualizes traffic accident data in the United States using Python libraries like **Pandas**, **Seaborn**, and **Matplotlib**.

##  Dataset
- **File:** `US_Accidents_March23.csv`
- The dataset includes information like accident time, weather conditions, and location coordinates.

##  Visualizations
The script (`task4.py`) generates and saves the following graphs:

1. **Accidents by Hour of the Day**  
   A bar chart showing which hours have the most accidents.

2. **Top 10 Weather Conditions During Accidents**  
   A horizontal bar chart of the most common weather conditions at the time of accidents.

3. **Accident Hotspots (Scatter Plot)**  
   A map-like scatter plot of accident locations (if latitude and longitude are available).

##  Output Images
These visualizations are saved automatically as:
- `accidents_by_hour.png`
- `accidents_by_weather.png`
- `accident_hotspots.png`

## 🛠 How to Run

1. Install dependencies:

   ```bash
   pip install pandas matplotlib seaborn
