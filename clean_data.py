"""
Unloket SMS Log Analytics — Data Cleaning Script
BUS 32130: Data Visualization for Decision-Making, Spring 2026
Authors: Odysseas Koufos, Miltiadis Hadjipanayiotou, Quinn Dziwura

This script loads the raw Unloket SMS log data, performs cleaning and
validation, and outputs a summary of what was found and fixed.
"""

import pandas as pd

# ── LOAD ──────────────────────────────────────────────────────────────────────
print("Loading data...")
df = pd.read_excel("Unloket_SMS_Log_Analytics.xlsx", sheet_name="Raw Data + Calculations")
print(f"  Rows loaded: {len(df)}")
print(f"  Columns: {list(df.columns)}\n")


# ── INSPECT ───────────────────────────────────────────────────────────────────
print("=== NULL CHECK ===")
null_counts = df.isnull().sum()
null_counts = null_counts[null_counts > 0]
print(null_counts if len(null_counts) > 0 else "  No nulls found.")
print()


# ── CLEAN ─────────────────────────────────────────────────────────────────────

# 1. Drop rows where Satisfaction Score is null
# These represent conversations that ended without a rating — we exclude
# them from satisfaction analysis rather than imputing a value.
before = len(df)
df_clean = df.dropna(subset=["Satisfaction Score"])
dropped_satisfaction = before - len(df_clean)
print(f"Dropped {dropped_satisfaction} rows with null Satisfaction Score")

# 2. Drop rows where Inquiry Category is null
before = len(df_clean)
df_clean = df_clean.dropna(subset=["Inquiry Category"])
dropped_category = before - len(df_clean)
print(f"Dropped {dropped_category} rows with null Inquiry Category")

# 3. Convert Sent Date to datetime
df_clean["Sent Date"] = pd.to_datetime(df_clean["Sent Date"], errors="coerce")
invalid_dates = df_clean["Sent Date"].isnull().sum()
print(f"Invalid dates coerced to NaT: {invalid_dates}")

# 4. Flag response time outliers (> 24 hours = 86400 seconds)
# We use median response time in the dashboard to avoid distortion from
# conversations that were left open for days.
if "Response Time Seconds" in df_clean.columns:
    outliers = df_clean[df_clean["Response Time Seconds"] > 86400]
    print(f"Response time outliers (>24hr): {len(outliers)} rows flagged")
    median_rt = df_clean["Response Time Seconds"].median()
    print(f"  Median response time: {median_rt:.1f} seconds ({median_rt/60:.2f} minutes)")
    mean_rt = df_clean["Response Time Seconds"].mean()
    print(f"  Mean response time:   {mean_rt:.1f} seconds ({mean_rt/60:.2f} minutes)")
    print(f"  Note: Mean is {mean_rt/median_rt:.0f}x the median — confirms outlier distortion")

print()


# ── SUMMARY STATS ─────────────────────────────────────────────────────────────
print("=== CLEAN DATASET SUMMARY ===")
print(f"Final row count: {len(df_clean)}")
print(f"Date range: {df_clean['Sent Date'].min().date()} to {df_clean['Sent Date'].max().date()}")

print("\nMessage count by Inquiry Category:")
print(df_clean["Inquiry Category"].value_counts().to_string())

if "AI Handled" in df_clean.columns:
    print("\nAI vs Staff Handling:")
    ai_counts = df_clean["AI Handled"].value_counts()
    total = len(df_clean)
    for val, count in ai_counts.items():
        label = "AI Resolved" if val == 1 else "Staff Handled"
        print(f"  {label}: {count} ({count/total*100:.1f}%)")

if "Satisfaction Score" in df_clean.columns:
    avg_sat = df_clean["Satisfaction Score"].mean()
    print(f"\nAvg Satisfaction Score: {avg_sat:.3f} / 5.0  ({avg_sat/5*100:.1f}%)")

print("\nData cleaning complete.")
