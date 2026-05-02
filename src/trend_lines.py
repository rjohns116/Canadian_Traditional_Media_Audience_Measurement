import pandas as pd
import matplotlib.pyplot as plt

#Import clean datasets
audiovisual_clean = pd.read_csv(r"C:\Users\rlynj\OneDrive\Documents\Project-2\data\cleaned\audiovisual_cleaned.csv")
radio_clean = pd.read_csv(r"C:\Users\rlynj\OneDrive\Documents\Project-2\data\cleaned\radio_cleaned.csv")
television_clean = pd.read_csv(r"C:\Users\rlynj\OneDrive\Documents\Project-2\data\cleaned\television_cleaned.csv")

#Total hours consumed from newer digital audiovisual channels
av_total_hours = audiovisual_clean.groupby("Broadcast_Year")["Total_Quarterly_Hours"].sum().reset_index()

#Total hours consumed from traditional radio and tv combined
radio_and_tv = pd.concat([radio_clean, television_clean])

#English hours
english = radio_and_tv[radio_and_tv["Broadcast_Language"] == "English"]
english_total_hours = english.groupby("Broadcast_Year")["Total_Quarterly_Hours"].sum().reset_index()

#French hours
french = radio_and_tv[radio_and_tv["Broadcast_Language"] == "French"]
french_total_hours = french.groupby("Broadcast_Year")["Total_Quarterly_Hours"].sum().reset_index()

#Plot each line in a figure
plt.figure(figsize=(8,8))
plt.plot(av_total_hours["Broadcast_Year"], av_total_hours["Total_Quarterly_Hours"], label = "Audiovisual", color="green")
plt.plot(english_total_hours["Broadcast_Year"], english_total_hours["Total_Quarterly_Hours"], label="English (Radio & TV)", color="red")
plt.plot(french_total_hours["Broadcast_Year"], french_total_hours["Total_Quarterly_Hours"], label = "French (Radio & TV)", color="blue")
plt.legend()

plt.xlabel("Broadcast Year")
plt.ylabel("Total Quarterly Hours (billions)")
plt.title("Canadian Media Consuption Hours Over Time")

#Save figure
plt.savefig(r"C:\Users\rlynj\OneDrive\Documents\Project-2\docs\consumption_hours_over_time.jpg")
