import pandas as pd
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

#Reading Data in a File
df = pd.read_csv("cricket_data.csv")

#Analyzing the Data
summary = df.describe()
print(summary)

#Additional insights
average_runs = df['Runs'].mean()
max_runs = df['Runs'].max()
min_runs = df['Runs'].min()

average_wickets = df['Wickets'].mean()
max_wickets = df['Wickets'].max()
min_wickets = df['Wickets'].min()

average_strike_rate = df['Strike Rate'].mean()
max_strike_rate = df['Strike Rate'].max()
min_strike_rate = df['Strike Rate'].min()

average_economy = df['Economy'].mean()
max_economy = df['Economy'].max()
min_economy = df['Economy'].min()

#Creating the PDF
pdf = SimpleDocTemplate("report.pdf")
styles = getSampleStyleSheet()

elements = []

#Title of the PDF
elements.append(Paragraph("Cricket Analysis Report", styles['Title']))
elements.append(Spacer(1, 12))

#Dataset Preview
elements.append(Paragraph("Cricket Dataset Preview:", styles['Heading2']))
data_table = [df.columns.tolist()] + df.values.tolist()

table = Table(data_table)
table.setStyle(TableStyle([('BACKGROUND', (0,0), (-1,0), colors.grey),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('GRID', (0,0), (-1,-1), 1, colors.black)]))

elements.append(table)
elements.append(Spacer(1, 12))

# Insights Section
elements.append(Paragraph("Key Insights:", styles['Heading2']))
elements.append(Paragraph("Runs Summary:", styles['Heading3']))
elements.append(Paragraph(f"Average Runs: {average_runs:.2f}", styles['Normal']))
elements.append(Paragraph(f"Maximum Runs: {max_runs}", styles['Normal']))
elements.append(Paragraph(f"Minimum Runs: {min_runs}", styles['Normal']))
elements.append(Paragraph("Wickets Summary:", styles['Heading3']))
elements.append(Paragraph(f"Average Wickets: {average_wickets:.2f}", styles['Normal']))
elements.append(Paragraph(f"Maximum Wickets: {max_wickets}", styles['Normal']))
elements.append(Paragraph(f"Minimum Wickets: {min_wickets}", styles['Normal']))
elements.append(Paragraph("Strike Rate Summary:", styles['Heading3']))
elements.append(Paragraph(f"Average Strike Rate: {average_strike_rate:.2f}", styles['Normal']))
elements.append(Paragraph(f"Maximum Strike Rate: {max_strike_rate}", styles['Normal']))
elements.append(Paragraph(f"Minimum Strike Rate: {min_strike_rate}", styles['Normal']))
elements.append(Paragraph("Economy Summary:", styles['Heading3']))
elements.append(Paragraph(f"Average Economy: {average_economy:.2f}", styles['Normal']))
elements.append(Paragraph(f"Maximum Economy: {max_economy}", styles['Normal']))
elements.append(Paragraph(f"Minimum Economy: {min_economy}", styles['Normal']))

# Build PDF
pdf.build(elements)
print("✅ PDF report generated successfully!")