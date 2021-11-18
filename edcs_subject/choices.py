MISS_ARV = (
    ("at_least_once_every_week", "At least once every week"),
    ("at_least_once_a_month", "At least once in a month"),
    ("at_least_once_3_months", "At least once in 3 months"),
    ("at_least_once_a_year", "At least once a year"),
    ("dont_remember", "I Do not remember"),
    ("others", "Other"),
)

LUNG_DISEASE = (
    ("yes_copd", "Yes, COPD"),
    ("yes_asthma", "Yes, Asthma"),
    ("yes_interstitial_lung_disease", "Yes, Interstitial Lung Disease"),
    ("No", "No"),
    ("decline_to_answer", "Decline to answer"),
    ("Dont_know", "Do not know"),
)
EDUCATION = (
    ("never_been_in_school", "Never been in school"),
    ("primary_education", "Completed Primary Education"),
    ("secondary_education", "Completed Secondary Education (‘’O’’ or ‘’A’’ level)"),
    ("vocational_training", "Vocational training"),
    ("tertiary_education", "Tertiary Education"),
    ("others", "Other"),
)

OCCUPATION = (
    ("civil_servant", "Civil Servant"),
    ("house_wife", "House wife"),
    ("peasant", "Peasant"),
    ("petty_trader", "Petty trader"),
    ("entrepreneur", "Entrepreneur"),
    ("unemployed", "Unemployed"),
    ("business_man", "Business man/woman"),
    ("others", "Other"),
)

MATERIAL_BUILD_FLOOR = (
    ("soil_sand_mud", "Soil/ sand/ mud"),
    ("cement_concrete_tiles", "Cement/ concrete/ tiles"),
    ("other", "Others"),
)

MATERIAL_BUILD_WALL = (
    ("soil_sand_mud", "There is no wall"),
    ("cement_concrete_tiles", "Grass"),
    ("other", "Canes/ Palm"),
    ("trees_mud", "Trees and mud"),
    ("stone_mud", "Stones and mud"),
    ("wood_timber", "Wood/timber"),
    ("cement_concrete_bricks", "Cement/ concrete blocks/ burnt blocks/bricks."),
    ("other", "Others"),
)

MATERIAL_BUILD_ROOFING = (
    ("soil_sand_mud", "Iron sheet/roofing tiles"),
    ("grass_leaves_soil", "Grass/ leaves/ palm leaves/ soil"),
    ("other_materials", "Other materials"),
)

COOKING = (
    ("electricity_stove", "Electricity stove"),
    ("gas_stove", "Gas stove"),
    ("kerosene_stove", "Kerosene stove"),
    ("charcoal", "Charcoal"),
    ("logs_woods", "Logs/woods"),
    ("grass_leaves", "Grass/leaves"),
    ("animal_waste", "Animal waste"),
    ("plants_waste", "Plants waste"),
    ("dont_cook", "We do not cook"),
    ("other", "Others"),
)

POWER_SOURCE = (
    ("electricity", "Electricity"),
    ("battery_torch", "Battery/ torch "),
    ("solar_energy", "Solar energy"),
    ("other", "Others"),
)

SMOKE_TOBACCO_PRODUCTS = (
    ("yes_current_smoker", "Yes, Current smoker"),
    ("yes_past_smoker", "Yes, past smoker"),
    ("never", "Never"),
)

TOBACCO_PRODUCTS = (
    ("yes_cigarettes", "Yes, Cigarettes"),
    ("yes_cigars", "Yes, Cigars"),
    ("yes_shisha", "Yes, Shisha"),
    ("yes_pipes", "Yes, pipes"),
    ("none_of_above", "None of the above"),
)

SMOKE_TOBACCO_PRODUCTS_FREQUENCY = (
    ("daily", "Daily"),
    ("every_other_day", "Every other day"),
    ("weekly", "Weekly (Not daily)"),
    ("monthly", "Monthly(Not weekly)"),
    ("others", "Others"),
)

SMOKE_INSIDE = (
    ("daily", "Daily"),
    ("weekly", "Weekly"),
    ("monthly", "Monthly"),
    ("less_than_monthly", "Less than monthly"),
    ("never", "Never"),
    ("others", "Others"),
)

ALCOHOL_CONSUMPTION = (
    ("yes_current_consumer", "Yes, Current consumer"),
    ("yes_past_consumer", "Yes, past consumer"),
    ("never", "Never"),
)

ALCOHOL_CONSUMPTION_FREQUENCY = (
    ("daily", "1-Daily"),
    ("every_other_day", "Every other day"),
    ("weekly", "Weekly (Not daily )"),
    ("monthly", "Monthly (Not weekly)"),
    ("others", "Others"),
)

QN60 = (
    ("less_than_12yrs", "≤ 12 years"),
    ("12_13yrs", "12-13 years"),
    ("14_15yrs", "14-15 years"),
    ("greater_than_16yrs", "≥ 16 years"),
)

QN61 = (
    ("nulliparous", "Nulliparous"),
    ("less_than_20yrs", "≤ 20years"),
    ("20_29yrs", "20-29 years"),
    ("30_39yrs", "30-39 years"),
    ("greater_than_39yrs", "≥ 39 years"),
)

QN62 = (
    ("nulliparous", "Nulliparous"),
    ("less_than_25yrs", "≤ 25years"),
    ("25_29_yrs", "25-29 years"),
    ("30_39yrs", "30-39 years"),
    ("greater_than_39yrs", "≥ 39 years"),
)

QN64 = (
    ("yes_current_user", "Yes, Current user"),
    ("yes_past_user", "Yes, Past user"),
    ("No", "No"),
    ("decline_to_answer", "Decline to answer"),
)

QN65 = (
    ("less_than_5yrs", "≤ 5 years"),
    ("greater_than_5yrs", "≥ 5 years"),
)

