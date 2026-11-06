import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# DATASET LOAD
df=pd.read_csv("UAE.csv")
print(df.head())
print(df.tail())
print(df.isnull().sum())
print(df.columns)

# CLEANING COLUMNS
df.columns=df.columns.str.strip().str.upper().str.replace("_"," ")
print(df.columns)

# DROPPING DUPLICATES
df=df.drop_duplicates()
print(df.shape)

# NUMERIC COLUMNS
df["RENT"]=df["RENT"].astype(float)
print(df["RENT"])

df["AREA IN SQFT"]=df["AREA IN SQFT"].astype(float)
print(df["AREA IN SQFT"])
df.info()


# QUESTION NO.1 CITY WISE AVERAGE RENT ANALYSIS

cheapest_city=df.groupby("CITY")["RENT"].mean().sort_values(ascending=True).head(4)
print(f"THE CHEAPEST CITIES ACCORDING TO AVERAGE RENT ARE:\n{cheapest_city}")

expensive_city=df.groupby("CITY")["RENT"].mean().sort_values(ascending=False).head(4)
print(f"THE MOST EXPENSIVE CITIES ACCORDING TO AVERAGE RENT ARE:\n{expensive_city}")


# QUESTION NO.2 PROPERTY TYPE WISE AVERAGE RENT ANALYSIS

cheapest_property_type=df.groupby("TYPE")["RENT"].mean().sort_values(ascending=True).head(4)
print(f"THE CHEAPEST PROPERTY TYPES ACCORDING TO AVERAGE RENT ARE:\n{cheapest_property_type}")

expensive_property_type=df.groupby("TYPE")["RENT"].mean().sort_values(ascending=False).head(4)
print(f"THE MOST EXPENSIVE PROPERTY TYPES ACCORDING TO AVERAGE RENT ARE:\n{expensive_property_type}")


# QUESTION NO.3 LOCATION WISE AVERAGE RENT ANALYSIS

cheapest_location_rent=df.groupby("LOCATION")["RENT"].mean().sort_values(ascending=True).head(5)
print(f"THE CHEAPEST LOCATIONS ACCORDING TO AVERAGE RENT ARE:\n{cheapest_location_rent}")

expensive_location_rent=df.groupby("LOCATION")["RENT"].mean().sort_values(ascending=False).head(5)
print(f"THE MOST EXPENSIVE LOCATIONS ACCORDING TO AVERAGE RENT ARE:\n{expensive_location_rent}")


# QUESTION NO.4 WHICH CITY HAS THE MINIMUM AND MAXIMUM INDIVIDUAL RENT PER SQFT

cheapest_city=df.groupby("CITY")["RENT PER SQFT"].min().idxmin()
print(f"{cheapest_city} HAS THE LOWEST INDIVIDUAL RENT PER SQFT LISTING")

expensive_city=df.groupby("CITY")["RENT PER SQFT"].max().idxmax()
print(f"{expensive_city} HAS THE HIGHEST INDIVIDUAL RENT PER SQFT LISTING")


# QUESTION NO.5 CITY WISE AVERAGE RENT PER SQFT

cheapest_city=df.groupby("CITY")["RENT PER SQFT"].mean().sort_values(ascending=True).head(4)
print(f"THE CHEAPEST CITIES ACCORDING TO AVERAGE RENT PER SQFT ARE:\n{cheapest_city}")

expensive_city=df.groupby("CITY")["RENT PER SQFT"].mean().sort_values(ascending=False).head(4)
print(f"THE MOST EXPENSIVE CITIES ACCORDING TO AVERAGE RENT PER SQFT ARE:\n{expensive_city}")


# QUESTION NO.6 WHICH PROPERTY TYPE HAS THE MINIMUM AND MAXIMUM INDIVIDUAL RENT PER SQFT

cheapest_property_type = df.groupby("TYPE")["RENT PER SQFT"].min().idxmin()
print(f"THE PROPERTY TYPE WITH THE LOWEST INDIVIDUAL RENT PER SQFT LISTING IS: {cheapest_property_type}")

