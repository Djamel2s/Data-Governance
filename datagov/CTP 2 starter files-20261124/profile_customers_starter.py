"""CTP 2 - Exercise 1 STARTER: profile customers.csv with pandas.
Run from the 02_CTP2 folder:  python profile_customers_starter.py
Goal: measure at least 8 rules (2 per dimension) and copy the numbers into quality_scorecard_template.csv
"""
import pandas as pd

df = pd.read_csv("../shopfast-kit/data/customers.csv", dtype=str)   # dtype=str: keep the raw text (e.g. 01300)
n = len(df)
print("Rows:", n)
print(df.head())

# --- Completeness: how many empty values per column? ---
print("\nEmpty values per column:\n", df.isna().sum())

# --- Uniqueness: is customer_id unique? ---
print("\nDuplicated customer_id rows:", df["customer_id"].duplicated(keep=False).sum())

# TODO 1 (Uniqueness): normalise email (strip + lower case) and count people registered twice
df["email_normalized"] = df["email"].str.strip().str.lower()
email_has_value = df["email_normalized"].notna() & df["email_normalized"].ne("")
print("\nDuplicated email rows:", (email_has_value & df["email_normalized"].duplicated(keep=False)).sum())
# TODO 2 (Validity): count emails that do not match the regex  ^[^@\s]+@[^@\s]+\.[a-zA-Z]{2,}$   (hint: .str.match)
print("\nInvalid email rows:", (~df["email_normalized"].str.match(r'^[^@\s]+@[^@\s]+\.[a-zA-Z]{2,}$', na=False)).sum())
# TODO 3 (Consistency): list the distinct values of country with value_counts() - how many spellings for 4 countries?
print("\nDistinct country:\n", df["country"].value_counts())
print("Inconsistent country rows:", (df["country"].notna() & ~df["country"].isin(["FR", "DE", "BE", "ES"])).sum())
# TODO 4 (Consistency): count signup_date values that are NOT in the format YYYY-MM-DD
print("\nInvalid signup_date:", (~df["signup_date"].str.match(r'^\d{4}-\d{2}-\d{2}$', na=False)).sum())
# TODO 5 (Validity): loyalty_tier values outside bronze / silver / gold / platinum
print("\nInvalid loyalty_tier:", (~df["loyalty_tier"].isin(["bronze", "silver", "gold", "platinum"])).sum())
# TODO 6 (Accuracy): birth dates in the future or before 1906 (convert the ISO ones with pd.to_datetime)
if "birth_date" in df.columns:
    df["birth_date-normalized"] = pd.to_datetime(df["birth_date"], errors="coerce")
    print("\nInvalid birth_date:", ((df["birth_date-normalized"] > pd.Timestamp.now()) | (df["birth_date-normalized"] < pd.Timestamp("1906-01-01"))).sum())
# TODO 7 (Validity): French postal codes that do not have 5 digits
is_french = df["country"].str.strip().str.lower().isin(["fr", "fra", "france"])
postal_code_valid = df["postal_code"].str.match(r'^\d{5}$', na=False)
print("\nInvalid postal_code:", (is_french & ~postal_code_valid).sum())
# Bonus: compute score_pct = 100 * (1 - failing_rows / n) for each rule
