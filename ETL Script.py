import pandas as pd
from sqlalchemy import create_engine

# --- 1. CONFIGURATION (CHANGE THESE TWO LINES) ---
CSV_FILE_PATH = 'loan_data.csv'  
DB_PASSWORD = 'YOUR_PASSWORD'    

print("1. Extracting data from CSV...")
df = pd.read_csv(CSV_FILE_PATH)

print("2. Transforming data into Star Schema...")
# Create Dimension Tables
dim_applicant = df[['person_age', 'person_income', 'person_home_ownership', 'person_emp_length']].drop_duplicates().reset_index(drop=True)
dim_applicant.index += 1  
dim_applicant['applicant_id'] = dim_applicant.index

dim_credit = df[['cb_person_default_on_file', 'cb_person_cred_hist_length']].drop_duplicates().reset_index(drop=True)
dim_credit.index += 1
dim_credit['credit_id'] = dim_credit.index

dim_loan_details = df[['loan_intent', 'loan_grade', 'loan_int_rate']].drop_duplicates().reset_index(drop=True)
dim_loan_details.index += 1
dim_loan_details['loan_detail_id'] = dim_loan_details.index

# Create Fact Table
fact_df = df.merge(dim_applicant, on=['person_age', 'person_income', 'person_home_ownership', 'person_emp_length'])
fact_df = fact_df.merge(dim_credit, on=['cb_person_default_on_file', 'cb_person_cred_hist_length'])
fact_df = fact_df.merge(dim_loan_details, on=['loan_intent', 'loan_grade', 'loan_int_rate'])

fact_table = fact_df[['applicant_id', 'credit_id', 'loan_detail_id', 'loan_amnt', 'loan_percent_income', 'loan_status']].copy()
fact_table.index += 1
fact_table['loan_id'] = fact_table.index

print("3. Loading data into PostgreSQL... (This takes a few seconds)")
engine = create_engine(f'postgresql://postgres:{DB_PASSWORD}@localhost:5432/loan_dwh')

dim_applicant.to_sql('dim_applicant', engine, if_exists='append', index=False)
dim_credit.to_sql('dim_credit_history', engine, if_exists='append', index=False)
dim_loan_details.to_sql('dim_loan_details', engine, if_exists='append', index=False)
fact_table.to_sql('fact_loan_performance', engine, if_exists='append', index=False)

print("SUCCESS! ETL Pipeline Complete. Database is loaded.")