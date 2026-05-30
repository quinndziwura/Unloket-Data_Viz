# Unloket-Data_Viz
**BUS 32130: Data Visualization for Decision-Making / Spring 2026**  
Odysseas Koufos · Miltiadis Hadjipanayiotou · Quinn Dziwura

# What This Project Is

Unloket is an AI hospitality concierge platform founded by Odysseas Koufos. It handles guest messaging automatically over SMS and WhatsApp for hotel properties, and is currently a finalist in the 2026 New Venture Challenge at the University of Chicago.

For this project, Odysseas gave us direct access to real operational data from a live pilot property operating the Unloket platform. Our goal was to build a dashboard that provides actionable insights to hotel management.


## The Question We're Answering

For hotel operators using Unloket: what is actually happening on your property, and is the AI concierge working?

We also sought to answer:
- What are guests asking about most?
- How fast is the system responding?
- How satisfied are guests with AI-handled interactions?
- What types of requests is the AI escalating to human staff members?
- What is the platform saving the property in a dollar amount?

## Target Audience

Hotel managers contemplating or currently using the Unloket platform. This dashboard is designed to be a live operational tool for day-to-day monitoring, as well as a proof-of-ROI model for pitching Unloket's model.

## The Dataset Used

- Live SMS and WhatsApp conversation logs pulled directly from the Unloket platform
- Totaling 3,641 messages, across 27 fields
- Dates ranging from December 2025 – April 2026

Key fields and Descriptions:
Inquiry Category | Type of guest request (General FAQ, Maintenance, etc.) |
Handler | Whether the AI or a staff member responded |
Satisfaction Score | Guest rating on a 1–5 scale |
Response Time Seconds | Time from message received to response sent |
Sent Date | Timestamp of the message |
Direction | Inbound (guest) or outbound (hotel) |
Message Body | Raw text of the conversation |

## Data Cleaning

Cleaning was performed in Python using pandas. See `clean_data.py` in this repo for the full script. This script was created by Claude.

Steps taken:
- Dropped rows where Satisfaction Score was null. These represent conversations that ended without a rating or usable value. We excluded them rather than imputing a value to avoid any distortion with the satisfaction KPI.
- Dropped rows where Inquiry Category was null.
- Converted Sent Date to datetime format, coverting invalid values to NaT (Not a Time)
- Flagged response time outliers greater than 86,400 seconds (24 hours). The mean response time was over 1,500 minutes, while the median was under 1 minute, so we were able to get rid of severe outlier distortion of the mean. We use median response time throughout the dashboard to rectify this.


## Tools Used

- Tableau: primary dashboard and all visualizations
- Python (pandas): data cleaning and validation
- Inkscape: annotated dashboard export for presentation context
- Google Slides: presentation deck


## Design Decisions

Color: We used Unloket's brand palette throughout: primary navy `#1A2E35`, gold `#C5B358`, sage `#7D8C7F`, and warm off-white `#F9F7F2`. We did this to create consistency between the dashboard and the company's existing brand identity and color scheme.

Typography: Newsreader (serif) for headlines, Manrope (sans-serif) for body and labels to matching Unloket's style guide.

Gestalt principles applied:
- Proximity: KPI tiles are grouped at the top as a unified summary row, visually separated from the detailed charts below
- Similarity: Consistent card styling across all KPI tiles signals they belong to the same category of information
- Figure/ground: Dark primary color on light background creates clear hierarchy throughout
- Continuity: The 'Total Message Count' line guides the eye naturally across the time axis,making the trend readable without much effort.
- Connection: The date slider across the top links all charts simultaneously, showing the viewer than all the visuals and KPI's share the same dataset.  

Chart choices:
- Bar charts for category comparisons as they are easy to rank visually and straightforward to understand. 
- Line chart for message volume over time to show trends and usage spikes.
- Text KPI tiles for single-number metrics as there was no chart needed, the message only requires a single number figure. 


## Limitations and Assumptions

- The data used only covers a single hotel property, our findings may not generalize to all hotels of varying types or sizes.
- Satisfaction scores are self-reported by guests and only available for a subset of conversations.
- "Money Saved" KPI is an estimate based on assumed staff hourly cost and average handling time, it is not an audited figure as it is merely an educated estimation.
- Response time outliers suggest some conversations were left open for extended periods, which may reflect edge cases rather than typical operations.
- We cannot confirm whether all messages in the dataset represent unique guests

## How We Used LLMs

We used Claude throughout this project for:
- Tableau troubleshooting: resolving data source connection errors and building calculated fields
- Python script development: writing and debugging the data cleaning script
- Presentation deck: primarily to match Unloket's color scheme
- README writeup: used soley for the layout and structure of standard README files, not for the content of the file.


## Project Files

File | Description 
`clean_data.py` | Python data cleaning script 
`Unloket_Presentation_v3.pptx` | Final presentation deck 
Tableau workbook | Final Tableau Workbook
'Google Drive - DataViz' | Google Drive containing our before and after Inkscape

---

## Public Tableau Workbook
(https://public.tableau.com/app/profile/quinn.dziwura/viz/UnloketDashboardV2_2/Dashboard22?publish=yes)

