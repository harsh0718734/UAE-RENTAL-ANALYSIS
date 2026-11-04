# Dubai Rental Market Analysis

## About the Project

I created this project to explore Dubai's rental property market and understand how rental prices vary across different cities, locations and property types.

For this project, I used Python to analyse rental property data and worked on 27 analytical questions. The analysis focuses on rental prices, property sizes, rent per square foot, bedrooms, bathrooms, furnishing status and property types.

The main objective was to understand the dataset, identify useful patterns and present the analysis through visualisations.

## Dataset Information

- **Dataset:** Dubai Rental Property Data
- **Total Records:** Approximately 73,742
- **Total Columns:** 17
- **Domain:** Real Estate / Rental Market

## Tools & Technologies

- Python
- Pandas
- Matplotlib
- Seaborn

## Data Cleaning & Preparation

Before starting the analysis, I performed the following data preparation steps:

- Loaded the dataset using Pandas.
- Checked the first and last records.
- Examined missing values in each column.
- Standardised column names by removing extra spaces and replacing underscores.
- Removed duplicate records.
- Converted relevant columns into numeric data types.
- Checked the dataset structure and statistical summary.

## Exploratory Data Analysis (27 Questions)

I explored different aspects of Dubai's rental market through 27 questions.

### Rental Price Analysis

1. Compared average rental prices across cities and identified the highest and lowest.
2. Analysed average rent across different property types.
3. Compared average rental prices across different locations.
4. Identified cities with the minimum and maximum individual rent per square foot.
5. Compared average rent per square foot across cities.
6. Identified property types with the minimum and maximum individual rent per square foot.
7. Analysed average rent per square foot across property types.
8. Identified locations with the minimum and maximum individual rent per square foot.
9. Compared average rent per square foot across locations.

### Property Area Analysis

10. Identified cities with the smallest and largest individual property areas.
11. Compared average property areas across cities.
12. Identified property types with the smallest and largest individual property areas.
13. Analysed average property areas across property types.
14. Identified locations with the smallest and largest individual property areas.
15. Compared average property areas across locations.

### Property Features & Market Trends

16. Analysed average rent based on bedrooms and rent categories.
17. Compared city-wise average rent across rent categories.
18. Studied bathroom-wise average rent based on furnishing status.
19. Created a correlation heatmap for numerical variables.
20. Compared average property area across cities based on furnishing.
21. Analysed city-wise average rent per square foot across rent categories.
22. Examined property type counts across different cities.
23. Compared average rent by property type across cities.
24. Analysed city-wise average rent based on furnishing status.
25. Identified the top 5 most expensive cities based on average rent.
26. Identified the top 5 cheapest building types based on average rent.
27. Identified the top 5 most expensive locations based on average rent.

## Project Visualisations & Analysis

I used Matplotlib and Seaborn to create charts that make the results easier to understand and compare.

### 1. Bathroom-wise Average Rent

![Bathroom-wise Average Rent](visualizations/baths_wise_average_rent.png)

This chart compares average rental prices based on the number of bathrooms. It helps understand how rental prices vary with bathroom availability.

### 2. Bedroom-wise Average Rent

![Bedroom-wise Average Rent](visualizations/bedroom_wise_average_rent.png)

This visualisation shows average rental prices based on the number of bedrooms and different rent categories.

### 3. City-wise Area by Furnishing

![City-wise Area by Furnishing](visualizations/city_wise_area_by_furnishing.png)

This chart compares average property areas across cities based on furnishing status. It helps examine differences in property sizes between furnished and unfurnished listings.

### 4. City-wise Average Rent

![City-wise Average Rent](visualizations/city_wise_average_rent.png)

This chart compares average rental prices across cities and helps identify differences in rental costs between locations.

### 5. City-wise Property Type Count

![City-wise Property Type Count](visualizations/city_wise_property_type_count.png)

This visualisation shows the distribution of different property types across cities. It helps understand which property types appear more frequently in the dataset.

### 6. City-wise Rent by Furnishing

![City-wise Rent by Furnishing](visualizations/city_wise_rent_by_furnishing.png)

This chart compares average rental prices across cities according to furnishing status. It helps explore how furnishing is associated with rental prices.

### 7. City-wise Rent per Sqft by Rent Category

![City-wise Rent per Sqft by Rent Category](visualizations/city_wise_rent_per_sqft_by_rent_category.png)

This visualisation compares average rent per square foot across cities and rent categories, providing another way to examine rental price differences.

### 8. Correlation Heatmap

![Correlation Heatmap](visualizations/correlation_heatmap.png)

The correlation heatmap displays relationships between numerical variables such as bedrooms, bathrooms, property area, rent and rent per square foot. It helps identify positive and negative correlations between these variables.

### 9. Property Type-wise Average Rent

![Property Type-wise Average Rent](visualizations/property_type_wise_average_rent.png)

This chart compares average rental prices across different property types and helps understand how rental costs vary by property category.

## Key Learnings

While working on this project, I gained practical experience in:

- Working with a real-world real estate dataset.
- Cleaning and preparing data using Pandas.
- Using GroupBy, aggregation and sorting operations.
- Performing Exploratory Data Analysis.
- Comparing rental prices and property features.
- Creating visualisations using Matplotlib and Seaborn.
- Understanding patterns and trends through data.
- Presenting analytical findings in a structured way.

## Conclusion

This project gave me an opportunity to work with real estate rental data and explore different factors affecting rental prices in Dubai.

By working through 27 analytical questions, I was able to compare cities, property types, locations, property sizes and furnishing categories.

It also helped me strengthen my Python, Pandas and data visualisation skills and improve my understanding of the Exploratory Data Analysis process.