expensive_property_type = df.groupby("TYPE")["RENT PER SQFT"].max().idxmax()
print(f"THE PROPERTY TYPE WITH THE HIGHEST INDIVIDUAL RENT PER SQFT LISTING IS: {expensive_property_type}")


# QUESTION NO.7 PROPERTY TYPE WISE AVERAGE RENT PER SQFT

cheapest_property_type = df.groupby("TYPE")["RENT PER SQFT"].mean().sort_values(ascending=True).head(4)
print(f"THE CHEAPEST PROPERTY TYPES ACCORDING TO AVERAGE RENT PER SQFT ARE:\n{cheapest_property_type}")

expensive_property_type = df.groupby("TYPE")["RENT PER SQFT"].mean().sort_values(ascending=False).head(4)
print(f"THE MOST EXPENSIVE PROPERTY TYPES ACCORDING TO AVERAGE RENT PER SQFT ARE:\n{expensive_property_type}")


# QUESTION NO.8 WHICH LOCATION HAS THE MINIMUM AND MAXIMUM INDIVIDUAL RENT PER SQFT

cheapest_location = df.groupby("LOCATION")["RENT PER SQFT"].min().idxmin()
print(f"THE LOCATION WITH THE LOWEST INDIVIDUAL RENT PER SQFT LISTING IS: {cheapest_location}")

expensive_location = df.groupby("LOCATION")["RENT PER SQFT"].max().idxmax()
print(f"THE LOCATION WITH THE HIGHEST INDIVIDUAL RENT PER SQFT LISTING IS: {expensive_location}")


# QUESTION NO.9 LOCATION WISE AVERAGE RENT PER SQFT

cheapest_location = df.groupby("LOCATION")["RENT PER SQFT"].mean().sort_values(ascending=True).head(5)
print(f"THE CHEAPEST LOCATIONS ACCORDING TO AVERAGE RENT PER SQFT ARE:\n{cheapest_location}")

expensive_location = df.groupby("LOCATION")["RENT PER SQFT"].mean().sort_values(ascending=False).head(5)
print(f"THE MOST EXPENSIVE LOCATIONS ACCORDING TO AVERAGE RENT PER SQFT ARE:\n{expensive_location}")


# QUESTION NO.10 WHICH CITY HAS THE SMALLEST AND LARGEST INDIVIDUAL AREA IN SQFT

smallest_area_city=df.groupby("CITY")["AREA IN SQFT"].min().idxmin()
print(f"THE CITY WITH THE SMALLEST INDIVIDUAL AREA IN SQFT IS: {smallest_area_city}")

largest_area_city=df.groupby("CITY")["AREA IN SQFT"].max().idxmax()
print(f"THE CITY WITH THE LARGEST INDIVIDUAL AREA IN SQFT IS: {largest_area_city}")


# QUESTION NO.11 CITY WISE AVERAGE AREA IN SQFT

smallest_area_city=df.groupby("CITY")["AREA IN SQFT"].mean().sort_values(ascending=True).head(5)
print(f"THE CITIES WITH THE SMALLEST AVERAGE AREA IN SQFT ARE:\n{smallest_area_city}")

largest_area_city=df.groupby("CITY")["AREA IN SQFT"].mean().sort_values(ascending=False).head(5)
print(f"THE CITIES WITH THE LARGEST AVERAGE AREA IN SQFT ARE:\n{largest_area_city}")


# QUESTION NO.12 WHICH PROPERTY TYPE HAS THE SMALLEST AND LARGEST INDIVIDUAL AREA IN SQFT

smallest_area_property_type=df.groupby("TYPE")["AREA IN SQFT"].min().idxmin()
print(f"THE PROPERTY TYPE WITH THE SMALLEST INDIVIDUAL AREA IN SQFT IS: {smallest_area_property_type}")

largest_area_property_type=df.groupby("TYPE")["AREA IN SQFT"].max().idxmax()
print(f"THE PROPERTY TYPE WITH THE LARGEST INDIVIDUAL AREA IN SQFT IS: {largest_area_property_type}")


