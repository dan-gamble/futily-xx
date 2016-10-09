PLAYER_LEVEL_SCHEMA = {
    'gold': {
        'color__in': ['totw_gold', 'rare_gold', 'gold'],
    },
    'silver': {
        'color__in': ['totw_silver', 'rare_silver', 'silver'],
    },
    'bronze': {
        'color__in': ['totw_bronze', 'rare_bronze', 'bronze'],
    },
    'totw_all': {
        'color__in': ['totw_gold', 'totw_silver', 'totw_bronze'],
    },
    'totw_gold': {
        'color': 'totw_gold',
    },
    'totw_silver': {
        'color': 'totw_silver',
    },
    'totw_bronze': {
        'color': 'totw_bronze',
    },
    'rare_all': {
        'color__in': ['rare_gold', 'rare_silver', 'rare_bronze'],
    },
    'rare_gold': {
        'color': 'rare_gold'
    },
    'rare_silver': {
        'color': 'rare_silver'
    },
    'rare_bronze': {
        'color': 'rare_bronze'
    },
    'nonrare_all': {
        'color__in': ['gold', 'silver', 'bronze'],
    },
    'nonrare_gold': {
        'color': 'gold'
    },
    'nonrare_silver': {
        'color': 'silver'
    },
    'nonrare_bronze': {
        'color': 'bronze'
    },
    'legend': {
        'color': 'legend'
    }
}
PLAYER_POSITION_SCHEMA = {
    'def': {
        'position__in': ['RB', 'RWB', 'CB', 'LB', 'LWB']
    },
    'mid': {
        'position__in': ['RM', 'RW', 'RF', 'CDM', 'CM', 'CAM', 'LM', 'LW', 'LF']
    },
    'att': {
        'position__in': ['CF', 'ST']
    },
    'rbs': {
        'position__in': ['RB', 'RWB']
    },
    'lbs': {
        'position__in': ['LB', 'LWB']
    },
    'rms': {
        'position__in': ['RM', 'RW', 'RF']
    },
    'lms': {
        'position__in': ['LM', 'LW', 'LF']
    },
    'cms': {
        'position__in': ['CDM', 'CM', 'CAM']
    },
    'sts': {
        'position__in': ['CF', 'ST']
    }
}
PLAYER_SORT_SCHEMA = {
    'rating': 'rating',
    'pace': 'card_att_1',
    'shooting': 'card_att_2',
    'passing': 'card_att_3',
    'dribbling': 'card_att_4',
    'defending': 'card_att_5',
    'physical': 'card_att_6'
}
