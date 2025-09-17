import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/IRS_2025_67/hand_solo_virtual_nav/install/hand_solo_virtual_nav'
