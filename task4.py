import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('US_Accidents_March23.csv')

# Preview the data
print("Dataset Preview:")
print(df.head())

# Basic info
print("\nBasic Info:")
print(df.info())

# Drop rows with missing values in relevant columns
df = df.dropna(subset=['Weather_Condition', 'Start_Time'])

# Convert Start_Time to datetime and extract hour
df['Start_Time'] = pd.to_datetime(df['Start_Time'], errors='coerce')
df['Hour'] = df['Start_Time'].dt.hour

# ---------------------------------------
# 🔍 1. Accidents by Time of Day
plt.figure(figsize=(10, 5))
sns.countplot(x='Hour', data=df, palette='viridis')
plt.title('Accidents by Hour of the Day')
plt.xlabel('Hour')
plt.ylabel('Number of Accidents')
plt.grid(True)
plt.tight_layout()
plt.savefig('accidents_by_hour.png', dpi=300, bbox_inches='tight')  # ✅ Save the figure
plt.show()

# ---------------------------------------
# 🔍 2. Accidents by Weather Conditions
plt.figure(figsize=(12, 6))
top_weather = df['Weather_Condition'].value_counts().nlargest(10).index
sns.countplot(data=df[df['Weather_Condition'].isin(top_weather)], 
              y='Weather_Condition', order=top_weather, palette='coolwarm')
plt.title('Top 10 Weather Conditions During Accidents')
plt.xlabel('Count')
plt.ylabel('Weather Condition')
plt.tight_layout()
plt.savefig('accidents_by_weather.png', dpi=300, bbox_inches='tight')  # ✅ Save the figure
plt.show()

# ---------------------------------------
# 🔍 3. Accident Hotspots (if Latitude and Longitude are present)
if 'Start_Lat' in df.columns and 'Start_Lng' in df.columns:
    plt.figure(figsize=(10, 8))
    sns.scatterplot(data=df.sample(5000), x='Start_Lng', y='Start_Lat', alpha=0.3)
    plt.title('Accident Hotspots Map')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('accident_hotspots.png', dpi=300, bbox_inches='tight')  # ✅ Save the figure
    plt.show()
else:
    print("\nStart_Lat/Start_Lng columns not found for hotspot plotting.")
