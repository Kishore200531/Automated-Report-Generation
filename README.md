# Automated-Report-Generation

Company: CODTECH IT SOLUTIONS

Name: UDATA JOSEPH KISHORE

Intern ID: CTIS7316

Domain: PYTHON PROGRAMMING

Duration: 4 Weeks

Mentor: NEELA SANTOSH KUMAR

Task Description:

I've used Pycharm for programming. Task Title: Automated Report Generation. In this code at starting I've imported the required libraries - Pandas imported as pd ( For Data Manipulation and Reading), SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle imported from reportlab.platypus (For structuring and formatting the data in the report/pdf), colors imported from reportlab.lib (For text coloring), getSampleStyleSheet imported from reportlab.lib.styles (For making data stuctured as Title, Heading, etc.). After importing the required libraries I've started reading the data using pandas library for loading and reading the data in cricket_data.csv file and is stored in the variable df. And then I've printed the summary of the data in the file which gives the details of count, mean, standarad deviation, minimum, maximum and some more using the describe() method. Aand then I've extracted some of the data insights for several fields in the file like avarage runs, maximum runs, minimum runs, average wickets, maximum wickets, minimum wickets, average strike rate, maximum strike rate, minimum strike rate, average economy, maximum economy, minimum economy using the methods such as mean(), max() and min(). After extraction of some insights I've created the PDF using SimpleDocTemplate() library and named it as report and stored this in pdf variable. And for styling the pdf I've used getSampleStyleSheet() library. To add the data to the pdf (report) I've used a list elements for storing the data. And then I've started formatting the pdf by giving it a title "Cricket Analysis Report" using Paragraph library and it is given a style called Title. And then this title text font size is given as (1,12) where width = 1, height = 12 using the Spacer library. And then I've loaded the preview of the cricket data by giving it a heading "Cricket Dataset Preview:" using Paragraph library. And the preview data is stored as a table so I've created a table using Table library by extracted the colums and their values to the data_table variable. This table is stored in the variable named table. And the text in the table is formatted and styled using TableStyle library and setStyle() method. And then the formatted and styled table is added to the list elements using append method and its font size is given by (1,12) as width = 1, height = 12. And then I've added the insights that are extracted from the cricket data to the elements lists by giving a heading "Key Insights". And then further the insights are given by sub headings (Runs Summary, Wickets Summary, Strike Rate Summary and Economy Summary with the average, maximum and minimum insights). Where these insights are styled by using Paragraph library using styles like Heading2 for main heading Key Insights and Heading3 for the sub headings such as Runs Summary, Wickets Summary, Strike Rate Summary and Economy Summary and then the insights are formatted as the Normal text. And then to build the pdf/report I've used build method and the data in file is taken from the list elements (pdf.build(elements)). And then finally I've printed that "PDF report generated successfully!" to notify us the pdf is created successfully with the data inside it.

Data Flow of the Program:

CSV -> DataFrame -> Analysis -> Insights -> Formatting -> PDF -> Output

I've used the cricket data for this report generation using python. You can go with any other dataset to create the report/pdf.
