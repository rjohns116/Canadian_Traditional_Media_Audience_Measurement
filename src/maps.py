import pandas as pd
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go


#Import clean datasets
audiovisual_clean = pd.read_csv(r"C:\Users\rlynj\OneDrive\Documents\Project-2\data\cleaned\audiovisual_cleaned.csv")
radio_clean = pd.read_csv(r"C:\Users\rlynj\OneDrive\Documents\Project-2\data\cleaned\radio_cleaned.csv")
television_clean = pd.read_csv(r"C:\Users\rlynj\OneDrive\Documents\Project-2\data\cleaned\television_cleaned.csv")

#Combine radio and television data
radio_and_tv = pd.concat([radio_clean, television_clean]).drop(columns = ["Service_Type", "Broadcast_Quarter"])

#Fold radio markets into television markets
radio_and_tv["Market"] = radio_and_tv["Market"].replace({
                         "Calgary" : "Central",
                         "Edmonton": "Central",
                         "Montreal": "Quebec",
                         "Toronto": "Ontario",
                         "Vancouver": "West"
})

#Create summarized dataframes for each map and store in a list
dfs = []

#Map 1
map_1 = radio_and_tv[radio_and_tv["Broadcast_Year"] == 2019]


map_1F = map_1[map_1["Broadcast_Language"] == "French"]
hours_per_market_F = map_1F.groupby("Market")["Total_Quarterly_Hours"].sum().reset_index()
hours_per_market_F["Latitude"] = [54.574, 54.037, 51.245, 51.051, 54.574]
hours_per_market_F["Longitude"] = [-61.217, -106.336, -86.999, -73.225, -126.644]
hours_per_market_F["Broadcast_Language"] = "French"

map_1E = map_1[map_1["Broadcast_Language"] == "English"]
hours_per_market_E = map_1E.groupby("Market")["Total_Quarterly_Hours"].sum().reset_index()
hours_per_market_E["Latitude"] = [53.574, 53.037, 50.245, 50.051, 53.574]
hours_per_market_E["Longitude"] = [-61.217, -106.336, -86.999, -73.225, -126.644]
hours_per_market_E["Broadcast_Language"] = "English"

hours_per_market_1 = pd.concat([hours_per_market_F, hours_per_market_E], ignore_index=True)
dfs.append(hours_per_market_1)

#Map 2
map_2 = radio_and_tv[radio_and_tv["Broadcast_Year"] == 2020]

map_2F = map_2[map_2["Broadcast_Language"] == "French"]
hours_per_market_F = map_2F.groupby("Market")["Total_Quarterly_Hours"].sum().reset_index()
hours_per_market_F["Latitude"] = [54.574, 54.037, 51.245, 51.051, 54.574]
hours_per_market_F["Longitude"] = [-61.217, -106.336, -86.999, -73.225, -126.644]
hours_per_market_F["Broadcast_Language"] = "French"

map_2E = map_2[map_2["Broadcast_Language"] == "English"]
hours_per_market_E = map_2E.groupby("Market")["Total_Quarterly_Hours"].sum().reset_index()
hours_per_market_E["Latitude"] = [53.574, 53.037, 50.245, 50.051, 53.574]
hours_per_market_E["Longitude"] = [-61.217, -106.336, -86.999, -73.225, -126.644]
hours_per_market_E["Broadcast_Language"] = "English"

hours_per_market_2 = pd.concat([hours_per_market_F, hours_per_market_E], ignore_index=True)
dfs.append(hours_per_market_2)

#Map 3
map_3 = radio_and_tv[radio_and_tv["Broadcast_Year"] == 2021]

map_3F = map_3[map_3["Broadcast_Language"] == "French"]
hours_per_market_F = map_3F.groupby("Market")["Total_Quarterly_Hours"].sum().reset_index()
hours_per_market_F["Latitude"] = [54.574, 54.037, 51.245, 51.051, 54.574]
hours_per_market_F["Longitude"] = [-61.217, -106.336, -86.999, -73.225, -126.644]
hours_per_market_F["Broadcast_Language"] = "French"

map_3E = map_3[map_3["Broadcast_Language"] == "English"]
hours_per_market_E = map_3E.groupby("Market")["Total_Quarterly_Hours"].sum().reset_index()
hours_per_market_E["Latitude"] = [53.574, 53.037, 50.245, 50.051, 53.574]
hours_per_market_E["Longitude"] = [-61.217, -106.336, -86.999, -73.225, -126.644]
hours_per_market_E["Broadcast_Language"] = "English"

hours_per_market_3 = pd.concat([hours_per_market_F, hours_per_market_E], ignore_index=True)
dfs.append(hours_per_market_3)

#Map 4
map_4 = radio_and_tv[radio_and_tv["Broadcast_Year"] == 2022]

map_4F = map_4[map_4["Broadcast_Language"] == "French"]
hours_per_market_F = map_4F.groupby("Market")["Total_Quarterly_Hours"].sum().reset_index()
hours_per_market_F["Latitude"] = [54.574, 54.037, 51.245, 51.051, 54.574]
hours_per_market_F["Longitude"] = [-61.217, -106.336, -86.999, -73.225, -126.644]
hours_per_market_F["Broadcast_Language"] = "French"

map_4E = map_4[map_4["Broadcast_Language"] == "English"]
hours_per_market_E = map_4E.groupby("Market")["Total_Quarterly_Hours"].sum().reset_index()
hours_per_market_E["Latitude"] = [53.574, 53.037, 50.245, 50.051, 53.574]
hours_per_market_E["Longitude"] = [-61.217, -106.336, -86.999, -73.225, -126.644]
hours_per_market_E["Broadcast_Language"] = "English"

