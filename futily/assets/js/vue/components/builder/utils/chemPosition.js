export const goodChem = {
  'ST': [ 'CF' ],
  'CF': [ 'CAM', 'ST' ],
  'LF': [ 'LW' ],
  'RF': [ 'RW' ],
  'LW': [ 'LM', 'LF' ],
  'RW': [ 'RM', 'RF' ],
  'LM': [ 'LW' ],
  'RM': [ 'RW' ],
  'CAM': [ 'CF', 'CM' ],
  'CM': [ 'CAM', 'CDM' ],
  'CDM': [ 'CM' ],
  'LB': [ 'LWB' ],
  'LWB': [ 'LB' ],
  'RB': [ 'RWB' ],
  'RWB': [ 'RB' ]
}

export const weakChem = {
  'LF': [ 'ST', 'CF', 'RF', 'LM' ],
  'RF': [ 'ST', 'CF', 'LF', 'RM' ],
  'ST': [ 'LF', 'RF' ],
  'CF': [ 'LF', 'RF' ],
  'LW': [ 'RW', 'LWB' ],
  'RW': [ 'LW', 'RWB' ],
  'RM': [ 'RF', 'CM', 'RB', 'LM', 'RWB' ],
  'LM': [ 'LF', 'CM', 'LB', 'LWB', 'RM' ],
  'CAM': [ 'CDM' ],
  'CM': [ 'LM', 'RM' ],
  'CDM': [ 'CB', 'CAM' ],
  'RB': [ 'RM', 'CB', 'LB', 'RWB' ],
  'LB': [ 'LM', 'CB', 'RB', 'LWB' ],
  'LWB': [ 'LM', 'LW', 'RWB' ],
  'RWB': [ 'RM', 'RW', 'LWB' ],
  'CB': [ 'RB', 'LB', 'CDM' ]
}
