from edcs_constants.constants import (
    NEVER,
    NOT_APPLICABLE,
    OTHER,
    YES_CURRENT_CHEW,
    YES_CURRENT_SMOKER,
    YES_PAST_CHEW,
    YES_PAST_SMOKER,
)

list_data = {
    "edcs_lists.covidsymptoms": [
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
    ],
    "edcs_lists.familymembers": [
        ("mother", "Mother"),
        ("father", "Father"),
        ("sister", "Sister"),
        ("brother", "Brother"),
        ("maternal_aunt", "Maternal Aunt"),
        ("maternal_uncle", "Maternal Uncle"),
        ("paternal_aunt", "Paternal Aunt"),
        ("paternal_uncle", "Paternal Uncle"),
        ("maternal_grandmother", "Maternal Grandmother"),
        ("maternal_grandfather", "Maternal Grandfather"),
        ("paternal_grandmother", "Paternal Grandmother"),
        ("paternal_grandfather", "Paternal Grandfather"),
        (OTHER, "Other"),
    ],
    "edcs_lists.lungcancersymptoms": [
        ("cough_3_week", "A cough that doesn't go away after 2 or 3 weeks"),
        ("long_standing_cough", "A long-standing cough that gets worse"),
        ("coughing_blood", "Coughing up blood or rust-colored sputum (spit or phlegm)"),
        (
            "chest_infections",
            " Chest infections that keep coming back such as bronchitis, pneumonia etc",
        ),
        (
            "chest_pain_coughing",
            " Chest pain that is often worsen when breathing or coughing",
        ),
        ("persistent_breathlessness", "Persistent breathlessness"),
        ("tiredness_lack_energy", "Persistent tiredness or lack of energy"),
        ("wheezing", " Wheezing"),
        ("shortness_of_breath", "Shortness of breath"),
        ("unexplained_weight_loss", "Unexplained weight loss"),
        (OTHER, "Other"),
    ],
    "edcs_lists.smokingtobaccoproducts": [
        (YES_CURRENT_SMOKER, "Yes, Current smoker"),
        (YES_PAST_SMOKER, "Yes, past smoker"),
        (YES_CURRENT_CHEW, "Yes, current chew tobacco"),
        (YES_PAST_CHEW, "Yes, past chew tobacco"),
        (NEVER, "Never"),
    ],
    "edcs_lists.tobaccoproducts": [
        (NOT_APPLICABLE, "Not applicable"),
        ("yes_cigarettes", "Yes, Cigarettes"),
        ("yes_cigars", "Yes, Cigars"),
        ("yes_shisha", "Yes, Shisha"),
        ("yes_pipes", "Yes, pipes"),
        (OTHER, "Other"),
    ],
    "edcs_lists.contraceptives": [
        (NOT_APPLICABLE, "Not applicable"),
        ("oral_contraceptives.", "Oral contraceptives."),
        ("injectables", "Injectables"),
        ("implants", "Implants"),
        ("intra_uterine_device", "Intra Uterine Device"),
        ("patch", "Patch"),
        ("rings", "Rings"),
        ("traditional_contraceptives", "Traditional contraceptives"),
        (OTHER, "Other"),
    ],
    "edcs_lists.covidvaccine": [
        (NOT_APPLICABLE, "Not applicable"),
        ("dont_know_type", "Don’t know type"),
        ("pfizer_biontech_moderna", "Pfizer/BioNTech Moderna"),
        ("oxford_astraZeneca", "Oxford/AstraZeneca"),
        ("janssen_johnson_Johnson", "Janssen\Johnson&Johnson"),
        ("novavax", "Novavax"),
        ("sinovac", "Sinovac"),
        ("sputnik", "Sputnik"),
        ("valneva", "Valneva"),
        ("sinopharm", "Sinopharm"),
        (OTHER, "Other"),
    ],
    "edcs_lists.hivsubtype": [
        (NOT_APPLICABLE, "Not applicable"),
        ("A", "A"),
        ("B", "B"),
        ("C", "C"),
        ("D", "D"),
        ("E", "E"),
        ("F", "F"),
        ("G", "G"),
        ("H", "H"),
        ("K", "K"),
    ],
    "edcs_lists.cookingdone": [
        ("inside_house", "Inside the house"),
        ("outside_house", "Outside the house"),
    ],
    "edcs_lists.cookingarea": [
        ("window_outside", "Window outside"),
        ("chimney", "Chimney"),
        ("exhaust", "Exhaust"),
        ("partial_open_outside", "Partially open to the outside"),
        ("none", "None"),
    ],
    "edcs_lists.airmonitorproblem": [
        (NOT_APPLICABLE, "Not applicable"),
        ("window_outside", "Window outside"),
        ("chimney", "Chimney"),
        ("exhaust", "Exhaust"),
        ("partial_open_outside", "Partially open to the outside"),
        ("none", "None"),
    ],
    "edcs_lists.cookingfuel": [
        ("kerosene", "Kerosene"),
        ("charcoal", "Charcoal"),
        ("coal", "Coal"),
        ("gas ", "Gas "),
        ("agricultural_crop", "Agricultural crop"),
        ("wood", "Wood"),
        ("gobar_gas ", "Gobar gas "),
        ("electricity", "Electricity"),
        ("straw_shrubs_grass ", "Straw/shrubs/grass "),
        ("agricultural_crop", "Agricultural crop"),
        ("animal_dung", "Animal dung"),
        (OTHER, "Other"),
    ],
    "edcs_lists.othercookingfuel": [
        ("no_other_fuel", "No other fuel except primary fuel used for cooking"),
        ("kerosene", "Kerosene"),
        ("charcoal", "Charcoal"),
        ("coal", "Coal"),
        ("gas ", "Gas "),
        ("agricultural_crop", "Agricultural crop"),
        ("wood", "Wood"),
        ("gobar_gas ", "Gobar gas "),
        ("electricity", "Electricity"),
        ("straw_shrubs_grass ", "Straw/shrubs/grass "),
        ("agricultural_crop", "Agricultural crop"),
        ("animal_dung", "Animal dung"),
        (OTHER, "Other"),
    ],
    "edcs_lists.solidfuel": [
        ("no_other_fuel", "No other fuel except primary fuel used for cooking"),
        ("kerosene", "Kerosene"),
        ("charcoal", "Charcoal"),
        ("coal", "Coal"),
        ("gas ", "Gas "),
        ("agricultural_crop", "Agricultural crop"),
        ("wood", "Wood"),
        ("gobar_gas ", "Gobar gas "),
        ("electricity", "Electricity"),
        ("straw_shrubs_grass ", "Straw/shrubs/grass "),
        ("agricultural_crop", "Agricultural crop"),
        ("animal_dung", "Animal dung"),
        (OTHER, "Other"),
    ],
    "edcs_lists.somaticmutations": [
        (NOT_APPLICABLE, "Not applicable"),
        ("EGFR", "EGFR"),
        ("KRAS", "KRAS"),
        ("ALK", "ALK"),
        ("HER2", "HER2"),
        ("ROS1", "ROS1"),
        ("MET", "MET"),
        ("BRAF", "BRAF"),
        ("ERBB2", "ERBB2"),
        ("RET", "RET"),
        ("TP53", "TP53"),
        ("CDKN2A", "CDKN2A"),
        ("RAF1", "RAF1"),
        ("MAP2K1", "MAP2K1"),
        ("SMAD4", "SMAD4"),
        ("NRAS", "NRAS"),
        ("AR", "AR"),
        ("FGFR3", "FGFR3"),
        ("PDGFRA", "PDGFRA"),
        ("B2M", "B2M"),
        ("FBXW7", "FBXW7"),
        ("KEAPI", "KEAPI"),
        ("POLE", "POLE"),
        ("PTEN", "PTEN"),
        ("U2AFI", "U2AFI"),
        ("AKT", "AKT"),
        ("ODR2", "ODR2"),
        ("ERBB3", "ERBB3"),
        ("IDH2", "IDH2"),
        ("FGFR4", "FGFR4"),
        ("NMYC", "NMYC"),
        ("ERG", "ERG"),
        ("MTOR", "MTOR"),
        ("FGFR1", "FGFR1"),
        ("APC", "APC"),
        ("CCND1", "CCND1"),
        ("MYC", "MYC"),
        ("CDK4", "CDK4"),
        ("CTNNBI", "CTNNBI"),
        ("RICTOR", "RICTOR"),
        ("CDKN2A", "CDKN2A"),
        ("HRAS", "HRAS"),
        ("KIT", "KIT"),
        ("SMO", "SMO"),
        ("AXL", "AXL"),
        ("FGFR2", "FGFR2"),
    ],
}

# preload_data = PreloadData(list_data=list_data)
