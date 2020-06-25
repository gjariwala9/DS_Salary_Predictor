import numpy as np


def cat_to_var(var, lst):
    inputs = []
    for i in lst:
        if i == var:
            inputs.append(1.0)
        else:
            inputs.append(0.0)
    return inputs

def return_prediction(model, sample_json):
    inputs = []
    
    inputs.append(sample_json['Rating'])
    inputs.append(sample_json['num_comp'])
    inputs.append(sample_json['hourly'])
    inputs.append(0)
    inputs.append(sample_json['same_state'])
    inputs.append(sample_json['age'])
    inputs.append(sample_json['python_yn'])
    inputs.append(sample_json['spark'])
    inputs.append(sample_json['aws'])
    inputs.append(sample_json['excel'])
    inputs.append(sample_json['desc_length'])
    
    size_lst = ['Other', 
                '1 to 50 employees', 
                '10000+ employees', 
                '1001 to 5000 employees', 
                '201 to 500 employees', 
                '5001 to 10000 employees', 
                '501 to 1000 employees', 
                '51 to 200 employees', 
                'Unknown']
    
    size = sample_json['size']
    
    inputs.extend(cat_to_var(size, size_lst))
            
    type_of_ownership_lst = ['Other', 
                            'College / University', 
                            'Company - Private', 
                            'Company - Public', 
                            'Government', 
                            'Hospital', 
                            'Nonprofit Organization', 
                            'Other Organization', 
                            'School / School District', 
                            'Subsidiary or Business Segment', 
                            'Unknown']
    
    type_of_ownership = sample_json['type_of_ownership']
    
    inputs.extend(cat_to_var(type_of_ownership, type_of_ownership_lst))
    
    industry_lst = ['Other', 
                    'Accounting', 
                    'Advertising & Marketing', 
                    'Aerospace & Defense', 
                    'Architectural & Engineering Services', 
                    'Auctions & Galleries', 
                    'Banks & Credit Unions', 
                    'Beauty & Personal Accessories Stores', 
                    'Biotech & Pharmaceuticals', 
                    'Brokerage Services', 
                    'Colleges & Universities', 
                    'Computer Hardware & Software', 
                    'Construction', 
                    'Consulting', 
                    'Consumer Product Rental', 
                    'Consumer Products Manufacturing', 
                    'Department, Clothing, & Shoe Stores', 
                    'Education Training Services', 
                    'Energy', 
                    'Enterprise Software & Network Solutions', 
                    'Farm Support Services', 
                    'Federal Agencies', 
                    'Financial Analytics & Research', 
                    'Financial Transaction Processing', 
                    'Food & Beverage Manufacturing', 
                    'Gambling', 
                    'Gas Stations', 
                    'Health Care Products Manufacturing', 
                    'Health Care Services & Hospitals', 
                    'Health, Beauty, & Fitness', 
                    'IT Services', 
                    'Industrial Manufacturing', 
                    'Insurance Agencies & Brokerages', 
                    'Insurance Carriers', 
                    'Internet', 
                    'Investment Banking & Asset Management', 
                    'K-12 Education', 
                    'Lending', 
                    'Logistics & Supply Chain', 
                    'Metals Brokers', 
                    'Mining', 
                    'Motion Picture Production & Distribution', 
                    'Other Retail Stores', 
                    'Real Estate', 
                    'Religious Organizations', 
                    'Research & Development', 
                    'Security Services', 
                    'Social Assistance', 
                    'Sporting Goods Stores', 
                    'Staffing & Outsourcing', 
                    'Stock Exchanges', 
                    'TV Broadcast & Cable Networks', 
                    'Telecommunications Manufacturing', 
                    'Telecommunications Services', 
                    'Transportation Equipment Manufacturing', 
                    'Transportation Management', 
                    'Travel Agencies', 
                    'Trucking', 
                    'Video Games', 
                    'Wholesale']
    
    Industry = sample_json['Industry']
    
    inputs.extend(cat_to_var(Industry, industry_lst))
    
    
    sector_lst = ['Other', 
              'Accounting & Legal', 
              'Aerospace & Defense', 
              'Agriculture & Forestry', 
              'Arts, Entertainment & Recreation', 
              'Biotech & Pharmaceuticals', 
              'Business Services', 
              'Construction, Repair & Maintenance', 
              'Consumer Services', 
              'Education', 
              'Finance', 
              'Government', 
              'Health Care', 
              'Information Technology', 
              'Insurance', 
              'Manufacturing', 
              'Media', 
              'Mining & Metals', 
              'Non-Profit', 
              'Oil, Gas, Energy & Utilities', 
              'Real Estate', 
              'Retail', 
              'Telecommunications', 
              'Transportation & Logistics', 
              'Travel & Tourism']
    
    Sector = sample_json['Sector']
    
    inputs.extend(cat_to_var(Sector, sector_lst))
            
    revenue_lst = ['$1 to $2 billion (USD)', 
                   '$1 to $5 million (USD)', 
                   '$10 to $25 million (USD)', 
                   '$10+ billion (USD)', 
                   '$100 to $500 million (USD)', 
                   '$2 to $5 billion (USD)', 
                   '$25 to $50 million (USD)', 
                   '$5 to $10 billion (USD)', 
                   '$5 to $10 million (USD)', 
                   '$50 to $100 million (USD)', 
                   '$500 million to $1 billion (USD)', 
                   'Other', 
                   'Less than $1 million (USD)', 
                   'Unknown / Non-Applicable']
    
    Revenue = sample_json['Revenue']
    
    inputs.extend(cat_to_var(Revenue, revenue_lst))
    
    job_state_lst = ['AL', 
                     'AZ', 
                     'CA', 
                     'CO', 
                     'CT', 
                     'DC', 
                     'DE', 
                     'FL', 
                     'GA', 
                     'IA', 
                     'ID', 
                     'IL', 
                     'IN', 
                     'KS', 
                     'KY', 
                     'LA', 
                     'MA', 
                     'MD', 
                     'MI', 
                     'MN', 
                     'MO', 
                     'NC', 
                     'NE', 
                     'NJ', 
                     'NM', 
                     'NY', 
                     'OH', 
                     'OR', 
                     'PA', 
                     'RI', 
                     'SC', 
                     'TN', 
                     'TX', 
                     'UT', 
                     'VA', 
                     'WA', 
                     'WI']
    
    job_state = sample_json['job_state']
    
    inputs.extend(cat_to_var(job_state, job_state_lst))
            
    job_simp_lst = ['analyst',
                    'data engineer',
                    'data scientist',
                    'director',
                    'manager',
                    'mle',
                    'na']       
    
    job_simp = sample_json['job_simp']
    
    inputs.extend(cat_to_var(job_simp, job_simp_lst))
    
    seniority_lst = ['jr',
                    'na',
                    'senior']
    
    seniority = sample_json['seniority']
    
    inputs.extend(cat_to_var(seniority, seniority_lst))
            
    
    predicted_salary = model.predict([inputs])[0]
    
    return round(predicted_salary, 2)