hours_per_market_4 = pd.concat([hours_per_market_F, hours_per_market_E], ignore_index=True)
dfs.append(hours_per_market_4)

#Map 5
map_5 = radio_and_tv[radio_and_tv["Broadcast_Year"] == 2023]

map_5F = map_5[map_5["Broadcast_Language"] == "French"]
hours_per_market_F = map_5F.groupby("Market")["Total_Quarterly_Hours"].sum().reset_index()
hours_per_market_F["Latitude"] = [54.574, 54.037, 51.245, 51.051, 54.574]
hours_per_market_F["Longitude"] = [-61.217, -106.336, -86.999, -73.225, -126.644]
hours_per_market_F["Broadcast_Language"] = "French"

map_5E = map_5[map_5["Broadcast_Language"] == "English"]
hours_per_market_E = map_5E.groupby("Market")["Total_Quarterly_Hours"].sum().reset_index()
hours_per_market_E["Latitude"] = [53.574, 53.037, 50.245, 50.051, 53.574]
hours_per_market_E["Longitude"] = [-61.217, -106.336, -86.999, -73.225, -126.644]
hours_per_market_E["Broadcast_Language"] = "English"

hours_per_market_5 = pd.concat([hours_per_market_F, hours_per_market_E], ignore_index=True)
dfs.append(hours_per_market_5)

#Map 6
map_6 = radio_and_tv[radio_and_tv["Broadcast_Year"] == 2024]

map_6F = map_6[map_6["Broadcast_Language"] == "French"]
hours_per_market_F = map_6F.groupby("Market")["Total_Quarterly_Hours"].sum().reset_index()
hours_per_market_F["Latitude"] = [54.574, 54.037, 51.245, 51.051, 54.574]
hours_per_market_F["Longitude"] = [-61.217, -106.336, -86.999, -73.225, -126.644]
hours_per_market_F["Broadcast_Language"] = "French"

map_6E = map_6[map_6["Broadcast_Language"] == "English"]
hours_per_market_E = map_6E.groupby("Market")["Total_Quarterly_Hours"].sum().reset_index()
hours_per_market_E["Latitude"] = [53.574, 53.037, 50.245, 50.051, 53.574]
hours_per_market_E["Longitude"] = [-61.217, -106.336, -86.999, -73.225, -126.644]
hours_per_market_E["Broadcast_Language"] = "English"

hours_per_market_3 = pd.concat([hours_per_market_F, hours_per_market_E], ignore_index=True)
dfs.append(hours_per_market_3)

#Map 7
map_7 = radio_and_tv[radio_and_tv["Broadcast_Year"] == 2025]

map_7F = map_7[map_7["Broadcast_Language"] == "French"]
hours_per_market_F = map_7F.groupby("Market")["Total_Quarterly_Hours"].sum().reset_index()
hours_per_market_F["Latitude"] = [54.574, 54.037, 51.245, 51.051, 54.574]
hours_per_market_F["Longitude"] = [-61.217, -106.336, -86.999, -73.225, -126.644]
hours_per_market_F["Broadcast_Language"] = "French"

map_7E = map_7[map_7["Broadcast_Language"] == "English"]
hours_per_market_E = map_7E.groupby("Market")["Total_Quarterly_Hours"].sum().reset_index()
hours_per_market_E["Latitude"] = [53.574, 53.037, 50.245, 50.051, 53.574]
hours_per_market_E["Longitude"] = [-61.217, -106.336, -86.999, -73.225, -126.644]
hours_per_market_E["Broadcast_Language"] = "English"

hours_per_market_7 = pd.concat([hours_per_market_F, hours_per_market_E], ignore_index=True)
dfs.append(hours_per_market_7)

#Create maps for each dataframe

figs = []

for df, i in zip(dfs, range(1,8)):
    fig = px.scatter_geo(df,
            lat = "Latitude",
            lon = "Longitude",
            color = "Broadcast_Language",
            size = "Total_Quarterly_Hours",
            scope = "north america",
            size_max = 50,
            hover_name = "Market",
            hover_data = {
                "Broadcast_Language": True,
                "Total_Quarterly_Hours": True,
                "Latitude": False,
                "Longitude": False
                },
               )

    fig.update_traces(marker=dict(sizemin=7))

    
    figs.append(fig)

#Create one figure to put all of the maps into with a dropdown menu
combined = go.Figure()

for i, fig in enumerate(figs):
    for t in fig.data:
        combined.add_trace(t.update(visible=(i == 0)))

buttons = []
years = [2019, 2020, 2021, 2022, 2023, 2024, 2025]

traces = [len(fig.data) for fig in figs]
total_traces = sum(traces)
start = 0

for i, year in enumerate(years):
    visibility = [False] * total_traces

    count = traces[i]

    for j in range(start, start + count):
        visibility[j] = True

    start += count
 
    buttons.append(
        dict(
            label = str(year),
            method = "update",
            args= [{"visible" : visibility},
                {"title": str(year)}]
        )
    )

combined.update_layout(
    updatemenus=[dict(
        active = 0,
        buttons = buttons,
        x=1.15,
        y=1.15)
    ],
    title = "Map 1"
)

combined.update_geos(scope="north america")

combined.write_html(r"C:\Users\rlynj\OneDrive\Documents\Project-2\docs\maps.html", include_plotlyjs = "cdn")

combined.show()