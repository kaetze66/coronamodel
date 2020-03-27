"""
Python model "corona_base_v2_treated.py"
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
    'fraction of symptomatic': 'fraction_of_symptomatic',
    'total infected': 'total_infected',
    'infected symptomatic recovery rate': 'infected_symptomatic_recovery_rate',
    'infected asymptomatic recovery rate': 'infected_asymptomatic_recovery_rate',
    'accumulated loss of productivity': 'accumulated_loss_of_productivity',
    'actual productivity': 'actual_productivity',
    'asymptomatic duration': 'asymptomatic_duration',
    'available test kits': 'available_test_kits',
    'available test kits for testing asymptomatic': 'available_test_kits_for_testing_asymptomatic',
    'available test kits for testing symptomatic': 'available_test_kits_for_testing_symptomatic',
    'base productivity factor': 'base_productivity_factor',
    'contact infectivity asymptomatic': 'contact_infectivity_asymptomatic',
    'contact infectivity quarantine': 'contact_infectivity_quarantine',
    'contact infectivity symptomatic': 'contact_infectivity_symptomatic',
    'contacts per person normal': 'contacts_per_person_normal',
    'contacts per person symptomatic': 'contacts_per_person_symptomatic',
    'Critical Cases': 'critical_cases',
    'critical cases recovery rate': 'critical_cases_recovery_rate',
    'death rate': 'death_rate',
    'deimmunization rate': 'deimmunization_rate',
    'Diseased': 'diseased',
    'duration of treatment': 'duration_of_treatment',
    'effect of kits availability on effectiveness of testing':
    'effect_of_kits_availability_on_effectiveness_of_testing',
    'fraction of asymptomatic case development': 'fraction_of_asymptomatic_case_development',
    'fraction of critical cases': 'fraction_of_critical_cases',
    'fraction of death': 'fraction_of_death',
    'immunity time': 'immunity_time',
    '"Infected (asymptomatic)"': 'infected_asymptomatic',
    '"Infected (symptomatic)"': 'infected_symptomatic',
    'infected critical case rate': 'infected_critical_case_rate',
    'infected productivity factor': 'infected_productivity_factor',
    'infection rate': 'infection_rate',
    'infection rate asymptomatic': 'infection_rate_asymptomatic',
    'infection rate quarantined': 'infection_rate_quarantined',
    'infection rate symptomatic': 'infection_rate_symptomatic',
    'infectivity per contact': 'infectivity_per_contact',
    'init accumulated loss of producitivity': 'init_accumulated_loss_of_producitivity',
    'init available test kits': 'init_available_test_kits',
    'init Critical Cases': 'init_critical_cases',
    'init Diseased': 'init_diseased',
    'init Infected asymptomatic': 'init_infected_asymptomatic',
    'init Infected symptomatic': 'init_infected_symptomatic',
    'init Isolated': 'init_isolated',
    'init productivity': 'init_productivity',
    'init Recovered': 'init_recovered',
    'init Susceptible': 'init_susceptible',
    'init total pop': 'init_total_pop',
    'init workforce': 'init_workforce',
    'Isolated': 'isolated',
    'isolated recovery rate': 'isolated_recovery_rate',
    'isolation rate asymptomatic': 'isolation_rate_asymptomatic',
    'isolation rate symptomatic': 'isolation_rate_symptomatic',
    'kits availability for testing table': 'kits_availability_for_testing_table',
    'kits per person': 'kits_per_person',
    'kits population ratio': 'kits_population_ratio',
    'max kits population ratio': 'max_kits_population_ratio',
    'new loss': 'new_loss',
    'non controlled population': 'non_controlled_population',
    'percentage workforce': 'percentage_workforce',
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
    'productivity index': 'productivity_index',
    'quarantine duration': 'quarantine_duration',
    'quarantined critical case rate': 'quarantined_critical_case_rate',
    'quarantined effectiveness': 'quarantined_effectiveness',
    'quarantined productivity factor': 'quarantined_productivity_factor',
    'Recovered': 'recovered',
    'self quarantine effectiveness': 'self_quarantine_effectiveness',
    'self quarantine policy': 'self_quarantine_policy',
    'self quarantine policy SWITCH': 'self_quarantine_policy_switch',
    'self quarantine start': 'self_quarantine_start',
    'social distancing effectiveness': 'social_distancing_effectiveness',
    'social distancing policy': 'social_distancing_policy',
    'social distancing policy SWITCH': 'social_distancing_policy_switch',
    'social distancing start': 'social_distancing_start',
    'Susceptible': 'susceptible',
    'symptomatic duration': 'symptomatic_duration',
    'symptomatic rate': 'symptomatic_rate',
    'testing duration': 'testing_duration',
    'tests for symptomatic': 'tests_for_symptomatic',
    'time unit': 'time_unit',
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
def fraction_of_symptomatic():
    """
    Real Name: b'fraction of symptomatic'
    Original Eqn: b'"Infected (symptomatic)"/total infected'
    Units: b'dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic() / total_infected()