# QUESTION NO.13 PROPERTY TYPE WISE AVERAGE AREA IN SQFT

smallest_area_property_type = df.groupby("TYPE")["AREA IN SQFT"].mean().sort_values(ascending=True).head(5)
print(f"THE PROPERTY TYPES WITH THE SMALLEST AVERAGE AREA IN SQFT ARE:\n{smallest_area_property_type}")

largest_area_property_type = df.groupby("TYPE")["AREA IN SQFT"].mean().sort_values(ascending=False).head(5)
print(f"THE PROPERTY TYPES WITH THE LARGEST AVERAGE AREA IN SQFT ARE:\n{largest_area_property_type}")


# QUESTION NO.14 WHICH LOCATION HAS THE SMALLEST AND LARGEST INDIVIDUAL AREA IN SQFT

smallest_area_location=df.groupby("LOCATION")["AREA IN SQFT"].min().idxmin()
print(f"THE LOCATION WITH THE SMALLEST INDIVIDUAL AREA IN SQFT IS: {smallest_area_location}")

largest_area_location=df.groupby("LOCATION")["AREA IN SQFT"].max().idxmax()
print(f"THE LOCATION WITH THE LARGEST INDIVIDUAL AREA IN SQFT IS: {largest_area_location}")


# QUESTION NO.15 LOCATION WISE AVERAGE AREA IN SQFT

smallest_area_location=df.groupby("LOCATION")["AREA IN SQFT"].mean().sort_values(ascending=True).head(5)
print(f"THE LOCATIONS WITH THE SMALLEST AVERAGE AREA IN SQFT ARE:\n{smallest_area_location}")

largest_area_location=df.groupby("LOCATION")["AREA IN SQFT"].mean().sort_values(ascending=False).head(5)
print(f"THE LOCATIONS WITH THE LARGEST AVERAGE AREA IN SQFT ARE:\n{largest_area_location}")



# QUESTION NO.16  BEDROOM-WISE AVERAGE RENT ANALYSIS BY RENT CATEGORY

plt.style.use("ggplot")
plt.figure(figsize=(10,4))
sns.barplot(x="BEDS",y="RENT",hue="RENT CATEGORY",data=df)
plt.xlabel("BEDS")
plt.ylabel("AVERAGE RENT")
plt.title("BAR PLOT:BEDROOM WISE AVERAGE RENT BY RENT CATEGORY")
plt.savefig("bedroom_wise_average_rent.png", bbox_inches="tight")
plt.show()

# QUESTION NO.17 CITY WISE AVERAGE RENT ANALYSIS  BY RENT CATEGORY
plt.style.use("ggplot")
plt.figure(figsize=(10,4))
sns.barplot(x="CITY",y="RENT",hue="RENT CATEGORY",data=df)
plt.xlabel("CITY")
plt.ylabel("AVERAGE RENT")
plt.title("BAR PLOT:CITY WISE AVERAGE RENT BY RENT CATEGORY")
plt.savefig("city_wise_average_rent.png", bbox_inches="tight")
plt.show()

# QUESTION NO.18 BATHS-WISE AVERAGE RENT ANALYSIS BY FURNISHING CATEGORY

plt.style.use("bmh")
plt.figure(figsize=(10,4))
sns.barplot(x="BATHS",y="RENT",hue="FURNISHING",data=df)
plt.xlabel("BATHS")
plt.ylabel("AVERAGE RENT")
plt.title("BAR PLOT:BATH WISE AVERAGE RENT BY FURNISHING CATEGORY")
plt.savefig("baths_wise_average_rent.png", bbox_inches="tight")
plt.show()


# QUESTION NO.19 CREATE A CORRELATION HEATMAP TO ANALYSE THE RELATIONSHIP

corr=df[["BEDS","BATHS","AREA IN SQFT","RENT","RENT PER SQFT"]].corr()

sns.heatmap(corr,annot=True,cmap="coolwarm")

