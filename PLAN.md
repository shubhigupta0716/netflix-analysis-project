Netflix Data Analysis Project

Problem Statements


1. Are Movies or TV Shows more common on Netflix?
2. What content ratings appear most frequently on the platform?
3. How has Netflix’s content library grown over the years?
4. Which countries contribute the most content to Netflix?
5. What genres are most popular among Netflix titles?

Goals

* Learn how to work with a real-world dataset using pandas.
* Clean and organize the data by handling missing values and formatting columns.
* Create visualizations that help answer the selected questions.
* Practice drawing meaningful conclusions from data.
* Document the entire workflow using Jupyter Notebook and GitHub.

Non-Goals

* Building machine learning models.
* Predicting future Netflix trends.
* Creating a recommendation system.
* Performing advanced text analysis on movie descriptions.

Requirements

Tools

* Python
* VS Code
* Jupyter Notebook
* Git and GitHub

Libraries

* pandas
* numpy
* matplotlib
* seaborn

Dataset

* Netflix Titles Dataset from Kaggle

Timeline

Set up the project structure, download the dataset, and understand the available data.

Clean the dataset by handling missing values and preparing it for analysis.

Create charts and visualizations to answer the selected problem statements.

Summarize findings, update documentation, and upload the completed project to GitHub.

Expected Outcome

By the end of the project, I will have a cleaned dataset, a Jupyter notebook containing the analysis, several visualizations, and a GitHub repository documenting the complete workflow and findings.

Why This Cleaning Strategy?

The Netflix dataset contained missing values in columns such as director, cast, and country. Instead of dropping these records, placeholder values were used to preserve as much information as possible. Date fields were converted to datetime format and duplicate records were removed to improve data quality.

What Happens With New Data?

When new Netflix records are added, the ingestion module will load the dataset and validate the schema. Great Expectations will check that important columns and data formats remain consistent. The cleaning module can then automatically apply the same transformations, making the pipeline reusable for future updates.