QN66 = (
    ("less_than_5yrs_ago", "≤ 5 years ago"),
    ("greater_than_5yrs_ago", "≥ 5 years ago"),
)

QN70 = (
    ("less_than_46yrs", "≤ 46 years"),
    ("46_50yrs", "46-50 years"),
    ("greater_than_51yrs", "≥ 51 years"),
)

QN72 = (
    ("textile_industry", "Textile industry"),
    ("chemical_production_industry", "Chemical production industry"),
    ("food_processing_industry", "Food processing industry"),
    ("drug_industry", "Drug industry"),
    ("milling_industry", "Milling industry"),
    ("construction_industry", "Construction industry"),
    ("other", "Other"),
)

SYMPTOMS = (
    ("headache", "Headache"),
    ("fever", "Fever"),
    ("muscle_ache", "Muscle ache"),
    ("weakness_tiredness", "Weakness/tiredness "),
    ("nausea_vomiting", "Nausea/vomiting"),
    ("abdominal_pain", "Abdominal pain"),
    ("diarrhea", "Diarrhea"),
    ("sore_throat", "Sore throat"),
    ("cough", "Cough"),
    ("shortness_of_breath", "Shortness of breath"),
    ("loss_taste", "Loss of taste"),
    ("no_loss_smell", "No Loss of smell"),
)

QN82 = (
    ("positive_test", "One or more positive test(s) "),
    ("negative_more_positive", "One or more negative tests, but none were positive"),
    ("all_test_failed", "All tests failed"),
    ("waiting_results", "Waiting for all results"),
)

COVID_VACCINE = (
    ("dont_know_type", "Don’t know type"),
    ("pfizer_biontech_moderna", "Pfizer/BioNTech Moderna"),
    ("oxford_astraZeneca", "Oxford/AstraZeneca"),
    ("janssen_johnson_Johnson", "Janssen\Johnson&Johnson"),
    ("novavax", "Novavax"),
    ("sinovac", "Sinovac"),
    ("sputnik", "Sputnik"),
    ("valneva", "Valneva"),
    ("sinopharm", "Sinopharm"),
)

QN87 = (
    ("government_uganda", "Government of Uganda"),
    ("research_study", "Research study/trial "),
    ("other", "Others"),
)

QN88 = (("one", "One"), ("two", "Two"), ("three_more", "Three or More"))

QN90 = (
    ("cough_dont_go_away", "A cough that doesn't go away after 2 or 3 weeks"),
    ("long_standing_cough", "A long-standing cough that gets worse"),
    ("coughing_blood", "Coughing up blood or rust-colored sputum (spit or phlegm)"),
    (
        "chest_infections",
        "Chest infections that keep coming back such as bronchitis, pneumonia etc",
    ),
    ("chest_pain", "Chest pain that is often worsen when breathing or coughing"),
    ("persistent_breathlessness", "Persistent breathlessness"),
    ("persistent_tiredness", "Persistent tiredness or lack of energy"),
    ("wheezing", "Wheezing"),
    ("shortness_of_breath", "Shortness of breath"),
    ("unexplained_weight_loss", "Unexplained weight loss"),
    ("other", "Others"),
)

QN91 = (
    ("less_than_1month", "Less than 1 month"),
    ("1_3months", "1-3 months"),
    ("3_6months", "3-6 months"),
    ("greater_than_6months", ">6 months"),
)

QN92 = (
    ("", "Sudden onset"),
    ("", "Gradual onset"),
    ("", "Progressive in severity"),
    ("", "Intermittent in severity"),
    ("other", "Others"),
)

QN94 = (
    ("mother", "Mother"),
    ("father", "Father"),
    ("brother", "Brother"),
    ("sister", "Sister"),
    ("grandparent_mother_side", "Grandparent from mother’s side"),
    ("grandparent_father_side", "Grandparent from father’s side"),
    ("other", "Others"),
)

QN95 = (
    ("Yes", "Yes"),
    ("No", "No"),
    ("family_history_unknown", "Family history unknown"),
)

QN98 = (
    ("blood_tests", "Blood tests"),
    ("chest_xray", "Chest X-ray"),
    ("ct_scan", "CT scan"),
    ("lung_cancer_biopsy", "Lung cancer biopsy"),
    ("sputum_tb_dx", "Sputum for TB diagnosis"),
    ("other", "Others"),
    ("none_of_above", "None of the above"),
)

QN100 = (
    ("yes", "Yes"),
    ("no_declined", "No, declined"),
    ("no_sputum", "No sputum"),
)

QN9101 = (
    ("tb_positive", "TB positive"),
    ("tb_negative", "TB negative (No TB)"),
    ("inconclusive_results", "Inconclusive results"),
)

QN102 = (
    ("lung_cancer_confirmed", "Lung cancer confirmed"),
    ("non_cancerous", "Non-cancerous"),
    ("inconclusive_results", "Inconclusive results"),
)

QN103 = (
    ("one", "One (1)"),
    ("two", "Two (2)"),
    ("three", "Three (3)"),
    ("four", "Four (4)"),
)

QN105 = (
    ("chemotherapy", "Chemotherapy"),
    ("radiation", "Radiation"),
    ("surgical_resection", "Surgical resection"),
    ("immunotherapy", "Immunotherapy"),
    ("tyrosine_kinase_inhibitor", "Tyrosine kinase inhibitor "),
    ("1_2above", "1 & 2 above"),
    ("other", "Others"),
)

QN106 = (
    ("hiv_positive", "HIV positive"),
    ("hiv_negative", "HIV negative"),
    ("inconclusive_results", "Inconclusive results"),
)

QN110 = (
    ("a", "A"),
    ("b", "B"),
    ("c", "C"),
)
