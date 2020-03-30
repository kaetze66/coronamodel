"""
Python model "corona_hackathon_agegroups_cons_treated.py"
Translated using PySD version 0.10.0
"""
from __future__ import division
import numpy as np
from pysd import utils
import xarray as xr

from pysd.py_backend.functions import cache
from pysd.py_backend import functions

_subscript_dict = {}

_namespace = {
    'TIME': 'time',
    'Time': 'time',
    'infection rate': 'infection_rate',
    'total infection rate': 'total_infection_rate',
    'Diseased 40': 'diseased_40',
    'accumulated cases 00': 'accumulated_cases_00',
    'accumulated cases 10': 'accumulated_cases_10',
    'accumulated cases 20': 'accumulated_cases_20',
    'accumulated cases 30': 'accumulated_cases_30',
    'accumulated cases 40': 'accumulated_cases_40',
    'duration of treatment 00': 'duration_of_treatment_00',
    'duration of treatment 10': 'duration_of_treatment_10',
    'duration of treatment 20': 'duration_of_treatment_20',
    'infection rate asymptomatic 80x00': 'infection_rate_asymptomatic_80x00',
    'infection rate asymptomatic 80x10': 'infection_rate_asymptomatic_80x10',
    'asymptomatic duration 00': 'asymptomatic_duration_00',
    'asymptomatic duration 10': 'asymptomatic_duration_10',
    'asymptomatic duration 20': 'asymptomatic_duration_20',
    'asymptomatic duration 30': 'asymptomatic_duration_30',
    'asymptomatic duration 40': 'asymptomatic_duration_40',
    'contacts per person normal 20x50': 'contacts_per_person_normal_20x50',
    'first infection 00': 'first_infection_00',
    'infection rate asymptomatic self 00': 'infection_rate_asymptomatic_self_00',
    'infection rate asymptomatic self 10': 'infection_rate_asymptomatic_self_10',
    'infection rate asymptomatic self 20': 'infection_rate_asymptomatic_self_20',
    'infection rate asymptomatic self 30': 'infection_rate_asymptomatic_self_30',
    'infection rate asymptomatic self 40': 'infection_rate_asymptomatic_self_40',
    'contacts per person normal 30x70': 'contacts_per_person_normal_30x70',
    'case fatality rate 00': 'case_fatality_rate_00',
    'case fatality rate 10': 'case_fatality_rate_10',
    'case fatality rate 20': 'case_fatality_rate_20',
    'case fatality rate 30': 'case_fatality_rate_30',
    'case fatality rate 40': 'case_fatality_rate_40',
    'infection rate quarantined self 10': 'infection_rate_quarantined_self_10',
    'infection rate quarantined self 20': 'infection_rate_quarantined_self_20',
    'infection rate quarantined self 30': 'infection_rate_quarantined_self_30',
    'infection rate quarantined self 40': 'infection_rate_quarantined_self_40',
    'contact infectivity asymptomatic 00x10': 'contact_infectivity_asymptomatic_00x10',
    'contact infectivity asymptomatic 00x20': 'contact_infectivity_asymptomatic_00x20',
    'contact infectivity asymptomatic 00x30': 'contact_infectivity_asymptomatic_00x30',
    'contact infectivity asymptomatic 00x40': 'contact_infectivity_asymptomatic_00x40',
    'contact infectivity asymptomatic 00x50': 'contact_infectivity_asymptomatic_00x50',
    'contact infectivity asymptomatic 00x60': 'contact_infectivity_asymptomatic_00x60',
    'contact infectivity asymptomatic 00x70': 'contact_infectivity_asymptomatic_00x70',
    'contact infectivity asymptomatic 00x80': 'contact_infectivity_asymptomatic_00x80',
    'contact infectivity asymptomatic 10x20': 'contact_infectivity_asymptomatic_10x20',
    'contact infectivity asymptomatic 10x30': 'contact_infectivity_asymptomatic_10x30',
    'contact infectivity asymptomatic 10x40': 'contact_infectivity_asymptomatic_10x40',
    'contact infectivity asymptomatic 10x50': 'contact_infectivity_asymptomatic_10x50',
    'contact infectivity asymptomatic 10x60': 'contact_infectivity_asymptomatic_10x60',
    'contact infectivity asymptomatic 10x70': 'contact_infectivity_asymptomatic_10x70',
    'contact infectivity asymptomatic 10x80': 'contact_infectivity_asymptomatic_10x80',
    'contact infectivity asymptomatic 20x30': 'contact_infectivity_asymptomatic_20x30',
    'contact infectivity asymptomatic 20x40': 'contact_infectivity_asymptomatic_20x40',
    'contact infectivity asymptomatic 20x50': 'contact_infectivity_asymptomatic_20x50',
    'contact infectivity asymptomatic 20x60': 'contact_infectivity_asymptomatic_20x60',
    'contact infectivity asymptomatic 20x70': 'contact_infectivity_asymptomatic_20x70',
    'contact infectivity asymptomatic 20x80': 'contact_infectivity_asymptomatic_20x80',
    'contact infectivity asymptomatic 30x40': 'contact_infectivity_asymptomatic_30x40',
    'contact infectivity asymptomatic 30x50': 'contact_infectivity_asymptomatic_30x50',
    'contact infectivity asymptomatic 30x60': 'contact_infectivity_asymptomatic_30x60',
    'contact infectivity asymptomatic 30x70': 'contact_infectivity_asymptomatic_30x70',
    'contact infectivity asymptomatic 30x80': 'contact_infectivity_asymptomatic_30x80',
    'contact infectivity asymptomatic 40x50': 'contact_infectivity_asymptomatic_40x50',
    'contact infectivity asymptomatic 40x60': 'contact_infectivity_asymptomatic_40x60',
    'contact infectivity asymptomatic 40x70': 'contact_infectivity_asymptomatic_40x70',
    'contact infectivity asymptomatic 40x80': 'contact_infectivity_asymptomatic_40x80',
    'infection rate symptomatic 30x20': 'infection_rate_symptomatic_30x20',
    'infection rate symptomatic 30x40': 'infection_rate_symptomatic_30x40',
    'infection rate symptomatic 30x50': 'infection_rate_symptomatic_30x50',
    'infection rate symptomatic 30x60': 'infection_rate_symptomatic_30x60',
    'infection rate symptomatic 30x70': 'infection_rate_symptomatic_30x70',
    'infection rate symptomatic 30x80': 'infection_rate_symptomatic_30x80',
    'infection rate symptomatic 40x00': 'infection_rate_symptomatic_40x00',
    'contact infectivity asymptomatic self 00': 'contact_infectivity_asymptomatic_self_00',
    'contact infectivity asymptomatic self 10': 'contact_infectivity_asymptomatic_self_10',
    'contact infectivity asymptomatic self 20': 'contact_infectivity_asymptomatic_self_20',
    'contact infectivity asymptomatic self 30': 'contact_infectivity_asymptomatic_self_30',
    'contact infectivity asymptomatic self 40': 'contact_infectivity_asymptomatic_self_40',
    'infection rate symptomatic 40x70': 'infection_rate_symptomatic_40x70',
    'infection rate symptomatic 40x80': 'infection_rate_symptomatic_40x80',
    'infection rate symptomatic 50x00': 'infection_rate_symptomatic_50x00',
    'infection rate symptomatic 50x10': 'infection_rate_symptomatic_50x10',
    'infection rate symptomatic 50x20': 'infection_rate_symptomatic_50x20',
    'contact infectivity quarantine self 00': 'contact_infectivity_quarantine_self_00',
    'contact infectivity quarantine self 10': 'contact_infectivity_quarantine_self_10',
    'contact infectivity quarantine self 20': 'contact_infectivity_quarantine_self_20',
    'contact infectivity quarantine self 30': 'contact_infectivity_quarantine_self_30',
    'contact infectivity quarantine self 40': 'contact_infectivity_quarantine_self_40',
    'infection rate symptomatic 60x00': 'infection_rate_symptomatic_60x00',
    'infection rate symptomatic 60x10': 'infection_rate_symptomatic_60x10',
    'infection rate symptomatic 60x20': 'infection_rate_symptomatic_60x20',
    'infection rate symptomatic 60x30': 'infection_rate_symptomatic_60x30',
    'contact infectivity symptomatic 00x10': 'contact_infectivity_symptomatic_00x10',
    'contact infectivity symptomatic 00x20': 'contact_infectivity_symptomatic_00x20',
    'contact infectivity symptomatic 00x30': 'contact_infectivity_symptomatic_00x30',
    'contact infectivity symptomatic 00x40': 'contact_infectivity_symptomatic_00x40',
    'contact infectivity symptomatic 00x50': 'contact_infectivity_symptomatic_00x50',
    'contact infectivity symptomatic 00x60': 'contact_infectivity_symptomatic_00x60',
    'contact infectivity symptomatic 00x70': 'contact_infectivity_symptomatic_00x70',
    'contact infectivity symptomatic 00x80': 'contact_infectivity_symptomatic_00x80',
    'contact infectivity symptomatic 10x20': 'contact_infectivity_symptomatic_10x20',
    'contact infectivity symptomatic 10x30': 'contact_infectivity_symptomatic_10x30',
    'contact infectivity symptomatic 10x40': 'contact_infectivity_symptomatic_10x40',
    'contact infectivity symptomatic 10x50': 'contact_infectivity_symptomatic_10x50',
    'contact infectivity symptomatic 10x60': 'contact_infectivity_symptomatic_10x60',
    'contact infectivity symptomatic 10x70': 'contact_infectivity_symptomatic_10x70',
    'contact infectivity symptomatic 10x80': 'contact_infectivity_symptomatic_10x80',
    'contact infectivity symptomatic 20x30': 'contact_infectivity_symptomatic_20x30',
    'contact infectivity symptomatic 20x40': 'contact_infectivity_symptomatic_20x40',
    'contact infectivity symptomatic 20x50': 'contact_infectivity_symptomatic_20x50',
    'contact infectivity symptomatic 20x60': 'contact_infectivity_symptomatic_20x60',
    'contact infectivity symptomatic 20x70': 'contact_infectivity_symptomatic_20x70',
    'contact infectivity symptomatic 20x80': 'contact_infectivity_symptomatic_20x80',
    'contact infectivity symptomatic 30x40': 'contact_infectivity_symptomatic_30x40',
    'contact infectivity symptomatic 30x50': 'contact_infectivity_symptomatic_30x50',
    'contact infectivity symptomatic 30x60': 'contact_infectivity_symptomatic_30x60',
    'contact infectivity symptomatic 30x70': 'contact_infectivity_symptomatic_30x70',
    'contact infectivity symptomatic 30x80': 'contact_infectivity_symptomatic_30x80',
    'contact infectivity symptomatic 40x50': 'contact_infectivity_symptomatic_40x50',
    'contact infectivity symptomatic 40x60': 'contact_infectivity_symptomatic_40x60',
    'contact infectivity symptomatic 40x70': 'contact_infectivity_symptomatic_40x70',
    'contact infectivity symptomatic 40x80': 'contact_infectivity_symptomatic_40x80',
    'Infected asymptomatic 40x60': 'infected_asymptomatic_40x60',
    'infection start 00': 'infection_start_00',
    'infection start 10': 'infection_start_10',
    'infection start 20': 'infection_start_20',
    'infection start 30': 'infection_start_30',
    'infection start 40': 'infection_start_40',
    'self quarantine policy 40': 'self_quarantine_policy_40',
    'contact infectivity symptomatic self 00': 'contact_infectivity_symptomatic_self_00',
    'contact infectivity symptomatic self 10': 'contact_infectivity_symptomatic_self_10',
    'contact infectivity symptomatic self 20': 'contact_infectivity_symptomatic_self_20',
    'contact infectivity symptomatic self 30': 'contact_infectivity_symptomatic_self_30',
    'contact infectivity symptomatic self 40': 'contact_infectivity_symptomatic_self_40',
    'init accumulated cases 00': 'init_accumulated_cases_00',
    'init accumulated cases 10': 'init_accumulated_cases_10',
    'init accumulated cases 20': 'init_accumulated_cases_20',
    'init accumulated cases 30': 'init_accumulated_cases_30',
    'contacts per person normal 00x10': 'contacts_per_person_normal_00x10',
    'contacts per person normal 00x20': 'contacts_per_person_normal_00x20',
    'contacts per person normal 00x30': 'contacts_per_person_normal_00x30',
    'contacts per person normal 00x40': 'contacts_per_person_normal_00x40',
    'contacts per person normal 00x50': 'contacts_per_person_normal_00x50',
    'contacts per person normal 00x60': 'contacts_per_person_normal_00x60',
    'contacts per person normal 00x70': 'contacts_per_person_normal_00x70',
    'contacts per person normal 00x80': 'contacts_per_person_normal_00x80',
    'contacts per person normal 10x20': 'contacts_per_person_normal_10x20',
    'contacts per person normal 10x30': 'contacts_per_person_normal_10x30',
    'contacts per person normal 10x40': 'contacts_per_person_normal_10x40',
    'contacts per person normal 10x50': 'contacts_per_person_normal_10x50',
    'contacts per person normal 10x60': 'contacts_per_person_normal_10x60',
    'contacts per person normal 10x70': 'contacts_per_person_normal_10x70',
    'contacts per person normal 10x80': 'contacts_per_person_normal_10x80',
    'contacts per person normal 20x30': 'contacts_per_person_normal_20x30',
    'contacts per person normal 20x40': 'contacts_per_person_normal_20x40',
    'social distancing effectiveness 10': 'social_distancing_effectiveness_10',
    'contacts per person normal 20x60': 'contacts_per_person_normal_20x60',
    'contacts per person normal 20x70': 'contacts_per_person_normal_20x70',
    'contacts per person normal 20x80': 'contacts_per_person_normal_20x80',
    'contacts per person normal 30x40': 'contacts_per_person_normal_30x40',
    'contacts per person normal 30x50': 'contacts_per_person_normal_30x50',
    'contacts per person normal 30x60': 'contacts_per_person_normal_30x60',
    'Infected symptomatic 00x60': 'infected_symptomatic_00x60',
    'contacts per person normal 30x80': 'contacts_per_person_normal_30x80',
    'contacts per person normal 40x50': 'contacts_per_person_normal_40x50',
    'contacts per person normal 40x60': 'contacts_per_person_normal_40x60',
    'contacts per person normal 40x70': 'contacts_per_person_normal_40x70',
    'contacts per person normal 40x80': 'contacts_per_person_normal_40x80',
    'init Infected asymptomatic 30': 'init_infected_asymptomatic_30',
    'init Infected asymptomatic 40': 'init_infected_asymptomatic_40',
    'Infected symptomatic 10x60': 'infected_symptomatic_10x60',
    'Infected symptomatic 10x70': 'infected_symptomatic_10x70',
    'Infected symptomatic 10x80': 'infected_symptomatic_10x80',
    'Infected symptomatic 20': 'infected_symptomatic_20',
    'Infected symptomatic 20x30': 'infected_symptomatic_20x30',
    'contacts per person normal self 00': 'contacts_per_person_normal_self_00',
    'contacts per person normal self 10': 'contacts_per_person_normal_self_10',
    'contacts per person normal self 20': 'contacts_per_person_normal_self_20',
    'contacts per person normal self 30': 'contacts_per_person_normal_self_30',
    'contacts per person normal self 40': 'contacts_per_person_normal_self_40',
    'Infected symptomatic 30': 'infected_symptomatic_30',
    'Infected symptomatic 30x40': 'infected_symptomatic_30x40',
    'Infected symptomatic 30x50': 'infected_symptomatic_30x50',
    'Infected symptomatic 30x60': 'infected_symptomatic_30x60',
    'contacts per person symptomatic 00x10': 'contacts_per_person_symptomatic_00x10',
    'contacts per person symptomatic 00x20': 'contacts_per_person_symptomatic_00x20',
    'contacts per person symptomatic 00x30': 'contacts_per_person_symptomatic_00x30',
    'contacts per person symptomatic 00x40': 'contacts_per_person_symptomatic_00x40',
    'contacts per person symptomatic 00x50': 'contacts_per_person_symptomatic_00x50',
    'contacts per person symptomatic 00x60': 'contacts_per_person_symptomatic_00x60',
    'contacts per person symptomatic 00x70': 'contacts_per_person_symptomatic_00x70',
    'contacts per person symptomatic 00x80': 'contacts_per_person_symptomatic_00x80',
    'contacts per person symptomatic 10x20': 'contacts_per_person_symptomatic_10x20',
    'contacts per person symptomatic 10x30': 'contacts_per_person_symptomatic_10x30',
    'contacts per person symptomatic 10x40': 'contacts_per_person_symptomatic_10x40',
    'contacts per person symptomatic 10x50': 'contacts_per_person_symptomatic_10x50',
    'contacts per person symptomatic 10x60': 'contacts_per_person_symptomatic_10x60',
    'contacts per person symptomatic 10x70': 'contacts_per_person_symptomatic_10x70',
    'contacts per person symptomatic 10x80': 'contacts_per_person_symptomatic_10x80',
    'contacts per person symptomatic 20x30': 'contacts_per_person_symptomatic_20x30',
    'contacts per person symptomatic 20x40': 'contacts_per_person_symptomatic_20x40',
    'contacts per person symptomatic 20x50': 'contacts_per_person_symptomatic_20x50',
    'contacts per person symptomatic 20x60': 'contacts_per_person_symptomatic_20x60',
    'contacts per person symptomatic 20x70': 'contacts_per_person_symptomatic_20x70',
    'contacts per person symptomatic 20x80': 'contacts_per_person_symptomatic_20x80',
    'contacts per person symptomatic 30x40': 'contacts_per_person_symptomatic_30x40',
    'contacts per person symptomatic 30x50': 'contacts_per_person_symptomatic_30x50',
    'contacts per person symptomatic 30x60': 'contacts_per_person_symptomatic_30x60',
    'contacts per person symptomatic 30x70': 'contacts_per_person_symptomatic_30x70',
    'contacts per person symptomatic 30x80': 'contacts_per_person_symptomatic_30x80',
    'contacts per person symptomatic 40x50': 'contacts_per_person_symptomatic_40x50',
    'contacts per person symptomatic 40x60': 'contacts_per_person_symptomatic_40x60',
    'contacts per person symptomatic 40x70': 'contacts_per_person_symptomatic_40x70',
    'contacts per person symptomatic 40x80': 'contacts_per_person_symptomatic_40x80',
    'infection rate 20': 'infection_rate_20',
    'init total population 00': 'init_total_population_00',
    'init total population 10': 'init_total_population_10',
    'init total population 20': 'init_total_population_20',
    'init total population 30': 'init_total_population_30',
    'init total population 40': 'init_total_population_40',
    'incidence per 100000 40': 'incidence_per_100000_40',
    'contacts per person symptomatic self 00': 'contacts_per_person_symptomatic_self_00',
    'contacts per person symptomatic self 10': 'contacts_per_person_symptomatic_self_10',
    'contacts per person symptomatic self 20': 'contacts_per_person_symptomatic_self_20',
    'contacts per person symptomatic self 30': 'contacts_per_person_symptomatic_self_30',
    'contacts per person symptomatic self 40': 'contacts_per_person_symptomatic_self_40',
    'Isolated 10': 'isolated_10',
    'Isolated 20': 'isolated_20',
    'Isolated 30': 'isolated_30',
    'Isolated 40': 'isolated_40',
    'infection rate asymptomatic 10x20': 'infection_rate_asymptomatic_10x20',
    'Critical Cases 00': 'critical_cases_00',
    'Critical Cases 10': 'critical_cases_10',
    'Critical Cases 20': 'critical_cases_20',
    'Critical Cases 30': 'critical_cases_30',
    'Critical Cases 40': 'critical_cases_40',
    'isolated critical case rate 10': 'isolated_critical_case_rate_10',
    'isolated critical case rate 20': 'isolated_critical_case_rate_20',
    'isolated critical case rate 30': 'isolated_critical_case_rate_30',
    'isolated critical case rate 40': 'isolated_critical_case_rate_40',
    'infection rate asymptomatic 20x40': 'infection_rate_asymptomatic_20x40',
    'critical cases recovery rate 00': 'critical_cases_recovery_rate_00',
    'critical cases recovery rate 10': 'critical_cases_recovery_rate_10',
    'critical cases recovery rate 20': 'critical_cases_recovery_rate_20',
    'critical cases recovery rate 30': 'critical_cases_recovery_rate_30',
    'critical cases recovery rate 40': 'critical_cases_recovery_rate_40',
    'isolated recovery rate 10': 'isolated_recovery_rate_10',
    'isolated recovery rate 20': 'isolated_recovery_rate_20',
    'isolated recovery rate 30': 'isolated_recovery_rate_30',
    'isolated recovery rate 40': 'isolated_recovery_rate_40',
    'infection rate asymptomatic 30x60': 'infection_rate_asymptomatic_30x60',
    'death rate 00': 'death_rate_00',
    'death rate 10': 'death_rate_10',
    'death rate 20': 'death_rate_20',
    'death rate 30': 'death_rate_30',
    'death rate 40': 'death_rate_40',
    'isolation duration 10': 'isolation_duration_10',
    'isolation duration 20': 'isolation_duration_20',
    'isolation duration 30': 'isolation_duration_30',
    'isolation duration 40': 'isolation_duration_40',
    'infection rate asymptomatic 40x80': 'infection_rate_asymptomatic_40x80',
    'deimmunization rate 00': 'deimmunization_rate_00',
    'deimmunization rate 10': 'deimmunization_rate_10',
    'deimmunization rate 20': 'deimmunization_rate_20',
    'deimmunization rate 30': 'deimmunization_rate_30',
    'deimmunization rate 40': 'deimmunization_rate_40',
    'isolation effectiveness 10': 'isolation_effectiveness_10',
    'isolation effectiveness 20': 'isolation_effectiveness_20',
    'isolation effectiveness 30': 'isolation_effectiveness_30',
    'isolation effectiveness 40': 'isolation_effectiveness_40',
    'infection rate asymptomatic 60x10': 'infection_rate_asymptomatic_60x10',
    'Diseased 00': 'diseased_00',
    'Diseased 10': 'diseased_10',
    'Diseased 20': 'diseased_20',
    'Diseased 30': 'diseased_30',
    'infected asymptomatic recovery rate 30': 'infected_asymptomatic_recovery_rate_30',
    'isolation rate asymptomatic 10': 'isolation_rate_asymptomatic_10',
    'isolation rate asymptomatic 20': 'isolation_rate_asymptomatic_20',
    'isolation rate asymptomatic 30': 'isolation_rate_asymptomatic_30',
    'isolation rate asymptomatic 40': 'isolation_rate_asymptomatic_40',
    'infection rate asymptomatic 70x30': 'infection_rate_asymptomatic_70x30',
    'infection rate asymptomatic 70x40': 'infection_rate_asymptomatic_70x40',
    'infected critical case rate 00': 'infected_critical_case_rate_00',
    'infected critical case rate 10': 'infected_critical_case_rate_10',
    'duration of treatment 30': 'duration_of_treatment_30',
    'duration of treatment 40': 'duration_of_treatment_40',
    'isolation rate symptomatic 10': 'isolation_rate_symptomatic_10',
    'isolation rate symptomatic 20': 'isolation_rate_symptomatic_20',
    'isolation rate symptomatic 30': 'isolation_rate_symptomatic_30',
    'isolation rate symptomatic 40': 'isolation_rate_symptomatic_40',
    'social distancing effectiveness 00': 'social_distancing_effectiveness_00',
    'infection rate asymptomatic 00x30': 'infection_rate_asymptomatic_00x30',
    'Infected symptomatic 00': 'infected_symptomatic_00',
    'first infection 10': 'first_infection_10',
    'first infection 20': 'first_infection_20',
    'first infection 30': 'first_infection_30',
    'first infection 40': 'first_infection_40',
    'Infected symptomatic 00x50': 'infected_symptomatic_00x50',
    'Infected asymptomatic 00x40': 'infected_asymptomatic_00x40',
    'new cases 00': 'new_cases_00',
    'new cases 10': 'new_cases_10',
    'new cases 20': 'new_cases_20',
    'fraction of asymptomatic case development 00': 'fraction_of_asymptomatic_case_development_00',
    'fraction of asymptomatic case development 10': 'fraction_of_asymptomatic_case_development_10',
    'fraction of asymptomatic case development 20': 'fraction_of_asymptomatic_case_development_20',
    'fraction of asymptomatic case development 30': 'fraction_of_asymptomatic_case_development_30',
    'fraction of asymptomatic case development 40': 'fraction_of_asymptomatic_case_development_40',
    'social distancing end 60': 'social_distancing_end_60',
    'non controlled pop 00x10': 'non_controlled_pop_00x10',
    'non controlled pop 00x20': 'non_controlled_pop_00x20',
    'non controlled pop 00x30': 'non_controlled_pop_00x30',
    'non controlled pop 00x40': 'non_controlled_pop_00x40',
    'fraction of critical cases 00': 'fraction_of_critical_cases_00',
    'fraction of critical cases 10': 'fraction_of_critical_cases_10',
    'fraction of critical cases 20': 'fraction_of_critical_cases_20',
    'fraction of critical cases 30': 'fraction_of_critical_cases_30',
    'fraction of critical cases 40': 'fraction_of_critical_cases_40',
    'non controlled pop 10x30': 'non_controlled_pop_10x30',
    'non controlled pop 10x40': 'non_controlled_pop_10x40',
    'non controlled pop 10x50': 'non_controlled_pop_10x50',
    'non controlled pop 10x60': 'non_controlled_pop_10x60',
    'non controlled pop 10x70': 'non_controlled_pop_10x70',
    'fraction of death 00': 'fraction_of_death_00',
    'fraction of death 10': 'fraction_of_death_10',
    'fraction of death 20': 'fraction_of_death_20',
    'fraction of death 30': 'fraction_of_death_30',
    'fraction of death 40': 'fraction_of_death_40',
    'non controlled pop 20x70': 'non_controlled_pop_20x70',
    'non controlled pop 20x80': 'non_controlled_pop_20x80',
    'non controlled pop 30x40': 'non_controlled_pop_30x40',
    'non controlled pop 30x50': 'non_controlled_pop_30x50',
    'non controlled pop 30x60': 'non_controlled_pop_30x60',
    'fraction of symptomatic 00': 'fraction_of_symptomatic_00',
    'fraction of symptomatic 10': 'fraction_of_symptomatic_10',
    'fraction of symptomatic 20': 'fraction_of_symptomatic_20',
    'fraction of symptomatic 30': 'fraction_of_symptomatic_30',
    'fraction of symptomatic 40': 'fraction_of_symptomatic_40',
    'non controlled pop 40x80': 'non_controlled_pop_40x80',
    'infection rate symptomatic 30x10': 'infection_rate_symptomatic_30x10',
    'infected symptomatic recovery rate 10': 'infected_symptomatic_recovery_rate_10',
    'infected symptomatic recovery rate 20': 'infected_symptomatic_recovery_rate_20',
    'infected symptomatic recovery rate 30': 'infected_symptomatic_recovery_rate_30',
    'immunity time 00': 'immunity_time_00',
    'immunity time 10': 'immunity_time_10',
    'immunity time 20': 'immunity_time_20',
    'immunity time 30': 'immunity_time_30',
    'immunity time 40': 'immunity_time_40',
    'non controlled population 20': 'non_controlled_population_20',
    'non controlled population 30': 'non_controlled_population_30',
    'non controlled population 40': 'non_controlled_population_40',
    'infection rate symptomatic 40x60': 'infection_rate_symptomatic_40x60',
    'infection rate 30': 'infection_rate_30',
    'incidence per 100000 00': 'incidence_per_100000_00',
    'incidence per 100000 10': 'incidence_per_100000_10',
    'incidence per 100000 20': 'incidence_per_100000_20',
    'incidence per 100000 30': 'incidence_per_100000_30',
    'infection rate symptomatic 50x30': 'infection_rate_symptomatic_50x30',
    'infection rate symptomatic 50x40': 'infection_rate_symptomatic_50x40',
    'infection rate asymptomatic 00x20': 'infection_rate_asymptomatic_00x20',
    'Infected asymptomatic 40x50': 'infected_asymptomatic_40x50',
    'infection rate asymptomatic 00x40': 'infection_rate_asymptomatic_00x40',
    'infection rate asymptomatic 00x50': 'infection_rate_asymptomatic_00x50',
    'Infected asymptomatic 00': 'infected_asymptomatic_00',
    'Infected asymptomatic 00x10': 'infected_asymptomatic_00x10',
    'Infected asymptomatic 00x20': 'infected_asymptomatic_00x20',
    'Infected asymptomatic 00x30': 'infected_asymptomatic_00x30',
    'infection rate asymptomatic 50x30': 'infection_rate_asymptomatic_50x30',
    'Infected asymptomatic 00x50': 'infected_asymptomatic_00x50',
    'Infected asymptomatic 00x60': 'infected_asymptomatic_00x60',
    'Infected asymptomatic 00x70': 'infected_asymptomatic_00x70',
    'Infected asymptomatic 00x80': 'infected_asymptomatic_00x80',
    'Infected asymptomatic 10': 'infected_asymptomatic_10',
    'Infected asymptomatic 10x20': 'infected_asymptomatic_10x20',
    'Infected asymptomatic 10x30': 'infected_asymptomatic_10x30',
    'Infected asymptomatic 10x40': 'infected_asymptomatic_10x40',
    'Infected asymptomatic 10x50': 'infected_asymptomatic_10x50',
    'Infected asymptomatic 10x60': 'infected_asymptomatic_10x60',
    'Infected asymptomatic 10x70': 'infected_asymptomatic_10x70',
    'Infected asymptomatic 10x80': 'infected_asymptomatic_10x80',
    'Infected asymptomatic 20': 'infected_asymptomatic_20',
    'Infected asymptomatic 20x30': 'infected_asymptomatic_20x30',
    'Infected asymptomatic 20x40': 'infected_asymptomatic_20x40',
    'Infected asymptomatic 20x50': 'infected_asymptomatic_20x50',
    'Infected asymptomatic 20x60': 'infected_asymptomatic_20x60',
    'Infected asymptomatic 20x70': 'infected_asymptomatic_20x70',
    'Infected asymptomatic 20x80': 'infected_asymptomatic_20x80',
    'Infected asymptomatic 30': 'infected_asymptomatic_30',
    'Infected asymptomatic 30x40': 'infected_asymptomatic_30x40',
    'Infected asymptomatic 30x50': 'infected_asymptomatic_30x50',
    'Infected asymptomatic 30x60': 'infected_asymptomatic_30x60',
    'Infected asymptomatic 30x70': 'infected_asymptomatic_30x70',
    'Infected asymptomatic 30x80': 'infected_asymptomatic_30x80',
    'Infected asymptomatic 40': 'infected_asymptomatic_40',
    'Infected symptomatic 40x70': 'infected_symptomatic_40x70',
    'self quarantine end 70': 'self_quarantine_end_70',
    'Infected asymptomatic 40x70': 'infected_asymptomatic_40x70',
    'Infected asymptomatic 40x80': 'infected_asymptomatic_40x80',
    'self quarantine policy 10': 'self_quarantine_policy_10',
    'self quarantine policy 20': 'self_quarantine_policy_20',
    'self quarantine policy 30': 'self_quarantine_policy_30',
    'social distancing start 20': 'social_distancing_start_20',
    'self quarantine policy 50': 'self_quarantine_policy_50',
    'self quarantine policy 60': 'self_quarantine_policy_60',
    'self quarantine policy 70': 'self_quarantine_policy_70',
    'self quarantine policy 80': 'self_quarantine_policy_80',
    'infection rate asymptomatic 60x00': 'infection_rate_asymptomatic_60x00',
    'self quarantine policy SWITCH self 00': 'self_quarantine_policy_switch_self_00',
    'self quarantine policy SWITCH self 10': 'self_quarantine_policy_switch_self_10',
    'infected asymptomatic recovery rate 00': 'infected_asymptomatic_recovery_rate_00',
    'infected asymptomatic recovery rate 10': 'infected_asymptomatic_recovery_rate_10',
    'infected asymptomatic recovery rate 20': 'infected_asymptomatic_recovery_rate_20',
    'init accumulated cases 40': 'init_accumulated_cases_40',
    'infected asymptomatic recovery rate 40': 'infected_asymptomatic_recovery_rate_40',
    'infection rate asymptomatic 70x00': 'infection_rate_asymptomatic_70x00',
    'infection rate asymptomatic 70x10': 'infection_rate_asymptomatic_70x10',
    'infection rate asymptomatic 70x20': 'infection_rate_asymptomatic_70x20',
    'self quarantine start 00': 'self_quarantine_start_00',
    'self quarantine start 10': 'self_quarantine_start_10',
    'init Critical Cases 00': 'init_critical_cases_00',
    'init Critical Cases 10': 'init_critical_cases_10',
    'infected critical case rate 20': 'infected_critical_case_rate_20',
    'infected critical case rate 30': 'infected_critical_case_rate_30',
    'infected critical case rate 40': 'infected_critical_case_rate_40',
    'infection rate asymptomatic 80x20': 'infection_rate_asymptomatic_80x20',
    'infection rate asymptomatic 80x30': 'infection_rate_asymptomatic_80x30',
    'infection rate asymptomatic 80x40': 'infection_rate_asymptomatic_80x40',
    'Infected symptomatic 40x60': 'infected_symptomatic_40x60',
    'infection rate asymptomatic 40x50': 'infection_rate_asymptomatic_40x50',
    'init Diseased 00': 'init_diseased_00',
    'Infected symptomatic 00x10': 'infected_symptomatic_00x10',
    'Infected symptomatic 00x20': 'infected_symptomatic_00x20',
    'Infected symptomatic 00x30': 'infected_symptomatic_00x30',
    'Infected symptomatic 00x40': 'infected_symptomatic_00x40',
    'infection rate asymptomatic 10x00': 'infection_rate_asymptomatic_10x00',
    'infection rate symptomatic 20x40': 'infection_rate_symptomatic_20x40',
    'Infected symptomatic 00x70': 'infected_symptomatic_00x70',
    'Infected symptomatic 00x80': 'infected_symptomatic_00x80',
    'Infected symptomatic 10': 'infected_symptomatic_10',
    'Infected symptomatic 10x20': 'infected_symptomatic_10x20',
    'Infected symptomatic 10x30': 'infected_symptomatic_10x30',
    'Infected symptomatic 10x40': 'infected_symptomatic_10x40',
    'Infected symptomatic 10x50': 'infected_symptomatic_10x50',
    'social distancing end 50': 'social_distancing_end_50',
    'infection rate asymptomatic 20x30': 'infection_rate_asymptomatic_20x30',
    'social distancing end 70': 'social_distancing_end_70',
    'social distancing end 80': 'social_distancing_end_80',
    'Infected symptomatic 20x40': 'infected_symptomatic_20x40',
    'Infected symptomatic 20x50': 'infected_symptomatic_20x50',
    'Infected symptomatic 20x60': 'infected_symptomatic_20x60',
    'Infected symptomatic 20x70': 'infected_symptomatic_20x70',
    'Infected symptomatic 20x80': 'infected_symptomatic_20x80',
    'init Infected symptomatic 40': 'init_infected_symptomatic_40',
    'social distancing policy 60': 'social_distancing_policy_60',
    'social distancing policy 70': 'social_distancing_policy_70',
    'social distancing policy 80': 'social_distancing_policy_80',
    'Infected symptomatic 30x70': 'infected_symptomatic_30x70',
    'Infected symptomatic 30x80': 'infected_symptomatic_30x80',
    'Infected symptomatic 40': 'infected_symptomatic_40',
    'Infected symptomatic 40x50': 'infected_symptomatic_40x50',
    'infection rate asymptomatic 40x30': 'infection_rate_asymptomatic_40x30',
    'infection rate symptomatic 10x50': 'infection_rate_symptomatic_10x50',
    'Infected symptomatic 40x80': 'infected_symptomatic_40x80',
    'infection rate symptomatic 10x70': 'infection_rate_symptomatic_10x70',
    'infection rate symptomatic 10x80': 'infection_rate_symptomatic_10x80',
    'infection rate symptomatic 20x00': 'infection_rate_symptomatic_20x00',
    'social distancing start 00': 'social_distancing_start_00',
    'social distancing start 10': 'social_distancing_start_10',
    'init Recovered 00': 'init_recovered_00',
    'social distancing start 30': 'social_distancing_start_30',
    'social distancing start 40': 'social_distancing_start_40',
    'init Recovered 30': 'init_recovered_30',
    'init Recovered 40': 'init_recovered_40',
    'infection rate symptomatic 30x00': 'infection_rate_symptomatic_30x00',
    'infected symptomatic recovery rate 00': 'infected_symptomatic_recovery_rate_00',
    'infection rate asymptomatic 60x20': 'infection_rate_asymptomatic_60x20',
    'infection rate asymptomatic 60x30': 'infection_rate_asymptomatic_60x30',
    'Susceptible 00': 'susceptible_00',
    'infected symptomatic recovery rate 40': 'infected_symptomatic_recovery_rate_40',
    'Susceptible 30': 'susceptible_30',
    'Susceptible 40': 'susceptible_40',
    'init Susceptible 30': 'init_susceptible_30',
    'init Susceptible 40': 'init_susceptible_40',
    'infection rate symptomatic 40x20': 'infection_rate_symptomatic_40x20',
    'infection rate 00': 'infection_rate_00',
    'infection rate 10': 'infection_rate_10',
    'infection rate asymptomatic 30x40': 'infection_rate_asymptomatic_30x40',
    'symptomatic contact fraction 00': 'symptomatic_contact_fraction_00',
    'infection rate 40': 'infection_rate_40',
    'symptomatic contact fraction 30': 'symptomatic_contact_fraction_30',
    'symptomatic contact fraction 40': 'symptomatic_contact_fraction_40',
    'infection rate asymptomatic 40x00': 'infection_rate_asymptomatic_40x00',
    'infection rate asymptomatic 40x10': 'infection_rate_asymptomatic_40x10',
    'infection rate asymptomatic 00x10': 'infection_rate_asymptomatic_00x10',
    'infection rate symptomatic 10x40': 'infection_rate_symptomatic_10x40',
    'self quarantine end 60': 'self_quarantine_end_60',
    'infection rate asymptomatic 40x60': 'infection_rate_asymptomatic_40x60',
    'symptomatic duration 00': 'symptomatic_duration_00',
    'infection rate asymptomatic 00x60': 'infection_rate_asymptomatic_00x60',
    'infection rate asymptomatic 00x70': 'infection_rate_asymptomatic_00x70',
    'infection rate asymptomatic 00x80': 'infection_rate_asymptomatic_00x80',
    'infection rate symptomatic 60x40': 'infection_rate_symptomatic_60x40',
    'infection rate asymptomatic 30x20': 'infection_rate_asymptomatic_30x20',
    'infection rate asymptomatic 10x30': 'infection_rate_asymptomatic_10x30',
    'infection rate asymptomatic 10x40': 'infection_rate_asymptomatic_10x40',
    'infection rate asymptomatic 10x50': 'infection_rate_asymptomatic_10x50',
    'infection rate asymptomatic 10x60': 'infection_rate_asymptomatic_10x60',
    'infection rate asymptomatic 10x70': 'infection_rate_asymptomatic_10x70',
    'infection rate asymptomatic 10x80': 'infection_rate_asymptomatic_10x80',
    'infection rate asymptomatic 20x00': 'infection_rate_asymptomatic_20x00',
    'infection rate asymptomatic 20x10': 'infection_rate_asymptomatic_20x10',
    'symptomatic rate 40': 'symptomatic_rate_40',
    'self quarantine policy SWITCH self 30': 'self_quarantine_policy_switch_self_30',
    'infection rate asymptomatic 20x50': 'infection_rate_asymptomatic_20x50',
    'infection rate asymptomatic 20x60': 'infection_rate_asymptomatic_20x60',
    'infection rate asymptomatic 20x70': 'infection_rate_asymptomatic_20x70',
    'infection rate asymptomatic 20x80': 'infection_rate_asymptomatic_20x80',
    'infection rate asymptomatic 30x00': 'infection_rate_asymptomatic_30x00',
    'infection rate asymptomatic 30x10': 'infection_rate_asymptomatic_30x10',
    'infection rate symptomatic 40x50': 'infection_rate_symptomatic_40x50',
    'infection rate symptomatic 00x40': 'infection_rate_symptomatic_00x40',
    'infection rate asymptomatic 30x50': 'infection_rate_asymptomatic_30x50',
    'infection rate symptomatic self 00': 'infection_rate_symptomatic_self_00',
    'infection rate asymptomatic 30x70': 'infection_rate_asymptomatic_30x70',
    'infection rate asymptomatic 30x80': 'infection_rate_asymptomatic_30x80',
    'infection rate symptomatic 10x00': 'infection_rate_symptomatic_10x00',
    'infection rate symptomatic 10x20': 'infection_rate_symptomatic_10x20',
    'infection rate asymptomatic 40x20': 'infection_rate_asymptomatic_40x20',
    'self quarantine end 50': 'self_quarantine_end_50',
    'init Isolated 30': 'init_isolated_30',
    'infection rate symptomatic 10x60': 'infection_rate_symptomatic_10x60',
    'infection rate asymptomatic 40x70': 'infection_rate_asymptomatic_40x70',
    'total infected 30': 'total_infected_30',
    'infection rate asymptomatic 50x00': 'infection_rate_asymptomatic_50x00',
    'infection rate asymptomatic 50x10': 'infection_rate_asymptomatic_50x10',
    'infection rate asymptomatic 50x20': 'infection_rate_asymptomatic_50x20',
    'infection rate symptomatic 00x30': 'infection_rate_symptomatic_00x30',
    'infection rate asymptomatic 50x40': 'infection_rate_asymptomatic_50x40',
    'total infection rate 00': 'total_infection_rate_00',
    'total infection rate 10': 'total_infection_rate_10',
    'total infection rate 20': 'total_infection_rate_20',
    'non controlled pop 40x70': 'non_controlled_pop_40x70',
    'total infection rate 30': 'total_infection_rate_30',
    'total infection rate 40': 'total_infection_rate_40',
    'symptomatic rate 30': 'symptomatic_rate_30',
    'infection rate asymptomatic 60x40': 'infection_rate_asymptomatic_60x40',
    'init Susceptible 00': 'init_susceptible_00',
    'self quarantine policy SWITCH self 40': 'self_quarantine_policy_switch_self_40',
    'isolation rate asymptomatic 00': 'isolation_rate_asymptomatic_00',
    'social distancing policy 00': 'social_distancing_policy_00',
    'infection rate symptomatic 40x10': 'infection_rate_symptomatic_40x10',
    'non controlled population 10': 'non_controlled_population_10',
    'infection rate symptomatic 40x30': 'infection_rate_symptomatic_40x30',
    'test fraction 20': 'test_fraction_20',
    'test fraction 30': 'test_fraction_30',
    'self quarantine start 20': 'self_quarantine_start_20',
    'init Critical Cases 20': 'init_critical_cases_20',
    'init Critical Cases 30': 'init_critical_cases_30',
    'isolation rate symptomatic 00': 'isolation_rate_symptomatic_00',
    'infection rate symptomatic self 30': 'infection_rate_symptomatic_self_30',
    'infection rate symptomatic self 40': 'infection_rate_symptomatic_self_40',
    'infection rate symptomatic 10x30': 'infection_rate_symptomatic_10x30',
    'init Isolated 20': 'init_isolated_20',
    'total infected 00': 'total_infected_00',
    'total infected 10': 'total_infected_10',
    'init Diseased 10': 'init_diseased_10',
    'init Diseased 20': 'init_diseased_20',
    'init Diseased 30': 'init_diseased_30',
    'init Diseased 40': 'init_diseased_40',
    'symptomatic duration 40': 'symptomatic_duration_40',
    'init Infected symptomatic 30': 'init_infected_symptomatic_30',
    'Recovered 00': 'recovered_00',
    'social distancing end 00': 'social_distancing_end_00',
    'init Infected asymptomatic 00': 'init_infected_asymptomatic_00',
    'new cases 30': 'new_cases_30',
    'infection rate quarantined self 00': 'infection_rate_quarantined_self_00',
    'social distancing end 40': 'social_distancing_end_40',
    'self quarantine end 40': 'self_quarantine_end_40',
    'self quarantine policy SWITCH self 20': 'self_quarantine_policy_switch_self_20',
    'Susceptible 10': 'susceptible_10',
    'infection rate symptomatic 80x00': 'infection_rate_symptomatic_80x00',
    'infection rate symptomatic 80x10': 'infection_rate_symptomatic_80x10',
    'infection rate symptomatic 80x20': 'infection_rate_symptomatic_80x20',
    'init Infected symptomatic 00': 'init_infected_symptomatic_00',
    'infection rate symptomatic 00x10': 'infection_rate_symptomatic_00x10',
    'infection rate symptomatic 00x20': 'infection_rate_symptomatic_00x20',
    'non controlled pop 00x70': 'non_controlled_pop_00x70',
    'social distancing policy 50': 'social_distancing_policy_50',
    'infection rate symptomatic 00x50': 'infection_rate_symptomatic_00x50',
    'infection rate symptomatic 00x60': 'infection_rate_symptomatic_00x60',
    'infection rate symptomatic 00x70': 'infection_rate_symptomatic_00x70',
    'infection rate symptomatic 00x80': 'infection_rate_symptomatic_00x80',
    'social distancing policy SWITCH self 00': 'social_distancing_policy_switch_self_00',
    'init Isolated 00': 'init_isolated_00',
    'init Isolated 10': 'init_isolated_10',
    'isolation duration 00': 'isolation_duration_00',
    'non controlled pop 20x40': 'non_controlled_pop_20x40',
    'init Isolated 40': 'init_isolated_40',
    'non controlled pop 20x60': 'non_controlled_pop_20x60',
    'self quarantine policy 00': 'self_quarantine_policy_00',
    'infection rate symptomatic 20x10': 'infection_rate_symptomatic_20x10',
    'infection rate symptomatic 20x30': 'infection_rate_symptomatic_20x30',
    'social distancing policy 40': 'social_distancing_policy_40',
    'infection rate symptomatic 20x50': 'infection_rate_symptomatic_20x50',
    'infection rate symptomatic 20x60': 'infection_rate_symptomatic_20x60',
    'infection rate symptomatic 20x70': 'infection_rate_symptomatic_20x70',
    'infection rate symptomatic 20x80': 'infection_rate_symptomatic_20x80',
    'infection rate symptomatic 70x20': 'infection_rate_symptomatic_70x20',
    'infection rate symptomatic 70x30': 'infection_rate_symptomatic_70x30',
    'infection rate symptomatic 70x40': 'infection_rate_symptomatic_70x40',
    'non controlled pop 10x80': 'non_controlled_pop_10x80',
    'non controlled pop 20x30': 'non_controlled_pop_20x30',
    'social distancing policy SWITCH self 40': 'social_distancing_policy_switch_self_40',
    'init Susceptible 10': 'init_susceptible_10',
    'init Susceptible 20': 'init_susceptible_20',
    'self quarantine effectiveness 20': 'self_quarantine_effectiveness_20',
    'non controlled population 00': 'non_controlled_population_00',
    'infection rate symptomatic 80x40': 'infection_rate_symptomatic_80x40',
    'isolated recovery rate 00': 'isolated_recovery_rate_00',
    'social distancing policy SWITCH self 20': 'social_distancing_policy_switch_self_20',
    'non controlled pop 00x80': 'non_controlled_pop_00x80',
    'test fraction 40': 'test_fraction_40',
    'symptomatic contact fraction 10': 'symptomatic_contact_fraction_10',
    'symptomatic contact fraction 20': 'symptomatic_contact_fraction_20',
    'init Critical Cases 40': 'init_critical_cases_40',
    'self quarantine end 20': 'self_quarantine_end_20',
    'self quarantine end 30': 'self_quarantine_end_30',
    'init Infected symptomatic 20': 'init_infected_symptomatic_20',
    'social distancing policy SWITCH self 30': 'social_distancing_policy_switch_self_30',
    'init Recovered 10': 'init_recovered_10',
    'non controlled pop 20x50': 'non_controlled_pop_20x50',
    'social distancing effectiveness 20': 'social_distancing_effectiveness_20',
    'Isolated 00': 'isolated_00',
    'symptomatic duration 20': 'symptomatic_duration_20',
    'symptomatic duration 30': 'symptomatic_duration_30',
    'symptomatic rate 20': 'symptomatic_rate_20',
    'test fraction 10': 'test_fraction_10',
    'non controlled pop 00x60': 'non_controlled_pop_00x60',
    'Recovered 10': 'recovered_10',
    'infection rate symptomatic 70x00': 'infection_rate_symptomatic_70x00',
    'infection rate symptomatic 70x10': 'infection_rate_symptomatic_70x10',
    'init Infected asymptomatic 10': 'init_infected_asymptomatic_10',
    'init Infected asymptomatic 20': 'init_infected_asymptomatic_20',
    'init Infected symptomatic 10': 'init_infected_symptomatic_10',
    'social distancing policy SWITCH self 10': 'social_distancing_policy_switch_self_10',
    'non controlled pop 00x50': 'non_controlled_pop_00x50',
    'non controlled pop 30x70': 'non_controlled_pop_30x70',
    'self quarantine effectiveness 00': 'self_quarantine_effectiveness_00',
    'self quarantine effectiveness 10': 'self_quarantine_effectiveness_10',
    'social distancing effectiveness 30': 'social_distancing_effectiveness_30',
    'infection rate symptomatic 80x30': 'infection_rate_symptomatic_80x30',
    'isolated critical case rate 00': 'isolated_critical_case_rate_00',
    'test fraction 00': 'test_fraction_00',
    'symptomatic rate 10': 'symptomatic_rate_10',
    'social distancing policy 30': 'social_distancing_policy_30',
    'non controlled pop 10x20': 'non_controlled_pop_10x20',
    'infection rate symptomatic self 10': 'infection_rate_symptomatic_self_10',
    'infection rate symptomatic self 20': 'infection_rate_symptomatic_self_20',
    'total infected 40': 'total_infected_40',
    'new cases 40': 'new_cases_40',
    'social distancing effectiveness 40': 'social_distancing_effectiveness_40',
    'self quarantine effectiveness 40': 'self_quarantine_effectiveness_40',
    'social distancing policy 20': 'social_distancing_policy_20',
    'Susceptible 20': 'susceptible_20',
    'self quarantine end 80': 'self_quarantine_end_80',
    'symptomatic duration 10': 'symptomatic_duration_10',
    'symptomatic rate 00': 'symptomatic_rate_00',
    'social distancing policy 10': 'social_distancing_policy_10',
    'social distancing end 20': 'social_distancing_end_20',
    'social distancing end 30': 'social_distancing_end_30',
    'self quarantine start 40': 'self_quarantine_start_40',
    'isolation effectiveness 00': 'isolation_effectiveness_00',
    'non controlled pop 40x50': 'non_controlled_pop_40x50',
    'non controlled pop 40x60': 'non_controlled_pop_40x60',
    'Recovered 20': 'recovered_20',
    'self quarantine end 10': 'self_quarantine_end_10',
    'self quarantine end 00': 'self_quarantine_end_00',
    'self quarantine effectiveness 30': 'self_quarantine_effectiveness_30',
    'init Recovered 20': 'init_recovered_20',
    'social distancing end 10': 'social_distancing_end_10',
    'total infected 20': 'total_infected_20',
    'Recovered 40': 'recovered_40',
    'self quarantine start 30': 'self_quarantine_start_30',
    'Recovered 30': 'recovered_30',
    'non controlled pop 30x80': 'non_controlled_pop_30x80',
    'infection rate symptomatic 80x60': 'infection_rate_symptomatic_80x60',
    'accumulated cases 50': 'accumulated_cases_50',
    'accumulated cases 60': 'accumulated_cases_60',
    'infection rate symptomatic self 50': 'infection_rate_symptomatic_self_50',
    'infection rate symptomatic self 60': 'infection_rate_symptomatic_self_60',
    'contacts per person symptomatic 50x60': 'contacts_per_person_symptomatic_50x60',
    'asymptomatic duration 50': 'asymptomatic_duration_50',
    'asymptomatic duration 60': 'asymptomatic_duration_60',
    'infection start 50': 'infection_start_50',
    'infection start 60': 'infection_start_60',
    'infection start 70': 'infection_start_70',
    'infection start 80': 'infection_start_80',
    'fraction of death 60': 'fraction_of_death_60',
    'contacts per person symptomatic self 60': 'contacts_per_person_symptomatic_self_60',
    'case fatality rate 50': 'case_fatality_rate_50',
    'case fatality rate 60': 'case_fatality_rate_60',
    'fraction of symptomatic 50': 'fraction_of_symptomatic_50',
    'fraction of symptomatic 60': 'fraction_of_symptomatic_60',
    'contact infectivity asymptomatic 50x60': 'contact_infectivity_asymptomatic_50x60',
    'contact infectivity asymptomatic 50x70': 'contact_infectivity_asymptomatic_50x70',
    'contact infectivity asymptomatic 50x80': 'contact_infectivity_asymptomatic_50x80',
    'contact infectivity asymptomatic 60x70': 'contact_infectivity_asymptomatic_60x70',
    'contact infectivity asymptomatic 60x80': 'contact_infectivity_asymptomatic_60x80',
    'Recovered 50': 'recovered_50',
    'Recovered 60': 'recovered_60',
    'contact infectivity asymptomatic self 50': 'contact_infectivity_asymptomatic_self_50',
    'contact infectivity asymptomatic self 60': 'contact_infectivity_asymptomatic_self_60',
    'incidence per 100000 60': 'incidence_per_100000_60',
    'self quarantine effectiveness 50': 'self_quarantine_effectiveness_50',
    'self quarantine effectiveness 60': 'self_quarantine_effectiveness_60',
    'contact infectivity quarantine self 50': 'contact_infectivity_quarantine_self_50',
    'contact infectivity quarantine self 60': 'contact_infectivity_quarantine_self_60',
    'Infected asymptomatic 50x60': 'infected_asymptomatic_50x60',
    'Infected asymptomatic 50x70': 'infected_asymptomatic_50x70',
    'contact infectivity symptomatic 50x60': 'contact_infectivity_symptomatic_50x60',
    'contact infectivity symptomatic 50x70': 'contact_infectivity_symptomatic_50x70',
    'contact infectivity symptomatic 50x80': 'contact_infectivity_symptomatic_50x80',
    'contact infectivity symptomatic 60x70': 'contact_infectivity_symptomatic_60x70',
    'contact infectivity symptomatic 60x80': 'contact_infectivity_symptomatic_60x80',
    'self quarantine policy SWITCH self 60': 'self_quarantine_policy_switch_self_60',
    'init Isolated 50': 'init_isolated_50',
    'contact infectivity symptomatic self 50': 'contact_infectivity_symptomatic_self_50',
    'contact infectivity symptomatic self 60': 'contact_infectivity_symptomatic_self_60',
    'infected asymptomatic recovery rate 60': 'infected_asymptomatic_recovery_rate_60',
    'self quarantine start 60': 'self_quarantine_start_60',
    'contacts per person normal 50x60': 'contacts_per_person_normal_50x60',
    'contacts per person normal 50x70': 'contacts_per_person_normal_50x70',
    'contacts per person normal 50x80': 'contacts_per_person_normal_50x80',
    'contacts per person normal 60x70': 'contacts_per_person_normal_60x70',
    'contacts per person normal 60x80': 'contacts_per_person_normal_60x80',
    'init Susceptible 50': 'init_susceptible_50',
    'init Susceptible 60': 'init_susceptible_60',
    'contacts per person normal self 50': 'contacts_per_person_normal_self_50',
    'contacts per person normal self 60': 'contacts_per_person_normal_self_60',
    'Infected symptomatic 50x70': 'infected_symptomatic_50x70',
    'init total population 50': 'init_total_population_50',
    'non controlled pop 60x80': 'non_controlled_pop_60x80',
    'contacts per person symptomatic 50x70': 'contacts_per_person_symptomatic_50x70',
    'contacts per person symptomatic 50x80': 'contacts_per_person_symptomatic_50x80',
    'contacts per person symptomatic 60x70': 'contacts_per_person_symptomatic_60x70',
    'contacts per person symptomatic 60x80': 'contacts_per_person_symptomatic_60x80',
    'Isolated 60': 'isolated_60',
    'Isolated 50': 'isolated_50',
    'contacts per person symptomatic self 50': 'contacts_per_person_symptomatic_self_50',
    'normal first infected': 'normal_first_infected',
    'isolated critical case rate 50': 'isolated_critical_case_rate_50',
    'isolated critical case rate 60': 'isolated_critical_case_rate_60',
    'Critical Cases 50': 'critical_cases_50',
    'Critical Cases 60': 'critical_cases_60',
    'isolated recovery rate 50': 'isolated_recovery_rate_50',
    'isolated recovery rate 60': 'isolated_recovery_rate_60',
    'infection rate asymptomatic 50x60': 'infection_rate_asymptomatic_50x60',
    'critical cases recovery rate 50': 'critical_cases_recovery_rate_50',
    'critical cases recovery rate 60': 'critical_cases_recovery_rate_60',
    'isolation duration 50': 'isolation_duration_50',
    'isolation duration 60': 'isolation_duration_60',
    'infection rate asymptomatic 60x80': 'infection_rate_asymptomatic_60x80',
    'death rate 50': 'death_rate_50',
    'death rate 60': 'death_rate_60',
    'isolation effectiveness 50': 'isolation_effectiveness_50',
    'isolation effectiveness 60': 'isolation_effectiveness_60',
    'infection rate asymptomatic 80x60': 'infection_rate_asymptomatic_80x60',
    'deimmunization rate 50': 'deimmunization_rate_50',
    'deimmunization rate 60': 'deimmunization_rate_60',
    'isolation rate asymptomatic 50': 'isolation_rate_asymptomatic_50',
    'isolation rate asymptomatic 60': 'isolation_rate_asymptomatic_60',
    'Infected asymptomatic 60': 'infected_asymptomatic_60',
    'Diseased 50': 'diseased_50',
    'Diseased 60': 'diseased_60',
    'isolation rate symptomatic 50': 'isolation_rate_symptomatic_50',
    'isolation rate symptomatic 60': 'isolation_rate_symptomatic_60',
    'infection rate quarantined self 60': 'infection_rate_quarantined_self_60',
    'duration of treatment 50': 'duration_of_treatment_50',
    'duration of treatment 60': 'duration_of_treatment_60',
    'infection rate symptomatic 50x70': 'infection_rate_symptomatic_50x70',
    'infection rate symptomatic 50x80': 'infection_rate_symptomatic_50x80',
    'infection rate symptomatic 60x50': 'infection_rate_symptomatic_60x50',
    'first infection 50': 'first_infection_50',
    'first infection 60': 'first_infection_60',
    'first infection 70': 'first_infection_70',
    'first infection 80': 'first_infection_80',
    'non controlled pop 50x60': 'non_controlled_pop_50x60',
    'fraction of asymptomatic case development 50': 'fraction_of_asymptomatic_case_development_50',
    'fraction of asymptomatic case development 60': 'fraction_of_asymptomatic_case_development_60',
    'non controlled pop 60x70': 'non_controlled_pop_60x70',
    'Infected symptomatic 50x80': 'infected_symptomatic_50x80',
    'Infected symptomatic 60': 'infected_symptomatic_60',
    'fraction of critical cases 50': 'fraction_of_critical_cases_50',
    'fraction of critical cases 60': 'fraction_of_critical_cases_60',
    'non controlled population 60': 'non_controlled_population_60',
    'non controlled population 50': 'non_controlled_population_50',
    'fraction of death 50': 'fraction_of_death_50',
    'infected symptomatic recovery rate 50': 'infected_symptomatic_recovery_rate_50',
    'infected symptomatic recovery rate 60': 'infected_symptomatic_recovery_rate_60',
    'social distancing start 60': 'social_distancing_start_60',
    'init accumulated cases 50': 'init_accumulated_cases_50',
    'init accumulated cases 60': 'init_accumulated_cases_60',
    'infection rate 50': 'infection_rate_50',
    'infection rate 60': 'infection_rate_60',
    'infection rate 70': 'infection_rate_70',
    'infection rate 80': 'infection_rate_80',
    'immunity time 50': 'immunity_time_50',
    'immunity time 60': 'immunity_time_60',
    'infection rate asymptomatic 50x80': 'infection_rate_asymptomatic_50x80',
    'infection rate asymptomatic 60x50': 'infection_rate_asymptomatic_60x50',
    'infection rate asymptomatic 60x70': 'infection_rate_asymptomatic_60x70',
    'incidence per 100000 50': 'incidence_per_100000_50',
    'init Diseased 60': 'init_diseased_60',
    'infection rate asymptomatic 70x60': 'infection_rate_asymptomatic_70x60',
    'symptomatic duration 60': 'symptomatic_duration_60',
    'infection rate asymptomatic 80x50': 'infection_rate_asymptomatic_80x50',
    'Infected asymptomatic 50': 'infected_asymptomatic_50',
    'init Infected asymptomatic 60': 'init_infected_asymptomatic_60',
    'symptomatic rate 60': 'symptomatic_rate_60',
    'Infected asymptomatic 50x80': 'infected_asymptomatic_50x80',
    'infection rate asymptomatic self 60': 'infection_rate_asymptomatic_self_60',
    'Infected asymptomatic 60x70': 'infected_asymptomatic_60x70',
    'Infected asymptomatic 60x80': 'infected_asymptomatic_60x80',
    'self quarantine policy SWITCH self 50': 'self_quarantine_policy_switch_self_50',
    'infection rate quarantined self 50': 'infection_rate_quarantined_self_50',
    'social distancing start 50': 'social_distancing_start_50',
    'Infected symptomatic 50x60': 'infected_symptomatic_50x60',
    'infected asymptomatic recovery rate 50': 'infected_asymptomatic_recovery_rate_50',
    'infection rate symptomatic 50x60': 'infection_rate_symptomatic_50x60',
    'self quarantine start 50': 'self_quarantine_start_50',
    'total infected 50': 'total_infected_50',
    'init Recovered 50': 'init_recovered_50',
    'infected critical case rate 50': 'infected_critical_case_rate_50',
    'infected critical case rate 60': 'infected_critical_case_rate_60',
    'social distancing effectiveness 60': 'social_distancing_effectiveness_60',
    'infection rate symptomatic 70x60': 'infection_rate_symptomatic_70x60',
    'total infection rate 60': 'total_infection_rate_60',
    'Infected symptomatic 50': 'infected_symptomatic_50',
    'init Infected symptomatic 60': 'init_infected_symptomatic_60',
    'non controlled pop 50x80': 'non_controlled_pop_50x80',
    'Infected symptomatic 60x70': 'infected_symptomatic_60x70',
    'Infected symptomatic 60x80': 'infected_symptomatic_60x80',
    'social distancing policy SWITCH self 60': 'social_distancing_policy_switch_self_60',
    'social distancing policy SWITCH self 50': 'social_distancing_policy_switch_self_50',
    'test fraction 50': 'test_fraction_50',
    'test fraction 60': 'test_fraction_60',
    'new cases 60': 'new_cases_60',
    'infection rate asymptomatic 70x50': 'infection_rate_asymptomatic_70x50',
    'total infection rate 80': 'total_infection_rate_80',
    'symptomatic duration 50': 'symptomatic_duration_50',
    'init Isolated 60': 'init_isolated_60',
    'Susceptible 50': 'susceptible_50',
    'Susceptible 60': 'susceptible_60',
    'total infected 60': 'total_infected_60',
    'infection rate asymptomatic 50x70': 'infection_rate_asymptomatic_50x70',
    'init Critical Cases 60': 'init_critical_cases_60',
    'symptomatic contact fraction 50': 'symptomatic_contact_fraction_50',
    'symptomatic contact fraction 60': 'symptomatic_contact_fraction_60',
    'init Infected symptomatic 50': 'init_infected_symptomatic_50',
    'new cases 50': 'new_cases_50',
    'infection rate symptomatic 80x50': 'infection_rate_symptomatic_80x50',
    'init Diseased 50': 'init_diseased_50',
    'non controlled pop 50x70': 'non_controlled_pop_50x70',
    'infection rate symptomatic 70x50': 'infection_rate_symptomatic_70x50',
    'symptomatic rate 50': 'symptomatic_rate_50',
    'init total population 60': 'init_total_population_60',
    'infection rate asymptomatic self 50': 'infection_rate_asymptomatic_self_50',
    'infection rate symptomatic 60x70': 'infection_rate_symptomatic_60x70',
    'infection rate symptomatic 60x80': 'infection_rate_symptomatic_60x80',
    'init Critical Cases 50': 'init_critical_cases_50',
    'social distancing effectiveness 50': 'social_distancing_effectiveness_50',
    'total infection rate 50': 'total_infection_rate_50',
    'init Infected asymptomatic 50': 'init_infected_asymptomatic_50',
    'init Recovered 60': 'init_recovered_60',
    'contact infectivity asymptomatic self 70': 'contact_infectivity_asymptomatic_self_70',
    'contact infectivity asymptomatic self 80': 'contact_infectivity_asymptomatic_self_80',
    'infection rate symptomatic self 80': 'infection_rate_symptomatic_self_80',
    'infection rate asymptomatic 70x80': 'infection_rate_asymptomatic_70x80',
    'infection rate asymptomatic 80x70': 'infection_rate_asymptomatic_80x70',
    'contact infectivity asymptomatic 70x80': 'contact_infectivity_asymptomatic_70x80',
    'infection rate asymptomatic self 70': 'infection_rate_asymptomatic_self_70',
    'infection rate asymptomatic self 80': 'infection_rate_asymptomatic_self_80',
    'infection rate symptomatic self 70': 'infection_rate_symptomatic_self_70',
    'contact infectivity symptomatic self 70': 'contact_infectivity_symptomatic_self_70',
    'contact infectivity symptomatic 70x80': 'contact_infectivity_symptomatic_70x80',
    'infection rate symptomatic 80x70': 'infection_rate_symptomatic_80x70',
    'contact infectivity symptomatic self 80': 'contact_infectivity_symptomatic_self_80',
    'infection rate symptomatic 70x80': 'infection_rate_symptomatic_70x80',
    'isolation rate asymptomatic 80': 'isolation_rate_asymptomatic_80',
    'isolation rate symptomatic 70': 'isolation_rate_symptomatic_70',
    'isolation rate symptomatic 80': 'isolation_rate_symptomatic_80',
    'isolation rate asymptomatic 70': 'isolation_rate_asymptomatic_70',
    'fraction of death 70': 'fraction_of_death_70',
    'accumulated cases 70': 'accumulated_cases_70',
    'accumulated cases 80': 'accumulated_cases_80',
    'fraction of symptomatic 70': 'fraction_of_symptomatic_70',
    'asymptomatic duration 70': 'asymptomatic_duration_70',
    'asymptomatic duration 80': 'asymptomatic_duration_80',
    'immunity time 70': 'immunity_time_70',
    'init Isolated 70': 'init_isolated_70',
    'init Isolated 80': 'init_isolated_80',
    'incidence per 100000 70': 'incidence_per_100000_70',
    'case fatality rate 70': 'case_fatality_rate_70',
    'case fatality rate 80': 'case_fatality_rate_80',
    'init Susceptible 70': 'init_susceptible_70',
    'init total population 70': 'init_total_population_70',
    'contact infectivity quarantine self 70': 'contact_infectivity_quarantine_self_70',
    'contact infectivity quarantine self 80': 'contact_infectivity_quarantine_self_80',
    'Isolated 80': 'isolated_80',
    'contacts per person normal 70x80': 'contacts_per_person_normal_70x80',
    'infected critical case rate 80': 'infected_critical_case_rate_80',
    'contacts per person normal self 70': 'contacts_per_person_normal_self_70',
    'contacts per person normal self 80': 'contacts_per_person_normal_self_80',
    'contacts per person symptomatic 70x80': 'contacts_per_person_symptomatic_70x80',
    'contacts per person symptomatic self 70': 'contacts_per_person_symptomatic_self_70',
    'contacts per person symptomatic self 80': 'contacts_per_person_symptomatic_self_80',
    'isolation effectiveness 70': 'isolation_effectiveness_70',
    'Critical Cases 70': 'critical_cases_70',
    'Critical Cases 80': 'critical_cases_80',
    'critical cases recovery rate 70': 'critical_cases_recovery_rate_70',
    'critical cases recovery rate 80': 'critical_cases_recovery_rate_80',
    'death rate 70': 'death_rate_70',
    'death rate 80': 'death_rate_80',
    'deimmunization rate 70': 'deimmunization_rate_70',
    'deimmunization rate 80': 'deimmunization_rate_80',
    'Diseased 70': 'diseased_70',
    'Diseased 80': 'diseased_80',
    'non controlled pop 70x80': 'non_controlled_pop_70x80',
    'duration of treatment 70': 'duration_of_treatment_70',
    'duration of treatment 80': 'duration_of_treatment_80',
    'non controlled population 80': 'non_controlled_population_80',
    'infected asymptomatic recovery rate 80': 'infected_asymptomatic_recovery_rate_80',
    'fraction of asymptomatic case development 70': 'fraction_of_asymptomatic_case_development_70',
    'fraction of asymptomatic case development 80': 'fraction_of_asymptomatic_case_development_80',
    'init Critical Cases 80': 'init_critical_cases_80',
    'fraction of critical cases 70': 'fraction_of_critical_cases_70',
    'fraction of critical cases 80': 'fraction_of_critical_cases_80',
    'init Diseased 80': 'init_diseased_80',
    'fraction of death 80': 'fraction_of_death_80',
    'init Infected asymptomatic 80': 'init_infected_asymptomatic_80',
    'fraction of symptomatic 80': 'fraction_of_symptomatic_80',
    'Recovered 80': 'recovered_80',
    'immunity time 80': 'immunity_time_80',
    'self quarantine effectiveness 80': 'self_quarantine_effectiveness_80',
    'infection rate quarantined self 70': 'infection_rate_quarantined_self_70',
    'incidence per 100000 80': 'incidence_per_100000_80',
    'Infected asymptomatic 70': 'infected_asymptomatic_70',
    'Infected asymptomatic 70x80': 'infected_asymptomatic_70x80',
    'Infected asymptomatic 80': 'infected_asymptomatic_80',
    'self quarantine policy SWITCH self 80': 'self_quarantine_policy_switch_self_80',
    'Infected symptomatic 70': 'infected_symptomatic_70',
    'Infected symptomatic 70x80': 'infected_symptomatic_70x80',
    'Infected symptomatic 80': 'infected_symptomatic_80',
    'social distancing effectiveness 70': 'social_distancing_effectiveness_70',
    'infected asymptomatic recovery rate 70': 'infected_asymptomatic_recovery_rate_70',
    'init accumulated cases 80': 'init_accumulated_cases_80',
    'infected critical case rate 70': 'infected_critical_case_rate_70',
    'init Critical Cases 70': 'init_critical_cases_70',
    'social distancing policy SWITCH self 70': 'social_distancing_policy_switch_self_70',
    'infected symptomatic recovery rate 70': 'infected_symptomatic_recovery_rate_70',
    'infected symptomatic recovery rate 80': 'infected_symptomatic_recovery_rate_80',
    'Susceptible 80': 'susceptible_80',
    'init Infected symptomatic 80': 'init_infected_symptomatic_80',
    'symptomatic contact fraction 80': 'symptomatic_contact_fraction_80',
    'symptomatic contact fraction 70': 'symptomatic_contact_fraction_70',
    'infection rate quarantined self 80': 'infection_rate_quarantined_self_80',
    'init Recovered 80': 'init_recovered_80',
    'symptomatic rate 70': 'symptomatic_rate_70',
    'init Susceptible 80': 'init_susceptible_80',
    'test fraction 70': 'test_fraction_70',
    'init total population 80': 'init_total_population_80',
    'init accumulated cases 70': 'init_accumulated_cases_70',
    'social distancing effectiveness 80': 'social_distancing_effectiveness_80',
    'total infected 70': 'total_infected_70',
    'isolated critical case rate 80': 'isolated_critical_case_rate_80',
    'total infection rate 70': 'total_infection_rate_70',
    'init Diseased 70': 'init_diseased_70',
    'social distancing policy SWITCH self 80': 'social_distancing_policy_switch_self_80',
    'isolation duration 70': 'isolation_duration_70',
    'init Infected asymptomatic 70': 'init_infected_asymptomatic_70',
    'social distancing start 80': 'social_distancing_start_80',
    'new cases 80': 'new_cases_80',
    'init Infected symptomatic 70': 'init_infected_symptomatic_70',
    'Recovered 70': 'recovered_70',
    'self quarantine effectiveness 70': 'self_quarantine_effectiveness_70',
    'isolated critical case rate 70': 'isolated_critical_case_rate_70',
    'self quarantine start 70': 'self_quarantine_start_70',
    'init Recovered 70': 'init_recovered_70',
    'symptomatic duration 80': 'symptomatic_duration_80',
    'self quarantine policy SWITCH self 70': 'self_quarantine_policy_switch_self_70',
    'symptomatic rate 80': 'symptomatic_rate_80',
    'isolation duration 80': 'isolation_duration_80',
    'new cases 70': 'new_cases_70',
    'total infected 80': 'total_infected_80',
    'self quarantine start 80': 'self_quarantine_start_80',
    'Isolated 70': 'isolated_70',
    'non controlled population 70': 'non_controlled_population_70',
    'social distancing start 70': 'social_distancing_start_70',
    'isolated recovery rate 80': 'isolated_recovery_rate_80',
    'isolated recovery rate 70': 'isolated_recovery_rate_70',
    'isolation effectiveness 80': 'isolation_effectiveness_80',
    'Susceptible 70': 'susceptible_70',
    'symptomatic duration 70': 'symptomatic_duration_70',
    'test fraction 80': 'test_fraction_80',
    'accumulated cases': 'accumulated_cases',
    'init total population': 'init_total_population',
    'incidence per 100000': 'incidence_per_100000',
    'new cases': 'new_cases',
    'init accumulated cases': 'init_accumulated_cases',
    'case fatality rate': 'case_fatality_rate',
    'isolation rate asymptomatic': 'isolation_rate_asymptomatic',
    'fraction of symptomatic': 'fraction_of_symptomatic',
    'total infected': 'total_infected',
    'infected symptomatic recovery rate': 'infected_symptomatic_recovery_rate',
    'infected asymptomatic recovery rate': 'infected_asymptomatic_recovery_rate',
    'available test kits': 'available_test_kits',
    'available test kits for testing asymptomatic': 'available_test_kits_for_testing_asymptomatic',
    'available test kits for testing symptomatic': 'available_test_kits_for_testing_symptomatic',
    'Critical Cases': 'critical_cases',
    'critical cases recovery rate': 'critical_cases_recovery_rate',
    'death rate': 'death_rate',
    'deimmunization rate': 'deimmunization_rate',
    'Diseased': 'diseased',
    'effect of kits availability on effectiveness of testing':
    'effect_of_kits_availability_on_effectiveness_of_testing',
    'Infected asymptomatic': 'infected_asymptomatic',
    'Infected symptomatic': 'infected_symptomatic',
    'infected critical case rate': 'infected_critical_case_rate',
    'infectivity per contact': 'infectivity_per_contact',
    'init available test kits': 'init_available_test_kits',
    'init Critical Cases': 'init_critical_cases',
    'init Diseased': 'init_diseased',
    'init Infected asymptomatic': 'init_infected_asymptomatic',
    'init Infected symptomatic': 'init_infected_symptomatic',
    'init Isolated': 'init_isolated',
    'init Recovered': 'init_recovered',
    'init Susceptible': 'init_susceptible',
    'Isolated': 'isolated',
    'isolated recovery rate': 'isolated_recovery_rate',
    'isolation rate symptomatic': 'isolation_rate_symptomatic',
    'kits availability for testing table': 'kits_availability_for_testing_table',
    'kits per person': 'kits_per_person',
    'kits population ratio': 'kits_population_ratio',
    'max kits population ratio': 'max_kits_population_ratio',
    'non controlled population': 'non_controlled_population',
    'produced test kits': 'produced_test_kits',
    'production phase1': 'production_phase1',
    'production phase2': 'production_phase2',
    'production phase3': 'production_phase3',
    'production start phase1': 'production_start_phase1',
    'production start phase2': 'production_start_phase2',
    'production start phase3': 'production_start_phase3',
    'production volume phase1': 'production_volume_phase1',
    'production volume phase2': 'production_volume_phase2',
    'production volume phase3': 'production_volume_phase3',
    'isolated critical case rate': 'isolated_critical_case_rate',
    'Recovered': 'recovered',
    'Susceptible': 'susceptible',
    'symptomatic rate': 'symptomatic_rate',
    'testing duration': 'testing_duration',
    'tests for symptomatic': 'tests_for_symptomatic',
    'used test kits': 'used_test_kits',
    'FINAL TIME': 'final_time',
    'INITIAL TIME': 'initial_time',
    'SAVEPER': 'saveper',
    'TIME STEP': 'time_step'
}

__pysd_version__ = "0.10.0"

__data = {'scope': None, 'time': lambda: 0}


def _init_outer_references(data):
    for key in data:
        __data[key] = data[key]


def time():
    return __data['time']()


@cache('step')
def infection_rate():
    """
    Real Name: b'infection rate'
    Original Eqn: b'total infection rate'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return total_infection_rate()


@cache('step')
def total_infection_rate():
    """
    Real Name: b'total infection rate'
    Original Eqn: b'total infection rate 80 +total infection rate 70 +total infection rate 60 +total infection rate 50 +total infection rate 40 +total infection rate 30 +total infection rate 20 +total infection rate 10 +total infection rate 00 +first infection 80 +first infection 70 +first infection 60 +first infection 50 +first infection 40 +first infection 30 +first infection 20 +first infection 10 +first infection 00'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return total_infection_rate_80() + total_infection_rate_70() + total_infection_rate_60(
    ) + total_infection_rate_50() + total_infection_rate_40() + total_infection_rate_30(
    ) + total_infection_rate_20() + total_infection_rate_10() + total_infection_rate_00(
    ) + first_infection_80() + first_infection_70() + first_infection_60() + first_infection_50(
    ) + first_infection_40() + first_infection_30() + first_infection_20() + first_infection_10(
    ) + first_infection_00()


@cache('step')
def diseased_40():
    """
    Real Name: b'Diseased 40'
    Original Eqn: b'INTEG ( death rate 40, init Diseased 40)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_diseased_40()


@cache('step')
def accumulated_cases_00():
    """
    Real Name: b'accumulated cases 00'
    Original Eqn: b'INTEG ( new cases 00, init accumulated cases 00)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_accumulated_cases_00()


@cache('step')
def accumulated_cases_10():
    """
    Real Name: b'accumulated cases 10'
    Original Eqn: b'INTEG ( new cases 10, init accumulated cases 10)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_accumulated_cases_10()


@cache('step')
def accumulated_cases_20():
    """
    Real Name: b'accumulated cases 20'
    Original Eqn: b'INTEG ( new cases 20, init accumulated cases 20)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_accumulated_cases_20()


@cache('step')
def accumulated_cases_30():
    """
    Real Name: b'accumulated cases 30'
    Original Eqn: b'INTEG ( new cases 30, init accumulated cases 30)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_accumulated_cases_30()


@cache('step')
def accumulated_cases_40():
    """
    Real Name: b'accumulated cases 40'
    Original Eqn: b'INTEG ( new cases 40, init accumulated cases 40)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_accumulated_cases_40()


@cache('run')
def duration_of_treatment_00():
    """
    Real Name: b'duration of treatment 00'
    Original Eqn: b'10'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 10


@cache('run')
def duration_of_treatment_10():
    """
    Real Name: b'duration of treatment 10'
    Original Eqn: b'10'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 10


@cache('run')
def duration_of_treatment_20():
    """
    Real Name: b'duration of treatment 20'
    Original Eqn: b'10'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 10


@cache('step')
def infection_rate_asymptomatic_80x00():
    """
    Real Name: b'infection rate asymptomatic 80x00'
    Original Eqn: b'Susceptible 00*Infected asymptomatic 00x80*contact infectivity asymptomatic 00x80*(social distancing policy SWITCH self 00 *social distancing policy 00+(1-social distancing policy SWITCH self 00))/non controlled pop 00x80'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_00() * infected_asymptomatic_00x80(
    ) * contact_infectivity_asymptomatic_00x80() * (
        social_distancing_policy_switch_self_00() * social_distancing_policy_00() +
        (1 - social_distancing_policy_switch_self_00())) / non_controlled_pop_00x80()


@cache('step')
def infection_rate_asymptomatic_80x10():
    """
    Real Name: b'infection rate asymptomatic 80x10'
    Original Eqn: b'Susceptible 10*Infected asymptomatic 10x80*contact infectivity asymptomatic 10x80*(social distancing policy SWITCH self 10 *social distancing policy 10+(1-social distancing policy SWITCH self 10))/non controlled pop 10x80'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_10() * infected_asymptomatic_10x80(
    ) * contact_infectivity_asymptomatic_10x80() * (
        social_distancing_policy_switch_self_10() * social_distancing_policy_10() +
        (1 - social_distancing_policy_switch_self_10())) / non_controlled_pop_10x80()


@cache('run')
def asymptomatic_duration_00():
    """
    Real Name: b'asymptomatic duration 00'
    Original Eqn: b'5'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 5


@cache('run')
def asymptomatic_duration_10():
    """
    Real Name: b'asymptomatic duration 10'
    Original Eqn: b'5'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 5


@cache('run')
def asymptomatic_duration_20():
    """
    Real Name: b'asymptomatic duration 20'
    Original Eqn: b'5'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 5


@cache('run')
def asymptomatic_duration_30():
    """
    Real Name: b'asymptomatic duration 30'
    Original Eqn: b'5'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 5


@cache('run')
def asymptomatic_duration_40():
    """
    Real Name: b'asymptomatic duration 40'
    Original Eqn: b'5'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 5


@cache('run')
def contacts_per_person_normal_20x50():
    """
    Real Name: b'contacts per person normal 20x50'
    Original Eqn: b'10'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 10


@cache('step')
def first_infection_00():
    """
    Real Name: b'first infection 00'
    Original Eqn: b'PULSE(infection start 00, 1)*normal first infected'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.pulse(__data['time'], infection_start_00(), 1) * normal_first_infected()


@cache('step')
def infection_rate_asymptomatic_self_00():
    """
    Real Name: b'infection rate asymptomatic self 00'
    Original Eqn: b'Infected asymptomatic 00*Susceptible 00*contact infectivity asymptomatic self 00*(social distancing policy SWITCH self 00\\\\ *social distancing policy 00+(1-social distancing policy SWITCH self 00))/non controlled population 00'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic_00() * susceptible_00(
    ) * contact_infectivity_asymptomatic_self_00() * (
        social_distancing_policy_switch_self_00() * social_distancing_policy_00() +
        (1 - social_distancing_policy_switch_self_00())) / non_controlled_population_00()


@cache('step')
def infection_rate_asymptomatic_self_10():
    """
    Real Name: b'infection rate asymptomatic self 10'
    Original Eqn: b'Infected asymptomatic 10*Susceptible 10*contact infectivity asymptomatic self 10*(social distancing policy SWITCH self 10\\\\ *social distancing policy 10+(1-social distancing policy SWITCH self 10))/non controlled population 10'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic_10() * susceptible_10(
    ) * contact_infectivity_asymptomatic_self_10() * (
        social_distancing_policy_switch_self_10() * social_distancing_policy_10() +
        (1 - social_distancing_policy_switch_self_10())) / non_controlled_population_10()


@cache('step')
def infection_rate_asymptomatic_self_20():
    """
    Real Name: b'infection rate asymptomatic self 20'
    Original Eqn: b'Infected asymptomatic 20*Susceptible 20*contact infectivity asymptomatic self 20*(social distancing policy SWITCH self 20\\\\ *social distancing policy 20+(1-social distancing policy SWITCH self 20))/non controlled population 20'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic_20() * susceptible_20(
    ) * contact_infectivity_asymptomatic_self_20() * (
        social_distancing_policy_switch_self_20() * social_distancing_policy_20() +
        (1 - social_distancing_policy_switch_self_20())) / non_controlled_population_20()


@cache('step')
def infection_rate_asymptomatic_self_30():
    """
    Real Name: b'infection rate asymptomatic self 30'
    Original Eqn: b'Infected asymptomatic 30*Susceptible 30*contact infectivity asymptomatic self 30*(social distancing policy SWITCH self 30\\\\ *social distancing policy 30+(1-social distancing policy SWITCH self 30))/non controlled population 30'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic_30() * susceptible_30(
    ) * contact_infectivity_asymptomatic_self_30() * (
        social_distancing_policy_switch_self_30() * social_distancing_policy_30() +
        (1 - social_distancing_policy_switch_self_30())) / non_controlled_population_30()


@cache('step')
def infection_rate_asymptomatic_self_40():
    """
    Real Name: b'infection rate asymptomatic self 40'
    Original Eqn: b'Infected asymptomatic 40*Susceptible 40*contact infectivity asymptomatic self 40*(social distancing policy SWITCH self 40\\\\ *social distancing policy 40+(1-social distancing policy SWITCH self 40))/non controlled population 40'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic_40() * susceptible_40(
    ) * contact_infectivity_asymptomatic_self_40() * (
        social_distancing_policy_switch_self_40() * social_distancing_policy_40() +
        (1 - social_distancing_policy_switch_self_40())) / non_controlled_population_40()


@cache('run')
def contacts_per_person_normal_30x70():
    """
    Real Name: b'contacts per person normal 30x70'
    Original Eqn: b'10'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 10


@cache('step')
def case_fatality_rate_00():
    """
    Real Name: b'case fatality rate 00'
    Original Eqn: b'ZIDZ( Diseased 00, accumulated cases 00)'
    Units: b'dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.zidz(diseased_00(), accumulated_cases_00())


@cache('step')
def case_fatality_rate_10():
    """
    Real Name: b'case fatality rate 10'
    Original Eqn: b'ZIDZ( Diseased 10, accumulated cases 10)'
    Units: b'dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.zidz(diseased_10(), accumulated_cases_10())


@cache('step')
def case_fatality_rate_20():
    """
    Real Name: b'case fatality rate 20'
    Original Eqn: b'ZIDZ( Diseased 20, accumulated cases 20)'
    Units: b'dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.zidz(diseased_20(), accumulated_cases_20())


@cache('step')
def case_fatality_rate_30():
    """
    Real Name: b'case fatality rate 30'
    Original Eqn: b'ZIDZ( Diseased 30, accumulated cases 30)'
    Units: b'dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.zidz(diseased_30(), accumulated_cases_30())


@cache('step')
def case_fatality_rate_40():
    """
    Real Name: b'case fatality rate 40'
    Original Eqn: b'ZIDZ( Diseased 40, accumulated cases 40)'
    Units: b'dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.zidz(diseased_40(), accumulated_cases_40())


@cache('step')
def infection_rate_quarantined_self_10():
    """
    Real Name: b'infection rate quarantined self 10'
    Original Eqn: b'Isolated 10*Susceptible 10*contact infectivity quarantine self 10/non controlled population 10'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return isolated_10() * susceptible_10() * contact_infectivity_quarantine_self_10(
    ) / non_controlled_population_10()


@cache('step')
def infection_rate_quarantined_self_20():
    """
    Real Name: b'infection rate quarantined self 20'
    Original Eqn: b'Isolated 20*Susceptible 20*contact infectivity quarantine self 20/non controlled population 20'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return isolated_20() * susceptible_20() * contact_infectivity_quarantine_self_20(
    ) / non_controlled_population_20()


@cache('step')
def infection_rate_quarantined_self_30():
    """
    Real Name: b'infection rate quarantined self 30'
    Original Eqn: b'Isolated 30*Susceptible 30*contact infectivity quarantine self 30/non controlled population 30'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return isolated_30() * susceptible_30() * contact_infectivity_quarantine_self_30(
    ) / non_controlled_population_30()


@cache('step')
def infection_rate_quarantined_self_40():
    """
    Real Name: b'infection rate quarantined self 40'
    Original Eqn: b'Isolated 40*Susceptible 40*contact infectivity quarantine self 40/non controlled population 40'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return isolated_40() * susceptible_40() * contact_infectivity_quarantine_self_40(
    ) / non_controlled_population_40()


@cache('step')
def contact_infectivity_asymptomatic_00x10():
    """
    Real Name: b'contact infectivity asymptomatic 00x10'
    Original Eqn: b'contacts per person normal 00x10*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_00x10() * infectivity_per_contact()


@cache('step')
def contact_infectivity_asymptomatic_00x20():
    """
    Real Name: b'contact infectivity asymptomatic 00x20'
    Original Eqn: b'contacts per person normal 00x20*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_00x20() * infectivity_per_contact()


@cache('step')
def contact_infectivity_asymptomatic_00x30():
    """
    Real Name: b'contact infectivity asymptomatic 00x30'
    Original Eqn: b'contacts per person normal 00x30*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_00x30() * infectivity_per_contact()


@cache('step')
def contact_infectivity_asymptomatic_00x40():
    """
    Real Name: b'contact infectivity asymptomatic 00x40'
    Original Eqn: b'contacts per person normal 00x40*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_00x40() * infectivity_per_contact()


@cache('step')
def contact_infectivity_asymptomatic_00x50():
    """
    Real Name: b'contact infectivity asymptomatic 00x50'
    Original Eqn: b'contacts per person normal 00x50*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_00x50() * infectivity_per_contact()


@cache('step')
def contact_infectivity_asymptomatic_00x60():
    """
    Real Name: b'contact infectivity asymptomatic 00x60'
    Original Eqn: b'contacts per person normal 00x60*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_00x60() * infectivity_per_contact()


@cache('step')
def contact_infectivity_asymptomatic_00x70():
    """
    Real Name: b'contact infectivity asymptomatic 00x70'
    Original Eqn: b'contacts per person normal 00x70*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_00x70() * infectivity_per_contact()


@cache('step')
def contact_infectivity_asymptomatic_00x80():
    """
    Real Name: b'contact infectivity asymptomatic 00x80'
    Original Eqn: b'contacts per person normal 00x80*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_00x80() * infectivity_per_contact()


@cache('step')
def contact_infectivity_asymptomatic_10x20():
    """
    Real Name: b'contact infectivity asymptomatic 10x20'
    Original Eqn: b'contacts per person normal 10x20*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_10x20() * infectivity_per_contact()


@cache('step')
def contact_infectivity_asymptomatic_10x30():
    """
    Real Name: b'contact infectivity asymptomatic 10x30'
    Original Eqn: b'contacts per person normal 10x30*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_10x30() * infectivity_per_contact()


@cache('step')
def contact_infectivity_asymptomatic_10x40():
    """
    Real Name: b'contact infectivity asymptomatic 10x40'
    Original Eqn: b'contacts per person normal 10x40*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_10x40() * infectivity_per_contact()


@cache('step')
def contact_infectivity_asymptomatic_10x50():
    """
    Real Name: b'contact infectivity asymptomatic 10x50'
    Original Eqn: b'contacts per person normal 10x50*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_10x50() * infectivity_per_contact()


@cache('step')
def contact_infectivity_asymptomatic_10x60():
    """
    Real Name: b'contact infectivity asymptomatic 10x60'
    Original Eqn: b'contacts per person normal 10x60*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_10x60() * infectivity_per_contact()


@cache('step')
def contact_infectivity_asymptomatic_10x70():
    """
    Real Name: b'contact infectivity asymptomatic 10x70'
    Original Eqn: b'contacts per person normal 10x70*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_10x70() * infectivity_per_contact()


@cache('step')
def contact_infectivity_asymptomatic_10x80():
    """
    Real Name: b'contact infectivity asymptomatic 10x80'
    Original Eqn: b'contacts per person normal 10x80*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_10x80() * infectivity_per_contact()


@cache('step')
def contact_infectivity_asymptomatic_20x30():
    """
    Real Name: b'contact infectivity asymptomatic 20x30'
    Original Eqn: b'contacts per person normal 20x30*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_20x30() * infectivity_per_contact()


@cache('step')
def contact_infectivity_asymptomatic_20x40():
    """
    Real Name: b'contact infectivity asymptomatic 20x40'
    Original Eqn: b'contacts per person normal 20x40*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_20x40() * infectivity_per_contact()


@cache('step')
def contact_infectivity_asymptomatic_20x50():
    """
    Real Name: b'contact infectivity asymptomatic 20x50'
    Original Eqn: b'contacts per person normal 20x50*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_20x50() * infectivity_per_contact()


@cache('step')
def contact_infectivity_asymptomatic_20x60():
    """
    Real Name: b'contact infectivity asymptomatic 20x60'
    Original Eqn: b'contacts per person normal 20x60*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_20x60() * infectivity_per_contact()


@cache('step')
def contact_infectivity_asymptomatic_20x70():
    """
    Real Name: b'contact infectivity asymptomatic 20x70'
    Original Eqn: b'contacts per person normal 20x70*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_20x70() * infectivity_per_contact()


@cache('step')
def contact_infectivity_asymptomatic_20x80():
    """
    Real Name: b'contact infectivity asymptomatic 20x80'
    Original Eqn: b'contacts per person normal 20x80*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_20x80() * infectivity_per_contact()


@cache('step')
def contact_infectivity_asymptomatic_30x40():
    """
    Real Name: b'contact infectivity asymptomatic 30x40'
    Original Eqn: b'contacts per person normal 30x40*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_30x40() * infectivity_per_contact()


@cache('step')
def contact_infectivity_asymptomatic_30x50():
    """
    Real Name: b'contact infectivity asymptomatic 30x50'
    Original Eqn: b'contacts per person normal 30x50*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_30x50() * infectivity_per_contact()


@cache('step')
def contact_infectivity_asymptomatic_30x60():
    """
    Real Name: b'contact infectivity asymptomatic 30x60'
    Original Eqn: b'contacts per person normal 30x60*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_30x60() * infectivity_per_contact()


@cache('step')
def contact_infectivity_asymptomatic_30x70():
    """
    Real Name: b'contact infectivity asymptomatic 30x70'
    Original Eqn: b'contacts per person normal 30x70*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_30x70() * infectivity_per_contact()


@cache('step')
def contact_infectivity_asymptomatic_30x80():
    """
    Real Name: b'contact infectivity asymptomatic 30x80'
    Original Eqn: b'contacts per person normal 30x80*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_30x80() * infectivity_per_contact()


@cache('step')
def contact_infectivity_asymptomatic_40x50():
    """
    Real Name: b'contact infectivity asymptomatic 40x50'
    Original Eqn: b'contacts per person normal 40x50*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_40x50() * infectivity_per_contact()


@cache('step')
def contact_infectivity_asymptomatic_40x60():
    """
    Real Name: b'contact infectivity asymptomatic 40x60'
    Original Eqn: b'contacts per person normal 40x60*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_40x60() * infectivity_per_contact()


@cache('step')
def contact_infectivity_asymptomatic_40x70():
    """
    Real Name: b'contact infectivity asymptomatic 40x70'
    Original Eqn: b'contacts per person normal 40x70*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_40x70() * infectivity_per_contact()


@cache('step')
def contact_infectivity_asymptomatic_40x80():
    """
    Real Name: b'contact infectivity asymptomatic 40x80'
    Original Eqn: b'contacts per person normal 40x80*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_40x80() * infectivity_per_contact()


@cache('step')
def infection_rate_symptomatic_30x20():
    """
    Real Name: b'infection rate symptomatic 30x20'
    Original Eqn: b'Susceptible 20*Infected symptomatic 20x30*contact infectivity symptomatic 20x30*(self quarantine policy SWITCH self 20\\\\ * self quarantine policy 20+(1-self quarantine policy SWITCH self 20))/non controlled pop 20x30'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_20() * infected_symptomatic_20x30() * contact_infectivity_symptomatic_20x30(
    ) * (self_quarantine_policy_switch_self_20() * self_quarantine_policy_20() +
         (1 - self_quarantine_policy_switch_self_20())) / non_controlled_pop_20x30()


@cache('step')
def infection_rate_symptomatic_30x40():
    """
    Real Name: b'infection rate symptomatic 30x40'
    Original Eqn: b'Susceptible 40*Infected symptomatic 30x40*contact infectivity symptomatic 30x40*(self quarantine policy SWITCH self 40\\\\ *self quarantine policy 40+(1-self quarantine policy SWITCH self 40))/non controlled pop 30x40'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_40() * infected_symptomatic_30x40() * contact_infectivity_symptomatic_30x40(
    ) * (self_quarantine_policy_switch_self_40() * self_quarantine_policy_40() +
         (1 - self_quarantine_policy_switch_self_40())) / non_controlled_pop_30x40()


@cache('step')
def infection_rate_symptomatic_30x50():
    """
    Real Name: b'infection rate symptomatic 30x50'
    Original Eqn: b'Susceptible 50*Infected symptomatic 30x50*contact infectivity symptomatic 30x50*(self quarantine policy SWITCH self 50\\\\ *self quarantine policy 50+(1-self quarantine policy SWITCH self 50))/non controlled pop 30x50'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_50() * infected_symptomatic_30x50() * contact_infectivity_symptomatic_30x50(
    ) * (self_quarantine_policy_switch_self_50() * self_quarantine_policy_50() +
         (1 - self_quarantine_policy_switch_self_50())) / non_controlled_pop_30x50()


@cache('step')
def infection_rate_symptomatic_30x60():
    """
    Real Name: b'infection rate symptomatic 30x60'
    Original Eqn: b'Susceptible 60*Infected symptomatic 30x60*contact infectivity symptomatic 30x60*(self quarantine policy SWITCH self 60\\\\ *self quarantine policy 60+(1-self quarantine policy SWITCH self 60))/non controlled pop 30x60'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_60() * infected_symptomatic_30x60() * contact_infectivity_symptomatic_30x60(
    ) * (self_quarantine_policy_switch_self_60() * self_quarantine_policy_60() +
         (1 - self_quarantine_policy_switch_self_60())) / non_controlled_pop_30x60()


@cache('step')
def infection_rate_symptomatic_30x70():
    """
    Real Name: b'infection rate symptomatic 30x70'
    Original Eqn: b'Susceptible 70*Infected symptomatic 30x70*contact infectivity symptomatic 30x70*(self quarantine policy SWITCH self 70\\\\ *self quarantine policy 70+(1-self quarantine policy SWITCH self 70))/non controlled pop 30x70'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_70() * infected_symptomatic_30x70() * contact_infectivity_symptomatic_30x70(
    ) * (self_quarantine_policy_switch_self_70() * self_quarantine_policy_70() +
         (1 - self_quarantine_policy_switch_self_70())) / non_controlled_pop_30x70()


@cache('step')
def infection_rate_symptomatic_30x80():
    """
    Real Name: b'infection rate symptomatic 30x80'
    Original Eqn: b'Susceptible 80*Infected symptomatic 30x80*contact infectivity symptomatic 30x80*(self quarantine policy SWITCH self 80\\\\ *self quarantine policy 80+(1-self quarantine policy SWITCH self 80))/non controlled pop 30x80'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_80() * infected_symptomatic_30x80() * contact_infectivity_symptomatic_30x80(
    ) * (self_quarantine_policy_switch_self_80() * self_quarantine_policy_80() +
         (1 - self_quarantine_policy_switch_self_80())) / non_controlled_pop_30x80()


@cache('step')
def infection_rate_symptomatic_40x00():
    """
    Real Name: b'infection rate symptomatic 40x00'
    Original Eqn: b'Susceptible 00*Infected symptomatic 00x40*contact infectivity symptomatic 00x40*(self quarantine policy SWITCH self 00\\\\ * self quarantine policy 00+(1-self quarantine policy SWITCH self 00))/non controlled pop 00x40'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_00() * infected_symptomatic_00x40() * contact_infectivity_symptomatic_00x40(
    ) * (self_quarantine_policy_switch_self_00() * self_quarantine_policy_00() +
         (1 - self_quarantine_policy_switch_self_00())) / non_controlled_pop_00x40()


@cache('step')
def contact_infectivity_asymptomatic_self_00():
    """
    Real Name: b'contact infectivity asymptomatic self 00'
    Original Eqn: b'contacts per person normal self 00*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_self_00() * infectivity_per_contact()


@cache('step')
def contact_infectivity_asymptomatic_self_10():
    """
    Real Name: b'contact infectivity asymptomatic self 10'
    Original Eqn: b'contacts per person normal self 10*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_self_10() * infectivity_per_contact()


@cache('step')
def contact_infectivity_asymptomatic_self_20():
    """
    Real Name: b'contact infectivity asymptomatic self 20'
    Original Eqn: b'contacts per person normal self 20*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_self_20() * infectivity_per_contact()


@cache('step')
def contact_infectivity_asymptomatic_self_30():
    """
    Real Name: b'contact infectivity asymptomatic self 30'
    Original Eqn: b'contacts per person normal self 30*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_self_30() * infectivity_per_contact()


@cache('step')
def contact_infectivity_asymptomatic_self_40():
    """
    Real Name: b'contact infectivity asymptomatic self 40'
    Original Eqn: b'contacts per person normal self 40*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_self_40() * infectivity_per_contact()


@cache('step')
def infection_rate_symptomatic_40x70():
    """
    Real Name: b'infection rate symptomatic 40x70'
    Original Eqn: b'Susceptible 70*Infected symptomatic 40x70*contact infectivity symptomatic 40x70*(self quarantine policy SWITCH self 70\\\\ *self quarantine policy 70+(1-self quarantine policy SWITCH self 70))/non controlled pop 40x70'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_70() * infected_symptomatic_40x70() * contact_infectivity_symptomatic_40x70(
    ) * (self_quarantine_policy_switch_self_70() * self_quarantine_policy_70() +
         (1 - self_quarantine_policy_switch_self_70())) / non_controlled_pop_40x70()


@cache('step')
def infection_rate_symptomatic_40x80():
    """
    Real Name: b'infection rate symptomatic 40x80'
    Original Eqn: b'Susceptible 80*Infected symptomatic 40x80*contact infectivity symptomatic 40x80*(self quarantine policy SWITCH self 80\\\\ *self quarantine policy 80+(1-self quarantine policy SWITCH self 80))/non controlled pop 40x80'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_80() * infected_symptomatic_40x80() * contact_infectivity_symptomatic_40x80(
    ) * (self_quarantine_policy_switch_self_80() * self_quarantine_policy_80() +
         (1 - self_quarantine_policy_switch_self_80())) / non_controlled_pop_40x80()


@cache('step')
def infection_rate_symptomatic_50x00():
    """
    Real Name: b'infection rate symptomatic 50x00'
    Original Eqn: b'Susceptible 00*Infected symptomatic 00x50*contact infectivity symptomatic 00x50*(self quarantine policy SWITCH self 00\\\\ * self quarantine policy 00+(1-self quarantine policy SWITCH self 00))/non controlled pop 00x50'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_00() * infected_symptomatic_00x50() * contact_infectivity_symptomatic_00x50(
    ) * (self_quarantine_policy_switch_self_00() * self_quarantine_policy_00() +
         (1 - self_quarantine_policy_switch_self_00())) / non_controlled_pop_00x50()


@cache('step')
def infection_rate_symptomatic_50x10():
    """
    Real Name: b'infection rate symptomatic 50x10'
    Original Eqn: b'Susceptible 10*Infected symptomatic 10x50*contact infectivity symptomatic 10x50*(self quarantine policy SWITCH self 10\\\\ * self quarantine policy 10+(1-self quarantine policy SWITCH self 10))/non controlled pop 10x50'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_10() * infected_symptomatic_10x50() * contact_infectivity_symptomatic_10x50(
    ) * (self_quarantine_policy_switch_self_10() * self_quarantine_policy_10() +
         (1 - self_quarantine_policy_switch_self_10())) / non_controlled_pop_10x50()


@cache('step')
def infection_rate_symptomatic_50x20():
    """
    Real Name: b'infection rate symptomatic 50x20'
    Original Eqn: b'Susceptible 20*Infected symptomatic 20x50*contact infectivity symptomatic 20x50*(self quarantine policy SWITCH self 20\\\\ * self quarantine policy 20+(1-self quarantine policy SWITCH self 20))/non controlled pop 20x50'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_20() * infected_symptomatic_20x50() * contact_infectivity_symptomatic_20x50(
    ) * (self_quarantine_policy_switch_self_20() * self_quarantine_policy_20() +
         (1 - self_quarantine_policy_switch_self_20())) / non_controlled_pop_20x50()


@cache('step')
def contact_infectivity_quarantine_self_00():
    """
    Real Name: b'contact infectivity quarantine self 00'
    Original Eqn: b'contact infectivity asymptomatic self 00*(1-isolation effectiveness 00)'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contact_infectivity_asymptomatic_self_00() * (1 - isolation_effectiveness_00())


@cache('step')
def contact_infectivity_quarantine_self_10():
    """
    Real Name: b'contact infectivity quarantine self 10'
    Original Eqn: b'contact infectivity asymptomatic self 10*(1-isolation effectiveness 10)'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contact_infectivity_asymptomatic_self_10() * (1 - isolation_effectiveness_10())


@cache('step')
def contact_infectivity_quarantine_self_20():
    """
    Real Name: b'contact infectivity quarantine self 20'
    Original Eqn: b'contact infectivity asymptomatic self 20*(1-isolation effectiveness 20)'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contact_infectivity_asymptomatic_self_20() * (1 - isolation_effectiveness_20())


@cache('step')
def contact_infectivity_quarantine_self_30():
    """
    Real Name: b'contact infectivity quarantine self 30'
    Original Eqn: b'contact infectivity asymptomatic self 30*(1-isolation effectiveness 30)'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contact_infectivity_asymptomatic_self_30() * (1 - isolation_effectiveness_30())


@cache('step')
def contact_infectivity_quarantine_self_40():
    """
    Real Name: b'contact infectivity quarantine self 40'
    Original Eqn: b'contact infectivity asymptomatic self 40*(1-isolation effectiveness 40)'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contact_infectivity_asymptomatic_self_40() * (1 - isolation_effectiveness_40())


@cache('step')
def infection_rate_symptomatic_60x00():
    """
    Real Name: b'infection rate symptomatic 60x00'
    Original Eqn: b'Susceptible 00*Infected symptomatic 00x60*contact infectivity symptomatic 00x60*(self quarantine policy SWITCH self 00\\\\ * self quarantine policy 00+(1-self quarantine policy SWITCH self 00))/non controlled pop 00x60'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_00() * infected_symptomatic_00x60() * contact_infectivity_symptomatic_00x60(
    ) * (self_quarantine_policy_switch_self_00() * self_quarantine_policy_00() +
         (1 - self_quarantine_policy_switch_self_00())) / non_controlled_pop_00x60()


@cache('step')
def infection_rate_symptomatic_60x10():
    """
    Real Name: b'infection rate symptomatic 60x10'
    Original Eqn: b'Susceptible 10*Infected symptomatic 10x60*contact infectivity symptomatic 10x60*(self quarantine policy SWITCH self 10\\\\ * self quarantine policy 10+(1-self quarantine policy SWITCH self 10))/non controlled pop 10x60'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_10() * infected_symptomatic_10x60() * contact_infectivity_symptomatic_10x60(
    ) * (self_quarantine_policy_switch_self_10() * self_quarantine_policy_10() +
         (1 - self_quarantine_policy_switch_self_10())) / non_controlled_pop_10x60()


@cache('step')
def infection_rate_symptomatic_60x20():
    """
    Real Name: b'infection rate symptomatic 60x20'
    Original Eqn: b'Susceptible 20*Infected symptomatic 20x60*contact infectivity symptomatic 20x60*(self quarantine policy SWITCH self 20\\\\ * self quarantine policy 20+(1-self quarantine policy SWITCH self 20))/non controlled pop 20x60'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_20() * infected_symptomatic_20x60() * contact_infectivity_symptomatic_20x60(
    ) * (self_quarantine_policy_switch_self_20() * self_quarantine_policy_20() +
         (1 - self_quarantine_policy_switch_self_20())) / non_controlled_pop_20x60()


@cache('step')
def infection_rate_symptomatic_60x30():
    """
    Real Name: b'infection rate symptomatic 60x30'
    Original Eqn: b'Susceptible 30*Infected symptomatic 30x60*contact infectivity symptomatic 30x60*(self quarantine policy SWITCH self 30\\\\ * self quarantine policy 30+(1-self quarantine policy SWITCH self 30))/non controlled pop 30x60'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_30() * infected_symptomatic_30x60() * contact_infectivity_symptomatic_30x60(
    ) * (self_quarantine_policy_switch_self_30() * self_quarantine_policy_30() +
         (1 - self_quarantine_policy_switch_self_30())) / non_controlled_pop_30x60()


@cache('step')
def contact_infectivity_symptomatic_00x10():
    """
    Real Name: b'contact infectivity symptomatic 00x10'
    Original Eqn: b'contacts per person symptomatic 00x10*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_symptomatic_00x10() * infectivity_per_contact()


@cache('step')
def contact_infectivity_symptomatic_00x20():
    """
    Real Name: b'contact infectivity symptomatic 00x20'
    Original Eqn: b'contacts per person symptomatic 00x20*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_symptomatic_00x20() * infectivity_per_contact()


@cache('step')
def contact_infectivity_symptomatic_00x30():
    """
    Real Name: b'contact infectivity symptomatic 00x30'
    Original Eqn: b'contacts per person symptomatic 00x30*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_symptomatic_00x30() * infectivity_per_contact()


@cache('step')
def contact_infectivity_symptomatic_00x40():
    """
    Real Name: b'contact infectivity symptomatic 00x40'
    Original Eqn: b'contacts per person symptomatic 00x40*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_symptomatic_00x40() * infectivity_per_contact()


@cache('step')
def contact_infectivity_symptomatic_00x50():
    """
    Real Name: b'contact infectivity symptomatic 00x50'
    Original Eqn: b'contacts per person symptomatic 00x50*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_symptomatic_00x50() * infectivity_per_contact()


@cache('step')
def contact_infectivity_symptomatic_00x60():
    """
    Real Name: b'contact infectivity symptomatic 00x60'
    Original Eqn: b'contacts per person symptomatic 00x60*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_symptomatic_00x60() * infectivity_per_contact()


@cache('step')
def contact_infectivity_symptomatic_00x70():
    """
    Real Name: b'contact infectivity symptomatic 00x70'
    Original Eqn: b'contacts per person symptomatic 00x70*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_symptomatic_00x70() * infectivity_per_contact()


@cache('step')
def contact_infectivity_symptomatic_00x80():
    """
    Real Name: b'contact infectivity symptomatic 00x80'
    Original Eqn: b'contacts per person symptomatic 00x80*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_symptomatic_00x80() * infectivity_per_contact()


@cache('step')
def contact_infectivity_symptomatic_10x20():
    """
    Real Name: b'contact infectivity symptomatic 10x20'
    Original Eqn: b'contacts per person symptomatic 10x20*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_symptomatic_10x20() * infectivity_per_contact()


@cache('step')
def contact_infectivity_symptomatic_10x30():
    """
    Real Name: b'contact infectivity symptomatic 10x30'
    Original Eqn: b'contacts per person symptomatic 10x30*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_symptomatic_10x30() * infectivity_per_contact()


@cache('step')
def contact_infectivity_symptomatic_10x40():
    """
    Real Name: b'contact infectivity symptomatic 10x40'
    Original Eqn: b'contacts per person symptomatic 10x40*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_symptomatic_10x40() * infectivity_per_contact()


@cache('step')
def contact_infectivity_symptomatic_10x50():
    """
    Real Name: b'contact infectivity symptomatic 10x50'
    Original Eqn: b'contacts per person symptomatic 10x50*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_symptomatic_10x50() * infectivity_per_contact()


@cache('step')
def contact_infectivity_symptomatic_10x60():
    """
    Real Name: b'contact infectivity symptomatic 10x60'
    Original Eqn: b'contacts per person symptomatic 10x60*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_symptomatic_10x60() * infectivity_per_contact()


@cache('step')
def contact_infectivity_symptomatic_10x70():
    """
    Real Name: b'contact infectivity symptomatic 10x70'
    Original Eqn: b'contacts per person symptomatic 10x70*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_symptomatic_10x70() * infectivity_per_contact()


@cache('step')
def contact_infectivity_symptomatic_10x80():
    """
    Real Name: b'contact infectivity symptomatic 10x80'
    Original Eqn: b'contacts per person symptomatic 10x80*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_symptomatic_10x80() * infectivity_per_contact()


@cache('step')
def contact_infectivity_symptomatic_20x30():
    """
    Real Name: b'contact infectivity symptomatic 20x30'
    Original Eqn: b'contacts per person symptomatic 20x30*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_symptomatic_20x30() * infectivity_per_contact()


@cache('step')
def contact_infectivity_symptomatic_20x40():
    """
    Real Name: b'contact infectivity symptomatic 20x40'
    Original Eqn: b'contacts per person symptomatic 20x40*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_symptomatic_20x40() * infectivity_per_contact()


@cache('step')
def contact_infectivity_symptomatic_20x50():
    """
    Real Name: b'contact infectivity symptomatic 20x50'
    Original Eqn: b'contacts per person symptomatic 20x50*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_symptomatic_20x50() * infectivity_per_contact()


@cache('step')
def contact_infectivity_symptomatic_20x60():
    """
    Real Name: b'contact infectivity symptomatic 20x60'
    Original Eqn: b'contacts per person symptomatic 20x60*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_symptomatic_20x60() * infectivity_per_contact()


@cache('step')
def contact_infectivity_symptomatic_20x70():
    """
    Real Name: b'contact infectivity symptomatic 20x70'
    Original Eqn: b'contacts per person symptomatic 20x70*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_symptomatic_20x70() * infectivity_per_contact()


@cache('step')
def contact_infectivity_symptomatic_20x80():
    """
    Real Name: b'contact infectivity symptomatic 20x80'
    Original Eqn: b'contacts per person symptomatic 20x80*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_symptomatic_20x80() * infectivity_per_contact()


@cache('step')
def contact_infectivity_symptomatic_30x40():
    """
    Real Name: b'contact infectivity symptomatic 30x40'
    Original Eqn: b'contacts per person symptomatic 30x40*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_symptomatic_30x40() * infectivity_per_contact()


@cache('step')
def contact_infectivity_symptomatic_30x50():
    """
    Real Name: b'contact infectivity symptomatic 30x50'
    Original Eqn: b'contacts per person symptomatic 30x50*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_symptomatic_30x50() * infectivity_per_contact()


@cache('step')
def contact_infectivity_symptomatic_30x60():
    """
    Real Name: b'contact infectivity symptomatic 30x60'
    Original Eqn: b'contacts per person symptomatic 30x60*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_symptomatic_30x60() * infectivity_per_contact()


@cache('step')
def contact_infectivity_symptomatic_30x70():
    """
    Real Name: b'contact infectivity symptomatic 30x70'
    Original Eqn: b'contacts per person symptomatic 30x70*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_symptomatic_30x70() * infectivity_per_contact()


@cache('step')
def contact_infectivity_symptomatic_30x80():
    """
    Real Name: b'contact infectivity symptomatic 30x80'
    Original Eqn: b'contacts per person symptomatic 30x80*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_symptomatic_30x80() * infectivity_per_contact()


@cache('step')
def contact_infectivity_symptomatic_40x50():
    """
    Real Name: b'contact infectivity symptomatic 40x50'
    Original Eqn: b'contacts per person symptomatic 40x50*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_symptomatic_40x50() * infectivity_per_contact()


@cache('step')
def contact_infectivity_symptomatic_40x60():
    """
    Real Name: b'contact infectivity symptomatic 40x60'
    Original Eqn: b'contacts per person symptomatic 40x60*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_symptomatic_40x60() * infectivity_per_contact()


@cache('step')
def contact_infectivity_symptomatic_40x70():
    """
    Real Name: b'contact infectivity symptomatic 40x70'
    Original Eqn: b'contacts per person symptomatic 40x70*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_symptomatic_40x70() * infectivity_per_contact()


@cache('step')
def contact_infectivity_symptomatic_40x80():
    """
    Real Name: b'contact infectivity symptomatic 40x80'
    Original Eqn: b'contacts per person symptomatic 40x80*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_symptomatic_40x80() * infectivity_per_contact()


@cache('step')
def infected_asymptomatic_40x60():
    """
    Real Name: b'Infected asymptomatic 40x60'
    Original Eqn: b'Infected asymptomatic 40+Infected asymptomatic 60'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic_40() + infected_asymptomatic_60()


@cache('run')
def infection_start_00():
    """
    Real Name: b'infection start 00'
    Original Eqn: b'-1'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return -1


@cache('run')
def infection_start_10():
    """
    Real Name: b'infection start 10'
    Original Eqn: b'-1'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return -1


@cache('run')
def infection_start_20():
    """
    Real Name: b'infection start 20'
    Original Eqn: b'-1'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return -1


@cache('run')
def infection_start_30():
    """
    Real Name: b'infection start 30'
    Original Eqn: b'-1'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return -1


@cache('run')
def infection_start_40():
    """
    Real Name: b'infection start 40'
    Original Eqn: b'-1'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return -1


@cache('step')
def self_quarantine_policy_40():
    """
    Real Name: b'self quarantine policy 40'
    Original Eqn: b'1-PULSE(self quarantine start 40, self quarantine end 40-self quarantine start 40)*self quarantine effectiveness 40'
    Units: b'dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return 1 - functions.pulse(__data['time'], self_quarantine_start_40(),
                               self_quarantine_end_40() -
                               self_quarantine_start_40()) * self_quarantine_effectiveness_40()


@cache('step')
def contact_infectivity_symptomatic_self_00():
    """
    Real Name: b'contact infectivity symptomatic self 00'
    Original Eqn: b'contacts per person symptomatic self 00*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_symptomatic_self_00() * infectivity_per_contact()


@cache('step')
def contact_infectivity_symptomatic_self_10():
    """
    Real Name: b'contact infectivity symptomatic self 10'
    Original Eqn: b'contacts per person symptomatic self 10*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_symptomatic_self_10() * infectivity_per_contact()


@cache('step')
def contact_infectivity_symptomatic_self_20():
    """
    Real Name: b'contact infectivity symptomatic self 20'
    Original Eqn: b'contacts per person symptomatic self 20*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_symptomatic_self_20() * infectivity_per_contact()


@cache('step')
def contact_infectivity_symptomatic_self_30():
    """
    Real Name: b'contact infectivity symptomatic self 30'
    Original Eqn: b'contacts per person symptomatic self 30*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_symptomatic_self_30() * infectivity_per_contact()


@cache('step')
def contact_infectivity_symptomatic_self_40():
    """
    Real Name: b'contact infectivity symptomatic self 40'
    Original Eqn: b'contacts per person symptomatic self 40*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_symptomatic_self_40() * infectivity_per_contact()


@cache('run')
def init_accumulated_cases_00():
    """
    Real Name: b'init accumulated cases 00'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('run')
def init_accumulated_cases_10():
    """
    Real Name: b'init accumulated cases 10'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('run')
def init_accumulated_cases_20():
    """
    Real Name: b'init accumulated cases 20'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('run')
def init_accumulated_cases_30():
    """
    Real Name: b'init accumulated cases 30'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('run')
def contacts_per_person_normal_00x10():
    """
    Real Name: b'contacts per person normal 00x10'
    Original Eqn: b'10'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 10


@cache('run')
def contacts_per_person_normal_00x20():
    """
    Real Name: b'contacts per person normal 00x20'
    Original Eqn: b'10'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 10


@cache('run')
def contacts_per_person_normal_00x30():
    """
    Real Name: b'contacts per person normal 00x30'
    Original Eqn: b'10'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 10


@cache('run')
def contacts_per_person_normal_00x40():
    """
    Real Name: b'contacts per person normal 00x40'
    Original Eqn: b'10'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 10


@cache('run')
def contacts_per_person_normal_00x50():
    """
    Real Name: b'contacts per person normal 00x50'
    Original Eqn: b'10'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 10


@cache('run')
def contacts_per_person_normal_00x60():
    """
    Real Name: b'contacts per person normal 00x60'
    Original Eqn: b'10'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 10


@cache('run')
def contacts_per_person_normal_00x70():
    """
    Real Name: b'contacts per person normal 00x70'
    Original Eqn: b'10'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 10


@cache('run')
def contacts_per_person_normal_00x80():
    """
    Real Name: b'contacts per person normal 00x80'
    Original Eqn: b'10'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 10


@cache('run')
def contacts_per_person_normal_10x20():
    """
    Real Name: b'contacts per person normal 10x20'
    Original Eqn: b'10'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 10


@cache('run')
def contacts_per_person_normal_10x30():
    """
    Real Name: b'contacts per person normal 10x30'
    Original Eqn: b'10'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 10


@cache('run')
def contacts_per_person_normal_10x40():
    """
    Real Name: b'contacts per person normal 10x40'
    Original Eqn: b'10'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 10


@cache('run')
def contacts_per_person_normal_10x50():
    """
    Real Name: b'contacts per person normal 10x50'
    Original Eqn: b'10'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 10


@cache('run')
def contacts_per_person_normal_10x60():
    """
    Real Name: b'contacts per person normal 10x60'
    Original Eqn: b'10'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 10


@cache('run')
def contacts_per_person_normal_10x70():
    """
    Real Name: b'contacts per person normal 10x70'
    Original Eqn: b'10'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 10


@cache('run')
def contacts_per_person_normal_10x80():
    """
    Real Name: b'contacts per person normal 10x80'
    Original Eqn: b'10'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 10


@cache('run')
def contacts_per_person_normal_20x30():
    """
    Real Name: b'contacts per person normal 20x30'
    Original Eqn: b'10'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 10


@cache('run')
def contacts_per_person_normal_20x40():
    """
    Real Name: b'contacts per person normal 20x40'
    Original Eqn: b'10'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 10


@cache('run')
def social_distancing_effectiveness_10():
    """
    Real Name: b'social distancing effectiveness 10'
    Original Eqn: b'0.6'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.6


@cache('run')
def contacts_per_person_normal_20x60():
    """
    Real Name: b'contacts per person normal 20x60'
    Original Eqn: b'10'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 10


@cache('run')
def contacts_per_person_normal_20x70():
    """
    Real Name: b'contacts per person normal 20x70'
    Original Eqn: b'10'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 10


@cache('run')
def contacts_per_person_normal_20x80():
    """
    Real Name: b'contacts per person normal 20x80'
    Original Eqn: b'10'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 10


@cache('run')
def contacts_per_person_normal_30x40():
    """
    Real Name: b'contacts per person normal 30x40'
    Original Eqn: b'10'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 10


@cache('run')
def contacts_per_person_normal_30x50():
    """
    Real Name: b'contacts per person normal 30x50'
    Original Eqn: b'10'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 10


@cache('run')
def contacts_per_person_normal_30x60():
    """
    Real Name: b'contacts per person normal 30x60'
    Original Eqn: b'10'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 10


@cache('step')
def infected_symptomatic_00x60():
    """
    Real Name: b'Infected symptomatic 00x60'
    Original Eqn: b'Infected symptomatic 00+Infected symptomatic 60'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_00() + infected_symptomatic_60()


@cache('run')
def contacts_per_person_normal_30x80():
    """
    Real Name: b'contacts per person normal 30x80'
    Original Eqn: b'10'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 10


@cache('run')
def contacts_per_person_normal_40x50():
    """
    Real Name: b'contacts per person normal 40x50'
    Original Eqn: b'10'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 10


@cache('run')
def contacts_per_person_normal_40x60():
    """
    Real Name: b'contacts per person normal 40x60'
    Original Eqn: b'10'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 10


@cache('run')
def contacts_per_person_normal_40x70():
    """
    Real Name: b'contacts per person normal 40x70'
    Original Eqn: b'10'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 10


@cache('run')
def contacts_per_person_normal_40x80():
    """
    Real Name: b'contacts per person normal 40x80'
    Original Eqn: b'10'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 10


@cache('run')
def init_infected_asymptomatic_30():
    """
    Real Name: b'init Infected asymptomatic 30'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('run')
def init_infected_asymptomatic_40():
    """
    Real Name: b'init Infected asymptomatic 40'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('step')
def infected_symptomatic_10x60():
    """
    Real Name: b'Infected symptomatic 10x60'
    Original Eqn: b'Infected symptomatic 10+Infected symptomatic 60'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_10() + infected_symptomatic_60()


@cache('step')
def infected_symptomatic_10x70():
    """
    Real Name: b'Infected symptomatic 10x70'
    Original Eqn: b'Infected symptomatic 10+Infected symptomatic 70'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_10() + infected_symptomatic_70()


@cache('step')
def infected_symptomatic_10x80():
    """
    Real Name: b'Infected symptomatic 10x80'
    Original Eqn: b'Infected symptomatic 10+Infected symptomatic 80'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_10() + infected_symptomatic_80()


@cache('step')
def infected_symptomatic_20():
    """
    Real Name: b'Infected symptomatic 20'
    Original Eqn: b'INTEG ( symptomatic rate 20-infected critical case rate 20-infected symptomatic recovery rate 20\\\\ -isolation rate symptomatic 20, init Infected symptomatic 20)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_infected_symptomatic_20()


@cache('step')
def infected_symptomatic_20x30():
    """
    Real Name: b'Infected symptomatic 20x30'
    Original Eqn: b'Infected symptomatic 20+Infected symptomatic 30'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_20() + infected_symptomatic_30()


@cache('run')
def contacts_per_person_normal_self_00():
    """
    Real Name: b'contacts per person normal self 00'
    Original Eqn: b'30'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 30


@cache('run')
def contacts_per_person_normal_self_10():
    """
    Real Name: b'contacts per person normal self 10'
    Original Eqn: b'30'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 30


@cache('run')
def contacts_per_person_normal_self_20():
    """
    Real Name: b'contacts per person normal self 20'
    Original Eqn: b'30'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 30


@cache('run')
def contacts_per_person_normal_self_30():
    """
    Real Name: b'contacts per person normal self 30'
    Original Eqn: b'30'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 30


@cache('run')
def contacts_per_person_normal_self_40():
    """
    Real Name: b'contacts per person normal self 40'
    Original Eqn: b'30'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 30


@cache('step')
def infected_symptomatic_30():
    """
    Real Name: b'Infected symptomatic 30'
    Original Eqn: b'INTEG ( symptomatic rate 30-infected critical case rate 30-infected symptomatic recovery rate 30\\\\ -isolation rate symptomatic 30, init Infected symptomatic 30)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_infected_symptomatic_30()


@cache('step')
def infected_symptomatic_30x40():
    """
    Real Name: b'Infected symptomatic 30x40'
    Original Eqn: b'Infected symptomatic 30+Infected symptomatic 40'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_30() + infected_symptomatic_40()


@cache('step')
def infected_symptomatic_30x50():
    """
    Real Name: b'Infected symptomatic 30x50'
    Original Eqn: b'Infected symptomatic 30+Infected symptomatic 50'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_30() + infected_symptomatic_50()


@cache('step')
def infected_symptomatic_30x60():
    """
    Real Name: b'Infected symptomatic 30x60'
    Original Eqn: b'Infected symptomatic 30+Infected symptomatic 60'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_30() + infected_symptomatic_60()


@cache('step')
def contacts_per_person_symptomatic_00x10():
    """
    Real Name: b'contacts per person symptomatic 00x10'
    Original Eqn: b'contacts per person normal 00x10*(symptomatic contact fraction 10+symptomatic contact fraction 00\\\\ )/2'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_00x10() * (symptomatic_contact_fraction_10() +
                                                 symptomatic_contact_fraction_00()) / 2


@cache('step')
def contacts_per_person_symptomatic_00x20():
    """
    Real Name: b'contacts per person symptomatic 00x20'
    Original Eqn: b'contacts per person normal 00x20*(symptomatic contact fraction 20+symptomatic contact fraction 00\\\\ )/2'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_00x20() * (symptomatic_contact_fraction_20() +
                                                 symptomatic_contact_fraction_00()) / 2


@cache('step')
def contacts_per_person_symptomatic_00x30():
    """
    Real Name: b'contacts per person symptomatic 00x30'
    Original Eqn: b'contacts per person normal 00x30*(symptomatic contact fraction 30+symptomatic contact fraction 00\\\\ )/2'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_00x30() * (symptomatic_contact_fraction_30() +
                                                 symptomatic_contact_fraction_00()) / 2


@cache('step')
def contacts_per_person_symptomatic_00x40():
    """
    Real Name: b'contacts per person symptomatic 00x40'
    Original Eqn: b'contacts per person normal 00x40*(symptomatic contact fraction 40+symptomatic contact fraction 00\\\\ )/2'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_00x40() * (symptomatic_contact_fraction_40() +
                                                 symptomatic_contact_fraction_00()) / 2


@cache('step')
def contacts_per_person_symptomatic_00x50():
    """
    Real Name: b'contacts per person symptomatic 00x50'
    Original Eqn: b'contacts per person normal 00x50*(symptomatic contact fraction 50+symptomatic contact fraction 00\\\\ )/2'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_00x50() * (symptomatic_contact_fraction_50() +
                                                 symptomatic_contact_fraction_00()) / 2


@cache('step')
def contacts_per_person_symptomatic_00x60():
    """
    Real Name: b'contacts per person symptomatic 00x60'
    Original Eqn: b'contacts per person normal 00x60*(symptomatic contact fraction 60+symptomatic contact fraction 00\\\\ )/2'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_00x60() * (symptomatic_contact_fraction_60() +
                                                 symptomatic_contact_fraction_00()) / 2


@cache('step')
def contacts_per_person_symptomatic_00x70():
    """
    Real Name: b'contacts per person symptomatic 00x70'
    Original Eqn: b'contacts per person normal 00x70*(symptomatic contact fraction 70+symptomatic contact fraction 00\\\\ )/2'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_00x70() * (symptomatic_contact_fraction_70() +
                                                 symptomatic_contact_fraction_00()) / 2


@cache('step')
def contacts_per_person_symptomatic_00x80():
    """
    Real Name: b'contacts per person symptomatic 00x80'
    Original Eqn: b'contacts per person normal 00x80*(symptomatic contact fraction 80+symptomatic contact fraction 00\\\\ )/2'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_00x80() * (symptomatic_contact_fraction_80() +
                                                 symptomatic_contact_fraction_00()) / 2


@cache('step')
def contacts_per_person_symptomatic_10x20():
    """
    Real Name: b'contacts per person symptomatic 10x20'
    Original Eqn: b'contacts per person normal 10x20*(symptomatic contact fraction 20+symptomatic contact fraction 10\\\\ )/2'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_10x20() * (symptomatic_contact_fraction_20() +
                                                 symptomatic_contact_fraction_10()) / 2


@cache('step')
def contacts_per_person_symptomatic_10x30():
    """
    Real Name: b'contacts per person symptomatic 10x30'
    Original Eqn: b'contacts per person normal 10x30*(symptomatic contact fraction 30+symptomatic contact fraction 10\\\\ )/2'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_10x30() * (symptomatic_contact_fraction_30() +
                                                 symptomatic_contact_fraction_10()) / 2


@cache('step')
def contacts_per_person_symptomatic_10x40():
    """
    Real Name: b'contacts per person symptomatic 10x40'
    Original Eqn: b'contacts per person normal 10x40*(symptomatic contact fraction 40+symptomatic contact fraction 10\\\\ )/2'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_10x40() * (symptomatic_contact_fraction_40() +
                                                 symptomatic_contact_fraction_10()) / 2


@cache('step')
def contacts_per_person_symptomatic_10x50():
    """
    Real Name: b'contacts per person symptomatic 10x50'
    Original Eqn: b'contacts per person normal 10x50*(symptomatic contact fraction 50+symptomatic contact fraction 10\\\\ )/2'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_10x50() * (symptomatic_contact_fraction_50() +
                                                 symptomatic_contact_fraction_10()) / 2


@cache('step')
def contacts_per_person_symptomatic_10x60():
    """
    Real Name: b'contacts per person symptomatic 10x60'
    Original Eqn: b'contacts per person normal 10x60*(symptomatic contact fraction 60+symptomatic contact fraction 10\\\\ )/2'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_10x60() * (symptomatic_contact_fraction_60() +
                                                 symptomatic_contact_fraction_10()) / 2


@cache('step')
def contacts_per_person_symptomatic_10x70():
    """
    Real Name: b'contacts per person symptomatic 10x70'
    Original Eqn: b'contacts per person normal 10x70*(symptomatic contact fraction 70+symptomatic contact fraction 10\\\\ )/2'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_10x70() * (symptomatic_contact_fraction_70() +
                                                 symptomatic_contact_fraction_10()) / 2


@cache('step')
def contacts_per_person_symptomatic_10x80():
    """
    Real Name: b'contacts per person symptomatic 10x80'
    Original Eqn: b'contacts per person normal 10x80*(symptomatic contact fraction 80+symptomatic contact fraction 10\\\\ )/2'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_10x80() * (symptomatic_contact_fraction_80() +
                                                 symptomatic_contact_fraction_10()) / 2


@cache('step')
def contacts_per_person_symptomatic_20x30():
    """
    Real Name: b'contacts per person symptomatic 20x30'
    Original Eqn: b'contacts per person normal 20x30*(symptomatic contact fraction 30+symptomatic contact fraction 20\\\\ )/2'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_20x30() * (symptomatic_contact_fraction_30() +
                                                 symptomatic_contact_fraction_20()) / 2


@cache('step')
def contacts_per_person_symptomatic_20x40():
    """
    Real Name: b'contacts per person symptomatic 20x40'
    Original Eqn: b'contacts per person normal 20x40*(symptomatic contact fraction 40+symptomatic contact fraction 20\\\\ )/2'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_20x40() * (symptomatic_contact_fraction_40() +
                                                 symptomatic_contact_fraction_20()) / 2


@cache('step')
def contacts_per_person_symptomatic_20x50():
    """
    Real Name: b'contacts per person symptomatic 20x50'
    Original Eqn: b'contacts per person normal 20x50*(symptomatic contact fraction 50+symptomatic contact fraction 20\\\\ )/2'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_20x50() * (symptomatic_contact_fraction_50() +
                                                 symptomatic_contact_fraction_20()) / 2


@cache('step')
def contacts_per_person_symptomatic_20x60():
    """
    Real Name: b'contacts per person symptomatic 20x60'
    Original Eqn: b'contacts per person normal 20x60*(symptomatic contact fraction 60+symptomatic contact fraction 20\\\\ )/2'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_20x60() * (symptomatic_contact_fraction_60() +
                                                 symptomatic_contact_fraction_20()) / 2


@cache('step')
def contacts_per_person_symptomatic_20x70():
    """
    Real Name: b'contacts per person symptomatic 20x70'
    Original Eqn: b'contacts per person normal 20x70*(symptomatic contact fraction 70+symptomatic contact fraction 20\\\\ )/2'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_20x70() * (symptomatic_contact_fraction_70() +
                                                 symptomatic_contact_fraction_20()) / 2


@cache('step')
def contacts_per_person_symptomatic_20x80():
    """
    Real Name: b'contacts per person symptomatic 20x80'
    Original Eqn: b'contacts per person normal 20x80*(symptomatic contact fraction 80+symptomatic contact fraction 20\\\\ )/2'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_20x80() * (symptomatic_contact_fraction_80() +
                                                 symptomatic_contact_fraction_20()) / 2


@cache('step')
def contacts_per_person_symptomatic_30x40():
    """
    Real Name: b'contacts per person symptomatic 30x40'
    Original Eqn: b'contacts per person normal 30x40*(symptomatic contact fraction 40+symptomatic contact fraction 30\\\\ )/2'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_30x40() * (symptomatic_contact_fraction_40() +
                                                 symptomatic_contact_fraction_30()) / 2


@cache('step')
def contacts_per_person_symptomatic_30x50():
    """
    Real Name: b'contacts per person symptomatic 30x50'
    Original Eqn: b'contacts per person normal 30x50*(symptomatic contact fraction 50+symptomatic contact fraction 30\\\\ )/2'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_30x50() * (symptomatic_contact_fraction_50() +
                                                 symptomatic_contact_fraction_30()) / 2


@cache('step')
def contacts_per_person_symptomatic_30x60():
    """
    Real Name: b'contacts per person symptomatic 30x60'
    Original Eqn: b'contacts per person normal 30x60*(symptomatic contact fraction 60+symptomatic contact fraction 30\\\\ )/2'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_30x60() * (symptomatic_contact_fraction_60() +
                                                 symptomatic_contact_fraction_30()) / 2


@cache('step')
def contacts_per_person_symptomatic_30x70():
    """
    Real Name: b'contacts per person symptomatic 30x70'
    Original Eqn: b'contacts per person normal 30x70*(symptomatic contact fraction 70+symptomatic contact fraction 30\\\\ )/2'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_30x70() * (symptomatic_contact_fraction_70() +
                                                 symptomatic_contact_fraction_30()) / 2


@cache('step')
def contacts_per_person_symptomatic_30x80():
    """
    Real Name: b'contacts per person symptomatic 30x80'
    Original Eqn: b'contacts per person normal 30x80*(symptomatic contact fraction 80+symptomatic contact fraction 30\\\\ )/2'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_30x80() * (symptomatic_contact_fraction_80() +
                                                 symptomatic_contact_fraction_30()) / 2


@cache('step')
def contacts_per_person_symptomatic_40x50():
    """
    Real Name: b'contacts per person symptomatic 40x50'
    Original Eqn: b'contacts per person normal 40x50*(symptomatic contact fraction 50+symptomatic contact fraction 40\\\\ )/2'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_40x50() * (symptomatic_contact_fraction_50() +
                                                 symptomatic_contact_fraction_40()) / 2


@cache('step')
def contacts_per_person_symptomatic_40x60():
    """
    Real Name: b'contacts per person symptomatic 40x60'
    Original Eqn: b'contacts per person normal 40x60*(symptomatic contact fraction 60+symptomatic contact fraction 40\\\\ )/2'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_40x60() * (symptomatic_contact_fraction_60() +
                                                 symptomatic_contact_fraction_40()) / 2


@cache('step')
def contacts_per_person_symptomatic_40x70():
    """
    Real Name: b'contacts per person symptomatic 40x70'
    Original Eqn: b'contacts per person normal 40x70*(symptomatic contact fraction 70+symptomatic contact fraction 40\\\\ )/2'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_40x70() * (symptomatic_contact_fraction_70() +
                                                 symptomatic_contact_fraction_40()) / 2


@cache('step')
def contacts_per_person_symptomatic_40x80():
    """
    Real Name: b'contacts per person symptomatic 40x80'
    Original Eqn: b'contacts per person normal 40x80*(symptomatic contact fraction 80+symptomatic contact fraction 40\\\\ )/2'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_40x80() * (symptomatic_contact_fraction_80() +
                                                 symptomatic_contact_fraction_40()) / 2


@cache('step')
def infection_rate_20():
    """
    Real Name: b'infection rate 20'
    Original Eqn: b'total infection rate 20+first infection 20'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return total_infection_rate_20() + first_infection_20()


@cache('step')
def init_total_population_00():
    """
    Real Name: b'init total population 00'
    Original Eqn: b'init Infected asymptomatic 00+init Susceptible 00'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return init_infected_asymptomatic_00() + init_susceptible_00()


@cache('step')
def init_total_population_10():
    """
    Real Name: b'init total population 10'
    Original Eqn: b'init Infected asymptomatic 10+init Susceptible 10'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return init_infected_asymptomatic_10() + init_susceptible_10()


@cache('step')
def init_total_population_20():
    """
    Real Name: b'init total population 20'
    Original Eqn: b'init Infected asymptomatic 20+init Susceptible 20'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return init_infected_asymptomatic_20() + init_susceptible_20()


@cache('step')
def init_total_population_30():
    """
    Real Name: b'init total population 30'
    Original Eqn: b'init Infected asymptomatic 30+init Susceptible 30'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return init_infected_asymptomatic_30() + init_susceptible_30()


@cache('step')
def init_total_population_40():
    """
    Real Name: b'init total population 40'
    Original Eqn: b'init Infected asymptomatic 40+init Susceptible 40'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return init_infected_asymptomatic_40() + init_susceptible_40()


@cache('step')
def incidence_per_100000_40():
    """
    Real Name: b'incidence per 100000 40'
    Original Eqn: b'accumulated cases 40/init total population 40*100000'
    Units: b'dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return accumulated_cases_40() / init_total_population_40() * 100000


@cache('step')
def contacts_per_person_symptomatic_self_00():
    """
    Real Name: b'contacts per person symptomatic self 00'
    Original Eqn: b'contacts per person normal self 00*symptomatic contact fraction 00'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_self_00() * symptomatic_contact_fraction_00()


@cache('step')
def contacts_per_person_symptomatic_self_10():
    """
    Real Name: b'contacts per person symptomatic self 10'
    Original Eqn: b'contacts per person normal self 10*symptomatic contact fraction 10'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_self_10() * symptomatic_contact_fraction_10()


@cache('step')
def contacts_per_person_symptomatic_self_20():
    """
    Real Name: b'contacts per person symptomatic self 20'
    Original Eqn: b'contacts per person normal self 20*symptomatic contact fraction 20'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_self_20() * symptomatic_contact_fraction_20()


@cache('step')
def contacts_per_person_symptomatic_self_30():
    """
    Real Name: b'contacts per person symptomatic self 30'
    Original Eqn: b'contacts per person normal self 30*symptomatic contact fraction 30'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_self_30() * symptomatic_contact_fraction_30()


@cache('step')
def contacts_per_person_symptomatic_self_40():
    """
    Real Name: b'contacts per person symptomatic self 40'
    Original Eqn: b'contacts per person normal self 40*symptomatic contact fraction 40'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_self_40() * symptomatic_contact_fraction_40()


@cache('step')
def isolated_10():
    """
    Real Name: b'Isolated 10'
    Original Eqn: b'INTEG ( isolation rate symptomatic 10+isolation rate asymptomatic 10-isolated recovery rate 10\\\\ -isolated critical case rate 10, init Isolated 10)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_isolated_10()


@cache('step')
def isolated_20():
    """
    Real Name: b'Isolated 20'
    Original Eqn: b'INTEG ( isolation rate symptomatic 20+isolation rate asymptomatic 20-isolated recovery rate 20\\\\ -isolated critical case rate 20, init Isolated 20)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_isolated_20()


@cache('step')
def isolated_30():
    """
    Real Name: b'Isolated 30'
    Original Eqn: b'INTEG ( isolation rate symptomatic 30+isolation rate asymptomatic 30-isolated recovery rate 30\\\\ -isolated critical case rate 30, init Isolated 30)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_isolated_30()


@cache('step')
def isolated_40():
    """
    Real Name: b'Isolated 40'
    Original Eqn: b'INTEG ( isolation rate symptomatic 40+isolation rate asymptomatic 40-isolated recovery rate 40\\\\ -isolated critical case rate 40, init Isolated 40)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_isolated_40()


@cache('step')
def infection_rate_asymptomatic_10x20():
    """
    Real Name: b'infection rate asymptomatic 10x20'
    Original Eqn: b'contact infectivity asymptomatic 10x20*(social distancing policy SWITCH self 20*social distancing policy 20\\\\ +(1-social distancing policy SWITCH self 20))*Infected asymptomatic 10x20*Susceptible 20\\\\ /non controlled pop 10x20'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contact_infectivity_asymptomatic_10x20() * (
        social_distancing_policy_switch_self_20() * social_distancing_policy_20() +
        (1 - social_distancing_policy_switch_self_20())
    ) * infected_asymptomatic_10x20() * susceptible_20() / non_controlled_pop_10x20()


@cache('step')
def critical_cases_00():
    """
    Real Name: b'Critical Cases 00'
    Original Eqn: b'INTEG ( infected critical case rate 00-critical cases recovery rate 00-death rate 00+isolated critical case rate 00\\\\ , init Critical Cases 00)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_critical_cases_00()


@cache('step')
def critical_cases_10():
    """
    Real Name: b'Critical Cases 10'
    Original Eqn: b'INTEG ( infected critical case rate 10-critical cases recovery rate 10-death rate 10+isolated critical case rate 10\\\\ , init Critical Cases 10)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_critical_cases_10()


@cache('step')
def critical_cases_20():
    """
    Real Name: b'Critical Cases 20'
    Original Eqn: b'INTEG ( infected critical case rate 20-critical cases recovery rate 20-death rate 20+isolated critical case rate 20\\\\ , init Critical Cases 20)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_critical_cases_20()


@cache('step')
def critical_cases_30():
    """
    Real Name: b'Critical Cases 30'
    Original Eqn: b'INTEG ( infected critical case rate 30-critical cases recovery rate 30-death rate 30+isolated critical case rate 30\\\\ , init Critical Cases 30)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_critical_cases_30()


@cache('step')
def critical_cases_40():
    """
    Real Name: b'Critical Cases 40'
    Original Eqn: b'INTEG ( infected critical case rate 40-critical cases recovery rate 40-death rate 40+isolated critical case rate 40\\\\ , init Critical Cases 40)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_critical_cases_40()


@cache('step')
def isolated_critical_case_rate_10():
    """
    Real Name: b'isolated critical case rate 10'
    Original Eqn: b'Isolated 10*fraction of critical cases 10/symptomatic duration 10'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return isolated_10() * fraction_of_critical_cases_10() / symptomatic_duration_10()


@cache('step')
def isolated_critical_case_rate_20():
    """
    Real Name: b'isolated critical case rate 20'
    Original Eqn: b'Isolated 20*fraction of critical cases 20/symptomatic duration 20'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return isolated_20() * fraction_of_critical_cases_20() / symptomatic_duration_20()


@cache('step')
def isolated_critical_case_rate_30():
    """
    Real Name: b'isolated critical case rate 30'
    Original Eqn: b'Isolated 30*fraction of critical cases 30/symptomatic duration 30'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return isolated_30() * fraction_of_critical_cases_30() / symptomatic_duration_30()


@cache('step')
def isolated_critical_case_rate_40():
    """
    Real Name: b'isolated critical case rate 40'
    Original Eqn: b'Isolated 40*fraction of critical cases 40/symptomatic duration 40'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return isolated_40() * fraction_of_critical_cases_40() / symptomatic_duration_40()


@cache('step')
def infection_rate_asymptomatic_20x40():
    """
    Real Name: b'infection rate asymptomatic 20x40'
    Original Eqn: b'contact infectivity asymptomatic 20x40*(social distancing policy SWITCH self 40*social distancing policy 40\\\\ +(1-social distancing policy SWITCH self 40))*Infected asymptomatic 20x40*Susceptible 40\\\\ /non controlled pop 20x40'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contact_infectivity_asymptomatic_20x40() * (
        social_distancing_policy_switch_self_40() * social_distancing_policy_40() +
        (1 - social_distancing_policy_switch_self_40())
    ) * infected_asymptomatic_20x40() * susceptible_40() / non_controlled_pop_20x40()


@cache('step')
def critical_cases_recovery_rate_00():
    """
    Real Name: b'critical cases recovery rate 00'
    Original Eqn: b'Critical Cases 00*(1-fraction of death 00)/duration of treatment 00'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return critical_cases_00() * (1 - fraction_of_death_00()) / duration_of_treatment_00()


@cache('step')
def critical_cases_recovery_rate_10():
    """
    Real Name: b'critical cases recovery rate 10'
    Original Eqn: b'Critical Cases 10*(1-fraction of death 10)/duration of treatment 10'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return critical_cases_10() * (1 - fraction_of_death_10()) / duration_of_treatment_10()


@cache('step')
def critical_cases_recovery_rate_20():
    """
    Real Name: b'critical cases recovery rate 20'
    Original Eqn: b'Critical Cases 20*(1-fraction of death 20)/duration of treatment 20'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return critical_cases_20() * (1 - fraction_of_death_20()) / duration_of_treatment_20()


@cache('step')
def critical_cases_recovery_rate_30():
    """
    Real Name: b'critical cases recovery rate 30'
    Original Eqn: b'Critical Cases 30*(1-fraction of death 30)/duration of treatment 30'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return critical_cases_30() * (1 - fraction_of_death_30()) / duration_of_treatment_30()


@cache('step')
def critical_cases_recovery_rate_40():
    """
    Real Name: b'critical cases recovery rate 40'
    Original Eqn: b'Critical Cases 40*(1-fraction of death 40)/duration of treatment 40'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return critical_cases_40() * (1 - fraction_of_death_40()) / duration_of_treatment_40()


@cache('step')
def isolated_recovery_rate_10():
    """
    Real Name: b'isolated recovery rate 10'
    Original Eqn: b'Isolated 10*(1-fraction of critical cases 10)/isolation duration 10'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return isolated_10() * (1 - fraction_of_critical_cases_10()) / isolation_duration_10()


@cache('step')
def isolated_recovery_rate_20():
    """
    Real Name: b'isolated recovery rate 20'
    Original Eqn: b'Isolated 20*(1-fraction of critical cases 20)/isolation duration 20'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return isolated_20() * (1 - fraction_of_critical_cases_20()) / isolation_duration_20()


@cache('step')
def isolated_recovery_rate_30():
    """
    Real Name: b'isolated recovery rate 30'
    Original Eqn: b'Isolated 30*(1-fraction of critical cases 30)/isolation duration 30'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return isolated_30() * (1 - fraction_of_critical_cases_30()) / isolation_duration_30()


@cache('step')
def isolated_recovery_rate_40():
    """
    Real Name: b'isolated recovery rate 40'
    Original Eqn: b'Isolated 40*(1-fraction of critical cases 40)/isolation duration 40'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return isolated_40() * (1 - fraction_of_critical_cases_40()) / isolation_duration_40()


@cache('step')
def infection_rate_asymptomatic_30x60():
    """
    Real Name: b'infection rate asymptomatic 30x60'
    Original Eqn: b'contact infectivity asymptomatic 30x60*(social distancing policy SWITCH self 60*social distancing policy 60\\\\ +(1-social distancing policy SWITCH self 60))*Infected asymptomatic 30x60*Susceptible 60\\\\ /non controlled pop 30x60'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contact_infectivity_asymptomatic_30x60() * (
        social_distancing_policy_switch_self_60() * social_distancing_policy_60() +
        (1 - social_distancing_policy_switch_self_60())
    ) * infected_asymptomatic_30x60() * susceptible_60() / non_controlled_pop_30x60()


@cache('step')
def death_rate_00():
    """
    Real Name: b'death rate 00'
    Original Eqn: b'Critical Cases 00*fraction of death 00/duration of treatment 00'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return critical_cases_00() * fraction_of_death_00() / duration_of_treatment_00()


@cache('step')
def death_rate_10():
    """
    Real Name: b'death rate 10'
    Original Eqn: b'Critical Cases 10*fraction of death 10/duration of treatment 10'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return critical_cases_10() * fraction_of_death_10() / duration_of_treatment_10()


@cache('step')
def death_rate_20():
    """
    Real Name: b'death rate 20'
    Original Eqn: b'Critical Cases 20*fraction of death 20/duration of treatment 20'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return critical_cases_20() * fraction_of_death_20() / duration_of_treatment_20()


@cache('step')
def death_rate_30():
    """
    Real Name: b'death rate 30'
    Original Eqn: b'Critical Cases 30*fraction of death 30/duration of treatment 30'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return critical_cases_30() * fraction_of_death_30() / duration_of_treatment_30()


@cache('step')
def death_rate_40():
    """
    Real Name: b'death rate 40'
    Original Eqn: b'Critical Cases 40*fraction of death 40/duration of treatment 40'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return critical_cases_40() * fraction_of_death_40() / duration_of_treatment_40()


@cache('run')
def isolation_duration_10():
    """
    Real Name: b'isolation duration 10'
    Original Eqn: b'14'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 14


@cache('run')
def isolation_duration_20():
    """
    Real Name: b'isolation duration 20'
    Original Eqn: b'14'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 14


@cache('run')
def isolation_duration_30():
    """
    Real Name: b'isolation duration 30'
    Original Eqn: b'14'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 14


@cache('run')
def isolation_duration_40():
    """
    Real Name: b'isolation duration 40'
    Original Eqn: b'14'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 14


@cache('step')
def infection_rate_asymptomatic_40x80():
    """
    Real Name: b'infection rate asymptomatic 40x80'
    Original Eqn: b'contact infectivity asymptomatic 40x80*(social distancing policy SWITCH self 80*social distancing policy 80\\\\ +(1-social distancing policy SWITCH self 80))*Infected asymptomatic 40x80*Susceptible 80\\\\ /non controlled pop 40x80'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contact_infectivity_asymptomatic_40x80() * (
        social_distancing_policy_switch_self_80() * social_distancing_policy_80() +
        (1 - social_distancing_policy_switch_self_80())
    ) * infected_asymptomatic_40x80() * susceptible_80() / non_controlled_pop_40x80()


@cache('step')
def deimmunization_rate_00():
    """
    Real Name: b'deimmunization rate 00'
    Original Eqn: b'Recovered 00/immunity time 00'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return recovered_00() / immunity_time_00()


@cache('step')
def deimmunization_rate_10():
    """
    Real Name: b'deimmunization rate 10'
    Original Eqn: b'Recovered 10/immunity time 10'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return recovered_10() / immunity_time_10()


@cache('step')
def deimmunization_rate_20():
    """
    Real Name: b'deimmunization rate 20'
    Original Eqn: b'Recovered 20/immunity time 20'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return recovered_20() / immunity_time_20()


@cache('step')
def deimmunization_rate_30():
    """
    Real Name: b'deimmunization rate 30'
    Original Eqn: b'Recovered 30/immunity time 30'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return recovered_30() / immunity_time_30()


@cache('step')
def deimmunization_rate_40():
    """
    Real Name: b'deimmunization rate 40'
    Original Eqn: b'Recovered 40/immunity time 40'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return recovered_40() / immunity_time_40()


@cache('run')
def isolation_effectiveness_10():
    """
    Real Name: b'isolation effectiveness 10'
    Original Eqn: b'0.9'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.9


@cache('run')
def isolation_effectiveness_20():
    """
    Real Name: b'isolation effectiveness 20'
    Original Eqn: b'0.9'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.9


@cache('run')
def isolation_effectiveness_30():
    """
    Real Name: b'isolation effectiveness 30'
    Original Eqn: b'0.9'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.9


@cache('run')
def isolation_effectiveness_40():
    """
    Real Name: b'isolation effectiveness 40'
    Original Eqn: b'0.9'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.9


@cache('step')
def infection_rate_asymptomatic_60x10():
    """
    Real Name: b'infection rate asymptomatic 60x10'
    Original Eqn: b'Susceptible 10*Infected asymptomatic 10x60*contact infectivity asymptomatic 10x60*(social distancing policy SWITCH self 10 *social distancing policy 10+(1-social distancing policy SWITCH self 10))/non controlled pop 10x60'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_10() * infected_asymptomatic_10x60(
    ) * contact_infectivity_asymptomatic_10x60() * (
        social_distancing_policy_switch_self_10() * social_distancing_policy_10() +
        (1 - social_distancing_policy_switch_self_10())) / non_controlled_pop_10x60()


@cache('step')
def diseased_00():
    """
    Real Name: b'Diseased 00'
    Original Eqn: b'INTEG ( death rate 00, init Diseased 00)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_diseased_00()


@cache('step')
def diseased_10():
    """
    Real Name: b'Diseased 10'
    Original Eqn: b'INTEG ( death rate 10, init Diseased 10)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_diseased_10()


@cache('step')
def diseased_20():
    """
    Real Name: b'Diseased 20'
    Original Eqn: b'INTEG ( death rate 20, init Diseased 20)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_diseased_20()


@cache('step')
def diseased_30():
    """
    Real Name: b'Diseased 30'
    Original Eqn: b'INTEG ( death rate 30, init Diseased 30)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_diseased_30()


@cache('step')
def infected_asymptomatic_recovery_rate_30():
    """
    Real Name: b'infected asymptomatic recovery rate 30'
    Original Eqn: b'fraction of asymptomatic case development 30*Infected asymptomatic 30/(asymptomatic duration 30\\\\ +symptomatic duration 30)'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return fraction_of_asymptomatic_case_development_30() * infected_asymptomatic_30() / (
        asymptomatic_duration_30() + symptomatic_duration_30())


@cache('step')
def isolation_rate_asymptomatic_10():
    """
    Real Name: b'isolation rate asymptomatic 10'
    Original Eqn: b'MIN(available test kits for testing asymptomatic*effect of kits availability on effectiveness of testing\\\\ /kits per person, Infected asymptomatic 10 )/testing duration'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return np.minimum(
        available_test_kits_for_testing_asymptomatic() *
        effect_of_kits_availability_on_effectiveness_of_testing() / kits_per_person(),
        infected_asymptomatic_10()) / testing_duration()


@cache('step')
def isolation_rate_asymptomatic_20():
    """
    Real Name: b'isolation rate asymptomatic 20'
    Original Eqn: b'MIN(available test kits for testing asymptomatic*effect of kits availability on effectiveness of testing\\\\ /kits per person, Infected asymptomatic 20 )/testing duration'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return np.minimum(
        available_test_kits_for_testing_asymptomatic() *
        effect_of_kits_availability_on_effectiveness_of_testing() / kits_per_person(),
        infected_asymptomatic_20()) / testing_duration()


@cache('step')
def isolation_rate_asymptomatic_30():
    """
    Real Name: b'isolation rate asymptomatic 30'
    Original Eqn: b'MIN(available test kits for testing asymptomatic*effect of kits availability on effectiveness of testing\\\\ /kits per person, Infected asymptomatic 30 )/testing duration'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return np.minimum(
        available_test_kits_for_testing_asymptomatic() *
        effect_of_kits_availability_on_effectiveness_of_testing() / kits_per_person(),
        infected_asymptomatic_30()) / testing_duration()


@cache('step')
def isolation_rate_asymptomatic_40():
    """
    Real Name: b'isolation rate asymptomatic 40'
    Original Eqn: b'MIN(available test kits for testing asymptomatic*effect of kits availability on effectiveness of testing\\\\ /kits per person, Infected asymptomatic 40 )/testing duration'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return np.minimum(
        available_test_kits_for_testing_asymptomatic() *
        effect_of_kits_availability_on_effectiveness_of_testing() / kits_per_person(),
        infected_asymptomatic_40()) / testing_duration()


@cache('step')
def infection_rate_asymptomatic_70x30():
    """
    Real Name: b'infection rate asymptomatic 70x30'
    Original Eqn: b'Susceptible 30*Infected asymptomatic 30x70*contact infectivity asymptomatic 30x70*(social distancing policy SWITCH self 30 *social distancing policy 30+(1-social distancing policy SWITCH self 30))/non controlled pop 30x70'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_30() * infected_asymptomatic_30x70(
    ) * contact_infectivity_asymptomatic_30x70() * (
        social_distancing_policy_switch_self_30() * social_distancing_policy_30() +
        (1 - social_distancing_policy_switch_self_30())) / non_controlled_pop_30x70()


@cache('step')
def infection_rate_asymptomatic_70x40():
    """
    Real Name: b'infection rate asymptomatic 70x40'
    Original Eqn: b'Susceptible 40*Infected asymptomatic 40x70*contact infectivity asymptomatic 40x70*(social distancing policy SWITCH self 40 *social distancing policy 40+(1-social distancing policy SWITCH self 40))/non controlled pop 40x70'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_40() * infected_asymptomatic_40x70(
    ) * contact_infectivity_asymptomatic_40x70() * (
        social_distancing_policy_switch_self_40() * social_distancing_policy_40() +
        (1 - social_distancing_policy_switch_self_40())) / non_controlled_pop_40x70()


@cache('step')
def infected_critical_case_rate_00():
    """
    Real Name: b'infected critical case rate 00'
    Original Eqn: b'Infected symptomatic 00*fraction of critical cases 00/symptomatic duration 00'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_00() * fraction_of_critical_cases_00() / symptomatic_duration_00()


@cache('step')
def infected_critical_case_rate_10():
    """
    Real Name: b'infected critical case rate 10'
    Original Eqn: b'Infected symptomatic 10*fraction of critical cases 10/symptomatic duration 10'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_10() * fraction_of_critical_cases_10() / symptomatic_duration_10()


@cache('run')
def duration_of_treatment_30():
    """
    Real Name: b'duration of treatment 30'
    Original Eqn: b'10'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 10


@cache('run')
def duration_of_treatment_40():
    """
    Real Name: b'duration of treatment 40'
    Original Eqn: b'10'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 10


@cache('step')
def isolation_rate_symptomatic_10():
    """
    Real Name: b'isolation rate symptomatic 10'
    Original Eqn: b'tests for symptomatic/kits per person/testing duration'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return tests_for_symptomatic() / kits_per_person() / testing_duration()


@cache('step')
def isolation_rate_symptomatic_20():
    """
    Real Name: b'isolation rate symptomatic 20'
    Original Eqn: b'tests for symptomatic/kits per person/testing duration'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return tests_for_symptomatic() / kits_per_person() / testing_duration()


@cache('step')
def isolation_rate_symptomatic_30():
    """
    Real Name: b'isolation rate symptomatic 30'
    Original Eqn: b'tests for symptomatic/kits per person/testing duration'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return tests_for_symptomatic() / kits_per_person() / testing_duration()


@cache('step')
def isolation_rate_symptomatic_40():
    """
    Real Name: b'isolation rate symptomatic 40'
    Original Eqn: b'tests for symptomatic/kits per person/testing duration'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return tests_for_symptomatic() / kits_per_person() / testing_duration()


@cache('run')
def social_distancing_effectiveness_00():
    """
    Real Name: b'social distancing effectiveness 00'
    Original Eqn: b'0.6'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.6


@cache('step')
def infection_rate_asymptomatic_00x30():
    """
    Real Name: b'infection rate asymptomatic 00x30'
    Original Eqn: b'contact infectivity asymptomatic 00x30*(social distancing policy SWITCH self 30*social distancing policy 30\\\\ +(1-social distancing policy SWITCH self 30))*Infected asymptomatic 00x30*Susceptible 30\\\\ /non controlled pop 00x30'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contact_infectivity_asymptomatic_00x30() * (
        social_distancing_policy_switch_self_30() * social_distancing_policy_30() +
        (1 - social_distancing_policy_switch_self_30())
    ) * infected_asymptomatic_00x30() * susceptible_30() / non_controlled_pop_00x30()


@cache('step')
def infected_symptomatic_00():
    """
    Real Name: b'Infected symptomatic 00'
    Original Eqn: b'INTEG ( symptomatic rate 00-infected critical case rate 00-infected symptomatic recovery rate 00\\\\ -isolation rate symptomatic 00, init Infected symptomatic 00)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_infected_symptomatic_00()


@cache('step')
def first_infection_10():
    """
    Real Name: b'first infection 10'
    Original Eqn: b'PULSE(infection start 10, 1)*normal first infected'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.pulse(__data['time'], infection_start_10(), 1) * normal_first_infected()


@cache('step')
def first_infection_20():
    """
    Real Name: b'first infection 20'
    Original Eqn: b'PULSE(infection start 20, 1)*normal first infected'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.pulse(__data['time'], infection_start_20(), 1) * normal_first_infected()


@cache('step')
def first_infection_30():
    """
    Real Name: b'first infection 30'
    Original Eqn: b'PULSE(infection start 30, 1)*normal first infected'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.pulse(__data['time'], infection_start_30(), 1) * normal_first_infected()


@cache('step')
def first_infection_40():
    """
    Real Name: b'first infection 40'
    Original Eqn: b'PULSE(infection start 40, 1)*normal first infected'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.pulse(__data['time'], infection_start_40(), 1) * normal_first_infected()


@cache('step')
def infected_symptomatic_00x50():
    """
    Real Name: b'Infected symptomatic 00x50'
    Original Eqn: b'Infected symptomatic 00+Infected symptomatic 50'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_00() + infected_symptomatic_50()


@cache('step')
def infected_asymptomatic_00x40():
    """
    Real Name: b'Infected asymptomatic 00x40'
    Original Eqn: b'Infected asymptomatic 00+Infected asymptomatic 40'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic_00() + infected_asymptomatic_40()


@cache('step')
def new_cases_00():
    """
    Real Name: b'new cases 00'
    Original Eqn: b'symptomatic rate 00*test fraction 00'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return symptomatic_rate_00() * test_fraction_00()


@cache('step')
def new_cases_10():
    """
    Real Name: b'new cases 10'
    Original Eqn: b'symptomatic rate 10*test fraction 10'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return symptomatic_rate_10() * test_fraction_10()


@cache('step')
def new_cases_20():
    """
    Real Name: b'new cases 20'
    Original Eqn: b'symptomatic rate 20*test fraction 20'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return symptomatic_rate_20() * test_fraction_20()


@cache('run')
def fraction_of_asymptomatic_case_development_00():
    """
    Real Name: b'fraction of asymptomatic case development 00'
    Original Eqn: b'0.5'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.5


@cache('run')
def fraction_of_asymptomatic_case_development_10():
    """
    Real Name: b'fraction of asymptomatic case development 10'
    Original Eqn: b'0.5'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.5


@cache('run')
def fraction_of_asymptomatic_case_development_20():
    """
    Real Name: b'fraction of asymptomatic case development 20'
    Original Eqn: b'0.5'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.5


@cache('run')
def fraction_of_asymptomatic_case_development_30():
    """
    Real Name: b'fraction of asymptomatic case development 30'
    Original Eqn: b'0.5'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.5


@cache('run')
def fraction_of_asymptomatic_case_development_40():
    """
    Real Name: b'fraction of asymptomatic case development 40'
    Original Eqn: b'0.5'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.5


@cache('run')
def social_distancing_end_60():
    """
    Real Name: b'social distancing end 60'
    Original Eqn: b'50'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 50


@cache('step')
def non_controlled_pop_00x10():
    """
    Real Name: b'non controlled pop 00x10'
    Original Eqn: b'non controlled population 00+non controlled population 10'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return non_controlled_population_00() + non_controlled_population_10()


@cache('step')
def non_controlled_pop_00x20():
    """
    Real Name: b'non controlled pop 00x20'
    Original Eqn: b'non controlled population 00+non controlled population 20'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return non_controlled_population_00() + non_controlled_population_20()


@cache('step')
def non_controlled_pop_00x30():
    """
    Real Name: b'non controlled pop 00x30'
    Original Eqn: b'non controlled population 00+non controlled population 30'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return non_controlled_population_00() + non_controlled_population_30()


@cache('step')
def non_controlled_pop_00x40():
    """
    Real Name: b'non controlled pop 00x40'
    Original Eqn: b'non controlled population 00+non controlled population 40'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return non_controlled_population_00() + non_controlled_population_40()


@cache('run')
def fraction_of_critical_cases_00():
    """
    Real Name: b'fraction of critical cases 00'
    Original Eqn: b'0.1'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.1


@cache('run')
def fraction_of_critical_cases_10():
    """
    Real Name: b'fraction of critical cases 10'
    Original Eqn: b'0.1'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.1


@cache('run')
def fraction_of_critical_cases_20():
    """
    Real Name: b'fraction of critical cases 20'
    Original Eqn: b'0.1'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.1


@cache('run')
def fraction_of_critical_cases_30():
    """
    Real Name: b'fraction of critical cases 30'
    Original Eqn: b'0.1'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.1


@cache('run')
def fraction_of_critical_cases_40():
    """
    Real Name: b'fraction of critical cases 40'
    Original Eqn: b'0.1'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.1


@cache('step')
def non_controlled_pop_10x30():
    """
    Real Name: b'non controlled pop 10x30'
    Original Eqn: b'non controlled population 10+non controlled population 30'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return non_controlled_population_10() + non_controlled_population_30()


@cache('step')
def non_controlled_pop_10x40():
    """
    Real Name: b'non controlled pop 10x40'
    Original Eqn: b'non controlled population 10+non controlled population 40'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return non_controlled_population_10() + non_controlled_population_40()


@cache('step')
def non_controlled_pop_10x50():
    """
    Real Name: b'non controlled pop 10x50'
    Original Eqn: b'non controlled population 10+non controlled population 50'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return non_controlled_population_10() + non_controlled_population_50()


@cache('step')
def non_controlled_pop_10x60():
    """
    Real Name: b'non controlled pop 10x60'
    Original Eqn: b'non controlled population 10+non controlled population 60'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return non_controlled_population_10() + non_controlled_population_60()


@cache('step')
def non_controlled_pop_10x70():
    """
    Real Name: b'non controlled pop 10x70'
    Original Eqn: b'non controlled population 10+non controlled population 70'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return non_controlled_population_10() + non_controlled_population_70()


@cache('run')
def fraction_of_death_00():
    """
    Real Name: b'fraction of death 00'
    Original Eqn: b'0.4'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.4


@cache('run')
def fraction_of_death_10():
    """
    Real Name: b'fraction of death 10'
    Original Eqn: b'0.4'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.4


@cache('run')
def fraction_of_death_20():
    """
    Real Name: b'fraction of death 20'
    Original Eqn: b'0.4'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.4


@cache('run')
def fraction_of_death_30():
    """
    Real Name: b'fraction of death 30'
    Original Eqn: b'0.4'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.4


@cache('run')
def fraction_of_death_40():
    """
    Real Name: b'fraction of death 40'
    Original Eqn: b'0.4'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.4


@cache('step')
def non_controlled_pop_20x70():
    """
    Real Name: b'non controlled pop 20x70'
    Original Eqn: b'non controlled population 20+non controlled population 70'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return non_controlled_population_20() + non_controlled_population_70()


@cache('step')
def non_controlled_pop_20x80():
    """
    Real Name: b'non controlled pop 20x80'
    Original Eqn: b'non controlled population 20+non controlled population 80'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return non_controlled_population_20() + non_controlled_population_80()


@cache('step')
def non_controlled_pop_30x40():
    """
    Real Name: b'non controlled pop 30x40'
    Original Eqn: b'non controlled population 30+non controlled population 40'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return non_controlled_population_30() + non_controlled_population_40()


@cache('step')
def non_controlled_pop_30x50():
    """
    Real Name: b'non controlled pop 30x50'
    Original Eqn: b'non controlled population 30+non controlled population 50'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return non_controlled_population_30() + non_controlled_population_50()


@cache('step')
def non_controlled_pop_30x60():
    """
    Real Name: b'non controlled pop 30x60'
    Original Eqn: b'non controlled population 30+non controlled population 60'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return non_controlled_population_30() + non_controlled_population_60()


@cache('step')
def fraction_of_symptomatic_00():
    """
    Real Name: b'fraction of symptomatic 00'
    Original Eqn: b'ZIDZ(Infected symptomatic 00, total infected 00)'
    Units: b'dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.zidz(infected_symptomatic_00(), total_infected_00())


@cache('step')
def fraction_of_symptomatic_10():
    """
    Real Name: b'fraction of symptomatic 10'
    Original Eqn: b'ZIDZ(Infected symptomatic 10, total infected 10)'
    Units: b'dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.zidz(infected_symptomatic_10(), total_infected_10())


@cache('step')
def fraction_of_symptomatic_20():
    """
    Real Name: b'fraction of symptomatic 20'
    Original Eqn: b'ZIDZ(Infected symptomatic 20, total infected 20)'
    Units: b'dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.zidz(infected_symptomatic_20(), total_infected_20())


@cache('step')
def fraction_of_symptomatic_30():
    """
    Real Name: b'fraction of symptomatic 30'
    Original Eqn: b'ZIDZ(Infected symptomatic 30, total infected 30)'
    Units: b'dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.zidz(infected_symptomatic_30(), total_infected_30())


@cache('step')
def fraction_of_symptomatic_40():
    """
    Real Name: b'fraction of symptomatic 40'
    Original Eqn: b'ZIDZ(Infected symptomatic 40, total infected 40)'
    Units: b'dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.zidz(infected_symptomatic_40(), total_infected_40())


@cache('step')
def non_controlled_pop_40x80():
    """
    Real Name: b'non controlled pop 40x80'
    Original Eqn: b'non controlled population 40+non controlled population 80'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return non_controlled_population_40() + non_controlled_population_80()


@cache('step')
def infection_rate_symptomatic_30x10():
    """
    Real Name: b'infection rate symptomatic 30x10'
    Original Eqn: b'Susceptible 10*Infected symptomatic 10x30*contact infectivity symptomatic 10x30*(self quarantine policy SWITCH self 10\\\\ * self quarantine policy 10+(1-self quarantine policy SWITCH self 10))/non controlled pop 10x30'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_10() * infected_symptomatic_10x30() * contact_infectivity_symptomatic_10x30(
    ) * (self_quarantine_policy_switch_self_10() * self_quarantine_policy_10() +
         (1 - self_quarantine_policy_switch_self_10())) / non_controlled_pop_10x30()


@cache('step')
def infected_symptomatic_recovery_rate_10():
    """
    Real Name: b'infected symptomatic recovery rate 10'
    Original Eqn: b'Infected symptomatic 10*(1-fraction of critical cases 10)/symptomatic duration 10'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_10() * (
        1 - fraction_of_critical_cases_10()) / symptomatic_duration_10()


@cache('step')
def infected_symptomatic_recovery_rate_20():
    """
    Real Name: b'infected symptomatic recovery rate 20'
    Original Eqn: b'Infected symptomatic 20*(1-fraction of critical cases 20)/symptomatic duration 20'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_20() * (
        1 - fraction_of_critical_cases_20()) / symptomatic_duration_20()


@cache('step')
def infected_symptomatic_recovery_rate_30():
    """
    Real Name: b'infected symptomatic recovery rate 30'
    Original Eqn: b'Infected symptomatic 30*(1-fraction of critical cases 30)/symptomatic duration 30'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_30() * (
        1 - fraction_of_critical_cases_30()) / symptomatic_duration_30()


@cache('run')
def immunity_time_00():
    """
    Real Name: b'immunity time 00'
    Original Eqn: b'360'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 360


@cache('run')
def immunity_time_10():
    """
    Real Name: b'immunity time 10'
    Original Eqn: b'360'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 360


@cache('run')
def immunity_time_20():
    """
    Real Name: b'immunity time 20'
    Original Eqn: b'360'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 360


@cache('run')
def immunity_time_30():
    """
    Real Name: b'immunity time 30'
    Original Eqn: b'360'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 360


@cache('run')
def immunity_time_40():
    """
    Real Name: b'immunity time 40'
    Original Eqn: b'360'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 360


@cache('step')
def non_controlled_population_20():
    """
    Real Name: b'non controlled population 20'
    Original Eqn: b'Infected symptomatic 20+Susceptible 20+Infected asymptomatic 20+Isolated 20+Recovered 20'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_20() + susceptible_20() + infected_asymptomatic_20() + isolated_20(
    ) + recovered_20()


@cache('step')
def non_controlled_population_30():
    """
    Real Name: b'non controlled population 30'
    Original Eqn: b'Infected symptomatic 30+Susceptible 30+Infected asymptomatic 30+Isolated 30+Recovered 30'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_30() + susceptible_30() + infected_asymptomatic_30() + isolated_30(
    ) + recovered_30()


@cache('step')
def non_controlled_population_40():
    """
    Real Name: b'non controlled population 40'
    Original Eqn: b'Infected symptomatic 40+Susceptible 40+Infected asymptomatic 40+Isolated 40+Recovered 40'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_40() + susceptible_40() + infected_asymptomatic_40() + isolated_40(
    ) + recovered_40()


@cache('step')
def infection_rate_symptomatic_40x60():
    """
    Real Name: b'infection rate symptomatic 40x60'
    Original Eqn: b'Susceptible 60*Infected symptomatic 40x60*contact infectivity symptomatic 40x60*(self quarantine policy SWITCH self 60\\\\ *self quarantine policy 60+(1-self quarantine policy SWITCH self 60))/non controlled pop 40x60'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_60() * infected_symptomatic_40x60() * contact_infectivity_symptomatic_40x60(
    ) * (self_quarantine_policy_switch_self_60() * self_quarantine_policy_60() +
         (1 - self_quarantine_policy_switch_self_60())) / non_controlled_pop_40x60()


@cache('step')
def infection_rate_30():
    """
    Real Name: b'infection rate 30'
    Original Eqn: b'total infection rate 30+first infection 30'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return total_infection_rate_30() + first_infection_30()


@cache('step')
def incidence_per_100000_00():
    """
    Real Name: b'incidence per 100000 00'
    Original Eqn: b'accumulated cases 00/init total population 00*100000'
    Units: b'dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return accumulated_cases_00() / init_total_population_00() * 100000


@cache('step')
def incidence_per_100000_10():
    """
    Real Name: b'incidence per 100000 10'
    Original Eqn: b'accumulated cases 10/init total population 10*100000'
    Units: b'dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return accumulated_cases_10() / init_total_population_10() * 100000


@cache('step')
def incidence_per_100000_20():
    """
    Real Name: b'incidence per 100000 20'
    Original Eqn: b'accumulated cases 20/init total population 20*100000'
    Units: b'dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return accumulated_cases_20() / init_total_population_20() * 100000


@cache('step')
def incidence_per_100000_30():
    """
    Real Name: b'incidence per 100000 30'
    Original Eqn: b'accumulated cases 30/init total population 30*100000'
    Units: b'dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return accumulated_cases_30() / init_total_population_30() * 100000


@cache('step')
def infection_rate_symptomatic_50x30():
    """
    Real Name: b'infection rate symptomatic 50x30'
    Original Eqn: b'Susceptible 30*Infected symptomatic 30x50*contact infectivity symptomatic 30x50*(self quarantine policy SWITCH self 30\\\\ * self quarantine policy 30+(1-self quarantine policy SWITCH self 30))/non controlled pop 30x50'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_30() * infected_symptomatic_30x50() * contact_infectivity_symptomatic_30x50(
    ) * (self_quarantine_policy_switch_self_30() * self_quarantine_policy_30() +
         (1 - self_quarantine_policy_switch_self_30())) / non_controlled_pop_30x50()


@cache('step')
def infection_rate_symptomatic_50x40():
    """
    Real Name: b'infection rate symptomatic 50x40'
    Original Eqn: b'Susceptible 40*Infected symptomatic 40x50*contact infectivity symptomatic 40x50*(self quarantine policy SWITCH self 40\\\\ * self quarantine policy 40+(1-self quarantine policy SWITCH self 40))/non controlled pop 40x50'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_40() * infected_symptomatic_40x50() * contact_infectivity_symptomatic_40x50(
    ) * (self_quarantine_policy_switch_self_40() * self_quarantine_policy_40() +
         (1 - self_quarantine_policy_switch_self_40())) / non_controlled_pop_40x50()


@cache('step')
def infection_rate_asymptomatic_00x20():
    """
    Real Name: b'infection rate asymptomatic 00x20'
    Original Eqn: b'contact infectivity asymptomatic 00x20*(social distancing policy SWITCH self 20*social distancing policy 20\\\\ +(1-social distancing policy SWITCH self 20))*Infected asymptomatic 00x20*Susceptible 20\\\\ /non controlled pop 00x20'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contact_infectivity_asymptomatic_00x20() * (
        social_distancing_policy_switch_self_20() * social_distancing_policy_20() +
        (1 - social_distancing_policy_switch_self_20())
    ) * infected_asymptomatic_00x20() * susceptible_20() / non_controlled_pop_00x20()


@cache('step')
def infected_asymptomatic_40x50():
    """
    Real Name: b'Infected asymptomatic 40x50'
    Original Eqn: b'Infected asymptomatic 40+Infected asymptomatic 50'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic_40() + infected_asymptomatic_50()


@cache('step')
def infection_rate_asymptomatic_00x40():
    """
    Real Name: b'infection rate asymptomatic 00x40'
    Original Eqn: b'contact infectivity asymptomatic 00x40*(social distancing policy SWITCH self 40*social distancing policy 40\\\\ +(1-social distancing policy SWITCH self 40))*Infected asymptomatic 00x40*Susceptible 40\\\\ /non controlled pop 00x40'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contact_infectivity_asymptomatic_00x40() * (
        social_distancing_policy_switch_self_40() * social_distancing_policy_40() +
        (1 - social_distancing_policy_switch_self_40())
    ) * infected_asymptomatic_00x40() * susceptible_40() / non_controlled_pop_00x40()


@cache('step')
def infection_rate_asymptomatic_00x50():
    """
    Real Name: b'infection rate asymptomatic 00x50'
    Original Eqn: b'contact infectivity asymptomatic 00x50*(social distancing policy SWITCH self 50*social distancing policy 50\\\\ +(1-social distancing policy SWITCH self 50))*Infected asymptomatic 00x50*Susceptible 50\\\\ /non controlled pop 00x50'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contact_infectivity_asymptomatic_00x50() * (
        social_distancing_policy_switch_self_50() * social_distancing_policy_50() +
        (1 - social_distancing_policy_switch_self_50())
    ) * infected_asymptomatic_00x50() * susceptible_50() / non_controlled_pop_00x50()


@cache('step')
def infected_asymptomatic_00():
    """
    Real Name: b'Infected asymptomatic 00'
    Original Eqn: b'INTEG ( infection rate 00-infected asymptomatic recovery rate 00-isolation rate asymptomatic 00\\\\ -symptomatic rate 00, init Infected asymptomatic 00)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_infected_asymptomatic_00()


@cache('step')
def infected_asymptomatic_00x10():
    """
    Real Name: b'Infected asymptomatic 00x10'
    Original Eqn: b'Infected asymptomatic 00+Infected asymptomatic 10'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic_00() + infected_asymptomatic_10()


@cache('step')
def infected_asymptomatic_00x20():
    """
    Real Name: b'Infected asymptomatic 00x20'
    Original Eqn: b'Infected asymptomatic 00+Infected asymptomatic 20'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic_00() + infected_asymptomatic_20()


@cache('step')
def infected_asymptomatic_00x30():
    """
    Real Name: b'Infected asymptomatic 00x30'
    Original Eqn: b'Infected asymptomatic 00+Infected asymptomatic 30'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic_00() + infected_asymptomatic_30()


@cache('step')
def infection_rate_asymptomatic_50x30():
    """
    Real Name: b'infection rate asymptomatic 50x30'
    Original Eqn: b'Susceptible 30*Infected asymptomatic 30x50*contact infectivity asymptomatic 30x50*(social distancing policy SWITCH self 30 *social distancing policy 30+(1-social distancing policy SWITCH self 30))/non controlled pop 30x50'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_30() * infected_asymptomatic_30x50(
    ) * contact_infectivity_asymptomatic_30x50() * (
        social_distancing_policy_switch_self_30() * social_distancing_policy_30() +
        (1 - social_distancing_policy_switch_self_30())) / non_controlled_pop_30x50()


@cache('step')
def infected_asymptomatic_00x50():
    """
    Real Name: b'Infected asymptomatic 00x50'
    Original Eqn: b'Infected asymptomatic 00+Infected asymptomatic 50'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic_00() + infected_asymptomatic_50()


@cache('step')
def infected_asymptomatic_00x60():
    """
    Real Name: b'Infected asymptomatic 00x60'
    Original Eqn: b'Infected asymptomatic 00+Infected asymptomatic 60'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic_00() + infected_asymptomatic_60()


@cache('step')
def infected_asymptomatic_00x70():
    """
    Real Name: b'Infected asymptomatic 00x70'
    Original Eqn: b'Infected asymptomatic 00+Infected asymptomatic 70'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic_00() + infected_asymptomatic_70()


@cache('step')
def infected_asymptomatic_00x80():
    """
    Real Name: b'Infected asymptomatic 00x80'
    Original Eqn: b'Infected asymptomatic 00+Infected asymptomatic 80'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic_00() + infected_asymptomatic_80()


@cache('step')
def infected_asymptomatic_10():
    """
    Real Name: b'Infected asymptomatic 10'
    Original Eqn: b'INTEG ( infection rate 10-infected asymptomatic recovery rate 10-isolation rate asymptomatic 10\\\\ -symptomatic rate 10, init Infected asymptomatic 10)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_infected_asymptomatic_10()


@cache('step')
def infected_asymptomatic_10x20():
    """
    Real Name: b'Infected asymptomatic 10x20'
    Original Eqn: b'Infected asymptomatic 10+Infected asymptomatic 20'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic_10() + infected_asymptomatic_20()


@cache('step')
def infected_asymptomatic_10x30():
    """
    Real Name: b'Infected asymptomatic 10x30'
    Original Eqn: b'Infected asymptomatic 10+Infected asymptomatic 30'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic_10() + infected_asymptomatic_30()


@cache('step')
def infected_asymptomatic_10x40():
    """
    Real Name: b'Infected asymptomatic 10x40'
    Original Eqn: b'Infected asymptomatic 10+Infected asymptomatic 40'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic_10() + infected_asymptomatic_40()


@cache('step')
def infected_asymptomatic_10x50():
    """
    Real Name: b'Infected asymptomatic 10x50'
    Original Eqn: b'Infected asymptomatic 10+Infected asymptomatic 50'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic_10() + infected_asymptomatic_50()


@cache('step')
def infected_asymptomatic_10x60():
    """
    Real Name: b'Infected asymptomatic 10x60'
    Original Eqn: b'Infected asymptomatic 10+Infected asymptomatic 60'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic_10() + infected_asymptomatic_60()


@cache('step')
def infected_asymptomatic_10x70():
    """
    Real Name: b'Infected asymptomatic 10x70'
    Original Eqn: b'Infected asymptomatic 10+Infected asymptomatic 70'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic_10() + infected_asymptomatic_70()


@cache('step')
def infected_asymptomatic_10x80():
    """
    Real Name: b'Infected asymptomatic 10x80'
    Original Eqn: b'Infected asymptomatic 10+Infected asymptomatic 80'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic_10() + infected_asymptomatic_80()


@cache('step')
def infected_asymptomatic_20():
    """
    Real Name: b'Infected asymptomatic 20'
    Original Eqn: b'INTEG ( infection rate 20-infected asymptomatic recovery rate 20-isolation rate asymptomatic 20\\\\ -symptomatic rate 20, init Infected asymptomatic 20)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_infected_asymptomatic_20()


@cache('step')
def infected_asymptomatic_20x30():
    """
    Real Name: b'Infected asymptomatic 20x30'
    Original Eqn: b'Infected asymptomatic 20+Infected asymptomatic 30'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic_20() + infected_asymptomatic_30()


@cache('step')
def infected_asymptomatic_20x40():
    """
    Real Name: b'Infected asymptomatic 20x40'
    Original Eqn: b'Infected asymptomatic 20+Infected asymptomatic 40'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic_20() + infected_asymptomatic_40()


@cache('step')
def infected_asymptomatic_20x50():
    """
    Real Name: b'Infected asymptomatic 20x50'
    Original Eqn: b'Infected asymptomatic 20+Infected asymptomatic 50'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic_20() + infected_asymptomatic_50()


@cache('step')
def infected_asymptomatic_20x60():
    """
    Real Name: b'Infected asymptomatic 20x60'
    Original Eqn: b'Infected asymptomatic 20+Infected asymptomatic 60'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic_20() + infected_asymptomatic_60()


@cache('step')
def infected_asymptomatic_20x70():
    """
    Real Name: b'Infected asymptomatic 20x70'
    Original Eqn: b'Infected asymptomatic 20+Infected asymptomatic 70'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic_20() + infected_asymptomatic_70()


@cache('step')
def infected_asymptomatic_20x80():
    """
    Real Name: b'Infected asymptomatic 20x80'
    Original Eqn: b'Infected asymptomatic 20+Infected asymptomatic 80'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic_20() + infected_asymptomatic_80()


@cache('step')
def infected_asymptomatic_30():
    """
    Real Name: b'Infected asymptomatic 30'
    Original Eqn: b'INTEG ( infection rate 30-infected asymptomatic recovery rate 30-isolation rate asymptomatic 30\\\\ -symptomatic rate 30, init Infected asymptomatic 30)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_infected_asymptomatic_30()


@cache('step')
def infected_asymptomatic_30x40():
    """
    Real Name: b'Infected asymptomatic 30x40'
    Original Eqn: b'Infected asymptomatic 30+Infected asymptomatic 40'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic_30() + infected_asymptomatic_40()


@cache('step')
def infected_asymptomatic_30x50():
    """
    Real Name: b'Infected asymptomatic 30x50'
    Original Eqn: b'Infected asymptomatic 30+Infected asymptomatic 50'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic_30() + infected_asymptomatic_50()


@cache('step')
def infected_asymptomatic_30x60():
    """
    Real Name: b'Infected asymptomatic 30x60'
    Original Eqn: b'Infected asymptomatic 30+Infected asymptomatic 60'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic_30() + infected_asymptomatic_60()


@cache('step')
def infected_asymptomatic_30x70():
    """
    Real Name: b'Infected asymptomatic 30x70'
    Original Eqn: b'Infected asymptomatic 30+Infected asymptomatic 70'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic_30() + infected_asymptomatic_70()


@cache('step')
def infected_asymptomatic_30x80():
    """
    Real Name: b'Infected asymptomatic 30x80'
    Original Eqn: b'Infected asymptomatic 30+Infected asymptomatic 80'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic_30() + infected_asymptomatic_80()


@cache('step')
def infected_asymptomatic_40():
    """
    Real Name: b'Infected asymptomatic 40'
    Original Eqn: b'INTEG ( infection rate 40-infected asymptomatic recovery rate 40-isolation rate asymptomatic 40\\\\ -symptomatic rate 40, init Infected asymptomatic 40)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_infected_asymptomatic_40()


@cache('step')
def infected_symptomatic_40x70():
    """
    Real Name: b'Infected symptomatic 40x70'
    Original Eqn: b'Infected symptomatic 40+Infected symptomatic 70'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_40() + infected_symptomatic_70()


@cache('run')
def self_quarantine_end_70():
    """
    Real Name: b'self quarantine end 70'
    Original Eqn: b'50'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 50


@cache('step')
def infected_asymptomatic_40x70():
    """
    Real Name: b'Infected asymptomatic 40x70'
    Original Eqn: b'Infected asymptomatic 40+Infected asymptomatic 70'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic_40() + infected_asymptomatic_70()


@cache('step')
def infected_asymptomatic_40x80():
    """
    Real Name: b'Infected asymptomatic 40x80'
    Original Eqn: b'Infected asymptomatic 40+Infected asymptomatic 80'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic_40() + infected_asymptomatic_80()


@cache('step')
def self_quarantine_policy_10():
    """
    Real Name: b'self quarantine policy 10'
    Original Eqn: b'1-PULSE(self quarantine start 10, self quarantine end 10-self quarantine start 10)*self quarantine effectiveness 10'
    Units: b'dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return 1 - functions.pulse(__data['time'], self_quarantine_start_10(),
                               self_quarantine_end_10() -
                               self_quarantine_start_10()) * self_quarantine_effectiveness_10()


@cache('step')
def self_quarantine_policy_20():
    """
    Real Name: b'self quarantine policy 20'
    Original Eqn: b'1-PULSE(self quarantine start 20, self quarantine end 20-self quarantine start 20)*self quarantine effectiveness 20'
    Units: b'dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return 1 - functions.pulse(__data['time'], self_quarantine_start_20(),
                               self_quarantine_end_20() -
                               self_quarantine_start_20()) * self_quarantine_effectiveness_20()


@cache('step')
def self_quarantine_policy_30():
    """
    Real Name: b'self quarantine policy 30'
    Original Eqn: b'1-PULSE(self quarantine start 30, self quarantine end 30-self quarantine start 30)*self quarantine effectiveness 30'
    Units: b'dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return 1 - functions.pulse(__data['time'], self_quarantine_start_30(),
                               self_quarantine_end_30() -
                               self_quarantine_start_30()) * self_quarantine_effectiveness_30()


@cache('run')
def social_distancing_start_20():
    """
    Real Name: b'social distancing start 20'
    Original Eqn: b'31'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 31


@cache('step')
def self_quarantine_policy_50():
    """
    Real Name: b'self quarantine policy 50'
    Original Eqn: b'1-PULSE(self quarantine start 50, self quarantine end 50-self quarantine start 50)*self quarantine effectiveness 50'
    Units: b'dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return 1 - functions.pulse(__data['time'], self_quarantine_start_50(),
                               self_quarantine_end_50() -
                               self_quarantine_start_50()) * self_quarantine_effectiveness_50()


@cache('step')
def self_quarantine_policy_60():
    """
    Real Name: b'self quarantine policy 60'
    Original Eqn: b'1-PULSE(self quarantine start 60, self quarantine end 60-self quarantine start 60)*self quarantine effectiveness 60'
    Units: b'dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return 1 - functions.pulse(__data['time'], self_quarantine_start_60(),
                               self_quarantine_end_60() -
                               self_quarantine_start_60()) * self_quarantine_effectiveness_60()


@cache('step')
def self_quarantine_policy_70():
    """
    Real Name: b'self quarantine policy 70'
    Original Eqn: b'1-PULSE(self quarantine start 70, self quarantine end 70-self quarantine start 70)*self quarantine effectiveness 70'
    Units: b'dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return 1 - functions.pulse(__data['time'], self_quarantine_start_70(),
                               self_quarantine_end_70() -
                               self_quarantine_start_70()) * self_quarantine_effectiveness_70()


@cache('step')
def self_quarantine_policy_80():
    """
    Real Name: b'self quarantine policy 80'
    Original Eqn: b'1-PULSE(self quarantine start 80, self quarantine end 80-self quarantine start 80)*self quarantine effectiveness 80'
    Units: b'dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return 1 - functions.pulse(__data['time'], self_quarantine_start_80(),
                               self_quarantine_end_80() -
                               self_quarantine_start_80()) * self_quarantine_effectiveness_80()


@cache('step')
def infection_rate_asymptomatic_60x00():
    """
    Real Name: b'infection rate asymptomatic 60x00'
    Original Eqn: b'Susceptible 00*Infected asymptomatic 00x60*contact infectivity asymptomatic 00x60*(social distancing policy SWITCH self 00 *social distancing policy 00+(1-social distancing policy SWITCH self 00))/non controlled pop 00x60'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_00() * infected_asymptomatic_00x60(
    ) * contact_infectivity_asymptomatic_00x60() * (
        social_distancing_policy_switch_self_00() * social_distancing_policy_00() +
        (1 - social_distancing_policy_switch_self_00())) / non_controlled_pop_00x60()


@cache('run')
def self_quarantine_policy_switch_self_00():
    """
    Real Name: b'self quarantine policy SWITCH self 00'
    Original Eqn: b'0'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('run')
def self_quarantine_policy_switch_self_10():
    """
    Real Name: b'self quarantine policy SWITCH self 10'
    Original Eqn: b'0'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('step')
def infected_asymptomatic_recovery_rate_00():
    """
    Real Name: b'infected asymptomatic recovery rate 00'
    Original Eqn: b'fraction of asymptomatic case development 00*Infected asymptomatic 00/(asymptomatic duration 00\\\\ +symptomatic duration 00)'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return fraction_of_asymptomatic_case_development_00() * infected_asymptomatic_00() / (
        asymptomatic_duration_00() + symptomatic_duration_00())


@cache('step')
def infected_asymptomatic_recovery_rate_10():
    """
    Real Name: b'infected asymptomatic recovery rate 10'
    Original Eqn: b'fraction of asymptomatic case development 10*Infected asymptomatic 10/(asymptomatic duration 10\\\\ +symptomatic duration 10)'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return fraction_of_asymptomatic_case_development_10() * infected_asymptomatic_10() / (
        asymptomatic_duration_10() + symptomatic_duration_10())


@cache('step')
def infected_asymptomatic_recovery_rate_20():
    """
    Real Name: b'infected asymptomatic recovery rate 20'
    Original Eqn: b'fraction of asymptomatic case development 20*Infected asymptomatic 20/(asymptomatic duration 20\\\\ +symptomatic duration 20)'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return fraction_of_asymptomatic_case_development_20() * infected_asymptomatic_20() / (
        asymptomatic_duration_20() + symptomatic_duration_20())


@cache('run')
def init_accumulated_cases_40():
    """
    Real Name: b'init accumulated cases 40'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('step')
def infected_asymptomatic_recovery_rate_40():
    """
    Real Name: b'infected asymptomatic recovery rate 40'
    Original Eqn: b'fraction of asymptomatic case development 40*Infected asymptomatic 40/(asymptomatic duration 40\\\\ +symptomatic duration 40)'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return fraction_of_asymptomatic_case_development_40() * infected_asymptomatic_40() / (
        asymptomatic_duration_40() + symptomatic_duration_40())


@cache('step')
def infection_rate_asymptomatic_70x00():
    """
    Real Name: b'infection rate asymptomatic 70x00'
    Original Eqn: b'Susceptible 00*Infected asymptomatic 00x70*contact infectivity asymptomatic 00x70*(social distancing policy SWITCH self 00 *social distancing policy 00+(1-social distancing policy SWITCH self 00))/non controlled pop 00x70'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_00() * infected_asymptomatic_00x70(
    ) * contact_infectivity_asymptomatic_00x70() * (
        social_distancing_policy_switch_self_00() * social_distancing_policy_00() +
        (1 - social_distancing_policy_switch_self_00())) / non_controlled_pop_00x70()


@cache('step')
def infection_rate_asymptomatic_70x10():
    """
    Real Name: b'infection rate asymptomatic 70x10'
    Original Eqn: b'Susceptible 10*Infected asymptomatic 10x70*contact infectivity asymptomatic 10x70*(social distancing policy SWITCH self 10 *social distancing policy 10+(1-social distancing policy SWITCH self 10))/non controlled pop 10x70'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_10() * infected_asymptomatic_10x70(
    ) * contact_infectivity_asymptomatic_10x70() * (
        social_distancing_policy_switch_self_10() * social_distancing_policy_10() +
        (1 - social_distancing_policy_switch_self_10())) / non_controlled_pop_10x70()


@cache('step')
def infection_rate_asymptomatic_70x20():
    """
    Real Name: b'infection rate asymptomatic 70x20'
    Original Eqn: b'Susceptible 20*Infected asymptomatic 20x70*contact infectivity asymptomatic 20x70*(social distancing policy SWITCH self 20 *social distancing policy 20+(1-social distancing policy SWITCH self 20))/non controlled pop 20x70'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_20() * infected_asymptomatic_20x70(
    ) * contact_infectivity_asymptomatic_20x70() * (
        social_distancing_policy_switch_self_20() * social_distancing_policy_20() +
        (1 - social_distancing_policy_switch_self_20())) / non_controlled_pop_20x70()


@cache('run')
def self_quarantine_start_00():
    """
    Real Name: b'self quarantine start 00'
    Original Eqn: b'21'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 21


@cache('run')
def self_quarantine_start_10():
    """
    Real Name: b'self quarantine start 10'
    Original Eqn: b'21'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 21


@cache('run')
def init_critical_cases_00():
    """
    Real Name: b'init Critical Cases 00'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('run')
def init_critical_cases_10():
    """
    Real Name: b'init Critical Cases 10'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('step')
def infected_critical_case_rate_20():
    """
    Real Name: b'infected critical case rate 20'
    Original Eqn: b'Infected symptomatic 20*fraction of critical cases 20/symptomatic duration 20'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_20() * fraction_of_critical_cases_20() / symptomatic_duration_20()


@cache('step')
def infected_critical_case_rate_30():
    """
    Real Name: b'infected critical case rate 30'
    Original Eqn: b'Infected symptomatic 30*fraction of critical cases 30/symptomatic duration 30'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_30() * fraction_of_critical_cases_30() / symptomatic_duration_30()


@cache('step')
def infected_critical_case_rate_40():
    """
    Real Name: b'infected critical case rate 40'
    Original Eqn: b'Infected symptomatic 40*fraction of critical cases 40/symptomatic duration 40'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_40() * fraction_of_critical_cases_40() / symptomatic_duration_40()


@cache('step')
def infection_rate_asymptomatic_80x20():
    """
    Real Name: b'infection rate asymptomatic 80x20'
    Original Eqn: b'Susceptible 20*Infected asymptomatic 20x80*contact infectivity asymptomatic 20x80*(social distancing policy SWITCH self 20 *social distancing policy 20+(1-social distancing policy SWITCH self 20))/non controlled pop 20x80'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_20() * infected_asymptomatic_20x80(
    ) * contact_infectivity_asymptomatic_20x80() * (
        social_distancing_policy_switch_self_20() * social_distancing_policy_20() +
        (1 - social_distancing_policy_switch_self_20())) / non_controlled_pop_20x80()


@cache('step')
def infection_rate_asymptomatic_80x30():
    """
    Real Name: b'infection rate asymptomatic 80x30'
    Original Eqn: b'Susceptible 30*Infected asymptomatic 30x80*contact infectivity asymptomatic 30x80*(social distancing policy SWITCH self 30 *social distancing policy 30+(1-social distancing policy SWITCH self 30))/non controlled pop 30x80'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_30() * infected_asymptomatic_30x80(
    ) * contact_infectivity_asymptomatic_30x80() * (
        social_distancing_policy_switch_self_30() * social_distancing_policy_30() +
        (1 - social_distancing_policy_switch_self_30())) / non_controlled_pop_30x80()


@cache('step')
def infection_rate_asymptomatic_80x40():
    """
    Real Name: b'infection rate asymptomatic 80x40'
    Original Eqn: b'Susceptible 40*Infected asymptomatic 40x80*contact infectivity asymptomatic 40x80*(social distancing policy SWITCH self 40 *social distancing policy 40+(1-social distancing policy SWITCH self 40))/non controlled pop 40x80'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_40() * infected_asymptomatic_40x80(
    ) * contact_infectivity_asymptomatic_40x80() * (
        social_distancing_policy_switch_self_40() * social_distancing_policy_40() +
        (1 - social_distancing_policy_switch_self_40())) / non_controlled_pop_40x80()


@cache('step')
def infected_symptomatic_40x60():
    """
    Real Name: b'Infected symptomatic 40x60'
    Original Eqn: b'Infected symptomatic 40+Infected symptomatic 60'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_40() + infected_symptomatic_60()


@cache('step')
def infection_rate_asymptomatic_40x50():
    """
    Real Name: b'infection rate asymptomatic 40x50'
    Original Eqn: b'contact infectivity asymptomatic 40x50*(social distancing policy SWITCH self 50*social distancing policy 50\\\\ +(1-social distancing policy SWITCH self 50))*Infected asymptomatic 40x50*Susceptible 50\\\\ /non controlled pop 40x50'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contact_infectivity_asymptomatic_40x50() * (
        social_distancing_policy_switch_self_50() * social_distancing_policy_50() +
        (1 - social_distancing_policy_switch_self_50())
    ) * infected_asymptomatic_40x50() * susceptible_50() / non_controlled_pop_40x50()


@cache('run')
def init_diseased_00():
    """
    Real Name: b'init Diseased 00'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('step')
def infected_symptomatic_00x10():
    """
    Real Name: b'Infected symptomatic 00x10'
    Original Eqn: b'Infected symptomatic 00+Infected symptomatic 10'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_00() + infected_symptomatic_10()


@cache('step')
def infected_symptomatic_00x20():
    """
    Real Name: b'Infected symptomatic 00x20'
    Original Eqn: b'Infected symptomatic 00+Infected symptomatic 20'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_00() + infected_symptomatic_20()


@cache('step')
def infected_symptomatic_00x30():
    """
    Real Name: b'Infected symptomatic 00x30'
    Original Eqn: b'Infected symptomatic 00+Infected symptomatic 30'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_00() + infected_symptomatic_30()


@cache('step')
def infected_symptomatic_00x40():
    """
    Real Name: b'Infected symptomatic 00x40'
    Original Eqn: b'Infected symptomatic 00+Infected symptomatic 40'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_00() + infected_symptomatic_40()


@cache('step')
def infection_rate_asymptomatic_10x00():
    """
    Real Name: b'infection rate asymptomatic 10x00'
    Original Eqn: b'Susceptible 00*Infected asymptomatic 00x10*contact infectivity asymptomatic 00x10*(social distancing policy SWITCH self 00 *social distancing policy 00+(1-social distancing policy SWITCH self 00))/non controlled pop 00x10'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_00() * infected_asymptomatic_00x10(
    ) * contact_infectivity_asymptomatic_00x10() * (
        social_distancing_policy_switch_self_00() * social_distancing_policy_00() +
        (1 - social_distancing_policy_switch_self_00())) / non_controlled_pop_00x10()


@cache('step')
def infection_rate_symptomatic_20x40():
    """
    Real Name: b'infection rate symptomatic 20x40'
    Original Eqn: b'Susceptible 40*Infected symptomatic 20x40*contact infectivity symptomatic 20x40*(self quarantine policy SWITCH self 40\\\\ *self quarantine policy 40+(1-self quarantine policy SWITCH self 40))/non controlled pop 20x40'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_40() * infected_symptomatic_20x40() * contact_infectivity_symptomatic_20x40(
    ) * (self_quarantine_policy_switch_self_40() * self_quarantine_policy_40() +
         (1 - self_quarantine_policy_switch_self_40())) / non_controlled_pop_20x40()


@cache('step')
def infected_symptomatic_00x70():
    """
    Real Name: b'Infected symptomatic 00x70'
    Original Eqn: b'Infected symptomatic 00+Infected symptomatic 70'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_00() + infected_symptomatic_70()


@cache('step')
def infected_symptomatic_00x80():
    """
    Real Name: b'Infected symptomatic 00x80'
    Original Eqn: b'Infected symptomatic 00+Infected symptomatic 80'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_00() + infected_symptomatic_80()


@cache('step')
def infected_symptomatic_10():
    """
    Real Name: b'Infected symptomatic 10'
    Original Eqn: b'INTEG ( symptomatic rate 10-infected critical case rate 10-infected symptomatic recovery rate 10\\\\ -isolation rate symptomatic 10, init Infected symptomatic 10)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_infected_symptomatic_10()


@cache('step')
def infected_symptomatic_10x20():
    """
    Real Name: b'Infected symptomatic 10x20'
    Original Eqn: b'Infected symptomatic 10+Infected symptomatic 20'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_10() + infected_symptomatic_20()


@cache('step')
def infected_symptomatic_10x30():
    """
    Real Name: b'Infected symptomatic 10x30'
    Original Eqn: b'Infected symptomatic 10+Infected symptomatic 30'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_10() + infected_symptomatic_30()


@cache('step')
def infected_symptomatic_10x40():
    """
    Real Name: b'Infected symptomatic 10x40'
    Original Eqn: b'Infected symptomatic 10+Infected symptomatic 40'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_10() + infected_symptomatic_40()


@cache('step')
def infected_symptomatic_10x50():
    """
    Real Name: b'Infected symptomatic 10x50'
    Original Eqn: b'Infected symptomatic 10+Infected symptomatic 50'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_10() + infected_symptomatic_50()


@cache('run')
def social_distancing_end_50():
    """
    Real Name: b'social distancing end 50'
    Original Eqn: b'50'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 50


@cache('step')
def infection_rate_asymptomatic_20x30():
    """
    Real Name: b'infection rate asymptomatic 20x30'
    Original Eqn: b'contact infectivity asymptomatic 20x30*(social distancing policy SWITCH self 30*social distancing policy 30\\\\ +(1-social distancing policy SWITCH self 30))*Infected asymptomatic 20x30*Susceptible 30\\\\ /non controlled pop 20x30'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contact_infectivity_asymptomatic_20x30() * (
        social_distancing_policy_switch_self_30() * social_distancing_policy_30() +
        (1 - social_distancing_policy_switch_self_30())
    ) * infected_asymptomatic_20x30() * susceptible_30() / non_controlled_pop_20x30()


@cache('run')
def social_distancing_end_70():
    """
    Real Name: b'social distancing end 70'
    Original Eqn: b'50'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 50


@cache('run')
def social_distancing_end_80():
    """
    Real Name: b'social distancing end 80'
    Original Eqn: b'50'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 50


@cache('step')
def infected_symptomatic_20x40():
    """
    Real Name: b'Infected symptomatic 20x40'
    Original Eqn: b'Infected symptomatic 20+Infected symptomatic 40'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_20() + infected_symptomatic_40()


@cache('step')
def infected_symptomatic_20x50():
    """
    Real Name: b'Infected symptomatic 20x50'
    Original Eqn: b'Infected symptomatic 20+Infected symptomatic 50'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_20() + infected_symptomatic_50()


@cache('step')
def infected_symptomatic_20x60():
    """
    Real Name: b'Infected symptomatic 20x60'
    Original Eqn: b'Infected symptomatic 20+Infected symptomatic 60'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_20() + infected_symptomatic_60()


@cache('step')
def infected_symptomatic_20x70():
    """
    Real Name: b'Infected symptomatic 20x70'
    Original Eqn: b'Infected symptomatic 20+Infected symptomatic 70'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_20() + infected_symptomatic_70()


@cache('step')
def infected_symptomatic_20x80():
    """
    Real Name: b'Infected symptomatic 20x80'
    Original Eqn: b'Infected symptomatic 20+Infected symptomatic 80'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_20() + infected_symptomatic_80()


@cache('run')
def init_infected_symptomatic_40():
    """
    Real Name: b'init Infected symptomatic 40'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('step')
def social_distancing_policy_60():
    """
    Real Name: b'social distancing policy 60'
    Original Eqn: b'1-PULSE(social distancing start 60, social distancing end 60-social distancing start 60\\\\ )*social distancing effectiveness 60'
    Units: b'dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return 1 - functions.pulse(__data['time'], social_distancing_start_60(),
                               social_distancing_end_60() - social_distancing_start_60()
                               ) * social_distancing_effectiveness_60()


@cache('step')
def social_distancing_policy_70():
    """
    Real Name: b'social distancing policy 70'
    Original Eqn: b'1-PULSE(social distancing start 70, social distancing end 70-social distancing start 70\\\\ )*social distancing effectiveness 70'
    Units: b'dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return 1 - functions.pulse(__data['time'], social_distancing_start_70(),
                               social_distancing_end_70() - social_distancing_start_70()
                               ) * social_distancing_effectiveness_70()


@cache('step')
def social_distancing_policy_80():
    """
    Real Name: b'social distancing policy 80'
    Original Eqn: b'1-PULSE(social distancing start 80, social distancing end 80-social distancing start 80\\\\ )*social distancing effectiveness 80'
    Units: b'dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return 1 - functions.pulse(__data['time'], social_distancing_start_80(),
                               social_distancing_end_80() - social_distancing_start_80()
                               ) * social_distancing_effectiveness_80()


@cache('step')
def infected_symptomatic_30x70():
    """
    Real Name: b'Infected symptomatic 30x70'
    Original Eqn: b'Infected symptomatic 30+Infected symptomatic 70'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_30() + infected_symptomatic_70()


@cache('step')
def infected_symptomatic_30x80():
    """
    Real Name: b'Infected symptomatic 30x80'
    Original Eqn: b'Infected symptomatic 30+Infected symptomatic 80'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_30() + infected_symptomatic_80()


@cache('step')
def infected_symptomatic_40():
    """
    Real Name: b'Infected symptomatic 40'
    Original Eqn: b'INTEG ( symptomatic rate 40-infected critical case rate 40-infected symptomatic recovery rate 40\\\\ -isolation rate symptomatic 40, init Infected symptomatic 40)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_infected_symptomatic_40()


@cache('step')
def infected_symptomatic_40x50():
    """
    Real Name: b'Infected symptomatic 40x50'
    Original Eqn: b'Infected symptomatic 40+Infected symptomatic 50'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_40() + infected_symptomatic_50()


@cache('step')
def infection_rate_asymptomatic_40x30():
    """
    Real Name: b'infection rate asymptomatic 40x30'
    Original Eqn: b'Susceptible 30*Infected asymptomatic 30x40*contact infectivity asymptomatic 30x40*(social distancing policy SWITCH self 30 *social distancing policy 30+(1-social distancing policy SWITCH self 30))/non controlled pop 30x40'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_30() * infected_asymptomatic_30x40(
    ) * contact_infectivity_asymptomatic_30x40() * (
        social_distancing_policy_switch_self_30() * social_distancing_policy_30() +
        (1 - social_distancing_policy_switch_self_30())) / non_controlled_pop_30x40()


@cache('step')
def infection_rate_symptomatic_10x50():
    """
    Real Name: b'infection rate symptomatic 10x50'
    Original Eqn: b'Susceptible 50*Infected symptomatic 10x50*contact infectivity symptomatic 10x50*(self quarantine policy SWITCH self 50\\\\ *self quarantine policy 50+(1-self quarantine policy SWITCH self 50))/non controlled pop 10x50'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_50() * infected_symptomatic_10x50() * contact_infectivity_symptomatic_10x50(
    ) * (self_quarantine_policy_switch_self_50() * self_quarantine_policy_50() +
         (1 - self_quarantine_policy_switch_self_50())) / non_controlled_pop_10x50()


@cache('step')
def infected_symptomatic_40x80():
    """
    Real Name: b'Infected symptomatic 40x80'
    Original Eqn: b'Infected symptomatic 40+Infected symptomatic 80'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_40() + infected_symptomatic_80()


@cache('step')
def infection_rate_symptomatic_10x70():
    """
    Real Name: b'infection rate symptomatic 10x70'
    Original Eqn: b'Susceptible 70*Infected symptomatic 10x70*contact infectivity symptomatic 10x70*(self quarantine policy SWITCH self 70\\\\ *self quarantine policy 70+(1-self quarantine policy SWITCH self 70))/non controlled pop 10x70'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_70() * infected_symptomatic_10x70() * contact_infectivity_symptomatic_10x70(
    ) * (self_quarantine_policy_switch_self_70() * self_quarantine_policy_70() +
         (1 - self_quarantine_policy_switch_self_70())) / non_controlled_pop_10x70()


@cache('step')
def infection_rate_symptomatic_10x80():
    """
    Real Name: b'infection rate symptomatic 10x80'
    Original Eqn: b'Susceptible 80*Infected symptomatic 10x80*contact infectivity symptomatic 10x80*(self quarantine policy SWITCH self 80\\\\ *self quarantine policy 80+(1-self quarantine policy SWITCH self 80))/non controlled pop 10x80'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_80() * infected_symptomatic_10x80() * contact_infectivity_symptomatic_10x80(
    ) * (self_quarantine_policy_switch_self_80() * self_quarantine_policy_80() +
         (1 - self_quarantine_policy_switch_self_80())) / non_controlled_pop_10x80()


@cache('step')
def infection_rate_symptomatic_20x00():
    """
    Real Name: b'infection rate symptomatic 20x00'
    Original Eqn: b'Susceptible 00*Infected symptomatic 00x20*contact infectivity symptomatic 00x20*(self quarantine policy SWITCH self 00\\\\ * self quarantine policy 00+(1-self quarantine policy SWITCH self 00))/non controlled pop 00x20'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_00() * infected_symptomatic_00x20() * contact_infectivity_symptomatic_00x20(
    ) * (self_quarantine_policy_switch_self_00() * self_quarantine_policy_00() +
         (1 - self_quarantine_policy_switch_self_00())) / non_controlled_pop_00x20()


@cache('run')
def social_distancing_start_00():
    """
    Real Name: b'social distancing start 00'
    Original Eqn: b'31'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 31


@cache('run')
def social_distancing_start_10():
    """
    Real Name: b'social distancing start 10'
    Original Eqn: b'31'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 31


@cache('run')
def init_recovered_00():
    """
    Real Name: b'init Recovered 00'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('run')
def social_distancing_start_30():
    """
    Real Name: b'social distancing start 30'
    Original Eqn: b'31'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 31


@cache('run')
def social_distancing_start_40():
    """
    Real Name: b'social distancing start 40'
    Original Eqn: b'31'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 31


@cache('run')
def init_recovered_30():
    """
    Real Name: b'init Recovered 30'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('run')
def init_recovered_40():
    """
    Real Name: b'init Recovered 40'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('step')
def infection_rate_symptomatic_30x00():
    """
    Real Name: b'infection rate symptomatic 30x00'
    Original Eqn: b'Susceptible 00*Infected symptomatic 00x30*contact infectivity symptomatic 00x30*(self quarantine policy SWITCH self 00\\\\ * self quarantine policy 00+(1-self quarantine policy SWITCH self 00))/non controlled pop 00x30'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_00() * infected_symptomatic_00x30() * contact_infectivity_symptomatic_00x30(
    ) * (self_quarantine_policy_switch_self_00() * self_quarantine_policy_00() +
         (1 - self_quarantine_policy_switch_self_00())) / non_controlled_pop_00x30()


@cache('step')
def infected_symptomatic_recovery_rate_00():
    """
    Real Name: b'infected symptomatic recovery rate 00'
    Original Eqn: b'Infected symptomatic 00*(1-fraction of critical cases 00)/symptomatic duration 00'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_00() * (
        1 - fraction_of_critical_cases_00()) / symptomatic_duration_00()


@cache('step')
def infection_rate_asymptomatic_60x20():
    """
    Real Name: b'infection rate asymptomatic 60x20'
    Original Eqn: b'Susceptible 20*Infected asymptomatic 20x60*contact infectivity asymptomatic 20x60*(social distancing policy SWITCH self 20 *social distancing policy 20+(1-social distancing policy SWITCH self 20))/non controlled pop 20x60'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_20() * infected_asymptomatic_20x60(
    ) * contact_infectivity_asymptomatic_20x60() * (
        social_distancing_policy_switch_self_20() * social_distancing_policy_20() +
        (1 - social_distancing_policy_switch_self_20())) / non_controlled_pop_20x60()


@cache('step')
def infection_rate_asymptomatic_60x30():
    """
    Real Name: b'infection rate asymptomatic 60x30'
    Original Eqn: b'Susceptible 30*Infected asymptomatic 30x60*contact infectivity asymptomatic 30x60*(social distancing policy SWITCH self 30 *social distancing policy 30+(1-social distancing policy SWITCH self 30))/non controlled pop 30x60'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_30() * infected_asymptomatic_30x60(
    ) * contact_infectivity_asymptomatic_30x60() * (
        social_distancing_policy_switch_self_30() * social_distancing_policy_30() +
        (1 - social_distancing_policy_switch_self_30())) / non_controlled_pop_30x60()


@cache('step')
def susceptible_00():
    """
    Real Name: b'Susceptible 00'
    Original Eqn: b'INTEG ( deimmunization rate 00-infection rate 00, init Susceptible 00)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_susceptible_00()


@cache('step')
def infected_symptomatic_recovery_rate_40():
    """
    Real Name: b'infected symptomatic recovery rate 40'
    Original Eqn: b'Infected symptomatic 40*(1-fraction of critical cases 40)/symptomatic duration 40'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_40() * (
        1 - fraction_of_critical_cases_40()) / symptomatic_duration_40()


@cache('step')
def susceptible_30():
    """
    Real Name: b'Susceptible 30'
    Original Eqn: b'INTEG ( deimmunization rate 30-infection rate 30, init Susceptible 30)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_susceptible_30()


@cache('step')
def susceptible_40():
    """
    Real Name: b'Susceptible 40'
    Original Eqn: b'INTEG ( deimmunization rate 40-infection rate 40, init Susceptible 40)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_susceptible_40()


@cache('run')
def init_susceptible_30():
    """
    Real Name: b'init Susceptible 30'
    Original Eqn: b'8e+06'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 8e+06


@cache('run')
def init_susceptible_40():
    """
    Real Name: b'init Susceptible 40'
    Original Eqn: b'8e+06'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 8e+06


@cache('step')
def infection_rate_symptomatic_40x20():
    """
    Real Name: b'infection rate symptomatic 40x20'
    Original Eqn: b'Susceptible 20*Infected symptomatic 20x40*contact infectivity symptomatic 20x40*(self quarantine policy SWITCH self 20\\\\ * self quarantine policy 20+(1-self quarantine policy SWITCH self 20))/non controlled pop 20x40'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_20() * infected_symptomatic_20x40() * contact_infectivity_symptomatic_20x40(
    ) * (self_quarantine_policy_switch_self_20() * self_quarantine_policy_20() +
         (1 - self_quarantine_policy_switch_self_20())) / non_controlled_pop_20x40()


@cache('step')
def infection_rate_00():
    """
    Real Name: b'infection rate 00'
    Original Eqn: b'total infection rate 00+first infection 00'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return total_infection_rate_00() + first_infection_00()


@cache('step')
def infection_rate_10():
    """
    Real Name: b'infection rate 10'
    Original Eqn: b'total infection rate 10+first infection 10'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return total_infection_rate_10() + first_infection_10()


@cache('step')
def infection_rate_asymptomatic_30x40():
    """
    Real Name: b'infection rate asymptomatic 30x40'
    Original Eqn: b'contact infectivity asymptomatic 30x40*(social distancing policy SWITCH self 40*social distancing policy 40\\\\ +(1-social distancing policy SWITCH self 40))*Infected asymptomatic 30x40*Susceptible 40\\\\ /non controlled pop 30x40'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contact_infectivity_asymptomatic_30x40() * (
        social_distancing_policy_switch_self_40() * social_distancing_policy_40() +
        (1 - social_distancing_policy_switch_self_40())
    ) * infected_asymptomatic_30x40() * susceptible_40() / non_controlled_pop_30x40()


@cache('run')
def symptomatic_contact_fraction_00():
    """
    Real Name: b'symptomatic contact fraction 00'
    Original Eqn: b'0.5'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.5


@cache('step')
def infection_rate_40():
    """
    Real Name: b'infection rate 40'
    Original Eqn: b'total infection rate 40+first infection 40'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return total_infection_rate_40() + first_infection_40()


@cache('run')
def symptomatic_contact_fraction_30():
    """
    Real Name: b'symptomatic contact fraction 30'
    Original Eqn: b'0.5'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.5


@cache('run')
def symptomatic_contact_fraction_40():
    """
    Real Name: b'symptomatic contact fraction 40'
    Original Eqn: b'0.5'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.5


@cache('step')
def infection_rate_asymptomatic_40x00():
    """
    Real Name: b'infection rate asymptomatic 40x00'
    Original Eqn: b'Susceptible 00*Infected asymptomatic 00x40*contact infectivity asymptomatic 00x40*(social distancing policy SWITCH self 00 *social distancing policy 00+(1-social distancing policy SWITCH self 00))/non controlled pop 00x40'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_00() * infected_asymptomatic_00x40(
    ) * contact_infectivity_asymptomatic_00x40() * (
        social_distancing_policy_switch_self_00() * social_distancing_policy_00() +
        (1 - social_distancing_policy_switch_self_00())) / non_controlled_pop_00x40()


@cache('step')
def infection_rate_asymptomatic_40x10():
    """
    Real Name: b'infection rate asymptomatic 40x10'
    Original Eqn: b'Susceptible 10*Infected asymptomatic 10x40*contact infectivity asymptomatic 10x40*(social distancing policy SWITCH self 10 *social distancing policy 10+(1-social distancing policy SWITCH self 10))/non controlled pop 10x40'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_10() * infected_asymptomatic_10x40(
    ) * contact_infectivity_asymptomatic_10x40() * (
        social_distancing_policy_switch_self_10() * social_distancing_policy_10() +
        (1 - social_distancing_policy_switch_self_10())) / non_controlled_pop_10x40()


@cache('step')
def infection_rate_asymptomatic_00x10():
    """
    Real Name: b'infection rate asymptomatic 00x10'
    Original Eqn: b'contact infectivity asymptomatic 00x10*(social distancing policy SWITCH self 10*social distancing policy 10\\\\ +(1-social distancing policy SWITCH self 10))*Infected asymptomatic 00x10*Susceptible 10\\\\ /non controlled pop 00x10'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contact_infectivity_asymptomatic_00x10() * (
        social_distancing_policy_switch_self_10() * social_distancing_policy_10() +
        (1 - social_distancing_policy_switch_self_10())
    ) * infected_asymptomatic_00x10() * susceptible_10() / non_controlled_pop_00x10()


@cache('step')
def infection_rate_symptomatic_10x40():
    """
    Real Name: b'infection rate symptomatic 10x40'
    Original Eqn: b'Susceptible 40*Infected symptomatic 10x40*contact infectivity symptomatic 10x40*(self quarantine policy SWITCH self 40\\\\ *self quarantine policy 40+(1-self quarantine policy SWITCH self 40))/non controlled pop 10x40'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_40() * infected_symptomatic_10x40() * contact_infectivity_symptomatic_10x40(
    ) * (self_quarantine_policy_switch_self_40() * self_quarantine_policy_40() +
         (1 - self_quarantine_policy_switch_self_40())) / non_controlled_pop_10x40()


@cache('run')
def self_quarantine_end_60():
    """
    Real Name: b'self quarantine end 60'
    Original Eqn: b'50'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 50


@cache('step')
def infection_rate_asymptomatic_40x60():
    """
    Real Name: b'infection rate asymptomatic 40x60'
    Original Eqn: b'contact infectivity asymptomatic 40x60*(social distancing policy SWITCH self 60*social distancing policy 60\\\\ +(1-social distancing policy SWITCH self 60))*Infected asymptomatic 40x60*Susceptible 60\\\\ /non controlled pop 40x60'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contact_infectivity_asymptomatic_40x60() * (
        social_distancing_policy_switch_self_60() * social_distancing_policy_60() +
        (1 - social_distancing_policy_switch_self_60())
    ) * infected_asymptomatic_40x60() * susceptible_60() / non_controlled_pop_40x60()


@cache('run')
def symptomatic_duration_00():
    """
    Real Name: b'symptomatic duration 00'
    Original Eqn: b'5'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 5


@cache('step')
def infection_rate_asymptomatic_00x60():
    """
    Real Name: b'infection rate asymptomatic 00x60'
    Original Eqn: b'contact infectivity asymptomatic 00x60*(social distancing policy SWITCH self 60*social distancing policy 60\\\\ +(1-social distancing policy SWITCH self 60))*Infected asymptomatic 00x60*Susceptible 60\\\\ /non controlled pop 00x60'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contact_infectivity_asymptomatic_00x60() * (
        social_distancing_policy_switch_self_60() * social_distancing_policy_60() +
        (1 - social_distancing_policy_switch_self_60())
    ) * infected_asymptomatic_00x60() * susceptible_60() / non_controlled_pop_00x60()


@cache('step')
def infection_rate_asymptomatic_00x70():
    """
    Real Name: b'infection rate asymptomatic 00x70'
    Original Eqn: b'contact infectivity asymptomatic 00x70*(social distancing policy SWITCH self 70*social distancing policy 70\\\\ +(1-social distancing policy SWITCH self 70))*Infected asymptomatic 00x70*Susceptible 70\\\\ /non controlled pop 00x70'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contact_infectivity_asymptomatic_00x70() * (
        social_distancing_policy_switch_self_70() * social_distancing_policy_70() +
        (1 - social_distancing_policy_switch_self_70())
    ) * infected_asymptomatic_00x70() * susceptible_70() / non_controlled_pop_00x70()


@cache('step')
def infection_rate_asymptomatic_00x80():
    """
    Real Name: b'infection rate asymptomatic 00x80'
    Original Eqn: b'contact infectivity asymptomatic 00x80*(social distancing policy SWITCH self 80*social distancing policy 80\\\\ +(1-social distancing policy SWITCH self 80))*Infected asymptomatic 00x80*Susceptible 80\\\\ /non controlled pop 00x80'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contact_infectivity_asymptomatic_00x80() * (
        social_distancing_policy_switch_self_80() * social_distancing_policy_80() +
        (1 - social_distancing_policy_switch_self_80())
    ) * infected_asymptomatic_00x80() * susceptible_80() / non_controlled_pop_00x80()


@cache('step')
def infection_rate_symptomatic_60x40():
    """
    Real Name: b'infection rate symptomatic 60x40'
    Original Eqn: b'Susceptible 40*Infected symptomatic 40x60*contact infectivity symptomatic 40x60*(self quarantine policy SWITCH self 40\\\\ * self quarantine policy 40+(1-self quarantine policy SWITCH self 40))/non controlled pop 40x60'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_40() * infected_symptomatic_40x60() * contact_infectivity_symptomatic_40x60(
    ) * (self_quarantine_policy_switch_self_40() * self_quarantine_policy_40() +
         (1 - self_quarantine_policy_switch_self_40())) / non_controlled_pop_40x60()


@cache('step')
def infection_rate_asymptomatic_30x20():
    """
    Real Name: b'infection rate asymptomatic 30x20'
    Original Eqn: b'Susceptible 20*Infected asymptomatic 20x30*contact infectivity asymptomatic 20x30*(social distancing policy SWITCH self 20 *social distancing policy 20+(1-social distancing policy SWITCH self 20))/non controlled pop 20x30'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_20() * infected_asymptomatic_20x30(
    ) * contact_infectivity_asymptomatic_20x30() * (
        social_distancing_policy_switch_self_20() * social_distancing_policy_20() +
        (1 - social_distancing_policy_switch_self_20())) / non_controlled_pop_20x30()


@cache('step')
def infection_rate_asymptomatic_10x30():
    """
    Real Name: b'infection rate asymptomatic 10x30'
    Original Eqn: b'contact infectivity asymptomatic 10x30*(social distancing policy SWITCH self 30*social distancing policy 30\\\\ +(1-social distancing policy SWITCH self 30))*Infected asymptomatic 10x30*Susceptible 30\\\\ /non controlled pop 10x30'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contact_infectivity_asymptomatic_10x30() * (
        social_distancing_policy_switch_self_30() * social_distancing_policy_30() +
        (1 - social_distancing_policy_switch_self_30())
    ) * infected_asymptomatic_10x30() * susceptible_30() / non_controlled_pop_10x30()


@cache('step')
def infection_rate_asymptomatic_10x40():
    """
    Real Name: b'infection rate asymptomatic 10x40'
    Original Eqn: b'contact infectivity asymptomatic 10x40*(social distancing policy SWITCH self 40*social distancing policy 40\\\\ +(1-social distancing policy SWITCH self 40))*Infected asymptomatic 10x40*Susceptible 40\\\\ /non controlled pop 10x40'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contact_infectivity_asymptomatic_10x40() * (
        social_distancing_policy_switch_self_40() * social_distancing_policy_40() +
        (1 - social_distancing_policy_switch_self_40())
    ) * infected_asymptomatic_10x40() * susceptible_40() / non_controlled_pop_10x40()


@cache('step')
def infection_rate_asymptomatic_10x50():
    """
    Real Name: b'infection rate asymptomatic 10x50'
    Original Eqn: b'contact infectivity asymptomatic 10x50*(social distancing policy SWITCH self 50*social distancing policy 50\\\\ +(1-social distancing policy SWITCH self 50))*Infected asymptomatic 10x50*Susceptible 50\\\\ /non controlled pop 10x50'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contact_infectivity_asymptomatic_10x50() * (
        social_distancing_policy_switch_self_50() * social_distancing_policy_50() +
        (1 - social_distancing_policy_switch_self_50())
    ) * infected_asymptomatic_10x50() * susceptible_50() / non_controlled_pop_10x50()


@cache('step')
def infection_rate_asymptomatic_10x60():
    """
    Real Name: b'infection rate asymptomatic 10x60'
    Original Eqn: b'contact infectivity asymptomatic 10x60*(social distancing policy SWITCH self 60*social distancing policy 60\\\\ +(1-social distancing policy SWITCH self 60))*Infected asymptomatic 10x60*Susceptible 60\\\\ /non controlled pop 10x60'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contact_infectivity_asymptomatic_10x60() * (
        social_distancing_policy_switch_self_60() * social_distancing_policy_60() +
        (1 - social_distancing_policy_switch_self_60())
    ) * infected_asymptomatic_10x60() * susceptible_60() / non_controlled_pop_10x60()


@cache('step')
def infection_rate_asymptomatic_10x70():
    """
    Real Name: b'infection rate asymptomatic 10x70'
    Original Eqn: b'contact infectivity asymptomatic 10x70*(social distancing policy SWITCH self 70*social distancing policy 70\\\\ +(1-social distancing policy SWITCH self 70))*Infected asymptomatic 10x70*Susceptible 70\\\\ /non controlled pop 10x70'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contact_infectivity_asymptomatic_10x70() * (
        social_distancing_policy_switch_self_70() * social_distancing_policy_70() +
        (1 - social_distancing_policy_switch_self_70())
    ) * infected_asymptomatic_10x70() * susceptible_70() / non_controlled_pop_10x70()


@cache('step')
def infection_rate_asymptomatic_10x80():
    """
    Real Name: b'infection rate asymptomatic 10x80'
    Original Eqn: b'contact infectivity asymptomatic 10x80*(social distancing policy SWITCH self 80*social distancing policy 80\\\\ +(1-social distancing policy SWITCH self 80))*Infected asymptomatic 10x80*Susceptible 80\\\\ /non controlled pop 10x80'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contact_infectivity_asymptomatic_10x80() * (
        social_distancing_policy_switch_self_80() * social_distancing_policy_80() +
        (1 - social_distancing_policy_switch_self_80())
    ) * infected_asymptomatic_10x80() * susceptible_80() / non_controlled_pop_10x80()


@cache('step')
def infection_rate_asymptomatic_20x00():
    """
    Real Name: b'infection rate asymptomatic 20x00'
    Original Eqn: b'Susceptible 00*Infected asymptomatic 00x20*contact infectivity asymptomatic 00x20*(social distancing policy SWITCH self 00 *social distancing policy 00+(1-social distancing policy SWITCH self 00))/non controlled pop 00x20'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_00() * infected_asymptomatic_00x20(
    ) * contact_infectivity_asymptomatic_00x20() * (
        social_distancing_policy_switch_self_00() * social_distancing_policy_00() +
        (1 - social_distancing_policy_switch_self_00())) / non_controlled_pop_00x20()


@cache('step')
def infection_rate_asymptomatic_20x10():
    """
    Real Name: b'infection rate asymptomatic 20x10'
    Original Eqn: b'Susceptible 10*Infected asymptomatic 10x20*contact infectivity asymptomatic 10x20*(social distancing policy SWITCH self 10 *social distancing policy 10+(1-social distancing policy SWITCH self 10))/non controlled pop 10x20'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_10() * infected_asymptomatic_10x20(
    ) * contact_infectivity_asymptomatic_10x20() * (
        social_distancing_policy_switch_self_10() * social_distancing_policy_10() +
        (1 - social_distancing_policy_switch_self_10())) / non_controlled_pop_10x20()


@cache('step')
def symptomatic_rate_40():
    """
    Real Name: b'symptomatic rate 40'
    Original Eqn: b'Infected asymptomatic 40/asymptomatic duration 40*(1-fraction of asymptomatic case development 40\\\\ )'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic_40() / asymptomatic_duration_40() * (
        1 - fraction_of_asymptomatic_case_development_40())


@cache('run')
def self_quarantine_policy_switch_self_30():
    """
    Real Name: b'self quarantine policy SWITCH self 30'
    Original Eqn: b'0'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('step')
def infection_rate_asymptomatic_20x50():
    """
    Real Name: b'infection rate asymptomatic 20x50'
    Original Eqn: b'contact infectivity asymptomatic 20x50*(social distancing policy SWITCH self 50*social distancing policy 50\\\\ +(1-social distancing policy SWITCH self 50))*Infected asymptomatic 20x50*Susceptible 50\\\\ /non controlled pop 20x50'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contact_infectivity_asymptomatic_20x50() * (
        social_distancing_policy_switch_self_50() * social_distancing_policy_50() +
        (1 - social_distancing_policy_switch_self_50())
    ) * infected_asymptomatic_20x50() * susceptible_50() / non_controlled_pop_20x50()


@cache('step')
def infection_rate_asymptomatic_20x60():
    """
    Real Name: b'infection rate asymptomatic 20x60'
    Original Eqn: b'contact infectivity asymptomatic 20x60*(social distancing policy SWITCH self 60*social distancing policy 60\\\\ +(1-social distancing policy SWITCH self 60))*Infected asymptomatic 20x60*Susceptible 60\\\\ /non controlled pop 20x60'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contact_infectivity_asymptomatic_20x60() * (
        social_distancing_policy_switch_self_60() * social_distancing_policy_60() +
        (1 - social_distancing_policy_switch_self_60())
    ) * infected_asymptomatic_20x60() * susceptible_60() / non_controlled_pop_20x60()


@cache('step')
def infection_rate_asymptomatic_20x70():
    """
    Real Name: b'infection rate asymptomatic 20x70'
    Original Eqn: b'contact infectivity asymptomatic 20x70*(social distancing policy SWITCH self 70*social distancing policy 70\\\\ +(1-social distancing policy SWITCH self 70))*Infected asymptomatic 20x70*Susceptible 70\\\\ /non controlled pop 20x70'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contact_infectivity_asymptomatic_20x70() * (
        social_distancing_policy_switch_self_70() * social_distancing_policy_70() +
        (1 - social_distancing_policy_switch_self_70())
    ) * infected_asymptomatic_20x70() * susceptible_70() / non_controlled_pop_20x70()


@cache('step')
def infection_rate_asymptomatic_20x80():
    """
    Real Name: b'infection rate asymptomatic 20x80'
    Original Eqn: b'contact infectivity asymptomatic 20x80*(social distancing policy SWITCH self 80*social distancing policy 80\\\\ +(1-social distancing policy SWITCH self 80))*Infected asymptomatic 20x80*Susceptible 80\\\\ /non controlled pop 20x80'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contact_infectivity_asymptomatic_20x80() * (
        social_distancing_policy_switch_self_80() * social_distancing_policy_80() +
        (1 - social_distancing_policy_switch_self_80())
    ) * infected_asymptomatic_20x80() * susceptible_80() / non_controlled_pop_20x80()


@cache('step')
def infection_rate_asymptomatic_30x00():
    """
    Real Name: b'infection rate asymptomatic 30x00'
    Original Eqn: b'Susceptible 00*Infected asymptomatic 00x30*contact infectivity asymptomatic 00x30*(social distancing policy SWITCH self 00 *social distancing policy 00+(1-social distancing policy SWITCH self 00))/non controlled pop 00x30'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_00() * infected_asymptomatic_00x30(
    ) * contact_infectivity_asymptomatic_00x30() * (
        social_distancing_policy_switch_self_00() * social_distancing_policy_00() +
        (1 - social_distancing_policy_switch_self_00())) / non_controlled_pop_00x30()


@cache('step')
def infection_rate_asymptomatic_30x10():
    """
    Real Name: b'infection rate asymptomatic 30x10'
    Original Eqn: b'Susceptible 10*Infected asymptomatic 10x30*contact infectivity asymptomatic 10x30*(social distancing policy SWITCH self 10 *social distancing policy 10+(1-social distancing policy SWITCH self 10))/non controlled pop 10x30'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_10() * infected_asymptomatic_10x30(
    ) * contact_infectivity_asymptomatic_10x30() * (
        social_distancing_policy_switch_self_10() * social_distancing_policy_10() +
        (1 - social_distancing_policy_switch_self_10())) / non_controlled_pop_10x30()


@cache('step')
def infection_rate_symptomatic_40x50():
    """
    Real Name: b'infection rate symptomatic 40x50'
    Original Eqn: b'Susceptible 50*Infected symptomatic 40x50*contact infectivity symptomatic 40x50*(self quarantine policy SWITCH self 50\\\\ *self quarantine policy 50+(1-self quarantine policy SWITCH self 50))/non controlled pop 40x50'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_50() * infected_symptomatic_40x50() * contact_infectivity_symptomatic_40x50(
    ) * (self_quarantine_policy_switch_self_50() * self_quarantine_policy_50() +
         (1 - self_quarantine_policy_switch_self_50())) / non_controlled_pop_40x50()


@cache('step')
def infection_rate_symptomatic_00x40():
    """
    Real Name: b'infection rate symptomatic 00x40'
    Original Eqn: b'Susceptible 40*Infected symptomatic 00x40*contact infectivity symptomatic 00x40*(self quarantine policy SWITCH self 40\\\\ *self quarantine policy 40+(1-self quarantine policy SWITCH self 40))/non controlled pop 00x40'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_40() * infected_symptomatic_00x40() * contact_infectivity_symptomatic_00x40(
    ) * (self_quarantine_policy_switch_self_40() * self_quarantine_policy_40() +
         (1 - self_quarantine_policy_switch_self_40())) / non_controlled_pop_00x40()


@cache('step')
def infection_rate_asymptomatic_30x50():
    """
    Real Name: b'infection rate asymptomatic 30x50'
    Original Eqn: b'contact infectivity asymptomatic 30x50*(social distancing policy SWITCH self 50*social distancing policy 50\\\\ +(1-social distancing policy SWITCH self 50))*Infected asymptomatic 30x50*Susceptible 50\\\\ /non controlled pop 30x50'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contact_infectivity_asymptomatic_30x50() * (
        social_distancing_policy_switch_self_50() * social_distancing_policy_50() +
        (1 - social_distancing_policy_switch_self_50())
    ) * infected_asymptomatic_30x50() * susceptible_50() / non_controlled_pop_30x50()


@cache('step')
def infection_rate_symptomatic_self_00():
    """
    Real Name: b'infection rate symptomatic self 00'
    Original Eqn: b'Infected symptomatic 00*Susceptible 00*contact infectivity symptomatic self 00*(self quarantine policy SWITCH self 00\\\\ *self quarantine policy 00+(1-self quarantine policy SWITCH self 00))/non controlled population 00'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_00() * susceptible_00() * contact_infectivity_symptomatic_self_00(
    ) * (self_quarantine_policy_switch_self_00() * self_quarantine_policy_00() +
         (1 - self_quarantine_policy_switch_self_00())) / non_controlled_population_00()


@cache('step')
def infection_rate_asymptomatic_30x70():
    """
    Real Name: b'infection rate asymptomatic 30x70'
    Original Eqn: b'contact infectivity asymptomatic 30x70*(social distancing policy SWITCH self 70*social distancing policy 70\\\\ +(1-social distancing policy SWITCH self 70))*Infected asymptomatic 30x70*Susceptible 70\\\\ /non controlled pop 30x70'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contact_infectivity_asymptomatic_30x70() * (
        social_distancing_policy_switch_self_70() * social_distancing_policy_70() +
        (1 - social_distancing_policy_switch_self_70())
    ) * infected_asymptomatic_30x70() * susceptible_70() / non_controlled_pop_30x70()


@cache('step')
def infection_rate_asymptomatic_30x80():
    """
    Real Name: b'infection rate asymptomatic 30x80'
    Original Eqn: b'contact infectivity asymptomatic 30x80*(social distancing policy SWITCH self 80*social distancing policy 80\\\\ +(1-social distancing policy SWITCH self 80))*Infected asymptomatic 30x80*Susceptible 80\\\\ /non controlled pop 30x80'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contact_infectivity_asymptomatic_30x80() * (
        social_distancing_policy_switch_self_80() * social_distancing_policy_80() +
        (1 - social_distancing_policy_switch_self_80())
    ) * infected_asymptomatic_30x80() * susceptible_80() / non_controlled_pop_30x80()


@cache('step')
def infection_rate_symptomatic_10x00():
    """
    Real Name: b'infection rate symptomatic 10x00'
    Original Eqn: b'Susceptible 00*Infected symptomatic 00x10*contact infectivity symptomatic 00x10*(self quarantine policy SWITCH self 00\\\\ * self quarantine policy 00+(1-self quarantine policy SWITCH self 00))/non controlled pop 00x10'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_00() * infected_symptomatic_00x10() * contact_infectivity_symptomatic_00x10(
    ) * (self_quarantine_policy_switch_self_00() * self_quarantine_policy_00() +
         (1 - self_quarantine_policy_switch_self_00())) / non_controlled_pop_00x10()


@cache('step')
def infection_rate_symptomatic_10x20():
    """
    Real Name: b'infection rate symptomatic 10x20'
    Original Eqn: b'Susceptible 20*Infected symptomatic 10x20*contact infectivity symptomatic 10x20*(self quarantine policy SWITCH self 20\\\\ *self quarantine policy 20+(1-self quarantine policy SWITCH self 20))/non controlled pop 10x20'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_20() * infected_symptomatic_10x20() * contact_infectivity_symptomatic_10x20(
    ) * (self_quarantine_policy_switch_self_20() * self_quarantine_policy_20() +
         (1 - self_quarantine_policy_switch_self_20())) / non_controlled_pop_10x20()


@cache('step')
def infection_rate_asymptomatic_40x20():
    """
    Real Name: b'infection rate asymptomatic 40x20'
    Original Eqn: b'Susceptible 20*Infected asymptomatic 20x40*contact infectivity asymptomatic 20x40*(social distancing policy SWITCH self 20 *social distancing policy 20+(1-social distancing policy SWITCH self 20))/non controlled pop 20x40'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_20() * infected_asymptomatic_20x40(
    ) * contact_infectivity_asymptomatic_20x40() * (
        social_distancing_policy_switch_self_20() * social_distancing_policy_20() +
        (1 - social_distancing_policy_switch_self_20())) / non_controlled_pop_20x40()


@cache('run')
def self_quarantine_end_50():
    """
    Real Name: b'self quarantine end 50'
    Original Eqn: b'50'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 50


@cache('run')
def init_isolated_30():
    """
    Real Name: b'init Isolated 30'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('step')
def infection_rate_symptomatic_10x60():
    """
    Real Name: b'infection rate symptomatic 10x60'
    Original Eqn: b'Susceptible 60*Infected symptomatic 10x60*contact infectivity symptomatic 10x60*(self quarantine policy SWITCH self 60\\\\ *self quarantine policy 60+(1-self quarantine policy SWITCH self 60))/non controlled pop 10x60'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_60() * infected_symptomatic_10x60() * contact_infectivity_symptomatic_10x60(
    ) * (self_quarantine_policy_switch_self_60() * self_quarantine_policy_60() +
         (1 - self_quarantine_policy_switch_self_60())) / non_controlled_pop_10x60()


@cache('step')
def infection_rate_asymptomatic_40x70():
    """
    Real Name: b'infection rate asymptomatic 40x70'
    Original Eqn: b'contact infectivity asymptomatic 40x70*(social distancing policy SWITCH self 70*social distancing policy 70\\\\ +(1-social distancing policy SWITCH self 70))*Infected asymptomatic 40x70*Susceptible 70\\\\ /non controlled pop 40x70'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contact_infectivity_asymptomatic_40x70() * (
        social_distancing_policy_switch_self_70() * social_distancing_policy_70() +
        (1 - social_distancing_policy_switch_self_70())
    ) * infected_asymptomatic_40x70() * susceptible_70() / non_controlled_pop_40x70()


@cache('step')
def total_infected_30():
    """
    Real Name: b'total infected 30'
    Original Eqn: b'Infected asymptomatic 30+Infected symptomatic 30'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic_30() + infected_symptomatic_30()


@cache('step')
def infection_rate_asymptomatic_50x00():
    """
    Real Name: b'infection rate asymptomatic 50x00'
    Original Eqn: b'Susceptible 00*Infected asymptomatic 00x50*contact infectivity asymptomatic 00x50*(social distancing policy SWITCH self 00 *social distancing policy 00+(1-social distancing policy SWITCH self 00))/non controlled pop 00x50'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_00() * infected_asymptomatic_00x50(
    ) * contact_infectivity_asymptomatic_00x50() * (
        social_distancing_policy_switch_self_00() * social_distancing_policy_00() +
        (1 - social_distancing_policy_switch_self_00())) / non_controlled_pop_00x50()


@cache('step')
def infection_rate_asymptomatic_50x10():
    """
    Real Name: b'infection rate asymptomatic 50x10'
    Original Eqn: b'Susceptible 10*Infected asymptomatic 10x50*contact infectivity asymptomatic 10x50*(social distancing policy SWITCH self 10 *social distancing policy 10+(1-social distancing policy SWITCH self 10))/non controlled pop 10x50'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_10() * infected_asymptomatic_10x50(
    ) * contact_infectivity_asymptomatic_10x50() * (
        social_distancing_policy_switch_self_10() * social_distancing_policy_10() +
        (1 - social_distancing_policy_switch_self_10())) / non_controlled_pop_10x50()


@cache('step')
def infection_rate_asymptomatic_50x20():
    """
    Real Name: b'infection rate asymptomatic 50x20'
    Original Eqn: b'Susceptible 20*Infected asymptomatic 20x50*contact infectivity asymptomatic 20x50*(social distancing policy SWITCH self 20 *social distancing policy 20+(1-social distancing policy SWITCH self 20))/non controlled pop 20x50'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_20() * infected_asymptomatic_20x50(
    ) * contact_infectivity_asymptomatic_20x50() * (
        social_distancing_policy_switch_self_20() * social_distancing_policy_20() +
        (1 - social_distancing_policy_switch_self_20())) / non_controlled_pop_20x50()


@cache('step')
def infection_rate_symptomatic_00x30():
    """
    Real Name: b'infection rate symptomatic 00x30'
    Original Eqn: b'Susceptible 30*Infected symptomatic 00x30*contact infectivity symptomatic 00x30*(self quarantine policy SWITCH self 30\\\\ *self quarantine policy 30+(1-self quarantine policy SWITCH self 30))/non controlled pop 00x30'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_30() * infected_symptomatic_00x30() * contact_infectivity_symptomatic_00x30(
    ) * (self_quarantine_policy_switch_self_30() * self_quarantine_policy_30() +
         (1 - self_quarantine_policy_switch_self_30())) / non_controlled_pop_00x30()


@cache('step')
def infection_rate_asymptomatic_50x40():
    """
    Real Name: b'infection rate asymptomatic 50x40'
    Original Eqn: b'Susceptible 40*Infected asymptomatic 40x50*contact infectivity asymptomatic 40x50*(social distancing policy SWITCH self 40 *social distancing policy 40+(1-social distancing policy SWITCH self 40))/non controlled pop 40x50'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_40() * infected_asymptomatic_40x50(
    ) * contact_infectivity_asymptomatic_40x50() * (
        social_distancing_policy_switch_self_40() * social_distancing_policy_40() +
        (1 - social_distancing_policy_switch_self_40())) / non_controlled_pop_40x50()


@cache('step')
def total_infection_rate_00():
    """
    Real Name: b'total infection rate 00'
    Original Eqn: b'infection rate asymptomatic self 00+infection rate quarantined self 00+infection rate symptomatic self 00 +infection rate asymptomatic 80x00+infection rate symptomatic 80x00 +infection rate asymptomatic 70x00+infection rate symptomatic 70x00 +infection rate asymptomatic 60x00+infection rate symptomatic 60x00 +infection rate asymptomatic 50x00+infection rate symptomatic 50x00 +infection rate asymptomatic 40x00+infection rate symptomatic 40x00 +infection rate asymptomatic 30x00+infection rate symptomatic 30x00 +infection rate asymptomatic 20x00+infection rate symptomatic 20x00 +infection rate asymptomatic 10x00+infection rate symptomatic 10x00'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infection_rate_asymptomatic_self_00() + infection_rate_quarantined_self_00(
    ) + infection_rate_symptomatic_self_00() + infection_rate_asymptomatic_80x00(
    ) + infection_rate_symptomatic_80x00() + infection_rate_asymptomatic_70x00(
    ) + infection_rate_symptomatic_70x00() + infection_rate_asymptomatic_60x00(
    ) + infection_rate_symptomatic_60x00() + infection_rate_asymptomatic_50x00(
    ) + infection_rate_symptomatic_50x00() + infection_rate_asymptomatic_40x00(
    ) + infection_rate_symptomatic_40x00() + infection_rate_asymptomatic_30x00(
    ) + infection_rate_symptomatic_30x00() + infection_rate_asymptomatic_20x00(
    ) + infection_rate_symptomatic_20x00() + infection_rate_asymptomatic_10x00(
    ) + infection_rate_symptomatic_10x00()


@cache('step')
def total_infection_rate_10():
    """
    Real Name: b'total infection rate 10'
    Original Eqn: b'infection rate asymptomatic self 10+infection rate quarantined self 10+infection rate symptomatic self 10 +infection rate asymptomatic 80x10+infection rate symptomatic 80x10 +infection rate asymptomatic 70x10+infection rate symptomatic 70x10 +infection rate asymptomatic 60x10+infection rate symptomatic 60x10 +infection rate asymptomatic 50x10+infection rate symptomatic 50x10 +infection rate asymptomatic 40x10+infection rate symptomatic 40x10 +infection rate asymptomatic 30x10+infection rate symptomatic 30x10 +infection rate asymptomatic 20x10+infection rate symptomatic 20x10 +infection rate asymptomatic 00x10+infection rate symptomatic 00x10'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infection_rate_asymptomatic_self_10() + infection_rate_quarantined_self_10(
    ) + infection_rate_symptomatic_self_10() + infection_rate_asymptomatic_80x10(
    ) + infection_rate_symptomatic_80x10() + infection_rate_asymptomatic_70x10(
    ) + infection_rate_symptomatic_70x10() + infection_rate_asymptomatic_60x10(
    ) + infection_rate_symptomatic_60x10() + infection_rate_asymptomatic_50x10(
    ) + infection_rate_symptomatic_50x10() + infection_rate_asymptomatic_40x10(
    ) + infection_rate_symptomatic_40x10() + infection_rate_asymptomatic_30x10(
    ) + infection_rate_symptomatic_30x10() + infection_rate_asymptomatic_20x10(
    ) + infection_rate_symptomatic_20x10() + infection_rate_asymptomatic_00x10(
    ) + infection_rate_symptomatic_00x10()


@cache('step')
def total_infection_rate_20():
    """
    Real Name: b'total infection rate 20'
    Original Eqn: b'infection rate asymptomatic self 20+infection rate quarantined self 20+infection rate symptomatic self 20 +infection rate asymptomatic 80x20+infection rate symptomatic 80x20 +infection rate asymptomatic 70x20+infection rate symptomatic 70x20 +infection rate asymptomatic 60x20+infection rate symptomatic 60x20 +infection rate asymptomatic 50x20+infection rate symptomatic 50x20 +infection rate asymptomatic 40x20+infection rate symptomatic 40x20 +infection rate asymptomatic 30x20+infection rate symptomatic 30x20 +infection rate asymptomatic 10x20+infection rate symptomatic 10x20 +infection rate asymptomatic 00x20+infection rate symptomatic 00x20'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infection_rate_asymptomatic_self_20() + infection_rate_quarantined_self_20(
    ) + infection_rate_symptomatic_self_20() + infection_rate_asymptomatic_80x20(
    ) + infection_rate_symptomatic_80x20() + infection_rate_asymptomatic_70x20(
    ) + infection_rate_symptomatic_70x20() + infection_rate_asymptomatic_60x20(
    ) + infection_rate_symptomatic_60x20() + infection_rate_asymptomatic_50x20(
    ) + infection_rate_symptomatic_50x20() + infection_rate_asymptomatic_40x20(
    ) + infection_rate_symptomatic_40x20() + infection_rate_asymptomatic_30x20(
    ) + infection_rate_symptomatic_30x20() + infection_rate_asymptomatic_10x20(
    ) + infection_rate_symptomatic_10x20() + infection_rate_asymptomatic_00x20(
    ) + infection_rate_symptomatic_00x20()


@cache('step')
def non_controlled_pop_40x70():
    """
    Real Name: b'non controlled pop 40x70'
    Original Eqn: b'non controlled population 40+non controlled population 70'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return non_controlled_population_40() + non_controlled_population_70()


@cache('step')
def total_infection_rate_30():
    """
    Real Name: b'total infection rate 30'
    Original Eqn: b'infection rate asymptomatic self 30+infection rate quarantined self 30+infection rate symptomatic self 30 +infection rate asymptomatic 80x30+infection rate symptomatic 80x30 +infection rate asymptomatic 70x30+infection rate symptomatic 70x30 +infection rate asymptomatic 60x30+infection rate symptomatic 60x30 +infection rate asymptomatic 50x30+infection rate symptomatic 50x30 +infection rate asymptomatic 40x30+infection rate symptomatic 40x30 +infection rate asymptomatic 20x30+infection rate symptomatic 20x30 +infection rate asymptomatic 10x30+infection rate symptomatic 10x30 +infection rate asymptomatic 00x30+infection rate symptomatic 00x30'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infection_rate_asymptomatic_self_30() + infection_rate_quarantined_self_30(
    ) + infection_rate_symptomatic_self_30() + infection_rate_asymptomatic_80x30(
    ) + infection_rate_symptomatic_80x30() + infection_rate_asymptomatic_70x30(
    ) + infection_rate_symptomatic_70x30() + infection_rate_asymptomatic_60x30(
    ) + infection_rate_symptomatic_60x30() + infection_rate_asymptomatic_50x30(
    ) + infection_rate_symptomatic_50x30() + infection_rate_asymptomatic_40x30(
    ) + infection_rate_symptomatic_40x30() + infection_rate_asymptomatic_20x30(
    ) + infection_rate_symptomatic_20x30() + infection_rate_asymptomatic_10x30(
    ) + infection_rate_symptomatic_10x30() + infection_rate_asymptomatic_00x30(
    ) + infection_rate_symptomatic_00x30()


@cache('step')
def total_infection_rate_40():
    """
    Real Name: b'total infection rate 40'
    Original Eqn: b'infection rate asymptomatic self 40+infection rate quarantined self 40+infection rate symptomatic self 40 +infection rate asymptomatic 80x40+infection rate symptomatic 80x40 +infection rate asymptomatic 70x40+infection rate symptomatic 70x40 +infection rate asymptomatic 60x40+infection rate symptomatic 60x40 +infection rate asymptomatic 50x40+infection rate symptomatic 50x40 +infection rate asymptomatic 30x40+infection rate symptomatic 30x40 +infection rate asymptomatic 20x40+infection rate symptomatic 20x40 +infection rate asymptomatic 10x40+infection rate symptomatic 10x40 +infection rate asymptomatic 00x40+infection rate symptomatic 00x40'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infection_rate_asymptomatic_self_40() + infection_rate_quarantined_self_40(
    ) + infection_rate_symptomatic_self_40() + infection_rate_asymptomatic_80x40(
    ) + infection_rate_symptomatic_80x40() + infection_rate_asymptomatic_70x40(
    ) + infection_rate_symptomatic_70x40() + infection_rate_asymptomatic_60x40(
    ) + infection_rate_symptomatic_60x40() + infection_rate_asymptomatic_50x40(
    ) + infection_rate_symptomatic_50x40() + infection_rate_asymptomatic_30x40(
    ) + infection_rate_symptomatic_30x40() + infection_rate_asymptomatic_20x40(
    ) + infection_rate_symptomatic_20x40() + infection_rate_asymptomatic_10x40(
    ) + infection_rate_symptomatic_10x40() + infection_rate_asymptomatic_00x40(
    ) + infection_rate_symptomatic_00x40()


@cache('step')
def symptomatic_rate_30():
    """
    Real Name: b'symptomatic rate 30'
    Original Eqn: b'Infected asymptomatic 30/asymptomatic duration 30*(1-fraction of asymptomatic case development 30\\\\ )'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic_30() / asymptomatic_duration_30() * (
        1 - fraction_of_asymptomatic_case_development_30())


@cache('step')
def infection_rate_asymptomatic_60x40():
    """
    Real Name: b'infection rate asymptomatic 60x40'
    Original Eqn: b'Susceptible 40*Infected asymptomatic 40x60*contact infectivity asymptomatic 40x60*(social distancing policy SWITCH self 40 *social distancing policy 40+(1-social distancing policy SWITCH self 40))/non controlled pop 40x60'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_40() * infected_asymptomatic_40x60(
    ) * contact_infectivity_asymptomatic_40x60() * (
        social_distancing_policy_switch_self_40() * social_distancing_policy_40() +
        (1 - social_distancing_policy_switch_self_40())) / non_controlled_pop_40x60()


@cache('run')
def init_susceptible_00():
    """
    Real Name: b'init Susceptible 00'
    Original Eqn: b'8e+06'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 8e+06


@cache('run')
def self_quarantine_policy_switch_self_40():
    """
    Real Name: b'self quarantine policy SWITCH self 40'
    Original Eqn: b'0'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('step')
def isolation_rate_asymptomatic_00():
    """
    Real Name: b'isolation rate asymptomatic 00'
    Original Eqn: b'MIN(available test kits for testing asymptomatic*effect of kits availability on effectiveness of testing\\\\ /kits per person, Infected asymptomatic 00 )/testing duration'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return np.minimum(
        available_test_kits_for_testing_asymptomatic() *
        effect_of_kits_availability_on_effectiveness_of_testing() / kits_per_person(),
        infected_asymptomatic_00()) / testing_duration()


@cache('step')
def social_distancing_policy_00():
    """
    Real Name: b'social distancing policy 00'
    Original Eqn: b'1-PULSE(social distancing start 00, social distancing end 00-social distancing start 00\\\\ )*social distancing effectiveness 00'
    Units: b'dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return 1 - functions.pulse(__data['time'], social_distancing_start_00(),
                               social_distancing_end_00() - social_distancing_start_00()
                               ) * social_distancing_effectiveness_00()


@cache('step')
def infection_rate_symptomatic_40x10():
    """
    Real Name: b'infection rate symptomatic 40x10'
    Original Eqn: b'Susceptible 10*Infected symptomatic 10x40*contact infectivity symptomatic 10x40*(self quarantine policy SWITCH self 10\\\\ * self quarantine policy 10+(1-self quarantine policy SWITCH self 10))/non controlled pop 10x40'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_10() * infected_symptomatic_10x40() * contact_infectivity_symptomatic_10x40(
    ) * (self_quarantine_policy_switch_self_10() * self_quarantine_policy_10() +
         (1 - self_quarantine_policy_switch_self_10())) / non_controlled_pop_10x40()


@cache('step')
def non_controlled_population_10():
    """
    Real Name: b'non controlled population 10'
    Original Eqn: b'Infected symptomatic 10+Susceptible 10+Infected asymptomatic 10+Isolated 10+Recovered 10'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_10() + susceptible_10() + infected_asymptomatic_10() + isolated_10(
    ) + recovered_10()


@cache('step')
def infection_rate_symptomatic_40x30():
    """
    Real Name: b'infection rate symptomatic 40x30'
    Original Eqn: b'Susceptible 30*Infected symptomatic 30x40*contact infectivity symptomatic 30x40*(self quarantine policy SWITCH self 30\\\\ * self quarantine policy 30+(1-self quarantine policy SWITCH self 30))/non controlled pop 30x40'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_30() * infected_symptomatic_30x40() * contact_infectivity_symptomatic_30x40(
    ) * (self_quarantine_policy_switch_self_30() * self_quarantine_policy_30() +
         (1 - self_quarantine_policy_switch_self_30())) / non_controlled_pop_30x40()


@cache('run')
def test_fraction_20():
    """
    Real Name: b'test fraction 20'
    Original Eqn: b'1'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1


@cache('run')
def test_fraction_30():
    """
    Real Name: b'test fraction 30'
    Original Eqn: b'1'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1


@cache('run')
def self_quarantine_start_20():
    """
    Real Name: b'self quarantine start 20'
    Original Eqn: b'21'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 21


@cache('run')
def init_critical_cases_20():
    """
    Real Name: b'init Critical Cases 20'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('run')
def init_critical_cases_30():
    """
    Real Name: b'init Critical Cases 30'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('step')
def isolation_rate_symptomatic_00():
    """
    Real Name: b'isolation rate symptomatic 00'
    Original Eqn: b'tests for symptomatic/kits per person/testing duration'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return tests_for_symptomatic() / kits_per_person() / testing_duration()


@cache('step')
def infection_rate_symptomatic_self_30():
    """
    Real Name: b'infection rate symptomatic self 30'
    Original Eqn: b'Infected symptomatic 30*Susceptible 30*contact infectivity symptomatic self 30*(self quarantine policy SWITCH self 30\\\\ *self quarantine policy 30+(1-self quarantine policy SWITCH self 30))/non controlled population 30'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_30() * susceptible_30() * contact_infectivity_symptomatic_self_30(
    ) * (self_quarantine_policy_switch_self_30() * self_quarantine_policy_30() +
         (1 - self_quarantine_policy_switch_self_30())) / non_controlled_population_30()


@cache('step')
def infection_rate_symptomatic_self_40():
    """
    Real Name: b'infection rate symptomatic self 40'
    Original Eqn: b'Infected symptomatic 40*Susceptible 40*contact infectivity symptomatic self 40*(self quarantine policy SWITCH self 40\\\\ *self quarantine policy 40+(1-self quarantine policy SWITCH self 40))/non controlled population 40'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_40() * susceptible_40() * contact_infectivity_symptomatic_self_40(
    ) * (self_quarantine_policy_switch_self_40() * self_quarantine_policy_40() +
         (1 - self_quarantine_policy_switch_self_40())) / non_controlled_population_40()


@cache('step')
def infection_rate_symptomatic_10x30():
    """
    Real Name: b'infection rate symptomatic 10x30'
    Original Eqn: b'Susceptible 30*Infected symptomatic 10x30*contact infectivity symptomatic 10x30*(self quarantine policy SWITCH self 30\\\\ *self quarantine policy 30+(1-self quarantine policy SWITCH self 30))/non controlled pop 10x30'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_30() * infected_symptomatic_10x30() * contact_infectivity_symptomatic_10x30(
    ) * (self_quarantine_policy_switch_self_30() * self_quarantine_policy_30() +
         (1 - self_quarantine_policy_switch_self_30())) / non_controlled_pop_10x30()


@cache('run')
def init_isolated_20():
    """
    Real Name: b'init Isolated 20'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('step')
def total_infected_00():
    """
    Real Name: b'total infected 00'
    Original Eqn: b'Infected asymptomatic 00+Infected symptomatic 00'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic_00() + infected_symptomatic_00()


@cache('step')
def total_infected_10():
    """
    Real Name: b'total infected 10'
    Original Eqn: b'Infected asymptomatic 10+Infected symptomatic 10'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic_10() + infected_symptomatic_10()


@cache('run')
def init_diseased_10():
    """
    Real Name: b'init Diseased 10'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('run')
def init_diseased_20():
    """
    Real Name: b'init Diseased 20'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('run')
def init_diseased_30():
    """
    Real Name: b'init Diseased 30'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('run')
def init_diseased_40():
    """
    Real Name: b'init Diseased 40'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('run')
def symptomatic_duration_40():
    """
    Real Name: b'symptomatic duration 40'
    Original Eqn: b'5'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 5


@cache('run')
def init_infected_symptomatic_30():
    """
    Real Name: b'init Infected symptomatic 30'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('step')
def recovered_00():
    """
    Real Name: b'Recovered 00'
    Original Eqn: b'INTEG ( critical cases recovery rate 00+infected asymptomatic recovery rate 00+infected symptomatic recovery rate 00\\\\ -deimmunization rate 00+isolated recovery rate 00, init Recovered 00)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_recovered_00()


@cache('run')
def social_distancing_end_00():
    """
    Real Name: b'social distancing end 00'
    Original Eqn: b'50'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 50


@cache('run')
def init_infected_asymptomatic_00():
    """
    Real Name: b'init Infected asymptomatic 00'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('step')
def new_cases_30():
    """
    Real Name: b'new cases 30'
    Original Eqn: b'symptomatic rate 30*test fraction 30'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return symptomatic_rate_30() * test_fraction_30()


@cache('step')
def infection_rate_quarantined_self_00():
    """
    Real Name: b'infection rate quarantined self 00'
    Original Eqn: b'Isolated 00*Susceptible 00*contact infectivity quarantine self 00/non controlled population 00'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return isolated_00() * susceptible_00() * contact_infectivity_quarantine_self_00(
    ) / non_controlled_population_00()


@cache('run')
def social_distancing_end_40():
    """
    Real Name: b'social distancing end 40'
    Original Eqn: b'50'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 50


@cache('run')
def self_quarantine_end_40():
    """
    Real Name: b'self quarantine end 40'
    Original Eqn: b'50'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 50


@cache('run')
def self_quarantine_policy_switch_self_20():
    """
    Real Name: b'self quarantine policy SWITCH self 20'
    Original Eqn: b'0'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('step')
def susceptible_10():
    """
    Real Name: b'Susceptible 10'
    Original Eqn: b'INTEG ( deimmunization rate 10-infection rate 10, init Susceptible 10)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_susceptible_10()


@cache('step')
def infection_rate_symptomatic_80x00():
    """
    Real Name: b'infection rate symptomatic 80x00'
    Original Eqn: b'Susceptible 00*Infected symptomatic 00x80*contact infectivity symptomatic 00x80*(self quarantine policy SWITCH self 00\\\\ * self quarantine policy 00+(1-self quarantine policy SWITCH self 00))/non controlled pop 00x80'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_00() * infected_symptomatic_00x80() * contact_infectivity_symptomatic_00x80(
    ) * (self_quarantine_policy_switch_self_00() * self_quarantine_policy_00() +
         (1 - self_quarantine_policy_switch_self_00())) / non_controlled_pop_00x80()


@cache('step')
def infection_rate_symptomatic_80x10():
    """
    Real Name: b'infection rate symptomatic 80x10'
    Original Eqn: b'Susceptible 10*Infected symptomatic 10x80*contact infectivity symptomatic 10x80*(self quarantine policy SWITCH self 10\\\\ * self quarantine policy 10+(1-self quarantine policy SWITCH self 10))/non controlled pop 10x80'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_10() * infected_symptomatic_10x80() * contact_infectivity_symptomatic_10x80(
    ) * (self_quarantine_policy_switch_self_10() * self_quarantine_policy_10() +
         (1 - self_quarantine_policy_switch_self_10())) / non_controlled_pop_10x80()


@cache('step')
def infection_rate_symptomatic_80x20():
    """
    Real Name: b'infection rate symptomatic 80x20'
    Original Eqn: b'Susceptible 20*Infected symptomatic 20x80*contact infectivity symptomatic 20x80*(self quarantine policy SWITCH self 20\\\\ * self quarantine policy 20+(1-self quarantine policy SWITCH self 20))/non controlled pop 20x80'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_20() * infected_symptomatic_20x80() * contact_infectivity_symptomatic_20x80(
    ) * (self_quarantine_policy_switch_self_20() * self_quarantine_policy_20() +
         (1 - self_quarantine_policy_switch_self_20())) / non_controlled_pop_20x80()


@cache('run')
def init_infected_symptomatic_00():
    """
    Real Name: b'init Infected symptomatic 00'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('step')
def infection_rate_symptomatic_00x10():
    """
    Real Name: b'infection rate symptomatic 00x10'
    Original Eqn: b'Susceptible 10*Infected symptomatic 00x10*contact infectivity symptomatic 00x10*(self quarantine policy SWITCH self 10\\\\ *self quarantine policy 10+(1-self quarantine policy SWITCH self 10))/non controlled pop 00x10'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_10() * infected_symptomatic_00x10() * contact_infectivity_symptomatic_00x10(
    ) * (self_quarantine_policy_switch_self_10() * self_quarantine_policy_10() +
         (1 - self_quarantine_policy_switch_self_10())) / non_controlled_pop_00x10()


@cache('step')
def infection_rate_symptomatic_00x20():
    """
    Real Name: b'infection rate symptomatic 00x20'
    Original Eqn: b'Susceptible 20*Infected symptomatic 00x20*contact infectivity symptomatic 00x20*(self quarantine policy SWITCH self 20\\\\ *self quarantine policy 20+(1-self quarantine policy SWITCH self 20))/non controlled pop 00x20'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_20() * infected_symptomatic_00x20() * contact_infectivity_symptomatic_00x20(
    ) * (self_quarantine_policy_switch_self_20() * self_quarantine_policy_20() +
         (1 - self_quarantine_policy_switch_self_20())) / non_controlled_pop_00x20()


@cache('step')
def non_controlled_pop_00x70():
    """
    Real Name: b'non controlled pop 00x70'
    Original Eqn: b'non controlled population 00+non controlled population 70'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return non_controlled_population_00() + non_controlled_population_70()


@cache('step')
def social_distancing_policy_50():
    """
    Real Name: b'social distancing policy 50'
    Original Eqn: b'1-PULSE(social distancing start 50, social distancing end 50-social distancing start 50\\\\ )*social distancing effectiveness 50'
    Units: b'dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return 1 - functions.pulse(__data['time'], social_distancing_start_50(),
                               social_distancing_end_50() - social_distancing_start_50()
                               ) * social_distancing_effectiveness_50()


@cache('step')
def infection_rate_symptomatic_00x50():
    """
    Real Name: b'infection rate symptomatic 00x50'
    Original Eqn: b'Susceptible 50*Infected symptomatic 00x50*contact infectivity symptomatic 00x50*(self quarantine policy SWITCH self 50\\\\ *self quarantine policy 50+(1-self quarantine policy SWITCH self 50))/non controlled pop 00x50'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_50() * infected_symptomatic_00x50() * contact_infectivity_symptomatic_00x50(
    ) * (self_quarantine_policy_switch_self_50() * self_quarantine_policy_50() +
         (1 - self_quarantine_policy_switch_self_50())) / non_controlled_pop_00x50()


@cache('step')
def infection_rate_symptomatic_00x60():
    """
    Real Name: b'infection rate symptomatic 00x60'
    Original Eqn: b'Susceptible 60*Infected symptomatic 00x60*contact infectivity symptomatic 00x60*(self quarantine policy SWITCH self 60\\\\ *self quarantine policy 60+(1-self quarantine policy SWITCH self 60))/non controlled pop 00x60'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_60() * infected_symptomatic_00x60() * contact_infectivity_symptomatic_00x60(
    ) * (self_quarantine_policy_switch_self_60() * self_quarantine_policy_60() +
         (1 - self_quarantine_policy_switch_self_60())) / non_controlled_pop_00x60()


@cache('step')
def infection_rate_symptomatic_00x70():
    """
    Real Name: b'infection rate symptomatic 00x70'
    Original Eqn: b'Susceptible 70*Infected symptomatic 00x70*contact infectivity symptomatic 00x70*(self quarantine policy SWITCH self 70\\\\ *self quarantine policy 70+(1-self quarantine policy SWITCH self 70))/non controlled pop 00x70'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_70() * infected_symptomatic_00x70() * contact_infectivity_symptomatic_00x70(
    ) * (self_quarantine_policy_switch_self_70() * self_quarantine_policy_70() +
         (1 - self_quarantine_policy_switch_self_70())) / non_controlled_pop_00x70()


@cache('step')
def infection_rate_symptomatic_00x80():
    """
    Real Name: b'infection rate symptomatic 00x80'
    Original Eqn: b'Susceptible 80*Infected symptomatic 00x80*contact infectivity symptomatic 00x80*(self quarantine policy SWITCH self 80\\\\ *self quarantine policy 80+(1-self quarantine policy SWITCH self 80))/non controlled pop 00x80'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_80() * infected_symptomatic_00x80() * contact_infectivity_symptomatic_00x80(
    ) * (self_quarantine_policy_switch_self_80() * self_quarantine_policy_80() +
         (1 - self_quarantine_policy_switch_self_80())) / non_controlled_pop_00x80()


@cache('run')
def social_distancing_policy_switch_self_00():
    """
    Real Name: b'social distancing policy SWITCH self 00'
    Original Eqn: b'0'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('run')
def init_isolated_00():
    """
    Real Name: b'init Isolated 00'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('run')
def init_isolated_10():
    """
    Real Name: b'init Isolated 10'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('run')
def isolation_duration_00():
    """
    Real Name: b'isolation duration 00'
    Original Eqn: b'14'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 14


@cache('step')
def non_controlled_pop_20x40():
    """
    Real Name: b'non controlled pop 20x40'
    Original Eqn: b'non controlled population 20+non controlled population 40'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return non_controlled_population_20() + non_controlled_population_40()


@cache('run')
def init_isolated_40():
    """
    Real Name: b'init Isolated 40'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('step')
def non_controlled_pop_20x60():
    """
    Real Name: b'non controlled pop 20x60'
    Original Eqn: b'non controlled population 20+non controlled population 60'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return non_controlled_population_20() + non_controlled_population_60()


@cache('step')
def self_quarantine_policy_00():
    """
    Real Name: b'self quarantine policy 00'
    Original Eqn: b'1-PULSE(self quarantine start 00, self quarantine end 00-self quarantine start 00)*self quarantine effectiveness 00'
    Units: b'dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return 1 - functions.pulse(__data['time'], self_quarantine_start_00(),
                               self_quarantine_end_00() -
                               self_quarantine_start_00()) * self_quarantine_effectiveness_00()


@cache('step')
def infection_rate_symptomatic_20x10():
    """
    Real Name: b'infection rate symptomatic 20x10'
    Original Eqn: b'Susceptible 10*Infected symptomatic 10x20*contact infectivity symptomatic 10x20*(self quarantine policy SWITCH self 10\\\\ * self quarantine policy 10+(1-self quarantine policy SWITCH self 10))/non controlled pop 10x20'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_10() * infected_symptomatic_10x20() * contact_infectivity_symptomatic_10x20(
    ) * (self_quarantine_policy_switch_self_10() * self_quarantine_policy_10() +
         (1 - self_quarantine_policy_switch_self_10())) / non_controlled_pop_10x20()


@cache('step')
def infection_rate_symptomatic_20x30():
    """
    Real Name: b'infection rate symptomatic 20x30'
    Original Eqn: b'Susceptible 30*Infected symptomatic 20x30*contact infectivity symptomatic 20x30*(self quarantine policy SWITCH self 30\\\\ *self quarantine policy 30+(1-self quarantine policy SWITCH self 30))/non controlled pop 20x30'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_30() * infected_symptomatic_20x30() * contact_infectivity_symptomatic_20x30(
    ) * (self_quarantine_policy_switch_self_30() * self_quarantine_policy_30() +
         (1 - self_quarantine_policy_switch_self_30())) / non_controlled_pop_20x30()


@cache('step')
def social_distancing_policy_40():
    """
    Real Name: b'social distancing policy 40'
    Original Eqn: b'1-PULSE(social distancing start 40, social distancing end 40-social distancing start 40\\\\ )*social distancing effectiveness 40'
    Units: b'dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return 1 - functions.pulse(__data['time'], social_distancing_start_40(),
                               social_distancing_end_40() - social_distancing_start_40()
                               ) * social_distancing_effectiveness_40()


@cache('step')
def infection_rate_symptomatic_20x50():
    """
    Real Name: b'infection rate symptomatic 20x50'
    Original Eqn: b'Susceptible 50*Infected symptomatic 20x50*contact infectivity symptomatic 20x50*(self quarantine policy SWITCH self 50\\\\ *self quarantine policy 50+(1-self quarantine policy SWITCH self 50))/non controlled pop 20x50'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_50() * infected_symptomatic_20x50() * contact_infectivity_symptomatic_20x50(
    ) * (self_quarantine_policy_switch_self_50() * self_quarantine_policy_50() +
         (1 - self_quarantine_policy_switch_self_50())) / non_controlled_pop_20x50()


@cache('step')
def infection_rate_symptomatic_20x60():
    """
    Real Name: b'infection rate symptomatic 20x60'
    Original Eqn: b'Susceptible 60*Infected symptomatic 20x60*contact infectivity symptomatic 20x60*(self quarantine policy SWITCH self 60\\\\ *self quarantine policy 60+(1-self quarantine policy SWITCH self 60))/non controlled pop 20x60'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_60() * infected_symptomatic_20x60() * contact_infectivity_symptomatic_20x60(
    ) * (self_quarantine_policy_switch_self_60() * self_quarantine_policy_60() +
         (1 - self_quarantine_policy_switch_self_60())) / non_controlled_pop_20x60()


@cache('step')
def infection_rate_symptomatic_20x70():
    """
    Real Name: b'infection rate symptomatic 20x70'
    Original Eqn: b'Susceptible 70*Infected symptomatic 20x70*contact infectivity symptomatic 20x70*(self quarantine policy SWITCH self 70\\\\ *self quarantine policy 70+(1-self quarantine policy SWITCH self 70))/non controlled pop 20x70'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_70() * infected_symptomatic_20x70() * contact_infectivity_symptomatic_20x70(
    ) * (self_quarantine_policy_switch_self_70() * self_quarantine_policy_70() +
         (1 - self_quarantine_policy_switch_self_70())) / non_controlled_pop_20x70()


@cache('step')
def infection_rate_symptomatic_20x80():
    """
    Real Name: b'infection rate symptomatic 20x80'
    Original Eqn: b'Susceptible 80*Infected symptomatic 20x80*contact infectivity symptomatic 20x80*(self quarantine policy SWITCH self 80\\\\ *self quarantine policy 80+(1-self quarantine policy SWITCH self 80))/non controlled pop 20x80'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_80() * infected_symptomatic_20x80() * contact_infectivity_symptomatic_20x80(
    ) * (self_quarantine_policy_switch_self_80() * self_quarantine_policy_80() +
         (1 - self_quarantine_policy_switch_self_80())) / non_controlled_pop_20x80()


@cache('step')
def infection_rate_symptomatic_70x20():
    """
    Real Name: b'infection rate symptomatic 70x20'
    Original Eqn: b'Susceptible 20*Infected symptomatic 20x70*contact infectivity symptomatic 20x70*(self quarantine policy SWITCH self 20\\\\ * self quarantine policy 20+(1-self quarantine policy SWITCH self 20))/non controlled pop 20x70'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_20() * infected_symptomatic_20x70() * contact_infectivity_symptomatic_20x70(
    ) * (self_quarantine_policy_switch_self_20() * self_quarantine_policy_20() +
         (1 - self_quarantine_policy_switch_self_20())) / non_controlled_pop_20x70()


@cache('step')
def infection_rate_symptomatic_70x30():
    """
    Real Name: b'infection rate symptomatic 70x30'
    Original Eqn: b'Susceptible 30*Infected symptomatic 30x70*contact infectivity symptomatic 30x70*(self quarantine policy SWITCH self 30\\\\ * self quarantine policy 30+(1-self quarantine policy SWITCH self 30))/non controlled pop 30x70'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_30() * infected_symptomatic_30x70() * contact_infectivity_symptomatic_30x70(
    ) * (self_quarantine_policy_switch_self_30() * self_quarantine_policy_30() +
         (1 - self_quarantine_policy_switch_self_30())) / non_controlled_pop_30x70()


@cache('step')
def infection_rate_symptomatic_70x40():
    """
    Real Name: b'infection rate symptomatic 70x40'
    Original Eqn: b'Susceptible 40*Infected symptomatic 40x70*contact infectivity symptomatic 40x70*(self quarantine policy SWITCH self 40\\\\ * self quarantine policy 40+(1-self quarantine policy SWITCH self 40))/non controlled pop 40x70'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_40() * infected_symptomatic_40x70() * contact_infectivity_symptomatic_40x70(
    ) * (self_quarantine_policy_switch_self_40() * self_quarantine_policy_40() +
         (1 - self_quarantine_policy_switch_self_40())) / non_controlled_pop_40x70()


@cache('step')
def non_controlled_pop_10x80():
    """
    Real Name: b'non controlled pop 10x80'
    Original Eqn: b'non controlled population 10+non controlled population 80'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return non_controlled_population_10() + non_controlled_population_80()


@cache('step')
def non_controlled_pop_20x30():
    """
    Real Name: b'non controlled pop 20x30'
    Original Eqn: b'non controlled population 20+non controlled population 30'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return non_controlled_population_20() + non_controlled_population_30()


@cache('run')
def social_distancing_policy_switch_self_40():
    """
    Real Name: b'social distancing policy SWITCH self 40'
    Original Eqn: b'0'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('run')
def init_susceptible_10():
    """
    Real Name: b'init Susceptible 10'
    Original Eqn: b'8e+06'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 8e+06


@cache('run')
def init_susceptible_20():
    """
    Real Name: b'init Susceptible 20'
    Original Eqn: b'8e+06'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 8e+06


@cache('run')
def self_quarantine_effectiveness_20():
    """
    Real Name: b'self quarantine effectiveness 20'
    Original Eqn: b'0.75'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.75


@cache('step')
def non_controlled_population_00():
    """
    Real Name: b'non controlled population 00'
    Original Eqn: b'Infected symptomatic 00+Susceptible 00+Infected asymptomatic 00+Isolated 00+Recovered 00'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_00() + susceptible_00() + infected_asymptomatic_00() + isolated_00(
    ) + recovered_00()


@cache('step')
def infection_rate_symptomatic_80x40():
    """
    Real Name: b'infection rate symptomatic 80x40'
    Original Eqn: b'Susceptible 40*Infected symptomatic 40x80*contact infectivity symptomatic 40x80*(self quarantine policy SWITCH self 40\\\\ * self quarantine policy 40+(1-self quarantine policy SWITCH self 40))/non controlled pop 40x80'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_40() * infected_symptomatic_40x80() * contact_infectivity_symptomatic_40x80(
    ) * (self_quarantine_policy_switch_self_40() * self_quarantine_policy_40() +
         (1 - self_quarantine_policy_switch_self_40())) / non_controlled_pop_40x80()


@cache('step')
def isolated_recovery_rate_00():
    """
    Real Name: b'isolated recovery rate 00'
    Original Eqn: b'Isolated 00*(1-fraction of critical cases 00)/isolation duration 00'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return isolated_00() * (1 - fraction_of_critical_cases_00()) / isolation_duration_00()


@cache('run')
def social_distancing_policy_switch_self_20():
    """
    Real Name: b'social distancing policy SWITCH self 20'
    Original Eqn: b'0'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('step')
def non_controlled_pop_00x80():
    """
    Real Name: b'non controlled pop 00x80'
    Original Eqn: b'non controlled population 00+non controlled population 80'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return non_controlled_population_00() + non_controlled_population_80()


@cache('run')
def test_fraction_40():
    """
    Real Name: b'test fraction 40'
    Original Eqn: b'1'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1


@cache('run')
def symptomatic_contact_fraction_10():
    """
    Real Name: b'symptomatic contact fraction 10'
    Original Eqn: b'0.5'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.5


@cache('run')
def symptomatic_contact_fraction_20():
    """
    Real Name: b'symptomatic contact fraction 20'
    Original Eqn: b'0.5'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.5


@cache('run')
def init_critical_cases_40():
    """
    Real Name: b'init Critical Cases 40'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('run')
def self_quarantine_end_20():
    """
    Real Name: b'self quarantine end 20'
    Original Eqn: b'50'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 50


@cache('run')
def self_quarantine_end_30():
    """
    Real Name: b'self quarantine end 30'
    Original Eqn: b'50'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 50


@cache('run')
def init_infected_symptomatic_20():
    """
    Real Name: b'init Infected symptomatic 20'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('run')
def social_distancing_policy_switch_self_30():
    """
    Real Name: b'social distancing policy SWITCH self 30'
    Original Eqn: b'0'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('run')
def init_recovered_10():
    """
    Real Name: b'init Recovered 10'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('step')
def non_controlled_pop_20x50():
    """
    Real Name: b'non controlled pop 20x50'
    Original Eqn: b'non controlled population 20+non controlled population 50'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return non_controlled_population_20() + non_controlled_population_50()


@cache('run')
def social_distancing_effectiveness_20():
    """
    Real Name: b'social distancing effectiveness 20'
    Original Eqn: b'0.6'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.6


@cache('step')
def isolated_00():
    """
    Real Name: b'Isolated 00'
    Original Eqn: b'INTEG ( isolation rate symptomatic 00+isolation rate asymptomatic 00-isolated recovery rate 00\\\\ -isolated critical case rate 00, init Isolated 00)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_isolated_00()


@cache('run')
def symptomatic_duration_20():
    """
    Real Name: b'symptomatic duration 20'
    Original Eqn: b'5'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 5


@cache('run')
def symptomatic_duration_30():
    """
    Real Name: b'symptomatic duration 30'
    Original Eqn: b'5'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 5


@cache('step')
def symptomatic_rate_20():
    """
    Real Name: b'symptomatic rate 20'
    Original Eqn: b'Infected asymptomatic 20/asymptomatic duration 20*(1-fraction of asymptomatic case development 20\\\\ )'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic_20() / asymptomatic_duration_20() * (
        1 - fraction_of_asymptomatic_case_development_20())


@cache('run')
def test_fraction_10():
    """
    Real Name: b'test fraction 10'
    Original Eqn: b'1'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1


@cache('step')
def non_controlled_pop_00x60():
    """
    Real Name: b'non controlled pop 00x60'
    Original Eqn: b'non controlled population 00+non controlled population 60'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return non_controlled_population_00() + non_controlled_population_60()


@cache('step')
def recovered_10():
    """
    Real Name: b'Recovered 10'
    Original Eqn: b'INTEG ( critical cases recovery rate 10+infected asymptomatic recovery rate 10+infected symptomatic recovery rate 10\\\\ -deimmunization rate 10+isolated recovery rate 10, init Recovered 10)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_recovered_10()


@cache('step')
def infection_rate_symptomatic_70x00():
    """
    Real Name: b'infection rate symptomatic 70x00'
    Original Eqn: b'Susceptible 00*Infected symptomatic 00x70*contact infectivity symptomatic 00x70*(self quarantine policy SWITCH self 00\\\\ * self quarantine policy 00+(1-self quarantine policy SWITCH self 00))/non controlled pop 00x70'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_00() * infected_symptomatic_00x70() * contact_infectivity_symptomatic_00x70(
    ) * (self_quarantine_policy_switch_self_00() * self_quarantine_policy_00() +
         (1 - self_quarantine_policy_switch_self_00())) / non_controlled_pop_00x70()


@cache('step')
def infection_rate_symptomatic_70x10():
    """
    Real Name: b'infection rate symptomatic 70x10'
    Original Eqn: b'Susceptible 10*Infected symptomatic 10x70*contact infectivity symptomatic 10x70*(self quarantine policy SWITCH self 10\\\\ * self quarantine policy 10+(1-self quarantine policy SWITCH self 10))/non controlled pop 10x70'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_10() * infected_symptomatic_10x70() * contact_infectivity_symptomatic_10x70(
    ) * (self_quarantine_policy_switch_self_10() * self_quarantine_policy_10() +
         (1 - self_quarantine_policy_switch_self_10())) / non_controlled_pop_10x70()


@cache('run')
def init_infected_asymptomatic_10():
    """
    Real Name: b'init Infected asymptomatic 10'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('run')
def init_infected_asymptomatic_20():
    """
    Real Name: b'init Infected asymptomatic 20'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('run')
def init_infected_symptomatic_10():
    """
    Real Name: b'init Infected symptomatic 10'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('run')
def social_distancing_policy_switch_self_10():
    """
    Real Name: b'social distancing policy SWITCH self 10'
    Original Eqn: b'0'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('step')
def non_controlled_pop_00x50():
    """
    Real Name: b'non controlled pop 00x50'
    Original Eqn: b'non controlled population 00+non controlled population 50'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return non_controlled_population_00() + non_controlled_population_50()


@cache('step')
def non_controlled_pop_30x70():
    """
    Real Name: b'non controlled pop 30x70'
    Original Eqn: b'non controlled population 30+non controlled population 70'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return non_controlled_population_30() + non_controlled_population_70()


@cache('run')
def self_quarantine_effectiveness_00():
    """
    Real Name: b'self quarantine effectiveness 00'
    Original Eqn: b'0.75'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.75


@cache('run')
def self_quarantine_effectiveness_10():
    """
    Real Name: b'self quarantine effectiveness 10'
    Original Eqn: b'0.75'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.75


@cache('run')
def social_distancing_effectiveness_30():
    """
    Real Name: b'social distancing effectiveness 30'
    Original Eqn: b'0.6'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.6


@cache('step')
def infection_rate_symptomatic_80x30():
    """
    Real Name: b'infection rate symptomatic 80x30'
    Original Eqn: b'Susceptible 30*Infected symptomatic 30x80*contact infectivity symptomatic 30x80*(self quarantine policy SWITCH self 30\\\\ * self quarantine policy 30+(1-self quarantine policy SWITCH self 30))/non controlled pop 30x80'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_30() * infected_symptomatic_30x80() * contact_infectivity_symptomatic_30x80(
    ) * (self_quarantine_policy_switch_self_30() * self_quarantine_policy_30() +
         (1 - self_quarantine_policy_switch_self_30())) / non_controlled_pop_30x80()


@cache('step')
def isolated_critical_case_rate_00():
    """
    Real Name: b'isolated critical case rate 00'
    Original Eqn: b'Isolated 00*fraction of critical cases 00/symptomatic duration 00'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return isolated_00() * fraction_of_critical_cases_00() / symptomatic_duration_00()


@cache('run')
def test_fraction_00():
    """
    Real Name: b'test fraction 00'
    Original Eqn: b'1'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1


@cache('step')
def symptomatic_rate_10():
    """
    Real Name: b'symptomatic rate 10'
    Original Eqn: b'Infected asymptomatic 10/asymptomatic duration 10*(1-fraction of asymptomatic case development 10\\\\ )'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic_10() / asymptomatic_duration_10() * (
        1 - fraction_of_asymptomatic_case_development_10())


@cache('step')
def social_distancing_policy_30():
    """
    Real Name: b'social distancing policy 30'
    Original Eqn: b'1-PULSE(social distancing start 30, social distancing end 30-social distancing start 30\\\\ )*social distancing effectiveness 30'
    Units: b'dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return 1 - functions.pulse(__data['time'], social_distancing_start_30(),
                               social_distancing_end_30() - social_distancing_start_30()
                               ) * social_distancing_effectiveness_30()


@cache('step')
def non_controlled_pop_10x20():
    """
    Real Name: b'non controlled pop 10x20'
    Original Eqn: b'non controlled population 10+non controlled population 20'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return non_controlled_population_10() + non_controlled_population_20()


@cache('step')
def infection_rate_symptomatic_self_10():
    """
    Real Name: b'infection rate symptomatic self 10'
    Original Eqn: b'Infected symptomatic 10*Susceptible 10*contact infectivity symptomatic self 10*(self quarantine policy SWITCH self 10\\\\ *self quarantine policy 10+(1-self quarantine policy SWITCH self 10))/non controlled population 10'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_10() * susceptible_10() * contact_infectivity_symptomatic_self_10(
    ) * (self_quarantine_policy_switch_self_10() * self_quarantine_policy_10() +
         (1 - self_quarantine_policy_switch_self_10())) / non_controlled_population_10()


@cache('step')
def infection_rate_symptomatic_self_20():
    """
    Real Name: b'infection rate symptomatic self 20'
    Original Eqn: b'Infected symptomatic 20*Susceptible 20*contact infectivity symptomatic self 20*(self quarantine policy SWITCH self 20\\\\ *self quarantine policy 20+(1-self quarantine policy SWITCH self 20))/non controlled population 20'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_20() * susceptible_20() * contact_infectivity_symptomatic_self_20(
    ) * (self_quarantine_policy_switch_self_20() * self_quarantine_policy_20() +
         (1 - self_quarantine_policy_switch_self_20())) / non_controlled_population_20()


@cache('step')
def total_infected_40():
    """
    Real Name: b'total infected 40'
    Original Eqn: b'Infected asymptomatic 40+Infected symptomatic 40'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic_40() + infected_symptomatic_40()


@cache('step')
def new_cases_40():
    """
    Real Name: b'new cases 40'
    Original Eqn: b'symptomatic rate 40*test fraction 40'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return symptomatic_rate_40() * test_fraction_40()


@cache('run')
def social_distancing_effectiveness_40():
    """
    Real Name: b'social distancing effectiveness 40'
    Original Eqn: b'0.6'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.6


@cache('run')
def self_quarantine_effectiveness_40():
    """
    Real Name: b'self quarantine effectiveness 40'
    Original Eqn: b'0.75'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.75


@cache('step')
def social_distancing_policy_20():
    """
    Real Name: b'social distancing policy 20'
    Original Eqn: b'1-PULSE(social distancing start 20, social distancing end 20-social distancing start 20\\\\ )*social distancing effectiveness 20'
    Units: b'dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return 1 - functions.pulse(__data['time'], social_distancing_start_20(),
                               social_distancing_end_20() - social_distancing_start_20()
                               ) * social_distancing_effectiveness_20()


@cache('step')
def susceptible_20():
    """
    Real Name: b'Susceptible 20'
    Original Eqn: b'INTEG ( deimmunization rate 20-infection rate 20, init Susceptible 20)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_susceptible_20()


@cache('run')
def self_quarantine_end_80():
    """
    Real Name: b'self quarantine end 80'
    Original Eqn: b'50'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 50


@cache('run')
def symptomatic_duration_10():
    """
    Real Name: b'symptomatic duration 10'
    Original Eqn: b'5'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 5


@cache('step')
def symptomatic_rate_00():
    """
    Real Name: b'symptomatic rate 00'
    Original Eqn: b'Infected asymptomatic 00/asymptomatic duration 00*(1-fraction of asymptomatic case development 00\\\\ )'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic_00() / asymptomatic_duration_00() * (
        1 - fraction_of_asymptomatic_case_development_00())


@cache('step')
def social_distancing_policy_10():
    """
    Real Name: b'social distancing policy 10'
    Original Eqn: b'1-PULSE(social distancing start 10, social distancing end 10-social distancing start 10\\\\ )*social distancing effectiveness 10'
    Units: b'dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return 1 - functions.pulse(__data['time'], social_distancing_start_10(),
                               social_distancing_end_10() - social_distancing_start_10()
                               ) * social_distancing_effectiveness_10()


@cache('run')
def social_distancing_end_20():
    """
    Real Name: b'social distancing end 20'
    Original Eqn: b'50'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 50


@cache('run')
def social_distancing_end_30():
    """
    Real Name: b'social distancing end 30'
    Original Eqn: b'50'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 50


@cache('run')
def self_quarantine_start_40():
    """
    Real Name: b'self quarantine start 40'
    Original Eqn: b'21'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 21


@cache('run')
def isolation_effectiveness_00():
    """
    Real Name: b'isolation effectiveness 00'
    Original Eqn: b'0.9'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.9


@cache('step')
def non_controlled_pop_40x50():
    """
    Real Name: b'non controlled pop 40x50'
    Original Eqn: b'non controlled population 40+non controlled population 50'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return non_controlled_population_40() + non_controlled_population_50()


@cache('step')
def non_controlled_pop_40x60():
    """
    Real Name: b'non controlled pop 40x60'
    Original Eqn: b'non controlled population 40+non controlled population 60'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return non_controlled_population_40() + non_controlled_population_60()


@cache('step')
def recovered_20():
    """
    Real Name: b'Recovered 20'
    Original Eqn: b'INTEG ( critical cases recovery rate 20+infected asymptomatic recovery rate 20+infected symptomatic recovery rate 20\\\\ -deimmunization rate 20+isolated recovery rate 20, init Recovered 20)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_recovered_20()


@cache('run')
def self_quarantine_end_10():
    """
    Real Name: b'self quarantine end 10'
    Original Eqn: b'50'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 50


@cache('run')
def self_quarantine_end_00():
    """
    Real Name: b'self quarantine end 00'
    Original Eqn: b'50'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 50


@cache('run')
def self_quarantine_effectiveness_30():
    """
    Real Name: b'self quarantine effectiveness 30'
    Original Eqn: b'0.75'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.75


@cache('run')
def init_recovered_20():
    """
    Real Name: b'init Recovered 20'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('run')
def social_distancing_end_10():
    """
    Real Name: b'social distancing end 10'
    Original Eqn: b'50'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 50


@cache('step')
def total_infected_20():
    """
    Real Name: b'total infected 20'
    Original Eqn: b'Infected asymptomatic 20+Infected symptomatic 20'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic_20() + infected_symptomatic_20()


@cache('step')
def recovered_40():
    """
    Real Name: b'Recovered 40'
    Original Eqn: b'INTEG ( critical cases recovery rate 40+infected asymptomatic recovery rate 40+infected symptomatic recovery rate 40\\\\ -deimmunization rate 40+isolated recovery rate 40, init Recovered 40)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_recovered_40()


@cache('run')
def self_quarantine_start_30():
    """
    Real Name: b'self quarantine start 30'
    Original Eqn: b'21'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 21


@cache('step')
def recovered_30():
    """
    Real Name: b'Recovered 30'
    Original Eqn: b'INTEG ( critical cases recovery rate 30+infected asymptomatic recovery rate 30+infected symptomatic recovery rate 30\\\\ -deimmunization rate 30+isolated recovery rate 30, init Recovered 30)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_recovered_30()


@cache('step')
def non_controlled_pop_30x80():
    """
    Real Name: b'non controlled pop 30x80'
    Original Eqn: b'non controlled population 30+non controlled population 80'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return non_controlled_population_30() + non_controlled_population_80()


@cache('step')
def infection_rate_symptomatic_80x60():
    """
    Real Name: b'infection rate symptomatic 80x60'
    Original Eqn: b'Susceptible 60*Infected symptomatic 60x80*contact infectivity symptomatic 60x80*(self quarantine policy SWITCH self 60\\\\ * self quarantine policy 60+(1-self quarantine policy SWITCH self 60))/non controlled pop 60x80'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_60() * infected_symptomatic_60x80() * contact_infectivity_symptomatic_60x80(
    ) * (self_quarantine_policy_switch_self_60() * self_quarantine_policy_60() +
         (1 - self_quarantine_policy_switch_self_60())) / non_controlled_pop_60x80()


@cache('step')
def accumulated_cases_50():
    """
    Real Name: b'accumulated cases 50'
    Original Eqn: b'INTEG ( new cases 50, init accumulated cases 50)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_accumulated_cases_50()


@cache('step')
def accumulated_cases_60():
    """
    Real Name: b'accumulated cases 60'
    Original Eqn: b'INTEG ( new cases 60, init accumulated cases 60)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_accumulated_cases_60()


@cache('step')
def infection_rate_symptomatic_self_50():
    """
    Real Name: b'infection rate symptomatic self 50'
    Original Eqn: b'Infected symptomatic 50*Susceptible 50*contact infectivity symptomatic self 50*(self quarantine policy SWITCH self 50\\\\ *self quarantine policy 50+(1-self quarantine policy SWITCH self 50))/non controlled population 50'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_50() * susceptible_50() * contact_infectivity_symptomatic_self_50(
    ) * (self_quarantine_policy_switch_self_50() * self_quarantine_policy_50() +
         (1 - self_quarantine_policy_switch_self_50())) / non_controlled_population_50()


@cache('step')
def infection_rate_symptomatic_self_60():
    """
    Real Name: b'infection rate symptomatic self 60'
    Original Eqn: b'Infected symptomatic 60*Susceptible 60*contact infectivity symptomatic self 60*(self quarantine policy SWITCH self 60\\\\ *self quarantine policy 60+(1-self quarantine policy SWITCH self 60))/non controlled population 60'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_60() * susceptible_60() * contact_infectivity_symptomatic_self_60(
    ) * (self_quarantine_policy_switch_self_60() * self_quarantine_policy_60() +
         (1 - self_quarantine_policy_switch_self_60())) / non_controlled_population_60()


@cache('step')
def contacts_per_person_symptomatic_50x60():
    """
    Real Name: b'contacts per person symptomatic 50x60'
    Original Eqn: b'contacts per person normal 50x60*(symptomatic contact fraction 60+symptomatic contact fraction 50\\\\ )/2'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_50x60() * (symptomatic_contact_fraction_60() +
                                                 symptomatic_contact_fraction_50()) / 2


@cache('run')
def asymptomatic_duration_50():
    """
    Real Name: b'asymptomatic duration 50'
    Original Eqn: b'5'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 5


@cache('run')
def asymptomatic_duration_60():
    """
    Real Name: b'asymptomatic duration 60'
    Original Eqn: b'5'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 5


@cache('run')
def infection_start_50():
    """
    Real Name: b'infection start 50'
    Original Eqn: b'-1'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return -1


@cache('run')
def infection_start_60():
    """
    Real Name: b'infection start 60'
    Original Eqn: b'-1'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return -1


@cache('run')
def infection_start_70():
    """
    Real Name: b'infection start 70'
    Original Eqn: b'-1'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return -1


@cache('run')
def infection_start_80():
    """
    Real Name: b'infection start 80'
    Original Eqn: b'20'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 20


@cache('run')
def fraction_of_death_60():
    """
    Real Name: b'fraction of death 60'
    Original Eqn: b'0.4'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.4


@cache('step')
def contacts_per_person_symptomatic_self_60():
    """
    Real Name: b'contacts per person symptomatic self 60'
    Original Eqn: b'contacts per person normal self 60*symptomatic contact fraction 60'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_self_60() * symptomatic_contact_fraction_60()


@cache('step')
def case_fatality_rate_50():
    """
    Real Name: b'case fatality rate 50'
    Original Eqn: b'ZIDZ( Diseased 50, accumulated cases 50)'
    Units: b'dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.zidz(diseased_50(), accumulated_cases_50())


@cache('step')
def case_fatality_rate_60():
    """
    Real Name: b'case fatality rate 60'
    Original Eqn: b'ZIDZ( Diseased 60, accumulated cases 60)'
    Units: b'dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.zidz(diseased_60(), accumulated_cases_60())


@cache('step')
def fraction_of_symptomatic_50():
    """
    Real Name: b'fraction of symptomatic 50'
    Original Eqn: b'ZIDZ(Infected symptomatic 50, total infected 50)'
    Units: b'dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.zidz(infected_symptomatic_50(), total_infected_50())


@cache('step')
def fraction_of_symptomatic_60():
    """
    Real Name: b'fraction of symptomatic 60'
    Original Eqn: b'ZIDZ(Infected symptomatic 60, total infected 60)'
    Units: b'dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.zidz(infected_symptomatic_60(), total_infected_60())


@cache('step')
def contact_infectivity_asymptomatic_50x60():
    """
    Real Name: b'contact infectivity asymptomatic 50x60'
    Original Eqn: b'contacts per person normal 50x60*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_50x60() * infectivity_per_contact()


@cache('step')
def contact_infectivity_asymptomatic_50x70():
    """
    Real Name: b'contact infectivity asymptomatic 50x70'
    Original Eqn: b'contacts per person normal 50x70*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_50x70() * infectivity_per_contact()


@cache('step')
def contact_infectivity_asymptomatic_50x80():
    """
    Real Name: b'contact infectivity asymptomatic 50x80'
    Original Eqn: b'contacts per person normal 50x80*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_50x80() * infectivity_per_contact()


@cache('step')
def contact_infectivity_asymptomatic_60x70():
    """
    Real Name: b'contact infectivity asymptomatic 60x70'
    Original Eqn: b'contacts per person normal 60x70*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_60x70() * infectivity_per_contact()


@cache('step')
def contact_infectivity_asymptomatic_60x80():
    """
    Real Name: b'contact infectivity asymptomatic 60x80'
    Original Eqn: b'contacts per person normal 60x80*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_60x80() * infectivity_per_contact()


@cache('step')
def recovered_50():
    """
    Real Name: b'Recovered 50'
    Original Eqn: b'INTEG ( critical cases recovery rate 50+infected asymptomatic recovery rate 50+infected symptomatic recovery rate 50\\\\ -deimmunization rate 50+isolated recovery rate 50, init Recovered 50)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_recovered_50()


@cache('step')
def recovered_60():
    """
    Real Name: b'Recovered 60'
    Original Eqn: b'INTEG ( critical cases recovery rate 60+infected asymptomatic recovery rate 60+infected symptomatic recovery rate 60\\\\ -deimmunization rate 60+isolated recovery rate 60, init Recovered 60)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_recovered_60()


@cache('step')
def contact_infectivity_asymptomatic_self_50():
    """
    Real Name: b'contact infectivity asymptomatic self 50'
    Original Eqn: b'contacts per person normal self 50*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_self_50() * infectivity_per_contact()


@cache('step')
def contact_infectivity_asymptomatic_self_60():
    """
    Real Name: b'contact infectivity asymptomatic self 60'
    Original Eqn: b'contacts per person normal self 60*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_self_60() * infectivity_per_contact()


@cache('step')
def incidence_per_100000_60():
    """
    Real Name: b'incidence per 100000 60'
    Original Eqn: b'accumulated cases 60/init total population 60*100000'
    Units: b'dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return accumulated_cases_60() / init_total_population_60() * 100000


@cache('run')
def self_quarantine_effectiveness_50():
    """
    Real Name: b'self quarantine effectiveness 50'
    Original Eqn: b'0.75'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.75


@cache('run')
def self_quarantine_effectiveness_60():
    """
    Real Name: b'self quarantine effectiveness 60'
    Original Eqn: b'0.75'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.75


@cache('step')
def contact_infectivity_quarantine_self_50():
    """
    Real Name: b'contact infectivity quarantine self 50'
    Original Eqn: b'contact infectivity asymptomatic self 50*(1-isolation effectiveness 50)'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contact_infectivity_asymptomatic_self_50() * (1 - isolation_effectiveness_50())


@cache('step')
def contact_infectivity_quarantine_self_60():
    """
    Real Name: b'contact infectivity quarantine self 60'
    Original Eqn: b'contact infectivity asymptomatic self 60*(1-isolation effectiveness 60)'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contact_infectivity_asymptomatic_self_60() * (1 - isolation_effectiveness_60())


@cache('step')
def infected_asymptomatic_50x60():
    """
    Real Name: b'Infected asymptomatic 50x60'
    Original Eqn: b'Infected asymptomatic 50+Infected asymptomatic 60'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic_50() + infected_asymptomatic_60()


@cache('step')
def infected_asymptomatic_50x70():
    """
    Real Name: b'Infected asymptomatic 50x70'
    Original Eqn: b'Infected asymptomatic 50+Infected asymptomatic 70'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic_50() + infected_asymptomatic_70()


@cache('step')
def contact_infectivity_symptomatic_50x60():
    """
    Real Name: b'contact infectivity symptomatic 50x60'
    Original Eqn: b'contacts per person symptomatic 50x60*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_symptomatic_50x60() * infectivity_per_contact()


@cache('step')
def contact_infectivity_symptomatic_50x70():
    """
    Real Name: b'contact infectivity symptomatic 50x70'
    Original Eqn: b'contacts per person symptomatic 50x70*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_symptomatic_50x70() * infectivity_per_contact()


@cache('step')
def contact_infectivity_symptomatic_50x80():
    """
    Real Name: b'contact infectivity symptomatic 50x80'
    Original Eqn: b'contacts per person symptomatic 50x80*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_symptomatic_50x80() * infectivity_per_contact()


@cache('step')
def contact_infectivity_symptomatic_60x70():
    """
    Real Name: b'contact infectivity symptomatic 60x70'
    Original Eqn: b'contacts per person symptomatic 60x70*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_symptomatic_60x70() * infectivity_per_contact()


@cache('step')
def contact_infectivity_symptomatic_60x80():
    """
    Real Name: b'contact infectivity symptomatic 60x80'
    Original Eqn: b'contacts per person symptomatic 60x80*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_symptomatic_60x80() * infectivity_per_contact()


@cache('run')
def self_quarantine_policy_switch_self_60():
    """
    Real Name: b'self quarantine policy SWITCH self 60'
    Original Eqn: b'0'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('run')
def init_isolated_50():
    """
    Real Name: b'init Isolated 50'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('step')
def contact_infectivity_symptomatic_self_50():
    """
    Real Name: b'contact infectivity symptomatic self 50'
    Original Eqn: b'contacts per person symptomatic self 50*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_symptomatic_self_50() * infectivity_per_contact()


@cache('step')
def contact_infectivity_symptomatic_self_60():
    """
    Real Name: b'contact infectivity symptomatic self 60'
    Original Eqn: b'contacts per person symptomatic self 60*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_symptomatic_self_60() * infectivity_per_contact()


@cache('step')
def infected_asymptomatic_recovery_rate_60():
    """
    Real Name: b'infected asymptomatic recovery rate 60'
    Original Eqn: b'fraction of asymptomatic case development 60*Infected asymptomatic 60/(asymptomatic duration 60\\\\ +symptomatic duration 60)'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return fraction_of_asymptomatic_case_development_60() * infected_asymptomatic_60() / (
        asymptomatic_duration_60() + symptomatic_duration_60())


@cache('run')
def self_quarantine_start_60():
    """
    Real Name: b'self quarantine start 60'
    Original Eqn: b'21'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 21


@cache('run')
def contacts_per_person_normal_50x60():
    """
    Real Name: b'contacts per person normal 50x60'
    Original Eqn: b'10'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 10


@cache('run')
def contacts_per_person_normal_50x70():
    """
    Real Name: b'contacts per person normal 50x70'
    Original Eqn: b'10'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 10


@cache('run')
def contacts_per_person_normal_50x80():
    """
    Real Name: b'contacts per person normal 50x80'
    Original Eqn: b'10'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 10


@cache('run')
def contacts_per_person_normal_60x70():
    """
    Real Name: b'contacts per person normal 60x70'
    Original Eqn: b'10'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 10


@cache('run')
def contacts_per_person_normal_60x80():
    """
    Real Name: b'contacts per person normal 60x80'
    Original Eqn: b'10'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 10


@cache('run')
def init_susceptible_50():
    """
    Real Name: b'init Susceptible 50'
    Original Eqn: b'8e+06'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 8e+06


@cache('run')
def init_susceptible_60():
    """
    Real Name: b'init Susceptible 60'
    Original Eqn: b'8e+06'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 8e+06


@cache('run')
def contacts_per_person_normal_self_50():
    """
    Real Name: b'contacts per person normal self 50'
    Original Eqn: b'30'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 30


@cache('run')
def contacts_per_person_normal_self_60():
    """
    Real Name: b'contacts per person normal self 60'
    Original Eqn: b'30'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 30


@cache('step')
def infected_symptomatic_50x70():
    """
    Real Name: b'Infected symptomatic 50x70'
    Original Eqn: b'Infected symptomatic 50+Infected symptomatic 70'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_50() + infected_symptomatic_70()


@cache('step')
def init_total_population_50():
    """
    Real Name: b'init total population 50'
    Original Eqn: b'init Infected asymptomatic 50+init Susceptible 50'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return init_infected_asymptomatic_50() + init_susceptible_50()


@cache('step')
def non_controlled_pop_60x80():
    """
    Real Name: b'non controlled pop 60x80'
    Original Eqn: b'non controlled population 60+non controlled population 80'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return non_controlled_population_60() + non_controlled_population_80()


@cache('step')
def contacts_per_person_symptomatic_50x70():
    """
    Real Name: b'contacts per person symptomatic 50x70'
    Original Eqn: b'contacts per person normal 50x70*(symptomatic contact fraction 70+symptomatic contact fraction 50\\\\ )/2'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_50x70() * (symptomatic_contact_fraction_70() +
                                                 symptomatic_contact_fraction_50()) / 2


@cache('step')
def contacts_per_person_symptomatic_50x80():
    """
    Real Name: b'contacts per person symptomatic 50x80'
    Original Eqn: b'contacts per person normal 50x80*(symptomatic contact fraction 80+symptomatic contact fraction 50\\\\ )/2'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_50x80() * (symptomatic_contact_fraction_80() +
                                                 symptomatic_contact_fraction_50()) / 2


@cache('step')
def contacts_per_person_symptomatic_60x70():
    """
    Real Name: b'contacts per person symptomatic 60x70'
    Original Eqn: b'contacts per person normal 60x70*(symptomatic contact fraction 70+symptomatic contact fraction 60\\\\ )/2'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_60x70() * (symptomatic_contact_fraction_70() +
                                                 symptomatic_contact_fraction_60()) / 2


@cache('step')
def contacts_per_person_symptomatic_60x80():
    """
    Real Name: b'contacts per person symptomatic 60x80'
    Original Eqn: b'contacts per person normal 60x80*(symptomatic contact fraction 80+symptomatic contact fraction 60\\\\ )/2'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_60x80() * (symptomatic_contact_fraction_80() +
                                                 symptomatic_contact_fraction_60()) / 2


@cache('step')
def isolated_60():
    """
    Real Name: b'Isolated 60'
    Original Eqn: b'INTEG ( isolation rate symptomatic 60+isolation rate asymptomatic 60-isolated recovery rate 60\\\\ -isolated critical case rate 60, init Isolated 60)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_isolated_60()


@cache('step')
def isolated_50():
    """
    Real Name: b'Isolated 50'
    Original Eqn: b'INTEG ( isolation rate symptomatic 50+isolation rate asymptomatic 50-isolated recovery rate 50\\\\ -isolated critical case rate 50, init Isolated 50)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_isolated_50()


@cache('step')
def contacts_per_person_symptomatic_self_50():
    """
    Real Name: b'contacts per person symptomatic self 50'
    Original Eqn: b'contacts per person normal self 50*symptomatic contact fraction 50'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_self_50() * symptomatic_contact_fraction_50()


@cache('run')
def normal_first_infected():
    """
    Real Name: b'normal first infected'
    Original Eqn: b'1'
    Units: b'person/Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1


@cache('step')
def isolated_critical_case_rate_50():
    """
    Real Name: b'isolated critical case rate 50'
    Original Eqn: b'Isolated 50*fraction of critical cases 50/symptomatic duration 50'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return isolated_50() * fraction_of_critical_cases_50() / symptomatic_duration_50()


@cache('step')
def isolated_critical_case_rate_60():
    """
    Real Name: b'isolated critical case rate 60'
    Original Eqn: b'Isolated 60*fraction of critical cases 60/symptomatic duration 60'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return isolated_60() * fraction_of_critical_cases_60() / symptomatic_duration_60()


@cache('step')
def critical_cases_50():
    """
    Real Name: b'Critical Cases 50'
    Original Eqn: b'INTEG ( infected critical case rate 50-critical cases recovery rate 50-death rate 50+isolated critical case rate 50\\\\ , init Critical Cases 50)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_critical_cases_50()


@cache('step')
def critical_cases_60():
    """
    Real Name: b'Critical Cases 60'
    Original Eqn: b'INTEG ( infected critical case rate 60-critical cases recovery rate 60-death rate 60+isolated critical case rate 60\\\\ , init Critical Cases 60)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_critical_cases_60()


@cache('step')
def isolated_recovery_rate_50():
    """
    Real Name: b'isolated recovery rate 50'
    Original Eqn: b'Isolated 50*(1-fraction of critical cases 50)/isolation duration 50'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return isolated_50() * (1 - fraction_of_critical_cases_50()) / isolation_duration_50()


@cache('step')
def isolated_recovery_rate_60():
    """
    Real Name: b'isolated recovery rate 60'
    Original Eqn: b'Isolated 60*(1-fraction of critical cases 60)/isolation duration 60'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return isolated_60() * (1 - fraction_of_critical_cases_60()) / isolation_duration_60()


@cache('step')
def infection_rate_asymptomatic_50x60():
    """
    Real Name: b'infection rate asymptomatic 50x60'
    Original Eqn: b'contact infectivity asymptomatic 50x60*(social distancing policy SWITCH self 60*social distancing policy 60\\\\ +(1-social distancing policy SWITCH self 60))*Infected asymptomatic 50x60*Susceptible 60\\\\ /non controlled pop 50x60'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contact_infectivity_asymptomatic_50x60() * (
        social_distancing_policy_switch_self_60() * social_distancing_policy_60() +
        (1 - social_distancing_policy_switch_self_60())
    ) * infected_asymptomatic_50x60() * susceptible_60() / non_controlled_pop_50x60()


@cache('step')
def critical_cases_recovery_rate_50():
    """
    Real Name: b'critical cases recovery rate 50'
    Original Eqn: b'Critical Cases 50*(1-fraction of death 50)/duration of treatment 50'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return critical_cases_50() * (1 - fraction_of_death_50()) / duration_of_treatment_50()


@cache('step')
def critical_cases_recovery_rate_60():
    """
    Real Name: b'critical cases recovery rate 60'
    Original Eqn: b'Critical Cases 60*(1-fraction of death 60)/duration of treatment 60'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return critical_cases_60() * (1 - fraction_of_death_60()) / duration_of_treatment_60()


@cache('run')
def isolation_duration_50():
    """
    Real Name: b'isolation duration 50'
    Original Eqn: b'14'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 14


@cache('run')
def isolation_duration_60():
    """
    Real Name: b'isolation duration 60'
    Original Eqn: b'14'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 14


@cache('step')
def infection_rate_asymptomatic_60x80():
    """
    Real Name: b'infection rate asymptomatic 60x80'
    Original Eqn: b'contact infectivity asymptomatic 60x80*(social distancing policy SWITCH self 80*social distancing policy 80\\\\ +(1-social distancing policy SWITCH self 80))*Infected asymptomatic 60x80*Susceptible 80\\\\ /non controlled pop 60x80'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contact_infectivity_asymptomatic_60x80() * (
        social_distancing_policy_switch_self_80() * social_distancing_policy_80() +
        (1 - social_distancing_policy_switch_self_80())
    ) * infected_asymptomatic_60x80() * susceptible_80() / non_controlled_pop_60x80()


@cache('step')
def death_rate_50():
    """
    Real Name: b'death rate 50'
    Original Eqn: b'Critical Cases 50*fraction of death 50/duration of treatment 50'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return critical_cases_50() * fraction_of_death_50() / duration_of_treatment_50()


@cache('step')
def death_rate_60():
    """
    Real Name: b'death rate 60'
    Original Eqn: b'Critical Cases 60*fraction of death 60/duration of treatment 60'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return critical_cases_60() * fraction_of_death_60() / duration_of_treatment_60()


@cache('run')
def isolation_effectiveness_50():
    """
    Real Name: b'isolation effectiveness 50'
    Original Eqn: b'0.9'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.9


@cache('run')
def isolation_effectiveness_60():
    """
    Real Name: b'isolation effectiveness 60'
    Original Eqn: b'0.9'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.9


@cache('step')
def infection_rate_asymptomatic_80x60():
    """
    Real Name: b'infection rate asymptomatic 80x60'
    Original Eqn: b'Susceptible 60*Infected asymptomatic 60x80*contact infectivity asymptomatic 60x80*(social distancing policy SWITCH self 60 *social distancing policy 60+(1-social distancing policy SWITCH self 60))/non controlled pop 60x80'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_60() * infected_asymptomatic_60x80(
    ) * contact_infectivity_asymptomatic_60x80() * (
        social_distancing_policy_switch_self_60() * social_distancing_policy_60() +
        (1 - social_distancing_policy_switch_self_60())) / non_controlled_pop_60x80()


@cache('step')
def deimmunization_rate_50():
    """
    Real Name: b'deimmunization rate 50'
    Original Eqn: b'Recovered 50/immunity time 50'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return recovered_50() / immunity_time_50()


@cache('step')
def deimmunization_rate_60():
    """
    Real Name: b'deimmunization rate 60'
    Original Eqn: b'Recovered 60/immunity time 60'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return recovered_60() / immunity_time_60()


@cache('step')
def isolation_rate_asymptomatic_50():
    """
    Real Name: b'isolation rate asymptomatic 50'
    Original Eqn: b'MIN(available test kits for testing asymptomatic*effect of kits availability on effectiveness of testing\\\\ /kits per person, Infected asymptomatic 50 )/testing duration'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return np.minimum(
        available_test_kits_for_testing_asymptomatic() *
        effect_of_kits_availability_on_effectiveness_of_testing() / kits_per_person(),
        infected_asymptomatic_50()) / testing_duration()


@cache('step')
def isolation_rate_asymptomatic_60():
    """
    Real Name: b'isolation rate asymptomatic 60'
    Original Eqn: b'MIN(available test kits for testing asymptomatic*effect of kits availability on effectiveness of testing\\\\ /kits per person, Infected asymptomatic 60 )/testing duration'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return np.minimum(
        available_test_kits_for_testing_asymptomatic() *
        effect_of_kits_availability_on_effectiveness_of_testing() / kits_per_person(),
        infected_asymptomatic_60()) / testing_duration()


@cache('step')
def infected_asymptomatic_60():
    """
    Real Name: b'Infected asymptomatic 60'
    Original Eqn: b'INTEG ( infection rate 60-infected asymptomatic recovery rate 60-isolation rate asymptomatic 60\\\\ -symptomatic rate 60, init Infected asymptomatic 60)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_infected_asymptomatic_60()


@cache('step')
def diseased_50():
    """
    Real Name: b'Diseased 50'
    Original Eqn: b'INTEG ( death rate 50, init Diseased 50)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_diseased_50()


@cache('step')
def diseased_60():
    """
    Real Name: b'Diseased 60'
    Original Eqn: b'INTEG ( death rate 60, init Diseased 60)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_diseased_60()


@cache('step')
def isolation_rate_symptomatic_50():
    """
    Real Name: b'isolation rate symptomatic 50'
    Original Eqn: b'tests for symptomatic/kits per person/testing duration'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return tests_for_symptomatic() / kits_per_person() / testing_duration()


@cache('step')
def isolation_rate_symptomatic_60():
    """
    Real Name: b'isolation rate symptomatic 60'
    Original Eqn: b'tests for symptomatic/kits per person/testing duration'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return tests_for_symptomatic() / kits_per_person() / testing_duration()


@cache('step')
def infection_rate_quarantined_self_60():
    """
    Real Name: b'infection rate quarantined self 60'
    Original Eqn: b'Isolated 60*Susceptible 60*contact infectivity quarantine self 60/non controlled population 60'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return isolated_60() * susceptible_60() * contact_infectivity_quarantine_self_60(
    ) / non_controlled_population_60()


@cache('run')
def duration_of_treatment_50():
    """
    Real Name: b'duration of treatment 50'
    Original Eqn: b'10'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 10


@cache('run')
def duration_of_treatment_60():
    """
    Real Name: b'duration of treatment 60'
    Original Eqn: b'10'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 10


@cache('step')
def infection_rate_symptomatic_50x70():
    """
    Real Name: b'infection rate symptomatic 50x70'
    Original Eqn: b'Susceptible 70*Infected symptomatic 50x70*contact infectivity symptomatic 50x70*(self quarantine policy SWITCH self 70\\\\ *self quarantine policy 70+(1-self quarantine policy SWITCH self 70))/non controlled pop 50x70'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_70() * infected_symptomatic_50x70() * contact_infectivity_symptomatic_50x70(
    ) * (self_quarantine_policy_switch_self_70() * self_quarantine_policy_70() +
         (1 - self_quarantine_policy_switch_self_70())) / non_controlled_pop_50x70()


@cache('step')
def infection_rate_symptomatic_50x80():
    """
    Real Name: b'infection rate symptomatic 50x80'
    Original Eqn: b'Susceptible 80*Infected symptomatic 50x80*contact infectivity symptomatic 50x80*(self quarantine policy SWITCH self 80\\\\ *self quarantine policy 80+(1-self quarantine policy SWITCH self 80))/non controlled pop 50x80'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_80() * infected_symptomatic_50x80() * contact_infectivity_symptomatic_50x80(
    ) * (self_quarantine_policy_switch_self_80() * self_quarantine_policy_80() +
         (1 - self_quarantine_policy_switch_self_80())) / non_controlled_pop_50x80()


@cache('step')
def infection_rate_symptomatic_60x50():
    """
    Real Name: b'infection rate symptomatic 60x50'
    Original Eqn: b'Susceptible 50*Infected symptomatic 50x60*contact infectivity symptomatic 50x60*(self quarantine policy SWITCH self 50\\\\ * self quarantine policy 50+(1-self quarantine policy SWITCH self 50))/non controlled pop 50x60'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_50() * infected_symptomatic_50x60() * contact_infectivity_symptomatic_50x60(
    ) * (self_quarantine_policy_switch_self_50() * self_quarantine_policy_50() +
         (1 - self_quarantine_policy_switch_self_50())) / non_controlled_pop_50x60()


@cache('step')
def first_infection_50():
    """
    Real Name: b'first infection 50'
    Original Eqn: b'PULSE(infection start 50, 1)*normal first infected'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.pulse(__data['time'], infection_start_50(), 1) * normal_first_infected()


@cache('step')
def first_infection_60():
    """
    Real Name: b'first infection 60'
    Original Eqn: b'PULSE(infection start 60, 1)*normal first infected'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.pulse(__data['time'], infection_start_60(), 1) * normal_first_infected()


@cache('step')
def first_infection_70():
    """
    Real Name: b'first infection 70'
    Original Eqn: b'PULSE(infection start 70, 1)*normal first infected'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.pulse(__data['time'], infection_start_70(), 1) * normal_first_infected()


@cache('step')
def first_infection_80():
    """
    Real Name: b'first infection 80'
    Original Eqn: b'PULSE(infection start 80, 1)*normal first infected'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.pulse(__data['time'], infection_start_80(), 1) * normal_first_infected()


@cache('step')
def non_controlled_pop_50x60():
    """
    Real Name: b'non controlled pop 50x60'
    Original Eqn: b'non controlled population 50+non controlled population 60'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return non_controlled_population_50() + non_controlled_population_60()


@cache('run')
def fraction_of_asymptomatic_case_development_50():
    """
    Real Name: b'fraction of asymptomatic case development 50'
    Original Eqn: b'0.5'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.5


@cache('run')
def fraction_of_asymptomatic_case_development_60():
    """
    Real Name: b'fraction of asymptomatic case development 60'
    Original Eqn: b'0.5'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.5


@cache('step')
def non_controlled_pop_60x70():
    """
    Real Name: b'non controlled pop 60x70'
    Original Eqn: b'non controlled population 60+non controlled population 70'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return non_controlled_population_60() + non_controlled_population_70()


@cache('step')
def infected_symptomatic_50x80():
    """
    Real Name: b'Infected symptomatic 50x80'
    Original Eqn: b'Infected symptomatic 50+Infected symptomatic 80'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_50() + infected_symptomatic_80()


@cache('step')
def infected_symptomatic_60():
    """
    Real Name: b'Infected symptomatic 60'
    Original Eqn: b'INTEG ( symptomatic rate 60-infected critical case rate 60-infected symptomatic recovery rate 60\\\\ -isolation rate symptomatic 60, init Infected symptomatic 60)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_infected_symptomatic_60()


@cache('run')
def fraction_of_critical_cases_50():
    """
    Real Name: b'fraction of critical cases 50'
    Original Eqn: b'0.1'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.1


@cache('run')
def fraction_of_critical_cases_60():
    """
    Real Name: b'fraction of critical cases 60'
    Original Eqn: b'0.1'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.1


@cache('step')
def non_controlled_population_60():
    """
    Real Name: b'non controlled population 60'
    Original Eqn: b'Infected symptomatic 60+Susceptible 60+Infected asymptomatic 60+Isolated 60+Recovered 60'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_60() + susceptible_60() + infected_asymptomatic_60() + isolated_60(
    ) + recovered_60()


@cache('step')
def non_controlled_population_50():
    """
    Real Name: b'non controlled population 50'
    Original Eqn: b'Infected symptomatic 50+Susceptible 50+Infected asymptomatic 50+Isolated 50+Recovered 50'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_50() + susceptible_50() + infected_asymptomatic_50() + isolated_50(
    ) + recovered_50()


@cache('run')
def fraction_of_death_50():
    """
    Real Name: b'fraction of death 50'
    Original Eqn: b'0.4'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.4


@cache('step')
def infected_symptomatic_recovery_rate_50():
    """
    Real Name: b'infected symptomatic recovery rate 50'
    Original Eqn: b'Infected symptomatic 50*(1-fraction of critical cases 50)/symptomatic duration 50'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_50() * (
        1 - fraction_of_critical_cases_50()) / symptomatic_duration_50()


@cache('step')
def infected_symptomatic_recovery_rate_60():
    """
    Real Name: b'infected symptomatic recovery rate 60'
    Original Eqn: b'Infected symptomatic 60*(1-fraction of critical cases 60)/symptomatic duration 60'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_60() * (
        1 - fraction_of_critical_cases_60()) / symptomatic_duration_60()


@cache('run')
def social_distancing_start_60():
    """
    Real Name: b'social distancing start 60'
    Original Eqn: b'31'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 31


@cache('run')
def init_accumulated_cases_50():
    """
    Real Name: b'init accumulated cases 50'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('run')
def init_accumulated_cases_60():
    """
    Real Name: b'init accumulated cases 60'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('step')
def infection_rate_50():
    """
    Real Name: b'infection rate 50'
    Original Eqn: b'total infection rate 50+first infection 50'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return total_infection_rate_50() + first_infection_50()


@cache('step')
def infection_rate_60():
    """
    Real Name: b'infection rate 60'
    Original Eqn: b'total infection rate 60+first infection 60'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return total_infection_rate_60() + first_infection_60()


@cache('step')
def infection_rate_70():
    """
    Real Name: b'infection rate 70'
    Original Eqn: b'total infection rate 70+first infection 70'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return total_infection_rate_70() + first_infection_70()


@cache('step')
def infection_rate_80():
    """
    Real Name: b'infection rate 80'
    Original Eqn: b'total infection rate 80+first infection 80'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return total_infection_rate_80() + first_infection_80()


@cache('run')
def immunity_time_50():
    """
    Real Name: b'immunity time 50'
    Original Eqn: b'360'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 360


@cache('run')
def immunity_time_60():
    """
    Real Name: b'immunity time 60'
    Original Eqn: b'360'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 360


@cache('step')
def infection_rate_asymptomatic_50x80():
    """
    Real Name: b'infection rate asymptomatic 50x80'
    Original Eqn: b'contact infectivity asymptomatic 50x80*(social distancing policy SWITCH self 80*social distancing policy 80\\\\ +(1-social distancing policy SWITCH self 80))*Infected asymptomatic 50x80*Susceptible 80\\\\ /non controlled pop 50x80'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contact_infectivity_asymptomatic_50x80() * (
        social_distancing_policy_switch_self_80() * social_distancing_policy_80() +
        (1 - social_distancing_policy_switch_self_80())
    ) * infected_asymptomatic_50x80() * susceptible_80() / non_controlled_pop_50x80()


@cache('step')
def infection_rate_asymptomatic_60x50():
    """
    Real Name: b'infection rate asymptomatic 60x50'
    Original Eqn: b'Susceptible 50*Infected asymptomatic 50x60*contact infectivity asymptomatic 50x60*(social distancing policy SWITCH self 50 *social distancing policy 50+(1-social distancing policy SWITCH self 50))/non controlled pop 50x60'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_50() * infected_asymptomatic_50x60(
    ) * contact_infectivity_asymptomatic_50x60() * (
        social_distancing_policy_switch_self_50() * social_distancing_policy_50() +
        (1 - social_distancing_policy_switch_self_50())) / non_controlled_pop_50x60()


@cache('step')
def infection_rate_asymptomatic_60x70():
    """
    Real Name: b'infection rate asymptomatic 60x70'
    Original Eqn: b'contact infectivity asymptomatic 60x70*(social distancing policy SWITCH self 70*social distancing policy 70\\\\ +(1-social distancing policy SWITCH self 70))*Infected asymptomatic 60x70*Susceptible 70\\\\ /non controlled pop 60x70'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contact_infectivity_asymptomatic_60x70() * (
        social_distancing_policy_switch_self_70() * social_distancing_policy_70() +
        (1 - social_distancing_policy_switch_self_70())
    ) * infected_asymptomatic_60x70() * susceptible_70() / non_controlled_pop_60x70()


@cache('step')
def incidence_per_100000_50():
    """
    Real Name: b'incidence per 100000 50'
    Original Eqn: b'accumulated cases 50/init total population 50*100000'
    Units: b'dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return accumulated_cases_50() / init_total_population_50() * 100000


@cache('run')
def init_diseased_60():
    """
    Real Name: b'init Diseased 60'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('step')
def infection_rate_asymptomatic_70x60():
    """
    Real Name: b'infection rate asymptomatic 70x60'
    Original Eqn: b'Susceptible 60*Infected asymptomatic 60x70*contact infectivity asymptomatic 60x70*(social distancing policy SWITCH self 60 *social distancing policy 60+(1-social distancing policy SWITCH self 60))/non controlled pop 60x70'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_60() * infected_asymptomatic_60x70(
    ) * contact_infectivity_asymptomatic_60x70() * (
        social_distancing_policy_switch_self_60() * social_distancing_policy_60() +
        (1 - social_distancing_policy_switch_self_60())) / non_controlled_pop_60x70()


@cache('run')
def symptomatic_duration_60():
    """
    Real Name: b'symptomatic duration 60'
    Original Eqn: b'5'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 5


@cache('step')
def infection_rate_asymptomatic_80x50():
    """
    Real Name: b'infection rate asymptomatic 80x50'
    Original Eqn: b'Susceptible 50*Infected asymptomatic 50x80*contact infectivity asymptomatic 50x80*(social distancing policy SWITCH self 50 *social distancing policy 50+(1-social distancing policy SWITCH self 50))/non controlled pop 50x80'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_50() * infected_asymptomatic_50x80(
    ) * contact_infectivity_asymptomatic_50x80() * (
        social_distancing_policy_switch_self_50() * social_distancing_policy_50() +
        (1 - social_distancing_policy_switch_self_50())) / non_controlled_pop_50x80()


@cache('step')
def infected_asymptomatic_50():
    """
    Real Name: b'Infected asymptomatic 50'
    Original Eqn: b'INTEG ( infection rate 50-infected asymptomatic recovery rate 50-isolation rate asymptomatic 50\\\\ -symptomatic rate 50, init Infected asymptomatic 50)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_infected_asymptomatic_50()


@cache('run')
def init_infected_asymptomatic_60():
    """
    Real Name: b'init Infected asymptomatic 60'
    Original Eqn: b'1'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1


@cache('step')
def symptomatic_rate_60():
    """
    Real Name: b'symptomatic rate 60'
    Original Eqn: b'Infected asymptomatic 60/asymptomatic duration 60*(1-fraction of asymptomatic case development 60\\\\ )'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic_60() / asymptomatic_duration_60() * (
        1 - fraction_of_asymptomatic_case_development_60())


@cache('step')
def infected_asymptomatic_50x80():
    """
    Real Name: b'Infected asymptomatic 50x80'
    Original Eqn: b'Infected asymptomatic 50+Infected asymptomatic 80'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic_50() + infected_asymptomatic_80()


@cache('step')
def infection_rate_asymptomatic_self_60():
    """
    Real Name: b'infection rate asymptomatic self 60'
    Original Eqn: b'Infected asymptomatic 60*Susceptible 60*contact infectivity asymptomatic self 60*(social distancing policy SWITCH self 60*social distancing policy 60+(1-social distancing policy SWITCH self 60))/non controlled population 60'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic_60() * susceptible_60(
    ) * contact_infectivity_asymptomatic_self_60() * (
        social_distancing_policy_switch_self_60() * social_distancing_policy_60() +
        (1 - social_distancing_policy_switch_self_60())) / non_controlled_population_60()


@cache('step')
def infected_asymptomatic_60x70():
    """
    Real Name: b'Infected asymptomatic 60x70'
    Original Eqn: b'Infected asymptomatic 60+Infected asymptomatic 70'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic_60() + infected_asymptomatic_70()


@cache('step')
def infected_asymptomatic_60x80():
    """
    Real Name: b'Infected asymptomatic 60x80'
    Original Eqn: b'Infected asymptomatic 60+Infected asymptomatic 80'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic_60() + infected_asymptomatic_80()


@cache('run')
def self_quarantine_policy_switch_self_50():
    """
    Real Name: b'self quarantine policy SWITCH self 50'
    Original Eqn: b'0'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('step')
def infection_rate_quarantined_self_50():
    """
    Real Name: b'infection rate quarantined self 50'
    Original Eqn: b'Isolated 50*Susceptible 50*contact infectivity quarantine self 50/non controlled population 50'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return isolated_50() * susceptible_50() * contact_infectivity_quarantine_self_50(
    ) / non_controlled_population_50()


@cache('run')
def social_distancing_start_50():
    """
    Real Name: b'social distancing start 50'
    Original Eqn: b'31'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 31


@cache('step')
def infected_symptomatic_50x60():
    """
    Real Name: b'Infected symptomatic 50x60'
    Original Eqn: b'Infected symptomatic 50+Infected symptomatic 60'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_50() + infected_symptomatic_60()


@cache('step')
def infected_asymptomatic_recovery_rate_50():
    """
    Real Name: b'infected asymptomatic recovery rate 50'
    Original Eqn: b'fraction of asymptomatic case development 50*Infected asymptomatic 50/(asymptomatic duration 50\\\\ +symptomatic duration 50)'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return fraction_of_asymptomatic_case_development_50() * infected_asymptomatic_50() / (
        asymptomatic_duration_50() + symptomatic_duration_50())


@cache('step')
def infection_rate_symptomatic_50x60():
    """
    Real Name: b'infection rate symptomatic 50x60'
    Original Eqn: b'Susceptible 60*Infected symptomatic 50x60*contact infectivity symptomatic 50x60*(self quarantine policy SWITCH self 60\\\\ *self quarantine policy 60+(1-self quarantine policy SWITCH self 60))/non controlled pop 50x60'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_60() * infected_symptomatic_50x60() * contact_infectivity_symptomatic_50x60(
    ) * (self_quarantine_policy_switch_self_60() * self_quarantine_policy_60() +
         (1 - self_quarantine_policy_switch_self_60())) / non_controlled_pop_50x60()


@cache('run')
def self_quarantine_start_50():
    """
    Real Name: b'self quarantine start 50'
    Original Eqn: b'21'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 21


@cache('step')
def total_infected_50():
    """
    Real Name: b'total infected 50'
    Original Eqn: b'Infected asymptomatic 50+Infected symptomatic 50'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic_50() + infected_symptomatic_50()


@cache('run')
def init_recovered_50():
    """
    Real Name: b'init Recovered 50'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('step')
def infected_critical_case_rate_50():
    """
    Real Name: b'infected critical case rate 50'
    Original Eqn: b'Infected symptomatic 50*fraction of critical cases 50/symptomatic duration 50'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_50() * fraction_of_critical_cases_50() / symptomatic_duration_50()


@cache('step')
def infected_critical_case_rate_60():
    """
    Real Name: b'infected critical case rate 60'
    Original Eqn: b'Infected symptomatic 60*fraction of critical cases 60/symptomatic duration 60'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_60() * fraction_of_critical_cases_60() / symptomatic_duration_60()


@cache('run')
def social_distancing_effectiveness_60():
    """
    Real Name: b'social distancing effectiveness 60'
    Original Eqn: b'0.6'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.6


@cache('step')
def infection_rate_symptomatic_70x60():
    """
    Real Name: b'infection rate symptomatic 70x60'
    Original Eqn: b'Susceptible 60*Infected symptomatic 60x70*contact infectivity symptomatic 60x70*(self quarantine policy SWITCH self 60\\\\ * self quarantine policy 60+(1-self quarantine policy SWITCH self 60))/non controlled pop 60x70'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_60() * infected_symptomatic_60x70() * contact_infectivity_symptomatic_60x70(
    ) * (self_quarantine_policy_switch_self_60() * self_quarantine_policy_60() +
         (1 - self_quarantine_policy_switch_self_60())) / non_controlled_pop_60x70()


@cache('step')
def total_infection_rate_60():
    """
    Real Name: b'total infection rate 60'
    Original Eqn: b'infection rate asymptomatic self 60+infection rate quarantined self 60+infection rate symptomatic self 60 +infection rate asymptomatic 80x60+infection rate symptomatic 80x60 +infection rate asymptomatic 70x60+infection rate symptomatic 70x60 +infection rate asymptomatic 50x60+infection rate symptomatic 50x60 +infection rate asymptomatic 40x60+infection rate symptomatic 40x60 +infection rate asymptomatic 30x60+infection rate symptomatic 30x60 +infection rate asymptomatic 20x60+infection rate symptomatic 20x60 +infection rate asymptomatic 10x60+infection rate symptomatic 10x60 +infection rate asymptomatic 00x60+infection rate symptomatic 00x60'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infection_rate_asymptomatic_self_60() + infection_rate_quarantined_self_60(
    ) + infection_rate_symptomatic_self_60() + infection_rate_asymptomatic_80x60(
    ) + infection_rate_symptomatic_80x60() + infection_rate_asymptomatic_70x60(
    ) + infection_rate_symptomatic_70x60() + infection_rate_asymptomatic_50x60(
    ) + infection_rate_symptomatic_50x60() + infection_rate_asymptomatic_40x60(
    ) + infection_rate_symptomatic_40x60() + infection_rate_asymptomatic_30x60(
    ) + infection_rate_symptomatic_30x60() + infection_rate_asymptomatic_20x60(
    ) + infection_rate_symptomatic_20x60() + infection_rate_asymptomatic_10x60(
    ) + infection_rate_symptomatic_10x60() + infection_rate_asymptomatic_00x60(
    ) + infection_rate_symptomatic_00x60()


@cache('step')
def infected_symptomatic_50():
    """
    Real Name: b'Infected symptomatic 50'
    Original Eqn: b'INTEG ( symptomatic rate 50-infected critical case rate 50-infected symptomatic recovery rate 50\\\\ -isolation rate symptomatic 50, init Infected symptomatic 50)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_infected_symptomatic_50()


@cache('run')
def init_infected_symptomatic_60():
    """
    Real Name: b'init Infected symptomatic 60'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('step')
def non_controlled_pop_50x80():
    """
    Real Name: b'non controlled pop 50x80'
    Original Eqn: b'non controlled population 50+non controlled population 80'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return non_controlled_population_50() + non_controlled_population_80()


@cache('step')
def infected_symptomatic_60x70():
    """
    Real Name: b'Infected symptomatic 60x70'
    Original Eqn: b'Infected symptomatic 60+Infected symptomatic 70'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_60() + infected_symptomatic_70()


@cache('step')
def infected_symptomatic_60x80():
    """
    Real Name: b'Infected symptomatic 60x80'
    Original Eqn: b'Infected symptomatic 60+Infected symptomatic 80'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_60() + infected_symptomatic_80()


@cache('run')
def social_distancing_policy_switch_self_60():
    """
    Real Name: b'social distancing policy SWITCH self 60'
    Original Eqn: b'0'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('run')
def social_distancing_policy_switch_self_50():
    """
    Real Name: b'social distancing policy SWITCH self 50'
    Original Eqn: b'0'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('run')
def test_fraction_50():
    """
    Real Name: b'test fraction 50'
    Original Eqn: b'1'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1


@cache('run')
def test_fraction_60():
    """
    Real Name: b'test fraction 60'
    Original Eqn: b'1'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1


@cache('step')
def new_cases_60():
    """
    Real Name: b'new cases 60'
    Original Eqn: b'symptomatic rate 60*test fraction 60'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return symptomatic_rate_60() * test_fraction_60()


@cache('step')
def infection_rate_asymptomatic_70x50():
    """
    Real Name: b'infection rate asymptomatic 70x50'
    Original Eqn: b'Susceptible 50*Infected asymptomatic 50x70*contact infectivity asymptomatic 50x70*(social distancing policy SWITCH self 50 *social distancing policy 50+(1-social distancing policy SWITCH self 50))/non controlled pop 50x70'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_50() * infected_asymptomatic_50x70(
    ) * contact_infectivity_asymptomatic_50x70() * (
        social_distancing_policy_switch_self_50() * social_distancing_policy_50() +
        (1 - social_distancing_policy_switch_self_50())) / non_controlled_pop_50x70()


@cache('step')
def total_infection_rate_80():
    """
    Real Name: b'total infection rate 80'
    Original Eqn: b'infection rate asymptomatic self 80+infection rate quarantined self 80+infection rate symptomatic self 80 +infection rate asymptomatic 70x80+infection rate symptomatic 70x80 +infection rate asymptomatic 60x80+infection rate symptomatic 60x80 +infection rate asymptomatic 50x80+infection rate symptomatic 50x80 +infection rate asymptomatic 40x80+infection rate symptomatic 40x80 +infection rate asymptomatic 30x80+infection rate symptomatic 30x80 +infection rate asymptomatic 20x80+infection rate symptomatic 20x80 +infection rate asymptomatic 10x80+infection rate symptomatic 10x80 +infection rate asymptomatic 00x80+infection rate symptomatic 00x80'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infection_rate_asymptomatic_self_80() + infection_rate_quarantined_self_80(
    ) + infection_rate_symptomatic_self_80() + infection_rate_asymptomatic_70x80(
    ) + infection_rate_symptomatic_70x80() + infection_rate_asymptomatic_60x80(
    ) + infection_rate_symptomatic_60x80() + infection_rate_asymptomatic_50x80(
    ) + infection_rate_symptomatic_50x80() + infection_rate_asymptomatic_40x80(
    ) + infection_rate_symptomatic_40x80() + infection_rate_asymptomatic_30x80(
    ) + infection_rate_symptomatic_30x80() + infection_rate_asymptomatic_20x80(
    ) + infection_rate_symptomatic_20x80() + infection_rate_asymptomatic_10x80(
    ) + infection_rate_symptomatic_10x80() + infection_rate_asymptomatic_00x80(
    ) + infection_rate_symptomatic_00x80()


@cache('run')
def symptomatic_duration_50():
    """
    Real Name: b'symptomatic duration 50'
    Original Eqn: b'5'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 5


@cache('run')
def init_isolated_60():
    """
    Real Name: b'init Isolated 60'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('step')
def susceptible_50():
    """
    Real Name: b'Susceptible 50'
    Original Eqn: b'INTEG ( deimmunization rate 50-infection rate 50, init Susceptible 50)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_susceptible_50()


@cache('step')
def susceptible_60():
    """
    Real Name: b'Susceptible 60'
    Original Eqn: b'INTEG ( deimmunization rate 60-infection rate 60, init Susceptible 60)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_susceptible_60()


@cache('step')
def total_infected_60():
    """
    Real Name: b'total infected 60'
    Original Eqn: b'Infected asymptomatic 60+Infected symptomatic 60'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic_60() + infected_symptomatic_60()


@cache('step')
def infection_rate_asymptomatic_50x70():
    """
    Real Name: b'infection rate asymptomatic 50x70'
    Original Eqn: b'contact infectivity asymptomatic 50x70*(social distancing policy SWITCH self 70*social distancing policy 70\\\\ +(1-social distancing policy SWITCH self 70))*Infected asymptomatic 50x70*Susceptible 70\\\\ /non controlled pop 50x70'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contact_infectivity_asymptomatic_50x70() * (
        social_distancing_policy_switch_self_70() * social_distancing_policy_70() +
        (1 - social_distancing_policy_switch_self_70())
    ) * infected_asymptomatic_50x70() * susceptible_70() / non_controlled_pop_50x70()


@cache('run')
def init_critical_cases_60():
    """
    Real Name: b'init Critical Cases 60'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('run')
def symptomatic_contact_fraction_50():
    """
    Real Name: b'symptomatic contact fraction 50'
    Original Eqn: b'0.5'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.5


@cache('run')
def symptomatic_contact_fraction_60():
    """
    Real Name: b'symptomatic contact fraction 60'
    Original Eqn: b'0.5'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.5


@cache('run')
def init_infected_symptomatic_50():
    """
    Real Name: b'init Infected symptomatic 50'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('step')
def new_cases_50():
    """
    Real Name: b'new cases 50'
    Original Eqn: b'symptomatic rate 50*test fraction 50'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return symptomatic_rate_50() * test_fraction_50()


@cache('step')
def infection_rate_symptomatic_80x50():
    """
    Real Name: b'infection rate symptomatic 80x50'
    Original Eqn: b'Susceptible 50*Infected symptomatic 50x80*contact infectivity symptomatic 50x80*(self quarantine policy SWITCH self 50\\\\ * self quarantine policy 50+(1-self quarantine policy SWITCH self 50))/non controlled pop 50x80'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_50() * infected_symptomatic_50x80() * contact_infectivity_symptomatic_50x80(
    ) * (self_quarantine_policy_switch_self_50() * self_quarantine_policy_50() +
         (1 - self_quarantine_policy_switch_self_50())) / non_controlled_pop_50x80()


@cache('run')
def init_diseased_50():
    """
    Real Name: b'init Diseased 50'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('step')
def non_controlled_pop_50x70():
    """
    Real Name: b'non controlled pop 50x70'
    Original Eqn: b'non controlled population 50+non controlled population 70'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return non_controlled_population_50() + non_controlled_population_70()


@cache('step')
def infection_rate_symptomatic_70x50():
    """
    Real Name: b'infection rate symptomatic 70x50'
    Original Eqn: b'Susceptible 50*Infected symptomatic 50x70*contact infectivity symptomatic 50x70*(self quarantine policy SWITCH self 50\\\\ * self quarantine policy 50+(1-self quarantine policy SWITCH self 50))/non controlled pop 50x70'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_50() * infected_symptomatic_50x70() * contact_infectivity_symptomatic_50x70(
    ) * (self_quarantine_policy_switch_self_50() * self_quarantine_policy_50() +
         (1 - self_quarantine_policy_switch_self_50())) / non_controlled_pop_50x70()


@cache('step')
def symptomatic_rate_50():
    """
    Real Name: b'symptomatic rate 50'
    Original Eqn: b'Infected asymptomatic 50/asymptomatic duration 50*(1-fraction of asymptomatic case development 50\\\\ )'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic_50() / asymptomatic_duration_50() * (
        1 - fraction_of_asymptomatic_case_development_50())


@cache('step')
def init_total_population_60():
    """
    Real Name: b'init total population 60'
    Original Eqn: b'init Infected asymptomatic 60+init Susceptible 60'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return init_infected_asymptomatic_60() + init_susceptible_60()


@cache('step')
def infection_rate_asymptomatic_self_50():
    """
    Real Name: b'infection rate asymptomatic self 50'
    Original Eqn: b'Infected asymptomatic 50*Susceptible 50*contact infectivity asymptomatic self 50*(social distancing policy SWITCH self 50\\\\ *social distancing policy 50+(1-social distancing policy SWITCH self 50))/non controlled population 50'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic_50() * susceptible_50(
    ) * contact_infectivity_asymptomatic_self_50() * (
        social_distancing_policy_switch_self_50() * social_distancing_policy_50() +
        (1 - social_distancing_policy_switch_self_50())) / non_controlled_population_50()


@cache('step')
def infection_rate_symptomatic_60x70():
    """
    Real Name: b'infection rate symptomatic 60x70'
    Original Eqn: b'Susceptible 70*Infected symptomatic 60x70*contact infectivity symptomatic 60x70*(self quarantine policy SWITCH self 70\\\\ *self quarantine policy 70+(1-self quarantine policy SWITCH self 70))/non controlled pop 60x70'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_70() * infected_symptomatic_60x70() * contact_infectivity_symptomatic_60x70(
    ) * (self_quarantine_policy_switch_self_70() * self_quarantine_policy_70() +
         (1 - self_quarantine_policy_switch_self_70())) / non_controlled_pop_60x70()


@cache('step')
def infection_rate_symptomatic_60x80():
    """
    Real Name: b'infection rate symptomatic 60x80'
    Original Eqn: b'Susceptible 80*Infected symptomatic 60x80*contact infectivity symptomatic 60x80*(self quarantine policy SWITCH self 80\\\\ *self quarantine policy 80+(1-self quarantine policy SWITCH self 80))/non controlled pop 60x80'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_80() * infected_symptomatic_60x80() * contact_infectivity_symptomatic_60x80(
    ) * (self_quarantine_policy_switch_self_80() * self_quarantine_policy_80() +
         (1 - self_quarantine_policy_switch_self_80())) / non_controlled_pop_60x80()


@cache('run')
def init_critical_cases_50():
    """
    Real Name: b'init Critical Cases 50'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('run')
def social_distancing_effectiveness_50():
    """
    Real Name: b'social distancing effectiveness 50'
    Original Eqn: b'0.6'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.6


@cache('step')
def total_infection_rate_50():
    """
    Real Name: b'total infection rate 50'
    Original Eqn: b'infection rate asymptomatic self 50+infection rate quarantined self 50+infection rate symptomatic self 50 +infection rate asymptomatic 80x50+infection rate symptomatic 80x50 +infection rate asymptomatic 70x50+infection rate symptomatic 70x50 +infection rate asymptomatic 60x50+infection rate symptomatic 60x50 +infection rate asymptomatic 40x50+infection rate symptomatic 40x50 +infection rate asymptomatic 30x50+infection rate symptomatic 30x50 +infection rate asymptomatic 20x50+infection rate symptomatic 20x50 +infection rate asymptomatic 10x50+infection rate symptomatic 10x50 +infection rate asymptomatic 00x50+infection rate symptomatic 00x50'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infection_rate_asymptomatic_self_50() + infection_rate_quarantined_self_50(
    ) + infection_rate_symptomatic_self_50() + infection_rate_asymptomatic_80x50(
    ) + infection_rate_symptomatic_80x50() + infection_rate_asymptomatic_70x50(
    ) + infection_rate_symptomatic_70x50() + infection_rate_asymptomatic_60x50(
    ) + infection_rate_symptomatic_60x50() + infection_rate_asymptomatic_40x50(
    ) + infection_rate_symptomatic_40x50() + infection_rate_asymptomatic_30x50(
    ) + infection_rate_symptomatic_30x50() + infection_rate_asymptomatic_20x50(
    ) + infection_rate_symptomatic_20x50() + infection_rate_asymptomatic_10x50(
    ) + infection_rate_symptomatic_10x50() + infection_rate_asymptomatic_00x50(
    ) + infection_rate_symptomatic_00x50()


@cache('run')
def init_infected_asymptomatic_50():
    """
    Real Name: b'init Infected asymptomatic 50'
    Original Eqn: b'1'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1


@cache('run')
def init_recovered_60():
    """
    Real Name: b'init Recovered 60'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('step')
def contact_infectivity_asymptomatic_self_70():
    """
    Real Name: b'contact infectivity asymptomatic self 70'
    Original Eqn: b'contacts per person normal self 70*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_self_70() * infectivity_per_contact()


@cache('step')
def contact_infectivity_asymptomatic_self_80():
    """
    Real Name: b'contact infectivity asymptomatic self 80'
    Original Eqn: b'contacts per person normal self 80*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_self_80() * infectivity_per_contact()


@cache('step')
def infection_rate_symptomatic_self_80():
    """
    Real Name: b'infection rate symptomatic self 80'
    Original Eqn: b'Infected symptomatic 80*Susceptible 80*contact infectivity symptomatic self 80*(self quarantine policy SWITCH self 80\\\\ *self quarantine policy 80+(1-self quarantine policy SWITCH self 80))/non controlled population 80'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_80() * susceptible_80() * contact_infectivity_symptomatic_self_80(
    ) * (self_quarantine_policy_switch_self_80() * self_quarantine_policy_80() +
         (1 - self_quarantine_policy_switch_self_80())) / non_controlled_population_80()


@cache('step')
def infection_rate_asymptomatic_70x80():
    """
    Real Name: b'infection rate asymptomatic 70x80'
    Original Eqn: b'contact infectivity asymptomatic 70x80*(social distancing policy SWITCH self 80*social distancing policy 80\\\\ +(1-social distancing policy SWITCH self 80))*Infected asymptomatic 70x80*Susceptible 80\\\\ /non controlled pop 70x80'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contact_infectivity_asymptomatic_70x80() * (
        social_distancing_policy_switch_self_80() * social_distancing_policy_80() +
        (1 - social_distancing_policy_switch_self_80())
    ) * infected_asymptomatic_70x80() * susceptible_80() / non_controlled_pop_70x80()


@cache('step')
def infection_rate_asymptomatic_80x70():
    """
    Real Name: b'infection rate asymptomatic 80x70'
    Original Eqn: b'Susceptible 70*Infected asymptomatic 70x80*contact infectivity asymptomatic 70x80*(social distancing policy SWITCH self 70\\\\ *social distancing policy 70+(1-social distancing policy SWITCH self 70))/non controlled pop 70x80'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_70() * infected_asymptomatic_70x80(
    ) * contact_infectivity_asymptomatic_70x80() * (
        social_distancing_policy_switch_self_70() * social_distancing_policy_70() +
        (1 - social_distancing_policy_switch_self_70())) / non_controlled_pop_70x80()


@cache('step')
def contact_infectivity_asymptomatic_70x80():
    """
    Real Name: b'contact infectivity asymptomatic 70x80'
    Original Eqn: b'contacts per person normal 70x80*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_70x80() * infectivity_per_contact()


@cache('step')
def infection_rate_asymptomatic_self_70():
    """
    Real Name: b'infection rate asymptomatic self 70'
    Original Eqn: b'Infected asymptomatic 70*Susceptible 70*contact infectivity asymptomatic self 70*(social distancing policy SWITCH self 70\\\\ *social distancing policy 70+(1-social distancing policy SWITCH self 70))/non controlled population 70'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic_70() * susceptible_70(
    ) * contact_infectivity_asymptomatic_self_70() * (
        social_distancing_policy_switch_self_70() * social_distancing_policy_70() +
        (1 - social_distancing_policy_switch_self_70())) / non_controlled_population_70()


@cache('step')
def infection_rate_asymptomatic_self_80():
    """
    Real Name: b'infection rate asymptomatic self 80'
    Original Eqn: b'Infected asymptomatic 80*Susceptible 80*contact infectivity asymptomatic self 80*(social distancing policy SWITCH self 80\\\\ *social distancing policy 80+(1-social distancing policy SWITCH self 80))/non controlled population 80'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic_80() * susceptible_80(
    ) * contact_infectivity_asymptomatic_self_80() * (
        social_distancing_policy_switch_self_80() * social_distancing_policy_80() +
        (1 - social_distancing_policy_switch_self_80())) / non_controlled_population_80()


@cache('step')
def infection_rate_symptomatic_self_70():
    """
    Real Name: b'infection rate symptomatic self 70'
    Original Eqn: b'Infected symptomatic 70*Susceptible 70*contact infectivity symptomatic self 70*(self quarantine policy SWITCH self 70\\\\ *self quarantine policy 70+(1-self quarantine policy SWITCH self 70))/non controlled population 70'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_70() * susceptible_70() * contact_infectivity_symptomatic_self_70(
    ) * (self_quarantine_policy_switch_self_70() * self_quarantine_policy_70() +
         (1 - self_quarantine_policy_switch_self_70())) / non_controlled_population_70()


@cache('step')
def contact_infectivity_symptomatic_self_70():
    """
    Real Name: b'contact infectivity symptomatic self 70'
    Original Eqn: b'contacts per person symptomatic self 70*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_symptomatic_self_70() * infectivity_per_contact()


@cache('step')
def contact_infectivity_symptomatic_70x80():
    """
    Real Name: b'contact infectivity symptomatic 70x80'
    Original Eqn: b'contacts per person symptomatic 70x80*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_symptomatic_70x80() * infectivity_per_contact()


@cache('step')
def infection_rate_symptomatic_80x70():
    """
    Real Name: b'infection rate symptomatic 80x70'
    Original Eqn: b'Susceptible 70*Infected symptomatic 70x80*contact infectivity symptomatic 70x80*(self quarantine policy SWITCH self 70\\\\ *self quarantine policy 70+(1-self quarantine policy SWITCH self 70))/non controlled pop 70x80'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_70() * infected_symptomatic_70x80() * contact_infectivity_symptomatic_70x80(
    ) * (self_quarantine_policy_switch_self_70() * self_quarantine_policy_70() +
         (1 - self_quarantine_policy_switch_self_70())) / non_controlled_pop_70x80()


@cache('step')
def contact_infectivity_symptomatic_self_80():
    """
    Real Name: b'contact infectivity symptomatic self 80'
    Original Eqn: b'contacts per person symptomatic self 80*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_symptomatic_self_80() * infectivity_per_contact()


@cache('step')
def infection_rate_symptomatic_70x80():
    """
    Real Name: b'infection rate symptomatic 70x80'
    Original Eqn: b'Susceptible 80*Infected symptomatic 70x80*contact infectivity symptomatic 70x80*(self quarantine policy SWITCH self 80\\\\ *self quarantine policy 80+(1-self quarantine policy SWITCH self 80))/non controlled pop 70x80'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_80() * infected_symptomatic_70x80() * contact_infectivity_symptomatic_70x80(
    ) * (self_quarantine_policy_switch_self_80() * self_quarantine_policy_80() +
         (1 - self_quarantine_policy_switch_self_80())) / non_controlled_pop_70x80()


@cache('step')
def isolation_rate_asymptomatic_80():
    """
    Real Name: b'isolation rate asymptomatic 80'
    Original Eqn: b'MIN(available test kits for testing asymptomatic*effect of kits availability on effectiveness of testing\\\\ /kits per person , Infected asymptomatic 80 )/testing duration'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return np.minimum(
        available_test_kits_for_testing_asymptomatic() *
        effect_of_kits_availability_on_effectiveness_of_testing() / kits_per_person(),
        infected_asymptomatic_80()) / testing_duration()


@cache('step')
def isolation_rate_symptomatic_70():
    """
    Real Name: b'isolation rate symptomatic 70'
    Original Eqn: b'tests for symptomatic/kits per person/testing duration'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return tests_for_symptomatic() / kits_per_person() / testing_duration()


@cache('step')
def isolation_rate_symptomatic_80():
    """
    Real Name: b'isolation rate symptomatic 80'
    Original Eqn: b'tests for symptomatic/kits per person/testing duration'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return tests_for_symptomatic() / kits_per_person() / testing_duration()


@cache('step')
def isolation_rate_asymptomatic_70():
    """
    Real Name: b'isolation rate asymptomatic 70'
    Original Eqn: b'MIN(available test kits for testing asymptomatic*effect of kits availability on effectiveness of testing\\\\ /kits per person , Infected asymptomatic 70 )/testing duration'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return np.minimum(
        available_test_kits_for_testing_asymptomatic() *
        effect_of_kits_availability_on_effectiveness_of_testing() / kits_per_person(),
        infected_asymptomatic_70()) / testing_duration()


@cache('run')
def fraction_of_death_70():
    """
    Real Name: b'fraction of death 70'
    Original Eqn: b'0.4'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.4


@cache('step')
def accumulated_cases_70():
    """
    Real Name: b'accumulated cases 70'
    Original Eqn: b'INTEG ( new cases 70, init accumulated cases 70)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_accumulated_cases_70()


@cache('step')
def accumulated_cases_80():
    """
    Real Name: b'accumulated cases 80'
    Original Eqn: b'INTEG ( new cases 80, init accumulated cases 80)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_accumulated_cases_80()


@cache('step')
def fraction_of_symptomatic_70():
    """
    Real Name: b'fraction of symptomatic 70'
    Original Eqn: b'ZIDZ(Infected symptomatic 70, total infected 70)'
    Units: b'dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.zidz(infected_symptomatic_70(), total_infected_70())


@cache('run')
def asymptomatic_duration_70():
    """
    Real Name: b'asymptomatic duration 70'
    Original Eqn: b'5'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 5


@cache('run')
def asymptomatic_duration_80():
    """
    Real Name: b'asymptomatic duration 80'
    Original Eqn: b'5'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 5


@cache('run')
def immunity_time_70():
    """
    Real Name: b'immunity time 70'
    Original Eqn: b'360'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 360


@cache('run')
def init_isolated_70():
    """
    Real Name: b'init Isolated 70'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('run')
def init_isolated_80():
    """
    Real Name: b'init Isolated 80'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('step')
def incidence_per_100000_70():
    """
    Real Name: b'incidence per 100000 70'
    Original Eqn: b'accumulated cases 70/init total population 70*100000'
    Units: b'dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return accumulated_cases_70() / init_total_population_70() * 100000


@cache('step')
def case_fatality_rate_70():
    """
    Real Name: b'case fatality rate 70'
    Original Eqn: b'ZIDZ( Diseased 70, accumulated cases 70)'
    Units: b'dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.zidz(diseased_70(), accumulated_cases_70())


@cache('step')
def case_fatality_rate_80():
    """
    Real Name: b'case fatality rate 80'
    Original Eqn: b'ZIDZ( Diseased 80, accumulated cases 80)'
    Units: b'dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.zidz(diseased_80(), accumulated_cases_80())


@cache('run')
def init_susceptible_70():
    """
    Real Name: b'init Susceptible 70'
    Original Eqn: b'4e+06'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 4e+06


@cache('step')
def init_total_population_70():
    """
    Real Name: b'init total population 70'
    Original Eqn: b'init Infected asymptomatic 70+init Susceptible 70'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return init_infected_asymptomatic_70() + init_susceptible_70()


@cache('step')
def contact_infectivity_quarantine_self_70():
    """
    Real Name: b'contact infectivity quarantine self 70'
    Original Eqn: b'contact infectivity asymptomatic self 70*(1-isolation effectiveness 70)'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contact_infectivity_asymptomatic_self_70() * (1 - isolation_effectiveness_70())


@cache('step')
def contact_infectivity_quarantine_self_80():
    """
    Real Name: b'contact infectivity quarantine self 80'
    Original Eqn: b'contact infectivity asymptomatic self 80*(1-isolation effectiveness 80)'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contact_infectivity_asymptomatic_self_80() * (1 - isolation_effectiveness_80())


@cache('step')
def isolated_80():
    """
    Real Name: b'Isolated 80'
    Original Eqn: b'INTEG ( isolation rate symptomatic 80+isolation rate asymptomatic 80-isolated recovery rate 80\\\\ -isolated critical case rate 80, init Isolated 80)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_isolated_80()


@cache('run')
def contacts_per_person_normal_70x80():
    """
    Real Name: b'contacts per person normal 70x80'
    Original Eqn: b'10'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 10


@cache('step')
def infected_critical_case_rate_80():
    """
    Real Name: b'infected critical case rate 80'
    Original Eqn: b'Infected symptomatic 80*fraction of critical cases 80/symptomatic duration 80'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_80() * fraction_of_critical_cases_80() / symptomatic_duration_80()


@cache('run')
def contacts_per_person_normal_self_70():
    """
    Real Name: b'contacts per person normal self 70'
    Original Eqn: b'20'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 20


@cache('run')
def contacts_per_person_normal_self_80():
    """
    Real Name: b'contacts per person normal self 80'
    Original Eqn: b'20'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 20


@cache('step')
def contacts_per_person_symptomatic_70x80():
    """
    Real Name: b'contacts per person symptomatic 70x80'
    Original Eqn: b'contacts per person normal 70x80*(symptomatic contact fraction 80+symptomatic contact fraction 70\\\\ )/2'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_70x80() * (symptomatic_contact_fraction_80() +
                                                 symptomatic_contact_fraction_70()) / 2


@cache('step')
def contacts_per_person_symptomatic_self_70():
    """
    Real Name: b'contacts per person symptomatic self 70'
    Original Eqn: b'contacts per person normal self 70*symptomatic contact fraction 70'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_self_70() * symptomatic_contact_fraction_70()


@cache('step')
def contacts_per_person_symptomatic_self_80():
    """
    Real Name: b'contacts per person symptomatic self 80'
    Original Eqn: b'contacts per person normal self 80*symptomatic contact fraction 80'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_self_80() * symptomatic_contact_fraction_80()


@cache('run')
def isolation_effectiveness_70():
    """
    Real Name: b'isolation effectiveness 70'
    Original Eqn: b'0.9'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.9


@cache('step')
def critical_cases_70():
    """
    Real Name: b'Critical Cases 70'
    Original Eqn: b'INTEG ( infected critical case rate 70-critical cases recovery rate 70-death rate 70+isolated critical case rate 70\\\\ , init Critical Cases 70)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_critical_cases_70()


@cache('step')
def critical_cases_80():
    """
    Real Name: b'Critical Cases 80'
    Original Eqn: b'INTEG ( infected critical case rate 80-critical cases recovery rate 80-death rate 80+isolated critical case rate 80\\\\ , init Critical Cases 80)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_critical_cases_80()


@cache('step')
def critical_cases_recovery_rate_70():
    """
    Real Name: b'critical cases recovery rate 70'
    Original Eqn: b'Critical Cases 70*(1-fraction of death 70)/duration of treatment 70'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return critical_cases_70() * (1 - fraction_of_death_70()) / duration_of_treatment_70()


@cache('step')
def critical_cases_recovery_rate_80():
    """
    Real Name: b'critical cases recovery rate 80'
    Original Eqn: b'Critical Cases 80*(1-fraction of death 80)/duration of treatment 80'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return critical_cases_80() * (1 - fraction_of_death_80()) / duration_of_treatment_80()


@cache('step')
def death_rate_70():
    """
    Real Name: b'death rate 70'
    Original Eqn: b'Critical Cases 70*fraction of death 70/duration of treatment 70'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return critical_cases_70() * fraction_of_death_70() / duration_of_treatment_70()


@cache('step')
def death_rate_80():
    """
    Real Name: b'death rate 80'
    Original Eqn: b'Critical Cases 80*fraction of death 80/duration of treatment 80'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return critical_cases_80() * fraction_of_death_80() / duration_of_treatment_80()


@cache('step')
def deimmunization_rate_70():
    """
    Real Name: b'deimmunization rate 70'
    Original Eqn: b'Recovered 70/immunity time 70'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return recovered_70() / immunity_time_70()


@cache('step')
def deimmunization_rate_80():
    """
    Real Name: b'deimmunization rate 80'
    Original Eqn: b'Recovered 80/immunity time 80'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return recovered_80() / immunity_time_80()


@cache('step')
def diseased_70():
    """
    Real Name: b'Diseased 70'
    Original Eqn: b'INTEG ( death rate 70, init Diseased 70)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_diseased_70()


@cache('step')
def diseased_80():
    """
    Real Name: b'Diseased 80'
    Original Eqn: b'INTEG ( death rate 80, init Diseased 80)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_diseased_80()


@cache('step')
def non_controlled_pop_70x80():
    """
    Real Name: b'non controlled pop 70x80'
    Original Eqn: b'non controlled population 70+non controlled population 80'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return non_controlled_population_70() + non_controlled_population_80()


@cache('run')
def duration_of_treatment_70():
    """
    Real Name: b'duration of treatment 70'
    Original Eqn: b'10'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 10


@cache('run')
def duration_of_treatment_80():
    """
    Real Name: b'duration of treatment 80'
    Original Eqn: b'10'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 10


@cache('step')
def non_controlled_population_80():
    """
    Real Name: b'non controlled population 80'
    Original Eqn: b'Infected symptomatic 80+Susceptible 80+Infected asymptomatic 80+Isolated 80+Recovered 80'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_80() + susceptible_80() + infected_asymptomatic_80() + isolated_80(
    ) + recovered_80()


@cache('step')
def infected_asymptomatic_recovery_rate_80():
    """
    Real Name: b'infected asymptomatic recovery rate 80'
    Original Eqn: b'fraction of asymptomatic case development 80*Infected asymptomatic 80/(asymptomatic duration 80\\\\ +symptomatic duration 80)'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return fraction_of_asymptomatic_case_development_80() * infected_asymptomatic_80() / (
        asymptomatic_duration_80() + symptomatic_duration_80())


@cache('run')
def fraction_of_asymptomatic_case_development_70():
    """
    Real Name: b'fraction of asymptomatic case development 70'
    Original Eqn: b'0.5'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.5


@cache('run')
def fraction_of_asymptomatic_case_development_80():
    """
    Real Name: b'fraction of asymptomatic case development 80'
    Original Eqn: b'0.5'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.5


@cache('run')
def init_critical_cases_80():
    """
    Real Name: b'init Critical Cases 80'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('run')
def fraction_of_critical_cases_70():
    """
    Real Name: b'fraction of critical cases 70'
    Original Eqn: b'0.1'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.1


@cache('run')
def fraction_of_critical_cases_80():
    """
    Real Name: b'fraction of critical cases 80'
    Original Eqn: b'0.1'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.1


@cache('run')
def init_diseased_80():
    """
    Real Name: b'init Diseased 80'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('run')
def fraction_of_death_80():
    """
    Real Name: b'fraction of death 80'
    Original Eqn: b'0.4'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.4


@cache('run')
def init_infected_asymptomatic_80():
    """
    Real Name: b'init Infected asymptomatic 80'
    Original Eqn: b'1'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1


@cache('step')
def fraction_of_symptomatic_80():
    """
    Real Name: b'fraction of symptomatic 80'
    Original Eqn: b'ZIDZ(Infected symptomatic 80, total infected 80)'
    Units: b'dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.zidz(infected_symptomatic_80(), total_infected_80())


@cache('step')
def recovered_80():
    """
    Real Name: b'Recovered 80'
    Original Eqn: b'INTEG ( critical cases recovery rate 80+infected asymptomatic recovery rate 80+infected symptomatic recovery rate 80\\\\ -deimmunization rate 80+isolated recovery rate 80, init Recovered 80)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_recovered_80()


@cache('run')
def immunity_time_80():
    """
    Real Name: b'immunity time 80'
    Original Eqn: b'360'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 360


@cache('run')
def self_quarantine_effectiveness_80():
    """
    Real Name: b'self quarantine effectiveness 80'
    Original Eqn: b'0.75'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.75


@cache('step')
def infection_rate_quarantined_self_70():
    """
    Real Name: b'infection rate quarantined self 70'
    Original Eqn: b'Isolated 70*Susceptible 70*contact infectivity quarantine self 70/non controlled population 70'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return isolated_70() * susceptible_70() * contact_infectivity_quarantine_self_70(
    ) / non_controlled_population_70()


@cache('step')
def incidence_per_100000_80():
    """
    Real Name: b'incidence per 100000 80'
    Original Eqn: b'accumulated cases 80/init total population 80*100000'
    Units: b'dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return accumulated_cases_80() / init_total_population_80() * 100000


@cache('step')
def infected_asymptomatic_70():
    """
    Real Name: b'Infected asymptomatic 70'
    Original Eqn: b'INTEG ( infection rate 70-infected asymptomatic recovery rate 70-isolation rate asymptomatic 70\\\\ -symptomatic rate 70, init Infected asymptomatic 70)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_infected_asymptomatic_70()


@cache('step')
def infected_asymptomatic_70x80():
    """
    Real Name: b'Infected asymptomatic 70x80'
    Original Eqn: b'Infected asymptomatic 70+Infected asymptomatic 80'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic_70() + infected_asymptomatic_80()


@cache('step')
def infected_asymptomatic_80():
    """
    Real Name: b'Infected asymptomatic 80'
    Original Eqn: b'INTEG ( infection rate 80-infected asymptomatic recovery rate 80-isolation rate asymptomatic 80\\\\ -symptomatic rate 80, init Infected asymptomatic 80)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_infected_asymptomatic_80()


@cache('run')
def self_quarantine_policy_switch_self_80():
    """
    Real Name: b'self quarantine policy SWITCH self 80'
    Original Eqn: b'0'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('step')
def infected_symptomatic_70():
    """
    Real Name: b'Infected symptomatic 70'
    Original Eqn: b'INTEG ( symptomatic rate 70-infected critical case rate 70-infected symptomatic recovery rate 70\\\\ -isolation rate symptomatic 70, init Infected symptomatic 70)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_infected_symptomatic_70()


@cache('step')
def infected_symptomatic_70x80():
    """
    Real Name: b'Infected symptomatic 70x80'
    Original Eqn: b'Infected symptomatic 70+Infected symptomatic 80'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_70() + infected_symptomatic_80()


@cache('step')
def infected_symptomatic_80():
    """
    Real Name: b'Infected symptomatic 80'
    Original Eqn: b'INTEG ( symptomatic rate 80-infected critical case rate 80-infected symptomatic recovery rate 80\\\\ -isolation rate symptomatic 80, init Infected symptomatic 80)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_infected_symptomatic_80()


@cache('run')
def social_distancing_effectiveness_70():
    """
    Real Name: b'social distancing effectiveness 70'
    Original Eqn: b'0.6'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.6


@cache('step')
def infected_asymptomatic_recovery_rate_70():
    """
    Real Name: b'infected asymptomatic recovery rate 70'
    Original Eqn: b'fraction of asymptomatic case development 70*Infected asymptomatic 70/(asymptomatic duration 70\\\\ +symptomatic duration 70)'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return fraction_of_asymptomatic_case_development_70() * infected_asymptomatic_70() / (
        asymptomatic_duration_70() + symptomatic_duration_70())


@cache('run')
def init_accumulated_cases_80():
    """
    Real Name: b'init accumulated cases 80'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('step')
def infected_critical_case_rate_70():
    """
    Real Name: b'infected critical case rate 70'
    Original Eqn: b'Infected symptomatic 70*fraction of critical cases 70/symptomatic duration 70'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_70() * fraction_of_critical_cases_70() / symptomatic_duration_70()


@cache('run')
def init_critical_cases_70():
    """
    Real Name: b'init Critical Cases 70'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('run')
def social_distancing_policy_switch_self_70():
    """
    Real Name: b'social distancing policy SWITCH self 70'
    Original Eqn: b'0'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('step')
def infected_symptomatic_recovery_rate_70():
    """
    Real Name: b'infected symptomatic recovery rate 70'
    Original Eqn: b'Infected symptomatic 70*(1-fraction of critical cases 70)/symptomatic duration 70'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_70() * (
        1 - fraction_of_critical_cases_70()) / symptomatic_duration_70()


@cache('step')
def infected_symptomatic_recovery_rate_80():
    """
    Real Name: b'infected symptomatic recovery rate 80'
    Original Eqn: b'Infected symptomatic 80*(1-fraction of critical cases 80)/symptomatic duration 80'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_80() * (
        1 - fraction_of_critical_cases_80()) / symptomatic_duration_80()


@cache('step')
def susceptible_80():
    """
    Real Name: b'Susceptible 80'
    Original Eqn: b'INTEG ( deimmunization rate 80-infection rate 80, init Susceptible 80)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_susceptible_80()


@cache('run')
def init_infected_symptomatic_80():
    """
    Real Name: b'init Infected symptomatic 80'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('run')
def symptomatic_contact_fraction_80():
    """
    Real Name: b'symptomatic contact fraction 80'
    Original Eqn: b'0.5'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.5


@cache('run')
def symptomatic_contact_fraction_70():
    """
    Real Name: b'symptomatic contact fraction 70'
    Original Eqn: b'0.5'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.5


@cache('step')
def infection_rate_quarantined_self_80():
    """
    Real Name: b'infection rate quarantined self 80'
    Original Eqn: b'Isolated 80*Susceptible 80*contact infectivity quarantine self 80/non controlled population 80'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return isolated_80() * susceptible_80() * contact_infectivity_quarantine_self_80(
    ) / non_controlled_population_80()


@cache('run')
def init_recovered_80():
    """
    Real Name: b'init Recovered 80'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('step')
def symptomatic_rate_70():
    """
    Real Name: b'symptomatic rate 70'
    Original Eqn: b'Infected asymptomatic 70/asymptomatic duration 70*(1-fraction of asymptomatic case development 70\\\\ )'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic_70() / asymptomatic_duration_70() * (
        1 - fraction_of_asymptomatic_case_development_70())


@cache('run')
def init_susceptible_80():
    """
    Real Name: b'init Susceptible 80'
    Original Eqn: b'4e+06'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 4e+06


@cache('run')
def test_fraction_70():
    """
    Real Name: b'test fraction 70'
    Original Eqn: b'1'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1


@cache('step')
def init_total_population_80():
    """
    Real Name: b'init total population 80'
    Original Eqn: b'init Infected asymptomatic 80+init Susceptible 80'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return init_infected_asymptomatic_80() + init_susceptible_80()


@cache('run')
def init_accumulated_cases_70():
    """
    Real Name: b'init accumulated cases 70'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('run')
def social_distancing_effectiveness_80():
    """
    Real Name: b'social distancing effectiveness 80'
    Original Eqn: b'0.6'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.6


@cache('step')
def total_infected_70():
    """
    Real Name: b'total infected 70'
    Original Eqn: b'Infected asymptomatic 70+Infected symptomatic 70'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic_70() + infected_symptomatic_70()


@cache('step')
def isolated_critical_case_rate_80():
    """
    Real Name: b'isolated critical case rate 80'
    Original Eqn: b'Isolated 80*fraction of critical cases 80/symptomatic duration 80'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return isolated_80() * fraction_of_critical_cases_80() / symptomatic_duration_80()


@cache('step')
def total_infection_rate_70():
    """
    Real Name: b'total infection rate 70'
    Original Eqn: b'infection rate asymptomatic self 70+infection rate quarantined self 70+infection rate symptomatic self 70 +infection rate asymptomatic 80x70+infection rate symptomatic 80x70 +infection rate asymptomatic 60x70+infection rate symptomatic 60x70 +infection rate asymptomatic 50x70+infection rate symptomatic 50x70 +infection rate asymptomatic 40x70+infection rate symptomatic 40x70 +infection rate asymptomatic 30x70+infection rate symptomatic 30x70 +infection rate asymptomatic 20x70+infection rate symptomatic 20x70 +infection rate asymptomatic 10x70+infection rate symptomatic 10x70 +infection rate asymptomatic 00x70+infection rate symptomatic 00x70'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infection_rate_asymptomatic_self_70() + infection_rate_quarantined_self_70(
    ) + infection_rate_symptomatic_self_70() + infection_rate_asymptomatic_80x70(
    ) + infection_rate_symptomatic_80x70() + infection_rate_asymptomatic_60x70(
    ) + infection_rate_symptomatic_60x70() + infection_rate_asymptomatic_50x70(
    ) + infection_rate_symptomatic_50x70() + infection_rate_asymptomatic_40x70(
    ) + infection_rate_symptomatic_40x70() + infection_rate_asymptomatic_30x70(
    ) + infection_rate_symptomatic_30x70() + infection_rate_asymptomatic_20x70(
    ) + infection_rate_symptomatic_20x70() + infection_rate_asymptomatic_10x70(
    ) + infection_rate_symptomatic_10x70() + infection_rate_asymptomatic_00x70(
    ) + infection_rate_symptomatic_00x70()


@cache('run')
def init_diseased_70():
    """
    Real Name: b'init Diseased 70'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('run')
def social_distancing_policy_switch_self_80():
    """
    Real Name: b'social distancing policy SWITCH self 80'
    Original Eqn: b'0'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('run')
def isolation_duration_70():
    """
    Real Name: b'isolation duration 70'
    Original Eqn: b'14'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 14


@cache('run')
def init_infected_asymptomatic_70():
    """
    Real Name: b'init Infected asymptomatic 70'
    Original Eqn: b'1'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1


@cache('run')
def social_distancing_start_80():
    """
    Real Name: b'social distancing start 80'
    Original Eqn: b'31'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 31


@cache('step')
def new_cases_80():
    """
    Real Name: b'new cases 80'
    Original Eqn: b'symptomatic rate 80*test fraction 80'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return symptomatic_rate_80() * test_fraction_80()


@cache('run')
def init_infected_symptomatic_70():
    """
    Real Name: b'init Infected symptomatic 70'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('step')
def recovered_70():
    """
    Real Name: b'Recovered 70'
    Original Eqn: b'INTEG ( critical cases recovery rate 70+infected asymptomatic recovery rate 70+infected symptomatic recovery rate 70\\\\ -deimmunization rate 70+isolated recovery rate 70, init Recovered 70)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_recovered_70()


@cache('run')
def self_quarantine_effectiveness_70():
    """
    Real Name: b'self quarantine effectiveness 70'
    Original Eqn: b'0.75'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.75


@cache('step')
def isolated_critical_case_rate_70():
    """
    Real Name: b'isolated critical case rate 70'
    Original Eqn: b'Isolated 70*fraction of critical cases 70/symptomatic duration 70'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return isolated_70() * fraction_of_critical_cases_70() / symptomatic_duration_70()


@cache('run')
def self_quarantine_start_70():
    """
    Real Name: b'self quarantine start 70'
    Original Eqn: b'21'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 21


@cache('run')
def init_recovered_70():
    """
    Real Name: b'init Recovered 70'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('run')
def symptomatic_duration_80():
    """
    Real Name: b'symptomatic duration 80'
    Original Eqn: b'5'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 5


@cache('run')
def self_quarantine_policy_switch_self_70():
    """
    Real Name: b'self quarantine policy SWITCH self 70'
    Original Eqn: b'0'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('step')
def symptomatic_rate_80():
    """
    Real Name: b'symptomatic rate 80'
    Original Eqn: b'Infected asymptomatic 80/asymptomatic duration 80*(1-fraction of asymptomatic case development 80\\\\ )'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic_80() / asymptomatic_duration_80() * (
        1 - fraction_of_asymptomatic_case_development_80())


@cache('run')
def isolation_duration_80():
    """
    Real Name: b'isolation duration 80'
    Original Eqn: b'14'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 14


@cache('step')
def new_cases_70():
    """
    Real Name: b'new cases 70'
    Original Eqn: b'symptomatic rate 70*test fraction 70'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return symptomatic_rate_70() * test_fraction_70()


@cache('step')
def total_infected_80():
    """
    Real Name: b'total infected 80'
    Original Eqn: b'Infected asymptomatic 80+Infected symptomatic 80'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic_80() + infected_symptomatic_80()


@cache('run')
def self_quarantine_start_80():
    """
    Real Name: b'self quarantine start 80'
    Original Eqn: b'21'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 21


@cache('step')
def isolated_70():
    """
    Real Name: b'Isolated 70'
    Original Eqn: b'INTEG ( isolation rate symptomatic 70+isolation rate asymptomatic 70-isolated recovery rate 70\\\\ -isolated critical case rate 70, init Isolated 70)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_isolated_70()


@cache('step')
def non_controlled_population_70():
    """
    Real Name: b'non controlled population 70'
    Original Eqn: b'Infected symptomatic 70+Susceptible 70+Infected asymptomatic 70+Isolated 70+Recovered 70'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_70() + susceptible_70() + infected_asymptomatic_70() + isolated_70(
    ) + recovered_70()


@cache('run')
def social_distancing_start_70():
    """
    Real Name: b'social distancing start 70'
    Original Eqn: b'31'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 31


@cache('step')
def isolated_recovery_rate_80():
    """
    Real Name: b'isolated recovery rate 80'
    Original Eqn: b'Isolated 80*(1-fraction of critical cases 80)/isolation duration 80'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return isolated_80() * (1 - fraction_of_critical_cases_80()) / isolation_duration_80()


@cache('step')
def isolated_recovery_rate_70():
    """
    Real Name: b'isolated recovery rate 70'
    Original Eqn: b'Isolated 70*(1-fraction of critical cases 70)/isolation duration 70'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return isolated_70() * (1 - fraction_of_critical_cases_70()) / isolation_duration_70()


@cache('run')
def isolation_effectiveness_80():
    """
    Real Name: b'isolation effectiveness 80'
    Original Eqn: b'0.9'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.9


@cache('step')
def susceptible_70():
    """
    Real Name: b'Susceptible 70'
    Original Eqn: b'INTEG ( deimmunization rate 70-infection rate 70, init Susceptible 70)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_susceptible_70()


@cache('run')
def symptomatic_duration_70():
    """
    Real Name: b'symptomatic duration 70'
    Original Eqn: b'5'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 5


@cache('run')
def test_fraction_80():
    """
    Real Name: b'test fraction 80'
    Original Eqn: b'1'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1


@cache('step')
def accumulated_cases():
    """
    Real Name: b'accumulated cases'
    Original Eqn: b'INTEG ( new cases, init accumulated cases)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_accumulated_cases()


@cache('step')
def init_total_population():
    """
    Real Name: b'init total population'
    Original Eqn: b'init Infected asymptomatic+init Susceptible'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return init_infected_asymptomatic() + init_susceptible()


@cache('step')
def incidence_per_100000():
    """
    Real Name: b'incidence per 100000'
    Original Eqn: b'accumulated cases/init total population*100000'
    Units: b'dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return accumulated_cases() / init_total_population() * 100000


@cache('step')
def new_cases():
    """
    Real Name: b'new cases'
    Original Eqn: b'new cases 80 +new cases 70 +new cases 60 +new cases 50 +new cases 40 +new cases 30 +new cases 20 +new cases 10 +new cases 00'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return new_cases_80() + new_cases_70() + new_cases_60() + new_cases_50() + new_cases_40(
    ) + new_cases_30() + new_cases_20() + new_cases_10() + new_cases_00()


@cache('step')
def init_accumulated_cases():
    """
    Real Name: b'init accumulated cases'
    Original Eqn: b'init accumulated cases 80 +init accumulated cases 70 +init accumulated cases 60 +init accumulated cases 50 +init accumulated cases 40 +init accumulated cases 30 +init accumulated cases 20 +init accumulated cases 10 +init accumulated cases 00'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return init_accumulated_cases_80() + init_accumulated_cases_70() + init_accumulated_cases_60(
    ) + init_accumulated_cases_50() + init_accumulated_cases_40() + init_accumulated_cases_30(
    ) + init_accumulated_cases_20() + init_accumulated_cases_10() + init_accumulated_cases_00()


@cache('step')
def case_fatality_rate():
    """
    Real Name: b'case fatality rate'
    Original Eqn: b'ZIDZ( Diseased, accumulated cases)'
    Units: b'dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.zidz(diseased(), accumulated_cases())


@cache('step')
def isolation_rate_asymptomatic():
    """
    Real Name: b'isolation rate asymptomatic'
    Original Eqn: b'isolation rate asymptomatic 80 +isolation rate asymptomatic 70 +isolation rate asymptomatic 60 +isolation rate asymptomatic 50 +isolation rate asymptomatic 40 +isolation rate asymptomatic 30 +isolation rate asymptomatic 20 +isolation rate asymptomatic 10 +isolation rate asymptomatic 00'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return isolation_rate_asymptomatic_80() + isolation_rate_asymptomatic_70(
    ) + isolation_rate_asymptomatic_60() + isolation_rate_asymptomatic_50(
    ) + isolation_rate_asymptomatic_40() + isolation_rate_asymptomatic_30(
    ) + isolation_rate_asymptomatic_20() + isolation_rate_asymptomatic_10(
    ) + isolation_rate_asymptomatic_00()


@cache('step')
def fraction_of_symptomatic():
    """
    Real Name: b'fraction of symptomatic'
    Original Eqn: b'ZIDZ(Infected symptomatic, total infected)'
    Units: b'dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.zidz(infected_symptomatic(), total_infected())


@cache('step')
def total_infected():
    """
    Real Name: b'total infected'
    Original Eqn: b'Infected asymptomatic+Infected symptomatic'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic() + infected_symptomatic()


@cache('step')
def infected_symptomatic_recovery_rate():
    """
    Real Name: b'infected symptomatic recovery rate'
    Original Eqn: b'infected symptomatic recovery rate 80 +infected symptomatic recovery rate 70 +infected symptomatic recovery rate 60 +infected symptomatic recovery rate 50 +infected symptomatic recovery rate 40 +infected symptomatic recovery rate 30 +infected symptomatic recovery rate 20 +infected symptomatic recovery rate 10 +infected symptomatic recovery rate 00'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic_recovery_rate_80() + infected_symptomatic_recovery_rate_70(
    ) + infected_symptomatic_recovery_rate_60() + infected_symptomatic_recovery_rate_50(
    ) + infected_symptomatic_recovery_rate_40() + infected_symptomatic_recovery_rate_30(
    ) + infected_symptomatic_recovery_rate_20() + infected_symptomatic_recovery_rate_10(
    ) + infected_symptomatic_recovery_rate_00()


@cache('step')
def infected_asymptomatic_recovery_rate():
    """
    Real Name: b'infected asymptomatic recovery rate'
    Original Eqn: b'infected asymptomatic recovery rate 80 +infected asymptomatic recovery rate 70 +infected asymptomatic recovery rate 60 +infected asymptomatic recovery rate 50 +infected asymptomatic recovery rate 40 +infected asymptomatic recovery rate 30 +infected asymptomatic recovery rate 20 +infected asymptomatic recovery rate 10 +infected asymptomatic recovery rate 00'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic_recovery_rate_80() + infected_asymptomatic_recovery_rate_70(
    ) + infected_asymptomatic_recovery_rate_60() + infected_asymptomatic_recovery_rate_50(
    ) + infected_asymptomatic_recovery_rate_40() + infected_asymptomatic_recovery_rate_30(
    ) + infected_asymptomatic_recovery_rate_20() + infected_asymptomatic_recovery_rate_10(
    ) + infected_asymptomatic_recovery_rate_00()


@cache('step')
def available_test_kits():
    """
    Real Name: b'available test kits'
    Original Eqn: b'INTEG ( produced test kits-used test kits, init available test kits)'
    Units: b'kit'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_available_test_kits()


@cache('step')
def available_test_kits_for_testing_asymptomatic():
    """
    Real Name: b'available test kits for testing asymptomatic'
    Original Eqn: b'MAX(available test kits for testing symptomatic-tests for symptomatic, 0)'
    Units: b'kit'
    Limits: (None, None)
    Type: component

    b''
    """
    return np.maximum(available_test_kits_for_testing_symptomatic() - tests_for_symptomatic(), 0)


@cache('step')
def available_test_kits_for_testing_symptomatic():
    """
    Real Name: b'available test kits for testing symptomatic'
    Original Eqn: b'MAX(available test kits, 0)'
    Units: b'kit'
    Limits: (None, None)
    Type: component

    b''
    """
    return np.maximum(available_test_kits(), 0)


@cache('step')
def critical_cases():
    """
    Real Name: b'Critical Cases'
    Original Eqn: b'INTEG ( infected critical case rate-critical cases recovery rate-death rate+isolated critical case rate\\\\ , init Critical Cases)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_critical_cases()


@cache('step')
def critical_cases_recovery_rate():
    """
    Real Name: b'critical cases recovery rate'
    Original Eqn: b'critical cases recovery rate 80 +critical cases recovery rate 70 +critical cases recovery rate 60 +critical cases recovery rate 50 +critical cases recovery rate 40 +critical cases recovery rate 30 +critical cases recovery rate 20 +critical cases recovery rate 10 +critical cases recovery rate 00'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return critical_cases_recovery_rate_80() + critical_cases_recovery_rate_70(
    ) + critical_cases_recovery_rate_60() + critical_cases_recovery_rate_50(
    ) + critical_cases_recovery_rate_40() + critical_cases_recovery_rate_30(
    ) + critical_cases_recovery_rate_20() + critical_cases_recovery_rate_10(
    ) + critical_cases_recovery_rate_00()


@cache('step')
def death_rate():
    """
    Real Name: b'death rate'
    Original Eqn: b'death rate 80 +death rate 70 +death rate 60 +death rate 50 +death rate 40 +death rate 30 +death rate 20 +death rate 10 +death rate 00'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return death_rate_80() + death_rate_70() + death_rate_60() + death_rate_50() + death_rate_40(
    ) + death_rate_30() + death_rate_20() + death_rate_10() + death_rate_00()


@cache('step')
def deimmunization_rate():
    """
    Real Name: b'deimmunization rate'
    Original Eqn: b'deimmunization rate 80 +deimmunization rate 70 +deimmunization rate 60 +deimmunization rate 50 +deimmunization rate 40 +deimmunization rate 30 +deimmunization rate 20 +deimmunization rate 10 +deimmunization rate 00'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return deimmunization_rate_80() + deimmunization_rate_70() + deimmunization_rate_60(
    ) + deimmunization_rate_50() + deimmunization_rate_40() + deimmunization_rate_30(
    ) + deimmunization_rate_20() + deimmunization_rate_10() + deimmunization_rate_00()


@cache('step')
def diseased():
    """
    Real Name: b'Diseased'
    Original Eqn: b'INTEG ( death rate, init Diseased)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_diseased()


@cache('step')
def effect_of_kits_availability_on_effectiveness_of_testing():
    """
    Real Name: b'effect of kits availability on effectiveness of testing'
    Original Eqn: b'kits availability for testing table(kits population ratio/max kits population ratio)'
    Units: b'dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return kits_availability_for_testing_table(kits_population_ratio() /
                                               max_kits_population_ratio())


@cache('step')
def infected_asymptomatic():
    """
    Real Name: b'Infected asymptomatic'
    Original Eqn: b'INTEG ( infection rate-infected asymptomatic recovery rate-isolation rate asymptomatic-symptomatic rate\\\\ , init Infected asymptomatic)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_infected_asymptomatic()


@cache('step')
def infected_symptomatic():
    """
    Real Name: b'Infected symptomatic'
    Original Eqn: b'INTEG ( symptomatic rate-infected critical case rate-infected symptomatic recovery rate-isolation rate symptomatic\\\\ , init Infected symptomatic)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_infected_symptomatic()


@cache('step')
def infected_critical_case_rate():
    """
    Real Name: b'infected critical case rate'
    Original Eqn: b'infected critical case rate 80 +infected critical case rate 70 +infected critical case rate 60 +infected critical case rate 50 +infected critical case rate 40 +infected critical case rate 30 +infected critical case rate 20 +infected critical case rate 10 +infected critical case rate 00'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_critical_case_rate_80() + infected_critical_case_rate_70(
    ) + infected_critical_case_rate_60() + infected_critical_case_rate_50(
    ) + infected_critical_case_rate_40() + infected_critical_case_rate_30(
    ) + infected_critical_case_rate_20() + infected_critical_case_rate_10(
    ) + infected_critical_case_rate_00()


@cache('run')
def infectivity_per_contact():
    """
    Real Name: b'infectivity per contact'
    Original Eqn: b'0.0125'
    Units: b'1/contact'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.0125


@cache('run')
def init_available_test_kits():
    """
    Real Name: b'init available test kits'
    Original Eqn: b'0'
    Units: b'kit'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('step')
def init_critical_cases():
    """
    Real Name: b'init Critical Cases'
    Original Eqn: b'init Critical Cases 80 +init Critical Cases 70 +init Critical Cases 60 +init Critical Cases 50 +init Critical Cases 40 +init Critical Cases 30 +init Critical Cases 20 +init Critical Cases 10 +init Critical Cases 00'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return init_critical_cases_80() + init_critical_cases_70() + init_critical_cases_60(
    ) + init_critical_cases_50() + init_critical_cases_40() + init_critical_cases_30(
    ) + init_critical_cases_20() + init_critical_cases_10() + init_critical_cases_00()


@cache('step')
def init_diseased():
    """
    Real Name: b'init Diseased'
    Original Eqn: b'init Diseased 80 +init Diseased 70 +init Diseased 60 +init Diseased 50 +init Diseased 40 +init Diseased 30 +init Diseased 20 +init Diseased 10 +init Diseased 00'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return init_diseased_80() + init_diseased_70() + init_diseased_60() + init_diseased_50(
    ) + init_diseased_40() + init_diseased_30() + init_diseased_20() + init_diseased_10(
    ) + init_diseased_00()


@cache('step')
def init_infected_asymptomatic():
    """
    Real Name: b'init Infected asymptomatic'
    Original Eqn: b'init Infected asymptomatic 80 +init Infected asymptomatic 70 +init Infected asymptomatic 60 +init Infected asymptomatic 50 +init Infected asymptomatic 40 +init Infected asymptomatic 30 +init Infected asymptomatic 20 +init Infected asymptomatic 10 +init Infected asymptomatic 00'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return init_infected_asymptomatic_80() + init_infected_asymptomatic_70(
    ) + init_infected_asymptomatic_60() + init_infected_asymptomatic_50(
    ) + init_infected_asymptomatic_40() + init_infected_asymptomatic_30(
    ) + init_infected_asymptomatic_20() + init_infected_asymptomatic_10(
    ) + init_infected_asymptomatic_00()


@cache('step')
def init_infected_symptomatic():
    """
    Real Name: b'init Infected symptomatic'
    Original Eqn: b'init Infected symptomatic 80 +init Infected symptomatic 70 +init Infected symptomatic 60 +init Infected symptomatic 50 +init Infected symptomatic 40 +init Infected symptomatic 30 +init Infected symptomatic 20 +init Infected symptomatic 10 +init Infected symptomatic 00'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return init_infected_symptomatic_80() + init_infected_symptomatic_70(
    ) + init_infected_symptomatic_60() + init_infected_symptomatic_50(
    ) + init_infected_symptomatic_40() + init_infected_symptomatic_30(
    ) + init_infected_symptomatic_20() + init_infected_symptomatic_10(
    ) + init_infected_symptomatic_00()


@cache('step')
def init_isolated():
    """
    Real Name: b'init Isolated'
    Original Eqn: b'init Isolated 80 +init Isolated 70 +init Isolated 60 +init Isolated 50 +init Isolated 40 +init Isolated 30 +init Isolated 20 +init Isolated 10 +init Isolated 00'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return init_isolated_80() + init_isolated_70() + init_isolated_60() + init_isolated_50(
    ) + init_isolated_40() + init_isolated_30() + init_isolated_20() + init_isolated_10(
    ) + init_isolated_00()


@cache('step')
def init_recovered():
    """
    Real Name: b'init Recovered'
    Original Eqn: b'init Recovered 80 +init Recovered 70 +init Recovered 60 +init Recovered 50 +init Recovered 40 +init Recovered 30 +init Recovered 20 +init Recovered 10 +init Recovered 00'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return init_recovered_80() + init_recovered_70() + init_recovered_60() + init_recovered_50(
    ) + init_recovered_40() + init_recovered_30() + init_recovered_20() + init_recovered_10(
    ) + init_recovered_00()


@cache('step')
def init_susceptible():
    """
    Real Name: b'init Susceptible'
    Original Eqn: b'init Susceptible 80 +init Susceptible 70 +init Susceptible 60 +init Susceptible 50 +init Susceptible 40 +init Susceptible 30 +init Susceptible 20 +init Susceptible 10 +init Susceptible 00'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return init_susceptible_80() + init_susceptible_70() + init_susceptible_60(
    ) + init_susceptible_50() + init_susceptible_40() + init_susceptible_30(
    ) + init_susceptible_20() + init_susceptible_10() + init_susceptible_00()


@cache('step')
def isolated():
    """
    Real Name: b'Isolated'
    Original Eqn: b'INTEG ( isolation rate symptomatic+isolation rate asymptomatic-isolated recovery rate-isolated critical case rate\\\\ , init Isolated)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_isolated()


@cache('step')
def isolated_recovery_rate():
    """
    Real Name: b'isolated recovery rate'
    Original Eqn: b'isolated recovery rate 80 +isolated recovery rate 70 +isolated recovery rate 60 +isolated recovery rate 50 +isolated recovery rate 40 +isolated recovery rate 30 +isolated recovery rate 20 +isolated recovery rate 10 +isolated recovery rate 00'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return isolated_recovery_rate_80() + isolated_recovery_rate_70() + isolated_recovery_rate_60(
    ) + isolated_recovery_rate_50() + isolated_recovery_rate_40() + isolated_recovery_rate_30(
    ) + isolated_recovery_rate_20() + isolated_recovery_rate_10() + isolated_recovery_rate_00()


@cache('step')
def isolation_rate_symptomatic():
    """
    Real Name: b'isolation rate symptomatic'
    Original Eqn: b'isolation rate symptomatic 80 +isolation rate symptomatic 70 +isolation rate symptomatic 60 +isolation rate symptomatic 50 +isolation rate symptomatic 40 +isolation rate symptomatic 30 +isolation rate symptomatic 20 +isolation rate symptomatic 10 +isolation rate symptomatic 00'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return isolation_rate_symptomatic_80() + isolation_rate_symptomatic_70(
    ) + isolation_rate_symptomatic_60() + isolation_rate_symptomatic_50(
    ) + isolation_rate_symptomatic_40() + isolation_rate_symptomatic_30(
    ) + isolation_rate_symptomatic_20() + isolation_rate_symptomatic_10(
    ) + isolation_rate_symptomatic_00()


def kits_availability_for_testing_table(x):
    """
    Real Name: b'kits availability for testing table'
    Original Eqn: b'( [(0,0)-(1,1)],(0,0),(0.25,0.6),(0.5,0.85),(1,1))'
    Units: b'dmnl'
    Limits: (None, None)
    Type: lookup

    b''
    """
    return functions.lookup(x, [0, 0.25, 0.5, 1], [0, 0.6, 0.85, 1])


@cache('run')
def kits_per_person():
    """
    Real Name: b'kits per person'
    Original Eqn: b'1'
    Units: b'kit/person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1


@cache('step')
def kits_population_ratio():
    """
    Real Name: b'kits population ratio'
    Original Eqn: b'available test kits for testing asymptomatic/non controlled population'
    Units: b'kit/person'
    Limits: (None, None)
    Type: component

    b''
    """
    return available_test_kits_for_testing_asymptomatic() / non_controlled_population()


@cache('run')
def max_kits_population_ratio():
    """
    Real Name: b'max kits population ratio'
    Original Eqn: b'1'
    Units: b'kit/person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1


@cache('step')
def non_controlled_population():
    """
    Real Name: b'non controlled population'
    Original Eqn: b'Infected symptomatic+Susceptible+Infected asymptomatic+Isolated+Recovered'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic() + susceptible() + infected_asymptomatic() + isolated(
    ) + recovered()


@cache('step')
def produced_test_kits():
    """
    Real Name: b'produced test kits'
    Original Eqn: b'(production phase1+production phase2+production phase3)*0'
    Units: b'kit/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return (production_phase1() + production_phase2() + production_phase3()) * 0


@cache('step')
def production_phase1():
    """
    Real Name: b'production phase1'
    Original Eqn: b'PULSE(production start phase1, production start phase2-production start phase1)*production volume phase1'
    Units: b'kit/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.pulse(
        __data['time'], production_start_phase1(),
        production_start_phase2() - production_start_phase1()) * production_volume_phase1()


@cache('step')
def production_phase2():
    """
    Real Name: b'production phase2'
    Original Eqn: b'PULSE(production start phase2, production start phase3-production start phase2)*production volume phase2'
    Units: b'kit/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.pulse(
        __data['time'], production_start_phase2(),
        production_start_phase3() - production_start_phase2()) * production_volume_phase2()


@cache('step')
def production_phase3():
    """
    Real Name: b'production phase3'
    Original Eqn: b'PULSE(production start phase3, FINAL TIME-production start phase3+1)*production volume phase3'
    Units: b'kit/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.pulse(
        __data['time'], production_start_phase3(),
        final_time() - production_start_phase3() + 1) * production_volume_phase3()


@cache('run')
def production_start_phase1():
    """
    Real Name: b'production start phase1'
    Original Eqn: b'50'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 50


@cache('run')
def production_start_phase2():
    """
    Real Name: b'production start phase2'
    Original Eqn: b'90'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 90


@cache('run')
def production_start_phase3():
    """
    Real Name: b'production start phase3'
    Original Eqn: b'250'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 250


@cache('run')
def production_volume_phase1():
    """
    Real Name: b'production volume phase1'
    Original Eqn: b'500'
    Units: b'kit/Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 500


@cache('run')
def production_volume_phase2():
    """
    Real Name: b'production volume phase2'
    Original Eqn: b'6000'
    Units: b'kit/Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 6000


@cache('run')
def production_volume_phase3():
    """
    Real Name: b'production volume phase3'
    Original Eqn: b'10000'
    Units: b'kit/Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 10000


@cache('step')
def isolated_critical_case_rate():
    """
    Real Name: b'isolated critical case rate'
    Original Eqn: b'isolated critical case rate 80 +isolated critical case rate 70 +isolated critical case rate 60 +isolated critical case rate 50 +isolated critical case rate 40 +isolated critical case rate 30 +isolated critical case rate 20 +isolated critical case rate 10 +isolated critical case rate 00'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return isolated_critical_case_rate_80() + isolated_critical_case_rate_70(
    ) + isolated_critical_case_rate_60() + isolated_critical_case_rate_50(
    ) + isolated_critical_case_rate_40() + isolated_critical_case_rate_30(
    ) + isolated_critical_case_rate_20() + isolated_critical_case_rate_10(
    ) + isolated_critical_case_rate_00()


@cache('step')
def recovered():
    """
    Real Name: b'Recovered'
    Original Eqn: b'INTEG ( critical cases recovery rate+infected asymptomatic recovery rate+infected symptomatic recovery rate\\\\ -deimmunization rate+isolated recovery rate, init Recovered)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_recovered()


@cache('step')
def susceptible():
    """
    Real Name: b'Susceptible'
    Original Eqn: b'INTEG ( deimmunization rate-infection rate, init Susceptible)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_susceptible()


@cache('step')
def symptomatic_rate():
    """
    Real Name: b'symptomatic rate'
    Original Eqn: b'symptomatic rate 80 +symptomatic rate 70 +symptomatic rate 60 +symptomatic rate 50 +symptomatic rate 40 +symptomatic rate 30 +symptomatic rate 20 +symptomatic rate 10 +symptomatic rate 00'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return symptomatic_rate_80() + symptomatic_rate_70() + symptomatic_rate_60(
    ) + symptomatic_rate_50() + symptomatic_rate_40() + symptomatic_rate_30(
    ) + symptomatic_rate_20() + symptomatic_rate_10() + symptomatic_rate_00()


@cache('run')
def testing_duration():
    """
    Real Name: b'testing duration'
    Original Eqn: b'0.5'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.5


@cache('step')
def tests_for_symptomatic():
    """
    Real Name: b'tests for symptomatic'
    Original Eqn: b'MIN(available test kits for testing symptomatic, Infected symptomatic*kits per person\\\\ )'
    Units: b'kit'
    Limits: (None, None)
    Type: component

    b''
    """
    return np.minimum(available_test_kits_for_testing_symptomatic(),
                      infected_symptomatic() * kits_per_person())


@cache('step')
def used_test_kits():
    """
    Real Name: b'used test kits'
    Original Eqn: b'(infected critical case rate+isolation rate symptomatic+isolation rate asymptomatic)\\\\ *kits per person'
    Units: b'kit/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return (infected_critical_case_rate() + isolation_rate_symptomatic() +
            isolation_rate_asymptomatic()) * kits_per_person()


@cache('run')
def final_time():
    """
    Real Name: b'FINAL TIME'
    Original Eqn: b'360'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 360


@cache('run')
def initial_time():
    """
    Real Name: b'INITIAL TIME'
    Original Eqn: b'0'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('step')
def saveper():
    """
    Real Name: b'SAVEPER'
    Original Eqn: b'TIME STEP'
    Units: b'Day'
    Limits: (0.0, None)
    Type: component

    b''
    """
    return time_step()


@cache('run')
def time_step():
    """
    Real Name: b'TIME STEP'
    Original Eqn: b'0.015625'
    Units: b'Day'
    Limits: (0.0, None)
    Type: constant

    b''
    """
    return 0.015625


_integ_diseased_40 = functions.Integ(lambda: death_rate_40(), lambda: init_diseased_40())

_integ_accumulated_cases_00 = functions.Integ(lambda: new_cases_00(),
                                              lambda: init_accumulated_cases_00())

_integ_accumulated_cases_10 = functions.Integ(lambda: new_cases_10(),
                                              lambda: init_accumulated_cases_10())

_integ_accumulated_cases_20 = functions.Integ(lambda: new_cases_20(),
                                              lambda: init_accumulated_cases_20())

_integ_accumulated_cases_30 = functions.Integ(lambda: new_cases_30(),
                                              lambda: init_accumulated_cases_30())

_integ_accumulated_cases_40 = functions.Integ(lambda: new_cases_40(),
                                              lambda: init_accumulated_cases_40())

_integ_infected_symptomatic_20 = functions.Integ(
    lambda: symptomatic_rate_20() - infected_critical_case_rate_20(
    ) - infected_symptomatic_recovery_rate_20() - isolation_rate_symptomatic_20(),
    lambda: init_infected_symptomatic_20())

_integ_infected_symptomatic_30 = functions.Integ(
    lambda: symptomatic_rate_30() - infected_critical_case_rate_30(
    ) - infected_symptomatic_recovery_rate_30() - isolation_rate_symptomatic_30(),
    lambda: init_infected_symptomatic_30())

_integ_isolated_10 = functions.Integ(
    lambda: isolation_rate_symptomatic_10() + isolation_rate_asymptomatic_10() -
    isolated_recovery_rate_10() - isolated_critical_case_rate_10(), lambda: init_isolated_10())

_integ_isolated_20 = functions.Integ(
    lambda: isolation_rate_symptomatic_20() + isolation_rate_asymptomatic_20() -
    isolated_recovery_rate_20() - isolated_critical_case_rate_20(), lambda: init_isolated_20())

_integ_isolated_30 = functions.Integ(
    lambda: isolation_rate_symptomatic_30() + isolation_rate_asymptomatic_30() -
    isolated_recovery_rate_30() - isolated_critical_case_rate_30(), lambda: init_isolated_30())

_integ_isolated_40 = functions.Integ(
    lambda: isolation_rate_symptomatic_40() + isolation_rate_asymptomatic_40() -
    isolated_recovery_rate_40() - isolated_critical_case_rate_40(), lambda: init_isolated_40())

_integ_critical_cases_00 = functions.Integ(
    lambda: infected_critical_case_rate_00() - critical_cases_recovery_rate_00() - death_rate_00()
    + isolated_critical_case_rate_00(), lambda: init_critical_cases_00())

_integ_critical_cases_10 = functions.Integ(
    lambda: infected_critical_case_rate_10() - critical_cases_recovery_rate_10() - death_rate_10()
    + isolated_critical_case_rate_10(), lambda: init_critical_cases_10())

_integ_critical_cases_20 = functions.Integ(
    lambda: infected_critical_case_rate_20() - critical_cases_recovery_rate_20() - death_rate_20()
    + isolated_critical_case_rate_20(), lambda: init_critical_cases_20())

_integ_critical_cases_30 = functions.Integ(
    lambda: infected_critical_case_rate_30() - critical_cases_recovery_rate_30() - death_rate_30()
    + isolated_critical_case_rate_30(), lambda: init_critical_cases_30())

_integ_critical_cases_40 = functions.Integ(
    lambda: infected_critical_case_rate_40() - critical_cases_recovery_rate_40() - death_rate_40()
    + isolated_critical_case_rate_40(), lambda: init_critical_cases_40())

_integ_diseased_00 = functions.Integ(lambda: death_rate_00(), lambda: init_diseased_00())

_integ_diseased_10 = functions.Integ(lambda: death_rate_10(), lambda: init_diseased_10())

_integ_diseased_20 = functions.Integ(lambda: death_rate_20(), lambda: init_diseased_20())

_integ_diseased_30 = functions.Integ(lambda: death_rate_30(), lambda: init_diseased_30())

_integ_infected_symptomatic_00 = functions.Integ(
    lambda: symptomatic_rate_00() - infected_critical_case_rate_00(
    ) - infected_symptomatic_recovery_rate_00() - isolation_rate_symptomatic_00(),
    lambda: init_infected_symptomatic_00())

_integ_infected_asymptomatic_00 = functions.Integ(
    lambda: infection_rate_00() - infected_asymptomatic_recovery_rate_00(
    ) - isolation_rate_asymptomatic_00() - symptomatic_rate_00(),
    lambda: init_infected_asymptomatic_00())

_integ_infected_asymptomatic_10 = functions.Integ(
    lambda: infection_rate_10() - infected_asymptomatic_recovery_rate_10(
    ) - isolation_rate_asymptomatic_10() - symptomatic_rate_10(),
    lambda: init_infected_asymptomatic_10())

_integ_infected_asymptomatic_20 = functions.Integ(
    lambda: infection_rate_20() - infected_asymptomatic_recovery_rate_20(
    ) - isolation_rate_asymptomatic_20() - symptomatic_rate_20(),
    lambda: init_infected_asymptomatic_20())

_integ_infected_asymptomatic_30 = functions.Integ(
    lambda: infection_rate_30() - infected_asymptomatic_recovery_rate_30(
    ) - isolation_rate_asymptomatic_30() - symptomatic_rate_30(),
    lambda: init_infected_asymptomatic_30())

_integ_infected_asymptomatic_40 = functions.Integ(
    lambda: infection_rate_40() - infected_asymptomatic_recovery_rate_40(
    ) - isolation_rate_asymptomatic_40() - symptomatic_rate_40(),
    lambda: init_infected_asymptomatic_40())

_integ_infected_symptomatic_10 = functions.Integ(
    lambda: symptomatic_rate_10() - infected_critical_case_rate_10(
    ) - infected_symptomatic_recovery_rate_10() - isolation_rate_symptomatic_10(),
    lambda: init_infected_symptomatic_10())

_integ_infected_symptomatic_40 = functions.Integ(
    lambda: symptomatic_rate_40() - infected_critical_case_rate_40(
    ) - infected_symptomatic_recovery_rate_40() - isolation_rate_symptomatic_40(),
    lambda: init_infected_symptomatic_40())

_integ_susceptible_00 = functions.Integ(lambda: deimmunization_rate_00() - infection_rate_00(),
                                        lambda: init_susceptible_00())

_integ_susceptible_30 = functions.Integ(lambda: deimmunization_rate_30() - infection_rate_30(),
                                        lambda: init_susceptible_30())

_integ_susceptible_40 = functions.Integ(lambda: deimmunization_rate_40() - infection_rate_40(),
                                        lambda: init_susceptible_40())

_integ_recovered_00 = functions.Integ(
    lambda: critical_cases_recovery_rate_00() + infected_asymptomatic_recovery_rate_00() +
    infected_symptomatic_recovery_rate_00() - deimmunization_rate_00() + isolated_recovery_rate_00(
    ), lambda: init_recovered_00())

_integ_susceptible_10 = functions.Integ(lambda: deimmunization_rate_10() - infection_rate_10(),
                                        lambda: init_susceptible_10())

_integ_isolated_00 = functions.Integ(
    lambda: isolation_rate_symptomatic_00() + isolation_rate_asymptomatic_00() -
    isolated_recovery_rate_00() - isolated_critical_case_rate_00(), lambda: init_isolated_00())

_integ_recovered_10 = functions.Integ(
    lambda: critical_cases_recovery_rate_10() + infected_asymptomatic_recovery_rate_10() +
    infected_symptomatic_recovery_rate_10() - deimmunization_rate_10() + isolated_recovery_rate_10(
    ), lambda: init_recovered_10())

_integ_susceptible_20 = functions.Integ(lambda: deimmunization_rate_20() - infection_rate_20(),
                                        lambda: init_susceptible_20())

_integ_recovered_20 = functions.Integ(
    lambda: critical_cases_recovery_rate_20() + infected_asymptomatic_recovery_rate_20() +
    infected_symptomatic_recovery_rate_20() - deimmunization_rate_20() + isolated_recovery_rate_20(
    ), lambda: init_recovered_20())

_integ_recovered_40 = functions.Integ(
    lambda: critical_cases_recovery_rate_40() + infected_asymptomatic_recovery_rate_40() +
    infected_symptomatic_recovery_rate_40() - deimmunization_rate_40() + isolated_recovery_rate_40(
    ), lambda: init_recovered_40())

_integ_recovered_30 = functions.Integ(
    lambda: critical_cases_recovery_rate_30() + infected_asymptomatic_recovery_rate_30() +
    infected_symptomatic_recovery_rate_30() - deimmunization_rate_30() + isolated_recovery_rate_30(
    ), lambda: init_recovered_30())

_integ_accumulated_cases_50 = functions.Integ(lambda: new_cases_50(),
                                              lambda: init_accumulated_cases_50())

_integ_accumulated_cases_60 = functions.Integ(lambda: new_cases_60(),
                                              lambda: init_accumulated_cases_60())

_integ_recovered_50 = functions.Integ(
    lambda: critical_cases_recovery_rate_50() + infected_asymptomatic_recovery_rate_50() +
    infected_symptomatic_recovery_rate_50() - deimmunization_rate_50() + isolated_recovery_rate_50(
    ), lambda: init_recovered_50())

_integ_recovered_60 = functions.Integ(
    lambda: critical_cases_recovery_rate_60() + infected_asymptomatic_recovery_rate_60() +
    infected_symptomatic_recovery_rate_60() - deimmunization_rate_60() + isolated_recovery_rate_60(
    ), lambda: init_recovered_60())

_integ_isolated_60 = functions.Integ(
    lambda: isolation_rate_symptomatic_60() + isolation_rate_asymptomatic_60() -
    isolated_recovery_rate_60() - isolated_critical_case_rate_60(), lambda: init_isolated_60())

_integ_isolated_50 = functions.Integ(
    lambda: isolation_rate_symptomatic_50() + isolation_rate_asymptomatic_50() -
    isolated_recovery_rate_50() - isolated_critical_case_rate_50(), lambda: init_isolated_50())

_integ_critical_cases_50 = functions.Integ(
    lambda: infected_critical_case_rate_50() - critical_cases_recovery_rate_50() - death_rate_50()
    + isolated_critical_case_rate_50(), lambda: init_critical_cases_50())

_integ_critical_cases_60 = functions.Integ(
    lambda: infected_critical_case_rate_60() - critical_cases_recovery_rate_60() - death_rate_60()
    + isolated_critical_case_rate_60(), lambda: init_critical_cases_60())

_integ_infected_asymptomatic_60 = functions.Integ(
    lambda: infection_rate_60() - infected_asymptomatic_recovery_rate_60(
    ) - isolation_rate_asymptomatic_60() - symptomatic_rate_60(),
    lambda: init_infected_asymptomatic_60())

_integ_diseased_50 = functions.Integ(lambda: death_rate_50(), lambda: init_diseased_50())

_integ_diseased_60 = functions.Integ(lambda: death_rate_60(), lambda: init_diseased_60())

_integ_infected_symptomatic_60 = functions.Integ(
    lambda: symptomatic_rate_60() - infected_critical_case_rate_60(
    ) - infected_symptomatic_recovery_rate_60() - isolation_rate_symptomatic_60(),
    lambda: init_infected_symptomatic_60())

_integ_infected_asymptomatic_50 = functions.Integ(
    lambda: infection_rate_50() - infected_asymptomatic_recovery_rate_50(
    ) - isolation_rate_asymptomatic_50() - symptomatic_rate_50(),
    lambda: init_infected_asymptomatic_50())

_integ_infected_symptomatic_50 = functions.Integ(
    lambda: symptomatic_rate_50() - infected_critical_case_rate_50(
    ) - infected_symptomatic_recovery_rate_50() - isolation_rate_symptomatic_50(),
    lambda: init_infected_symptomatic_50())

_integ_susceptible_50 = functions.Integ(lambda: deimmunization_rate_50() - infection_rate_50(),
                                        lambda: init_susceptible_50())

_integ_susceptible_60 = functions.Integ(lambda: deimmunization_rate_60() - infection_rate_60(),
                                        lambda: init_susceptible_60())

_integ_accumulated_cases_70 = functions.Integ(lambda: new_cases_70(),
                                              lambda: init_accumulated_cases_70())

_integ_accumulated_cases_80 = functions.Integ(lambda: new_cases_80(),
                                              lambda: init_accumulated_cases_80())

_integ_isolated_80 = functions.Integ(
    lambda: isolation_rate_symptomatic_80() + isolation_rate_asymptomatic_80() -
    isolated_recovery_rate_80() - isolated_critical_case_rate_80(), lambda: init_isolated_80())

_integ_critical_cases_70 = functions.Integ(
    lambda: infected_critical_case_rate_70() - critical_cases_recovery_rate_70() - death_rate_70()
    + isolated_critical_case_rate_70(), lambda: init_critical_cases_70())

_integ_critical_cases_80 = functions.Integ(
    lambda: infected_critical_case_rate_80() - critical_cases_recovery_rate_80() - death_rate_80()
    + isolated_critical_case_rate_80(), lambda: init_critical_cases_80())

_integ_diseased_70 = functions.Integ(lambda: death_rate_70(), lambda: init_diseased_70())

_integ_diseased_80 = functions.Integ(lambda: death_rate_80(), lambda: init_diseased_80())

_integ_recovered_80 = functions.Integ(
    lambda: critical_cases_recovery_rate_80() + infected_asymptomatic_recovery_rate_80() +
    infected_symptomatic_recovery_rate_80() - deimmunization_rate_80() + isolated_recovery_rate_80(
    ), lambda: init_recovered_80())

_integ_infected_asymptomatic_70 = functions.Integ(
    lambda: infection_rate_70() - infected_asymptomatic_recovery_rate_70(
    ) - isolation_rate_asymptomatic_70() - symptomatic_rate_70(),
    lambda: init_infected_asymptomatic_70())

_integ_infected_asymptomatic_80 = functions.Integ(
    lambda: infection_rate_80() - infected_asymptomatic_recovery_rate_80(
    ) - isolation_rate_asymptomatic_80() - symptomatic_rate_80(),
    lambda: init_infected_asymptomatic_80())

_integ_infected_symptomatic_70 = functions.Integ(
    lambda: symptomatic_rate_70() - infected_critical_case_rate_70(
    ) - infected_symptomatic_recovery_rate_70() - isolation_rate_symptomatic_70(),
    lambda: init_infected_symptomatic_70())

_integ_infected_symptomatic_80 = functions.Integ(
    lambda: symptomatic_rate_80() - infected_critical_case_rate_80(
    ) - infected_symptomatic_recovery_rate_80() - isolation_rate_symptomatic_80(),
    lambda: init_infected_symptomatic_80())

_integ_susceptible_80 = functions.Integ(lambda: deimmunization_rate_80() - infection_rate_80(),
                                        lambda: init_susceptible_80())

_integ_recovered_70 = functions.Integ(
    lambda: critical_cases_recovery_rate_70() + infected_asymptomatic_recovery_rate_70() +
    infected_symptomatic_recovery_rate_70() - deimmunization_rate_70() + isolated_recovery_rate_70(
    ), lambda: init_recovered_70())

_integ_isolated_70 = functions.Integ(
    lambda: isolation_rate_symptomatic_70() + isolation_rate_asymptomatic_70() -
    isolated_recovery_rate_70() - isolated_critical_case_rate_70(), lambda: init_isolated_70())

_integ_susceptible_70 = functions.Integ(lambda: deimmunization_rate_70() - infection_rate_70(),
                                        lambda: init_susceptible_70())

_integ_accumulated_cases = functions.Integ(lambda: new_cases(), lambda: init_accumulated_cases())

_integ_available_test_kits = functions.Integ(lambda: produced_test_kits() - used_test_kits(),
                                             lambda: init_available_test_kits())

_integ_critical_cases = functions.Integ(
    lambda: infected_critical_case_rate() - critical_cases_recovery_rate() - death_rate() +
    isolated_critical_case_rate(), lambda: init_critical_cases())

_integ_diseased = functions.Integ(lambda: death_rate(), lambda: init_diseased())

_integ_infected_asymptomatic = functions.Integ(
    lambda: infection_rate() - infected_asymptomatic_recovery_rate() - isolation_rate_asymptomatic(
    ) - symptomatic_rate(), lambda: init_infected_asymptomatic())

_integ_infected_symptomatic = functions.Integ(
    lambda: symptomatic_rate() - infected_critical_case_rate(
    ) - infected_symptomatic_recovery_rate() - isolation_rate_symptomatic(),
    lambda: init_infected_symptomatic())

_integ_isolated = functions.Integ(
    lambda: isolation_rate_symptomatic() + isolation_rate_asymptomatic() - isolated_recovery_rate(
    ) - isolated_critical_case_rate(), lambda: init_isolated())

_integ_recovered = functions.Integ(
    lambda: critical_cases_recovery_rate() + infected_asymptomatic_recovery_rate(
    ) + infected_symptomatic_recovery_rate() - deimmunization_rate() + isolated_recovery_rate(),
    lambda: init_recovered())

_integ_susceptible = functions.Integ(lambda: deimmunization_rate() - infection_rate(),
                                     lambda: init_susceptible())
