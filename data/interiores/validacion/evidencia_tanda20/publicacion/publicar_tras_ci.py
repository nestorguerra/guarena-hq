from pathlib import Path
import subprocess,json,hashlib,datetime,argparse
parser=argparse.ArgumentParser();parser.add_argument("--ci",required=True,type=int);opts=parser.parse_args()
p=Path('.cache/calidad/tanda20');expected=(p/'commit_producto.txt').read_text().strip();assert len(expected)==40

def cmd(*args):
 r=subprocess.run(args,capture_output=True,text=True,check=True);return r.stdout.strip()
run=json.loads(cmd('/opt/homebrew/bin/gh','run','view',str(opts.ci),'--json','databaseId,headSha,status,conclusion,url,jobs'))
assert run['headSha']==expected and run['status']=='completed' and run['conclusion']=='success',run
workflow=json.loads(cmd('/opt/homebrew/bin/gh','api','repos/nestorguerra/guarena-hq/actions/runs/'+str(opts.ci),'--jq','{id,path,head_sha,status,conclusion}'))
assert workflow['id']==opts.ci and workflow['path']=='.github/workflows/validar.yml',workflow
assert workflow['head_sha']==expected and workflow['status']=='completed' and workflow['conclusion']=='success',workflow
jobs={j['name']:j for j in run['jobs']};required={'validate_signs','validate_interiors'}
assert required<=jobs.keys(),('Faltan validadores obligatorios',required-jobs.keys())
assert all(j['conclusion']=='success' for j in run['jobs']),run['jobs']
assert cmd('git','rev-parse','HEAD')==expected
assert not cmd('git','status','--porcelain'), 'Cambios activos antes de publicar'
f=json.loads((p/'estado_candidato.json').read_text())['archivos'];assert all(hashlib.sha256(Path(q).read_bytes()).hexdigest()==h for q,h in f.items())
cmd('git','fetch','origin','+refs/pull/2/merge:refs/remotes/origin/pr2-merge','main:refs/remotes/origin/main')
tree=cmd('git','rev-parse',expected+'^{tree}');tested=cmd('git','rev-parse','origin/pr2-merge^{tree}');assert tested==tree,(tested,tree)
base=cmd('git','rev-parse','origin/main');cmd('git','merge-base','--is-ancestor',base,expected)
rec={'fecha':datetime.datetime.now(datetime.timezone.utc).isoformat(),'commit':expected,'ci':run,'workflow_verificado':workflow,'main_anterior':base,'arbol_ci_y_producto':tree,'merge_ci':cmd('git','rev-parse','origin/pr2-merge')}
(p/'publicar_precondiciones.json').write_text(json.dumps(rec,ensure_ascii=False,indent=1)+'\n')
print(cmd('git','push','origin',expected+':main'))
remote=cmd('/opt/homebrew/bin/gh','api','repos/nestorguerra/guarena-hq/branches/main','--jq','.commit.sha');assert remote==expected,remote
rec['main_verificado']=remote;(p/'main_actualizado.json').write_text(json.dumps(rec,ensure_ascii=False,indent=1)+'\n');print('Main actualizado y releído:',remote)