plt.title("HEAT MAP:DUBAI PROPERTY CORRELATION HEATMAP")
plt.savefig("correlation_heatmap.png", bbox_inches="tight")
plt.show()

# QUESTION NO.20 CITY WISE AREA IN  SQFT BY FURNISHING CATEGORY


plt.style.use("ggplot")
plt.figure(figsize=(10,4))
sns.barplot(x="CITY",y="AREA IN SQFT",hue="FURNISHING",data=df)
plt.xlabel("CITY")
plt.ylabel("AVERAGE AREA IN SQFT")
plt.title("BAR PLOT:CITY WISE AVERAGE AREA IN SQFT BY FURNISHING")
plt.savefig("city_wise_area_by_furnishing.png", bbox_inches="tight")
plt.show()

# QUESTION NO.21 CITY WISE AVERAGE RENT PER SQFT BY RENT CATEGORY

plt.style.use("ggplot")
plt.figure(figsize=(10,4))
sns.barplot(x="CITY",y="RENT PER SQFT",hue="RENT CATEGORY",data=df)
plt.xlabel("CITY")
plt.ylabel("AVERAGE RENT PER SQFT")
plt.title("BAR PLOT:CITY WISE AVERAGE RENT PER SQFT BY RENT CATEGORY")
plt.savefig("city_wise_rent_per_sqft_by_rent_category.png", bbox_inches="tight")
plt.show()

# QUESTION NO.22 CITY-WISE PROPERTY TYPE COUNT

plt.style.use("bmh")
plt.figure(figsize=(8,4))
sns.countplot(x="CITY", hue="TYPE", data=df)
plt.xlabel("CITY")
plt.ylabel("PROPERTY COUNT")
plt.title("COUNT PLOT:CITY-WISE PROPERTY TYPE COUNT")
plt.savefig("city_wise_property_type_count.png", bbox_inches="tight")
plt.show()

# QUESTION NO.23 PROPERTY TYPE LISTING  VS AVERAGE RENT BY CITY CATEGORY

plt.style.use("ggplot")
plt.figure(figsize=(10,5))
sns.barplot(x="TYPE",y="RENT" ,hue="CITY",data=df)
plt.xlabel("PROPERTY TYPE")
plt.ylabel("AVERAGE RENT")
plt.title("BARPLOT:PROPERTY TYPE VS AVERAGE RENT BY CITY CATEGORY")
plt.savefig("property_type_wise_average_rent.png", bbox_inches="tight")
plt.show()

# QUESTION NO.24  CITY VS RENT BY FURNISHING CATEGORY

plt.style.use("ggplot")
plt.figure(figsize=(10,4))
sns.barplot(x="CITY",y="RENT",hue="FURNISHING",data=df)
plt.xlabel("CITY")
plt.ylabel("AVERAGE RENT")
plt.title("BAR PLOT:CITY WISE AVERAGE RENT BY FURNISHING CATEGORY")
plt.savefig("city_wise_rent_by_furnishing.png", bbox_inches="tight")
plt.show()

# QUESTION NO.25 TOP 5 EXPENSIVE CITIES

expensive_cities=df.groupby("CITY")["RENT"].mean().sort_values(ascending=False).head(5)
print(f"THE TOP 5 EXPENSIVE CITIES ARE: {expensive_cities}")

# QUESTION NO.26 TOP 5 CHEAPEST BUILDING TYPES
cheapest_building_types=df.groupby("TYPE")["RENT"].mean().sort_values(ascending=True).head(5)
print(f"THE TOP 5 CHEAPEST BUILDING TYPES ARE: {cheapest_building_types}")

# QUESTION NO.27 TOP 5 EXPENSIVE LOCATION TO STAY
expensive_locations=df.groupby("LOCATION")["RENT"].mean().sort_values(ascending=False).head(5)
print(f"THE TOP 5 EXPENSIVE LOCATIONS TO STAY ARE: {expensive_locations}")

print(df.describe())
df.info()

print("UAE RENTAL ANALYSIS PROJECT COMPLETED SUCCESSFULLY")
print("THANK YOU")
