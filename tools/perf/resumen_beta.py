"""Summarize every completed alternating run; missing runs are an error, not a green result."""
import argparse,json,statistics
from pathlib import Path

p=argparse.ArgumentParser();p.add_argument('directory');a=p.parse_args();root=Path(a.directory)
setup=json.loads((root/'setup.json').read_text());rounds=setup['rounds']
data={k:[json.loads((root/(k+'_'+str(i)+'.json')).read_text()) for i in range(rounds)] for k in ['before','after']}
assert rounds>=3,'At least three alternating rounds are required'
for runs in data.values():
 for d in runs:
  assert not d['errors'] and not d.get('end',{}).get('errors')
  if not setup['auto']:assert d['quality']=='alta' and d['pr']==1.5,'Fixed quality differs'
def median(k,fn):return statistics.median(fn(d) for d in data[k])
out={'rounds':rounds,'adaptive':setup['auto'],'load_network_mbps':setup['mbps'],'control_ms':{k:median(k,lambda d:d['control_ms']) for k in data}}
out['control_ms_range']={k:[min(d['control_ms'] for d in data[k]),max(d['control_ms'] for d in data[k])] for k in data}
out['load_reduction_percent']=100*(1-out['control_ms']['after']/out['control_ms']['before'])
out['ready_method']=setup.get('ready_method','legacy_fast_forward_only_valid_for_steady_render')
out['load_25_percent']=out['load_reduction_percent']>=25 if out['ready_method']=='normal_intro_no_fast_forward' else None
if not setup['load_only']:
 out['routes']={}
 for route in ['walk','spin','drive']:
  row={k:{m:median(k,lambda d:d[route]['fps'] if m=='fps' else d[route]['ms'][m]) for m in ['fps','mean','p95','p99']} for k in data}
  # Use measured frame times, not the FPS display already rounded to one decimal.
  row['fps_gain_percent']=100*(row['before']['mean']/row['after']['mean']-1)
  row['fps_range']={k:[min(d[route]['fps'] for d in data[k]),max(d[route]['fps'] for d in data[k])] for k in data}
  row['mean_time_reduction_percent']=100*(1-row['after']['mean']/row['before']['mean'])
  row['gain_25_percent']=row['fps_gain_percent']>=25
  row['at_least_30fps']=row['after']['fps']>=30
  row['p95_p99_no_regression']=all(row['after'][m]<=row['before'][m] for m in ['p95','p99'])
  out['routes'][route]=row
(root/'summary.json').write_text(json.dumps(out,ensure_ascii=False,indent=1)+'\n')
print(json.dumps(out,ensure_ascii=False,indent=1))
