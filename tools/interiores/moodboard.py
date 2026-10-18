# The moodboard of a typology (technical backlog, I-02): real photographs of interiors of that kind from Wikimedia
# Commons, found by searching its files, with their page, author and licence — metadata only: no picture is downloaded,
# and none goes into the game. They are reference for whoever builds and reviews the kit.
#   python3 tools/interiores/moodboard.py <tipología> "<búsqueda>" ["<búsqueda>" …]   → the kit's moodboard (10–14)
import json, os, re, sys, urllib.parse, urllib.request
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
API = 'https://commons.wikimedia.org/w/api.php'
FREE = re.compile(r'^(CC0|CC BY(-SA)? [0-9.]+|Public domain|PD.*|CC BY(-SA)?.*)$', re.I)

def buscar(q, n=40):
    url = API + '?' + urllib.parse.urlencode({'action': 'query', 'generator': 'search', 'gsrsearch': q + ' filetype:bitmap', 'gsrnamespace': 6, 'gsrlimit': n,
                                              'prop': 'imageinfo', 'iiprop': 'url|extmetadata', 'format': 'json'})
    req = urllib.request.Request(url, headers={'User-Agent': 'GuarenaHQ-moodboard/1.0 (reference only)'})
    data = json.load(urllib.request.urlopen(req, timeout=60))
    out = []
    for p in (data.get('query', {}).get('pages') or {}).values():
        ii = (p.get('imageinfo') or [{}])[0]; md = ii.get('extmetadata', {})
        lic = (md.get('LicenseShortName') or {}).get('value', '')
        autor = re.sub(r'<[^>]+>', '', (md.get('Artist') or {}).get('value', '')).strip()
        if not lic or not autor or not FREE.match(lic): continue
        out.append({'titulo': p['title'].replace('File:', ''), 'url': ii.get('descriptionurl'), 'autor': autor[:120], 'licencia': lic})
    return out

if __name__ == '__main__':
    tip, qs = sys.argv[1], sys.argv[2:]
    seen, refs = set(), []
    for q in qs:
        for r in buscar(q):
            if r['url'] in seen: continue
            seen.add(r['url']); refs.append(r)
    print(json.dumps(refs[:30], ensure_ascii=False, indent=1))
