affirmed_general_exposure_example_map = {}
negated_general_exposure_example_map = {}
no_exposure_general_exposure_example_map = {}

# FOOD
affirmed_general_exposure_example_map['FOOD'] = ['Patient admits to eating raw oysters from the ocean',
    'Patient confesses to buying expired discount oysters in the market',
    'Patient recently ate 10 pounds of shellfish',
    "Recently consumed undercooked meat at a local restaurant.",
    "Consumed unpasteurized dairy products from a local farm.",
    ]

negated_general_exposure_example_map['FOOD'] = ['Patient denies eating oysters',
    'Patient denies eating seafood',
    'Patient has not recently eaten seafood',
    'Has not recently eaten oysters',
    "Pt has not consumed undercooked pork.",]

no_exposure_general_exposure_example_map['FOOD'] = ['Patient cautioned to be careful about raw oysters',
   'Patient takes oyster shell supplements for calcium',
   'Patient encouraged to not eat shellfish on upcoming vacation',
   'Advised to not eat raw pork',
   'Cautioned against drinking unpasteurized milk',
   ]
   
# WATER
affirmed_general_exposure_example_map['WATER'] = ['Patient walked in pond water with open wounds',
    "Recently waded in a river without shoes or boots.",
    "History of wading in floodwaters during a recent storm.",
    "She started feeling ill after being in a public jacuzzi",
    'Swam in the ocean with an open wound'
]

negated_general_exposure_example_map['WATER'] = ['Patient denies recent water activities',
    'Patient has not recently been swimming',
    "Denies contact with standing or stagnant water.",
    "Has not been swimming in freshwater lakes or rivers.",
    "Did not go wading in the river when camping last weekend."
]

no_exposure_general_exposure_example_map['WATER'] = ['Make sure to drink plenty of water after your procedure',
    'Do not go swimming for at least 72 hours',
    'Never learned to swim',
    'Lives on Cold River drive',
    'Owns an air stream trailer',
]
   
# ENVIRONMENTAL
affirmed_general_exposure_example_map['ENVIRONMENTAL'] = ["Reports handling soil and construction materials without gloves.",
    "Participated in humanitarian work in an area with poor sanitation.",
    "Not feeling well after inhaling dust in an attic.",
    "Symptoms started after playing in a sandbox.",
    "Sickness started following working in a flower bed without gloves.",
]
    
negated_general_exposure_example_map['ENVIRONMENTAL'] = ["No history of working with hazardous chemicals.",
    "No recent handling soil or gardening without gloves.",
    "Has not recently inhaled dust.",
    "to their knowledge, they have not been in contact with organic solvents",
    'They have never been in contact with mold',
]
    
no_exposure_general_exposure_example_map['ENVIRONMENTAL'] = ["Record collection has been gathering dust",
    "Cleaned the basement recently",
    "Attic was cleaned for 4 hours",
    "Keeps a jello mold in the kitchen",
    "Make sure to dispose of solvents properly"
]
   
# PEOPLE
affirmed_general_exposure_example_map['PEOPLE'] = ['Known exposure for multiple days to a person who was positive for COVID',
    'Exposed over the past week to a family member with the flu',
    'Exposed recently to family member with influenza',
    'Lives with cousin who test positive for RSV',
    'Her college aged children in her home had similar symptoms',
]

negated_general_exposure_example_map['PEOPLE'] = ['Patient has not been recently exposed to others with respiratory illness',
    'Has not been around other sick people',
    'No one in their family has been sick',
    'No known exposures to anyone is is COVID+',
    'Has not been around anyone with the flu',
    ]

no_exposure_general_exposure_example_map['PEOPLE'] = ['Be sure to wear a mask to prevent spread of COVID',
    'Encouraged to get COVID vaccine',
    'Reminded patient of increase of RSV in this state',
    'Reminded patient of current infectious disease precautions',
    'Reviewed precautions of unprotected sex with patient before their trip',
   ]
   
# finally, there are many sentences which are false positives which get identified as exposures for some reason
# so while they are not associated with any particular exposure type, we will add them here
no_exposure_general_exposure_example_map['UNSPECIFIED'] = ['Plan of care discussed with patients and significant other.',
'Will reassess diagnosis in a few days after mediciation',
'lots of infectious stull already sent',
'I have requested a consultation by: Infectious Disease',
'This is a transfer of care request',
]