@cache('step')
def total_infected():
    """
    Real Name: b'total infected'
    Original Eqn: b'"Infected (asymptomatic)"+"Infected (symptomatic)"'
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
    Original Eqn: b'"Infected (symptomatic)"*(1-fraction of critical cases)/symptomatic duration'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic() * (1 - fraction_of_critical_cases()) / symptomatic_duration()


@cache('step')
def infected_asymptomatic_recovery_rate():
    """
    Real Name: b'infected asymptomatic recovery rate'
    Original Eqn: b'fraction of asymptomatic case development*"Infected (asymptomatic)"/(asymptomatic duration\\\\ +symptomatic duration)'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return fraction_of_asymptomatic_case_development() * infected_asymptomatic() / (
        asymptomatic_duration() + symptomatic_duration())


@cache('step')
def accumulated_loss_of_productivity():
    """
    Real Name: b'accumulated loss of productivity'
    Original Eqn: b'INTEG ( new loss, init accumulated loss of producitivity)'
    Units: b'dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_accumulated_loss_of_productivity()


@cache('step')
def actual_productivity():
    """
    Real Name: b'actual productivity'
    Original Eqn: b'((Recovered+Susceptible+"Infected (asymptomatic)")*base productivity factor+Isolated\\\\ *quarantined productivity factor+"Infected (symptomatic)"* infected productivity factor)*percentage workforce'
    Units: b'dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return ((recovered() + susceptible() + infected_asymptomatic()) * base_productivity_factor() +
            isolated() * quarantined_productivity_factor() +
            infected_symptomatic() * infected_productivity_factor()) * percentage_workforce()


@cache('run')
def asymptomatic_duration():
    """
    Real Name: b'asymptomatic duration'
    Original Eqn: b'5'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 5


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


@cache('run')
def base_productivity_factor():
    """
    Real Name: b'base productivity factor'
    Original Eqn: b'1'
    Units: b'dmnl/person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1


@cache('step')
def contact_infectivity_asymptomatic():
    """
    Real Name: b'contact infectivity asymptomatic'
    Original Eqn: b'contacts per person normal*infectivity per contact*social distancing policy*social distancing policy SWITCH\\\\ +(1-social distancing policy SWITCH)*contacts per person normal*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal() * infectivity_per_contact() * social_distancing_policy(
    ) * social_distancing_policy_switch() + (1 - social_distancing_policy_switch(
    )) * contacts_per_person_normal() * infectivity_per_contact()


@cache('step')
def contact_infectivity_quarantine():
    """
    Real Name: b'contact infectivity quarantine'
    Original Eqn: b'contact infectivity asymptomatic*(1-quarantined effectiveness)'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contact_infectivity_asymptomatic() * (1 - quarantined_effectiveness())


