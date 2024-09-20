import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


# Import my CSV file
file_path = r'C:\Users\PIQIU\pfad\assignment1/Sun_rise_set_2024.csv'
data = pd.read_csv(file_path)

# Check data
print(data.head(30))

# Extract date and sunrise time
sunrise_data = data[['Date', 'Sunrise']]

# Convert the date column to datetime format
sunrise_data['Date'] = pd.to_datetime(sunrise_data['Date'])
sunrise_data['Sunrise'] = pd.to_datetime(sunrise_data['Sunrise'])
sunrise_data = sunrise_data.iloc[:30]

# Draw a line chart
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(sunrise_data['Date'], sunrise_data['Sunrise'], marker='o', linestyle='-', color='red', linewidth=2) 

# Draw 'sun point'！
ax.scatter(sunrise_data['Date'], sunrise_data['Sunrise'], marker='*', color='orange', s=250, label='Sunrise Time!') 

# Set chart settings
ax.set_title ('2024-01 Sun Rise Time', fontsize=24, fontweight='bold', color='darkblue')
ax.set_xlabel ('Date', fontsize=14)
ax.set_ylabel ('Sunrise Time', fontsize=14)

# Set x-axis date format and tick intervals
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
ax.xaxis.set_major_locator(mdates.DayLocator(interval=4))

# Add grid
ax.grid(visible=True, linestyle='--', alpha=0.5)
ax.legend()

plt.tight_layout()
plt.show()
