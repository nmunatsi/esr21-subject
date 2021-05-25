from edc_constants.constants import OTHER

from edc_list_data import PreloadData

list_data = {
    'esr21_subject.saecriteria': [
        ('death', 'Death'),
        ('life_threatening', 'Life-threatening'),
        ('hospitalization', 'Initial or prolonged hospitalization'),
        ('birth_defects', 'Congenital anomaly/birth defect'),
        ('incapacity', 'Persistent or significant disability/incapacity'),
        (OTHER, 'Other important medical event'),
    ],
    'esr21_subject.subjectrace': [
        ('american', 'American Indian or Alaska Native'),
        ('asian', 'Asian'),
        ('african', 'Black or African American'),
        ('pacific_islander', 'Native Hawaiian or Other Pacific Islanders'),
        ('white', 'White'),
    ],
}

preload_data = PreloadData(
    list_data=list_data)