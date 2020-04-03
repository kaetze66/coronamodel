# coronamodel
code for the hackathon

output folder for all the output files (.csv and graphs)

settings folder for all the settings for running the model

data folder for all the data for calibration

# policy settings:
currently two policies are available (social distancing and self quarantine) that impact the number of contacts per day per person
social distancing impacts the normal contacts (for everyone), self quarantine impacts the symptomatic

SWITCH = 1 means the policy is activated

start = day when the policy is implemented

effectiveness = by how much the contacts per day are reduced

to use the model:

clone repository

install packages (most of them are standard, pysd needs to be installed from pip (pip install pysd)

run model.py

settings for the model can be adjusted by changing the .csv files in the settings folder