@cache('step')
def contact_infectivity_symptomatic():
    """
    Real Name: b'contact infectivity symptomatic'
    Original Eqn: b'contacts per person symptomatic*infectivity per contact*self quarantine policy*self quarantine policy SWITCH\\\\ +(1-self quarantine policy SWITCH)*contacts per person symptomatic*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_symptomatic() * infectivity_per_contact() * self_quarantine_policy(
    ) * self_quarantine_policy_switch() + (1 - self_quarantine_policy_switch(
    )) * contacts_per_person_symptomatic() * infectivity_per_contact()


@cache('run')
def contacts_per_person_normal():
    """
    Real Name: b'contacts per person normal'
    Original Eqn: b'30'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 30


@cache('run')
def contacts_per_person_symptomatic():
    """
    Real Name: b'contacts per person symptomatic'
    Original Eqn: b'15'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 15


@cache('step')
def critical_cases():
    """
    Real Name: b'Critical Cases'
    Original Eqn: b'INTEG ( infected critical case rate-critical cases recovery rate-death rate+quarantined critical case rate\\\\ , init Critical Cases)'
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
    Original Eqn: b'Critical Cases*(1-fraction of death)/duration of treatment'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return critical_cases() * (1 - fraction_of_death()) / duration_of_treatment()


@cache('step')
def death_rate():
    """
    Real Name: b'death rate'
    Original Eqn: b'Critical Cases*fraction of death/duration of treatment'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return critical_cases() * fraction_of_death() / duration_of_treatment()


@cache('step')
def deimmunization_rate():
    """
    Real Name: b'deimmunization rate'
    Original Eqn: b'Recovered/immunity time'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return recovered() / immunity_time()


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


@cache('run')
def duration_of_treatment():
    """
    Real Name: b'duration of treatment'
    Original Eqn: b'10'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 10


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


@cache('run')
def fraction_of_asymptomatic_case_development():
    """
    Real Name: b'fraction of asymptomatic case development'
    Original Eqn: b'0.5'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.5


@cache('run')
def fraction_of_critical_cases():
    """
    Real Name: b'fraction of critical cases'
    Original Eqn: b'0.1'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.1


@cache('run')
def fraction_of_death():
    """
    Real Name: b'fraction of death'
    Original Eqn: b'0.4'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.4


@cache('run')
def immunity_time():
    """
    Real Name: b'immunity time'
    Original Eqn: b'360'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 360


@cache('step')
def infected_asymptomatic():
    """
    Real Name: b'"Infected (asymptomatic)"'
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
    Real Name: b'"Infected (symptomatic)"'
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
    Original Eqn: b'"Infected (symptomatic)"*fraction of critical cases/symptomatic duration'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic() * fraction_of_critical_cases() / symptomatic_duration()


@cache('run')
def infected_productivity_factor():
    """
    Real Name: b'infected productivity factor'
    Original Eqn: b'0.5'
    Units: b'dmnl/person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.5


@cache('step')
def infection_rate():
    """
    Real Name: b'infection rate'
    Original Eqn: b'infection rate asymptomatic+infection rate symptomatic+infection rate quarantined'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infection_rate_asymptomatic() + infection_rate_symptomatic(
    ) + infection_rate_quarantined()


@cache('step')
def infection_rate_asymptomatic():
    """
    Real Name: b'infection rate asymptomatic'
    Original Eqn: b'"Infected (asymptomatic)"*Susceptible*contact infectivity asymptomatic/non controlled population'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic() * susceptible() * contact_infectivity_asymptomatic(
    ) / non_controlled_population()


@cache('step')
def infection_rate_quarantined():
    """
    Real Name: b'infection rate quarantined'
    Original Eqn: b'Isolated*Susceptible*contact infectivity quarantine/non controlled population'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return isolated() * susceptible() * contact_infectivity_quarantine(
    ) / non_controlled_population()


@cache('step')
def infection_rate_symptomatic():
    """
    Real Name: b'infection rate symptomatic'
    Original Eqn: b'"Infected (symptomatic)"*Susceptible*contact infectivity symptomatic/non controlled population'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic() * susceptible() * contact_infectivity_symptomatic(
    ) / non_controlled_population()


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
def init_accumulated_loss_of_producitivity():
    """
    Real Name: b'init accumulated loss of producitivity'
    Original Eqn: b'0'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


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


