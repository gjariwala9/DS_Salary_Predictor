import flask
from flask import Flask, render_template, session, url_for, redirect, flash
from flask_wtf import FlaskForm
from wtforms import TextField, SubmitField, SelectField, RadioField, TextAreaField, DecimalField, IntegerField
from wtforms.validators import DataRequired
from wtforms.widgets import html5 as h5widgets


class DSForm(FlaskForm):
    Rating = DecimalField('Rating', validators=[DataRequired()], widget=h5widgets.NumberInput(min=0, max=5, step=0.1))
    num_comp = TextField('Number of Competitors', validators=[DataRequired()], widget=h5widgets.NumberInput(min=0, max=500, step=1))
    hourly = RadioField('Is the salary hourly base?', coerce=float, default=0, choices=[(1.0,'Yes'),(0.0,'No')])
    same_state = RadioField("Is the job at the headquarters?", coerce=float, default=1, choices=[(1.0,'Yes'),(0.0,'No')])
    age = TextField('Age of the company', validators=[DataRequired()], widget=h5widgets.NumberInput(min=0, max=500, step=1))
    python_yn = RadioField('Is Python Required?', coerce=float, default=1, choices=[(1.0,'Yes'),(0.0,'No')])
    spark = RadioField('Is Spark Required?', coerce=float, default=1, choices=[(1.0,'Yes'),(0.0,'No')])
    aws = RadioField('Is AWS Required?', coerce=float, default=1, choices=[(1.0,'Yes'),(0.0,'No')])
    excel = RadioField('Is Excel Required?', coerce=float, default=1, choices=[(1.0,'Yes'),(0.0,'No')])

    desc =TextAreaField('Description', validators=[DataRequired()])
    size_lst = [('Unknown', 'Unknown'),
                ('1 to 50 employees', '1 to 50 employees'),
                ('51 to 200 employees', '51 to 200 employees'),
                ('201 to 500 employees', '201 to 500 employees'),
                ('501 to 1000 employees', '501 to 1000 employees'),
                ('1001 to 5000 employees', '1001 to 5000 employees'),
                ('5001 to 10000 employees', '5001 to 10000 employees') ,
                ('10000+ employees', '10000+ employees'),
                ('Other', 'Other')
                ]
    size = SelectField('Size of company', choices=size_lst, default=1)

    type_of_ownership_lst = [('Unknown', 'Unknown'),
                            ('College / University', 'College / University'),
                            ('Company - Private', 'Company - Private'),
                            ('Company - Public', 'Company - Public'),
                            ('Government', 'Government'),
                            ('Hospital', 'Hospital'),
                            ('Nonprofit Organization', 'Nonprofit Organization'),
                            ('Other Organization', 'Other Organization'),
                            ('School / School District', 'School / School District'),
                            ('Subsidiary or Business Segment', 'Subsidiary or Business Segment'),
                            ('Other', 'Other'),
                            ]
    type_of_ownership = SelectField('Type of Ownership', choices=type_of_ownership_lst, default=1)

    industry_lst = [
                    ('Accounting', 'Accounting'),
                    ('Advertising & Marketing', 'Advertising & Marketing'),
                    ('Aerospace & Defense', 'Aerospace & Defense'),
                    ('Architectural & Engineering Services', 'Architectural & Engineering Services'),
                    ('Auctions & Galleries', 'Auctions & Galleries'),
                    ('Banks & Credit Unions', 'Banks & Credit Unions'),
                    ('Beauty & Personal Accessories Stores', 'Beauty & Personal Accessories Stores'),
                    ('Biotech & Pharmaceuticals', 'Biotech & Pharmaceuticals'),
                    ('Brokerage Services', 'Brokerage Services'),
                    ('Colleges & Universities', 'Colleges & Universities'),
                    ('Computer Hardware & Software', 'Computer Hardware & Software'),
                    ('Construction', 'Construction'),
                    ('Consulting', 'Consulting'),
                    ('Consumer Product Rental', 'Consumer Product Rental'),
                    ('Consumer Products Manufacturing', 'Consumer Products Manufacturing'),
                    ('Department, Clothing, & Shoe Stores', 'Department, Clothing, & Shoe Stores'),
                    ('Education Training Services', 'Education Training Services'),
                    ('Energy', 'Energy'),
                    ('Enterprise Software & Network Solutions', 'Enterprise Software & Network Solutions'),
                    ('Farm Support Services', 'Farm Support Services'),
                    ('Federal Agencies', 'Federal Agencies'),
                    ('Financial Analytics & Research', 'Financial Analytics & Research'),
                    ('Financial Transaction Processing', 'Financial Transaction Processing'),
                    ('Food & Beverage Manufacturing', 'Food & Beverage Manufacturing'),
                    ('Gambling', 'Gambling'),
                    ('Gas Stations', 'Gas Stations'),
                    ('Health Care Products Manufacturing', 'Health Care Products Manufacturing'),
                    ('Health Care Services & Hospitals', 'Health Care Services & Hospitals'),
                    ('Health, Beauty, & Fitness', 'Health, Beauty, & Fitness'),
                    ('IT Services', 'IT Services'),
                    ('Industrial Manufacturing', 'Industrial Manufacturing'),
                    ('Insurance Agencies & Brokerages', 'Insurance Agencies & Brokerages'),
                    ('Insurance Carriers', 'Insurance Carriers'),
                    ('Internet', 'Internet'),
                    ('Investment Banking & Asset Management', 'Investment Banking & Asset Management'),
                    ('K-12 Education', 'K-12 Education'),
                    ('Lending', 'Lending'),
                    ('Logistics & Supply Chain', 'Logistics & Supply Chain'),
                    ('Metals Brokers', 'Metals Brokers'),
                    ('Mining', 'Mining'),
                    ('Motion Picture Production & Distribution', 'Motion Picture Production & Distribution'),
                    ('Other Retail Stores', 'Other Retail Stores'),
                    ('Real Estate', 'Real Estate'),
                    ('Religious Organizations', 'Religious Organizations'),
                    ('Research & Development', 'Research & Development'),
                    ('Security Services', 'Security Services'),
                    ('Social Assistance', 'Social Assistance'),
                    ('Sporting Goods Stores', 'Sporting Goods Stores'),
                    ('Staffing & Outsourcing', 'Staffing & Outsourcing'),
                    ('Stock Exchanges', 'Stock Exchanges'),
                    ('TV Broadcast & Cable Networks', 'TV Broadcast & Cable Networks'),
                    ('Telecommunications Manufacturing', 'Telecommunications Manufacturing'),
                    ('Telecommunications Services', 'Telecommunications Services'),
                    ('Transportation Equipment Manufacturing', 'Transportation Equipment Manufacturing'),
                    ('Transportation Management', 'Transportation Management'),
                    ('Travel Agencies', 'Travel Agencies'),
                    ('Trucking', 'Trucking'),
                    ('Video Games', 'Video Games'),
                    ('Wholesale', 'Wholesale'),
                    ('Other', 'Other')
                    ]
    Industry = SelectField('Industry', choices=industry_lst, default=1)

    sector_lst = [
                ('Accounting & Legal', 'Accounting & Legal'),
                ('Aerospace & Defense', 'Aerospace & Defense'),
                ('Agriculture & Forestry', 'Agriculture & Forestry'),
                ('Arts, Entertainment & Recreation', 'Arts, Entertainment & Recreation'),
                ('Biotech & Pharmaceuticals', 'Biotech & Pharmaceuticals'),
                ('Business Services', 'Business Services'),
                ('Construction, Repair & Maintenance', 'Construction, Repair & Maintenance'),
                ('Consumer Services', 'Consumer Services'),
                ('Education', 'Education'),
                ('Finance', 'Finance'),
                ('Government', 'Government'),
                ('Health Care', 'Health Care'),
                ('Information Technology', 'Information Technology'),
                ('Insurance', 'Insurance'),
                ('Manufacturing', 'Manufacturing'),
                ('Media', 'Media'),
                ('Mining & Metals', 'Mining & Metals'),
                ('Non-Profit', 'Non-Profit'),
                ('Oil, Gas, Energy & Utilities', 'Oil, Gas, Energy & Utilities'),
                ('Real Estate', 'Real Estate'),
                ('Retail', 'Retail'),
                ('Telecommunications', 'Telecommunications'),
                ('Transportation & Logistics', 'Transportation & Logistics'),
                ('Travel & Tourism', 'Travel & Tourism'),
                ('Other', 'Other')
                ]
    Sector = SelectField('Sector', choices=sector_lst, default=1)

    revenue_lst = [
    				('Unknown / Non-Applicable', 'Unknown / Non-Applicable'),
    				('Less than $1 million (USD)', 'Less than $1 million (USD)'),
    				('$1 to $5 million (USD)', '$1 to $5 million (USD)'),
    				('$5 to $10 million (USD)', '$5 to $10 million (USD)'),
    				('$10 to $25 million (USD)', '$10 to $25 million (USD)'),
    				('$25 to $50 million (USD)', '$25 to $50 million (USD)'),
    				('$50 to $100 million (USD)', '$50 to $100 million (USD)'),
    				('$100 to $500 million (USD)', '$100 to $500 million (USD)'),
    				('$500 million to $1 billion (USD)', '$500 million to $1 billion (USD)'),
					('$1 to $2 billion (USD)', '$1 to $2 billion (USD)'),
					('$2 to $5 billion (USD)', '$2 to $5 billion (USD)'),
					('$5 to $10 billion (USD)', '$5 to $10 billion (USD)'),
					('$10+ billion (USD)', '$10+ billion (USD)'),
					('Other', 'Other')
					]
    Revenue = SelectField('Revenue', choices=revenue_lst, default=1)

    job_state_lst = [
					('AL', 'Alabama'),
					('AZ', 'Arizona'),
					('CA', 'California'),
					('CO', 'Colorado'),
					('CT', 'Connecticu'),
					('DE', 'Delaware'),
					('FL', 'Florida'),
					('GA', 'Georgia'),
					('ID', 'Idaho'),
					('IL', 'Illinois '),
					('IN', 'Indiana '),
					('IA', 'Iowa '),
					('KS', 'Kansas'),
					('KY', 'Kentucky'),
					('LA', 'Louisiana'),
					('MD', 'Maryland'),
					('MA', 'Massachusetts'),
					('MI', 'Michigan'),
					('MN', 'Minnesota'),
					('MO', 'Missouri'),
					('NE', 'Nebraska'),
					('NJ', 'New Jersey'),
					('NM', 'New Mexico'),
					('NY', 'New York'),
					('NC', 'North Carolina'),
					('OH', 'Ohio'),
					('OR', 'Oregon'),
					('PA', 'Pennsylvania'),
					('RI', 'Rhode Island'),
					('SC', 'South Carolina'),
					('TN', 'Tennessee'),
					('TX', 'Texas'),
					('UT', 'Utah'),
					('VA', 'Virginia'),
					('WA', 'Washington'),
					('DC', 'Washington, D.C'),
					('WI', 'Wisconsin'),
					]
    job_state = SelectField('State', choices=job_state_lst, default=1)

    job_simp_lst = [
					('analyst', 'Analyst'),
					('data engineer', 'Data Engineer'),
					('data scientist', 'Data Scientist'),
					('director', 'Director'),
					('manager', 'Manager'),
					('mle', 'Machine Learning Engineer'),
					('na', 'Other'),
					]      
    job_simp = SelectField('Title', choices=job_simp_lst, default=1)

    seniority_lst = [
					('jr', 'Junior'),
					('senior', 'Senior'),
					('na', 'Other'),
					]
    
    seniority = SelectField('Position', choices=seniority_lst, default=1)

    submit = SubmitField("Predict")
