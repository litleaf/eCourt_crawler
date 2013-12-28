# -*- coding: utf-8 -*-
import yaml
import os

lawsuit_id = set()

for i, n in enumerate(os.listdir('./')):
    if not n.endswith('.yaml'):
        continue
    with open(n) as f:
        data = yaml.load(f)
        for r in data['rows']:
            lawsuit_id.add(r['identifier'])
    
    if i is 10:
        break

print len(lawsuit_id)