@cache('run')
def init_critical_cases():
    """
    Real Name: b'init Critical Cases'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('run')
def init_diseased():
    """
    Real Name: b'init Diseased'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('run')
def init_infected_asymptomatic():
    """
    Real Name: b'init Infected asymptomatic'
    Original Eqn: b'1'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1


@cache('run')
def init_infected_symptomatic():
    """
    Real Name: b'init Infected symptomatic'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('run')
def init_isolated():
    """
    Real Name: b'init Isolated'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('step')
def init_productivity():
    """
    Real Name: b'init productivity'
    Original Eqn: b'base productivity factor*init workforce'
    Units: b'dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return base_productivity_factor() * init_workforce()


@cache('run')
def init_recovered():
    """
    Real Name: b'init Recovered'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('run')
def init_susceptible():
    """
    Real Name: b'init Susceptible'
    Original Eqn: b'8e+06'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 8e+06


@cache('step')
def init_total_pop():
    """
    Real Name: b'init total pop'
    Original Eqn: b'init Infected symptomatic+init Susceptible'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return init_infected_symptomatic() + init_susceptible()


@cache('step')
def init_workforce():
    """
    Real Name: b'init workforce'
    Original Eqn: b'init total pop*percentage workforce'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return init_total_pop() * percentage_workforce()


@cache('step')
def isolated():
    """
    Real Name: b'Isolated'
    Original Eqn: b'INTEG ( isolation rate symptomatic+isolation rate asymptomatic-isolated recovery rate-quarantined critical case rate\\\\ , init Isolated)'
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
    Original Eqn: b'Isolated*(1-fraction of critical cases)/quarantine duration'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return isolated() * (1 - fraction_of_critical_cases()) / quarantine_duration()


@cache('step')
def isolation_rate_asymptomatic():
    """
    Real Name: b'isolation rate asymptomatic'
    Original Eqn: b'MIN(available test kits for testing asymptomatic*effect of kits availability on effectiveness of testing\\\\ , "Infected (asymptomatic)")/testing duration'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return np.minimum(
        available_test_kits_for_testing_asymptomatic() *
        effect_of_kits_availability_on_effectiveness_of_testing(),
        infected_asymptomatic()) / testing_duration()


@cache('step')
def isolation_rate_symptomatic():
    """
    Real Name: b'isolation rate symptomatic'
    Original Eqn: b'tests for symptomatic/kits per person/testing duration'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return tests_for_symptomatic() / kits_per_person() / testing_duration()


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
def new_loss():
    """
    Real Name: b'new loss'
    Original Eqn: b'(1-productivity index)/time unit'
    Units: b'dmnl/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return (1 - productivity_index()) / time_unit()


@cache('step')
def non_controlled_population():
    """
    Real Name: b'non controlled population'
    Original Eqn: b'"Infected (symptomatic)"+Susceptible+"Infected (asymptomatic)"+Isolated+Recovered'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic() + susceptible() + infected_asymptomatic() + isolated(
    ) + recovered()


@cache('run')
def percentage_workforce():
    """
    Real Name: b'percentage workforce'
    Original Eqn: b'0.8'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.8


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
def productivity_index():
    """
    Real Name: b'productivity index'
    Original Eqn: b'actual productivity/init productivity'
    Units: b'dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return actual_productivity() / init_productivity()


@cache('run')
def quarantine_duration():
    """
    Real Name: b'quarantine duration'
    Original Eqn: b'14'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 14


@cache('step')
def quarantined_critical_case_rate():
    """
    Real Name: b'quarantined critical case rate'
    Original Eqn: b'Isolated*fraction of critical cases/symptomatic duration'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return isolated() * fraction_of_critical_cases() / symptomatic_duration()


@cache('run')
def quarantined_effectiveness():
    """
    Real Name: b'quarantined effectiveness'
    Original Eqn: b'0.9'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.9


