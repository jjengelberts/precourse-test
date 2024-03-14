# This script removes the read-only flags introduced by nbgrader


import os
import json

for file in os.listdir():
    if file[-6:] == '.ipynb':
        with open(file, 'r') as f:
            chal = json.load(f)
        if 'cells' in chal:
            for idx in range(len(chal['cells'])):
                if 'editable' in chal['cells'][idx]['metadata']:
                    chal['cells'][idx]['metadata']['editable'] = True
        else:
            # No cells found
            continue
        with open(file, 'w') as f:
            json.dump(chal, f)