# Unloket-Data_Viz
**BUS 32130: Data Visualization for Decision-Making / Spring 2026**  
Odysseas Koufos · Miltiadis Hadjipanayiotou · Quinn Dziwura

# What This Project Is

Unloket is an AI hospitality concierge platform founded by Odysseas Koufos. It handles guest messaging automatically over SMS and WhatsApp for hotel properties, and is currently a finalist in the 2026 New Venture Challenge at the University of Chicago.
For this project, Odysseas gave us direct access to operational data from multiple properties and testing cycles. Our goal was to build a dashboard that provides actionable insights to hotel management, owners of small independent hotels, and short-term stay operators.



## The Question We're Answering

For hotel operators using Unloket: what is actually happening on your property, and is the AI concierge working?

We also sought to answer:
- How responsive the solution is
- Guest engagement with the messaging platform
- Guest satisfaction
- How much work is the AI handling vs staff
- How much money does the AI saves
- What are the most asked FAQs
- What inquiries create the most problems
- What can the AI not handle well
- What should management do next

## Target Audience

Hotel managers and small hotel owners contemplating or currently using the Unloket platform. This dashboard is designed to be a live operational tool for day-to-day monitoring, as well as a proof-of-ROI model for pitching Unloket's model. Small hotel owners need to wear multiple hats and need a complete set of data and information to make strategic decisions.

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
- Claude: used to clean the data first by exporting CSV files. The data was qualitative, and we asked Claude to restructure and code in order to categorize the data. Claude was also used in - -
- Inkscape to tune and refine visuals.



## Design Decisions

Color: We used Unloket's brand palette throughout: primary navy `#1A2E35`, gold `#C5B358`, sage `#7D8C7F`, and warm off-white `#F9F7F2`. We did this to create consistency between the dashboard and the company's existing brand identity and color scheme.

Typography: Newsreader (serif) for headlines, Manrope (sans-serif) for body and labels to matching Unloket's style guide.



Chart choices:
- Bar charts for category comparisons as they are easy to rank visually and straightforward to understand. 
- Line chart for message volume over time to show trends and usage spikes.
- Text KPI tiles for single-number metrics as there was no chart needed, the message only requires a single number figure. 


## Limitations and Assumptions

- The data used covers multiple properties as well as data from testing periods of the solution.
- Satisfaction scores are self-reported by guests and only available for a subset of conversations.
- "Money Saved" KPI is an estimate based on assumed staff hourly cost and average handling time; it is not an audited figure, as it is merely an educated estimation.
- Most of the data does not represent new guests at the hotels. This is because entries were also from testing periods. Most of the recorded requests were made by two phone numbers: +30 6987408304   and +1 (704) 706-0066. Every new interaction from these phone numbers was treated as a new entry, and customers in the hotels.

## How We Used LLMs

We used Claude throughout this project for:
- Tableau troubleshooting: resolving data source connection errors and building calculated fields
- Python script development: writing and debugging the data cleaning script
- Presentation deck: primarily to match Unloket's color scheme
- README writeup: used soley for the layout and structure of standard README files, not for the content of the file.


## Project Files

| File | Description |
| `clean_data.py` | Python data cleaning script |
| `Unloket_Slides.pptx` | Final presentation deck |
| `Inkscape_before.png` | Dashboard screenshot before Inkscape annotation |
| `Inkscape_After.svg` | Finalized annotated Inkscape file |
| 'Unloket-Data_Viz_Writeup.pdf' | The writeup we used to draft this README file

---

## Public Tableau Workbook
(https://public.tableau.com/app/profile/quinn.dziwura/viz/UnloketDashboardV2_2/Dashboard22?publish=yes)