@cache('run')
def quarantined_productivity_factor():
    """
    Real Name: b'quarantined productivity factor'
    Original Eqn: b'0.75'
    Units: b'dmnl/person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.75


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


@cache('run')
def self_quarantine_effectiveness():
    """
    Real Name: b'self quarantine effectiveness'
    Original Eqn: b'0.75'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.75


@cache('step')
def self_quarantine_policy():
    """
    Real Name: b'self quarantine policy'
    Original Eqn: b'1-PULSE(self quarantine start, FINAL TIME-self quarantine start+1)*self quarantine effectiveness'
    Units: b'dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return 1 - functions.pulse(
        __data['time'], self_quarantine_start(),
        final_time() - self_quarantine_start() + 1) * self_quarantine_effectiveness()


@cache('run')
def self_quarantine_policy_switch():
    """
    Real Name: b'self quarantine policy SWITCH'
    Original Eqn: b'0'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('run')
def self_quarantine_start():
    """
    Real Name: b'self quarantine start'
    Original Eqn: b'21'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 21


@cache('run')
def social_distancing_effectiveness():
    """
    Real Name: b'social distancing effectiveness'
    Original Eqn: b'0.6'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.6


@cache('step')
def social_distancing_policy():
    """
    Real Name: b'social distancing policy'
    Original Eqn: b'1-PULSE(social distancing start, FINAL TIME-social distancing start+1)*social distancing effectiveness'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return 1 - functions.pulse(
        __data['time'], social_distancing_start(),
        final_time() - social_distancing_start() + 1) * social_distancing_effectiveness()


@cache('run')
def social_distancing_policy_switch():
    """
    Real Name: b'social distancing policy SWITCH'
    Original Eqn: b'0'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('run')
def social_distancing_start():
    """
    Real Name: b'social distancing start'
    Original Eqn: b'31'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 31


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


@cache('run')
def symptomatic_duration():
    """
    Real Name: b'symptomatic duration'
    Original Eqn: b'5'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 5


@cache('step')
def symptomatic_rate():
    """
    Real Name: b'symptomatic rate'
    Original Eqn: b'"Infected (asymptomatic)"/asymptomatic duration*(1-fraction of asymptomatic case development\\\\ )'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic() / asymptomatic_duration() * (
        1 - fraction_of_asymptomatic_case_development())


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
    Original Eqn: b'MIN(available test kits for testing symptomatic, "Infected (symptomatic)"*kits per person\\\\ )'
    Units: b'kit'
    Limits: (None, None)
    Type: component

    b''
    """
    return np.minimum(available_test_kits_for_testing_symptomatic(),
                      infected_symptomatic() * kits_per_person())


@cache('run')
def time_unit():
    """
    Real Name: b'time unit'
    Original Eqn: b'1'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1


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
    Original Eqn: b'1080'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1080


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


_integ_accumulated_loss_of_productivity = functions.Integ(
    lambda: new_loss(), lambda: init_accumulated_loss_of_producitivity())

_integ_available_test_kits = functions.Integ(lambda: produced_test_kits() - used_test_kits(),
                                             lambda: init_available_test_kits())

_integ_critical_cases = functions.Integ(
    lambda: infected_critical_case_rate() - critical_cases_recovery_rate() - death_rate() +
    quarantined_critical_case_rate(), lambda: init_critical_cases())

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
    ) - quarantined_critical_case_rate(), lambda: init_isolated())

_integ_recovered = functions.Integ(
    lambda: critical_cases_recovery_rate() + infected_asymptomatic_recovery_rate(
    ) + infected_symptomatic_recovery_rate() - deimmunization_rate() + isolated_recovery_rate(),
    lambda: init_recovered())

_integ_susceptible = functions.Integ(lambda: deimmunization_rate() - infection_rate(),
                                     lambda: init_susceptible())
