
import vytools.utils as utils
import vytools.stage
from vytools.composerun import run
from vytools.config import CONFIG, ITEMS
import yaml, re, json, os, shutil, copy
import cerberus
import logging
from pathlib import Path

KEYSRULES = '[a-zA-Z0-9_]+'
SCHEMA = utils.BASE_SCHEMA.copy()
SCHEMA.update({
  'thingtype':{'type':'string', 'allowed':['compose']},
  'ui':{'type':'string', 'maxlength': 64, 'required': False},
  'subcompose':{'type':'list',
    'schema': {
      'type': 'dict',
      'schema': {
        'name': {'type': 'string', 'maxlength': 64},
        'calibration':{'type': 'dict', 'required':False}
      }
    }
  },
  'anchors':{'type': 'dict', 'required': False, 'keysrules': {'type': 'string', 'regex': KEYSRULES}}
})
VALIDATE = cerberus.Validator(SCHEMA)

def parse(name, pth, reponame, items=None):
  if items is None: items = vytools.ITEMS
  item = {
    'name':name,
    'thingtype':'compose',
    'repo':reponame,
    'depends_on':[],
    'path':pth
  }
  itemx = {'ui':None, 'subcompose':[], 'anchors':{}}
  try:
    with open(pth,'r') as r:
      content = yaml.safe_load(r.read())
      xvy = content.get('x-vy',{})
      itemx.update((k, xvy[k]) for k in itemx.keys() & xvy.keys())
      if itemx['ui'] is None: del itemx['ui']
      item.update(itemx)
    return utils._add_item(item, items, VALIDATE)
  except Exception as exc:
    logging.error('Failed to parse/load compose file "{n}" at "{p}":\n    {e}'.format(n=name,p=pth,e=exc))
    return False
ANCHORTHINGTYPES = ['stage','definition','vydir']
ANCHORTYPES = ['definition','argument','artifact','stage','vydir','directory','file']

def find_all(items, contextpaths=None):
  success = utils.search_all(r'(.+)\.compose\.y[a]*ml', parse, items, contextpaths=contextpaths)
  if success: # process definitions
    for (type_name, item) in items.items():
      if type_name.startswith('compose:'):
        successi = True
        item['depends_on'] = []
        for e in item['anchors']:
          atype = [a for a in ANCHORTYPES if item['anchors'][e].startswith(a+':')]
          if len(atype) == 1 and atype[0] in ANCHORTHINGTYPES: 
            successi &= utils._check_add(item['anchors'][e], atype[0], item, items, type_name)
          elif len(atype) != 1:
            successi = False
            logging.error('Unknown anchor type "{t} {v}" in {n}. Should be one of: {a}'.format(t=e,v=item['anchors'][e],n=type_name,a=','.join(ANCHORTYPES)))
        if 'ui' in item:
          successi &= utils._check_add(item['ui'].split('/')[0], 'vydir', item, items, type_name)
        for e in item['subcompose']:
          successi &= utils._check_add(e['name'], 'compose', item, items, type_name)
        success &= successi
        if not successi:
          logging.error('Failed to interpret/link compose {c}'.format(c=type_name))
  return success

def build(rootcompose, items=None, anchors=None, built=None, build_level=1, object_mods=None, eppath=None, label=None):
  if items is None: items = ITEMS
  if anchors is None: anchors = {} # These are the anchor values specified by the episode or otherwise
  if built is None: built = []
  if label is None: label = rootcompose.replace('compose:','') 
  if not utils.exists([rootcompose], items):
    return False
  elif not rootcompose.startswith('compose:'):
    logging.error('Item {} is not a compose file'.format(rootcompose))
    return False

  stage_versions = []
  item = items[rootcompose]
  name = item['name']

  cmd = []
  dependencies = [rootcompose]

  child_anchors = {} # Populate with the merged/filled out anchor values from subcomposes
  for sa in item['subcompose']:
    subname = sa['name']
    sublabel = label + '.'+subname.replace('compose:','')
    subcmds = build(subname, items=items, anchors=copy.deepcopy(anchors), built=built,
                            build_level=build_level, object_mods=object_mods, eppath=eppath, label=sublabel)
    if subcmds == False:
      return False
    else:
      child_anchors.update(subcmds['anchors']) # Brutal overwrites not namespacing. I don't think I want namespacing
      cmd += subcmds['command']
      dependencies += [d for d in subcmds['dependencies'] if d not in dependencies]
      stage_versions += [sv for sv in subcmds['stage_versions'] if sv not in stage_versions]

  anchor_defaults = copy.deepcopy(item.get('anchors',{}))
  anchor_values = copy.deepcopy(anchors)
  ordered = []
  for atype in ANCHORTYPES:
    ordered += [k for k,v in anchor_defaults.items() if v.startswith(atype+':')]
  replace_obj = {}
  for tag in ordered: # SORTED TO ENSURE THIS ORDER DEFINITION, ARGUMENT, STAGE, ARTIFACT
    val = anchor_defaults[tag]
    if val.startswith('definition:'):
      obj_mods = object_mods[tag] if object_mods and tag in object_mods else None
      if tag not in anchor_values:
        logging.warning('Anchor "{}" was not set for use in compose "{}"'.format(tag,rootcompose))
        replace_obj[tag] = {}
        deplist_ = []
      else:
        replace_obj[tag],deplist_ = vytools.object.expand(anchor_values[tag],
            val, items, object_mods=obj_mods)
      if replace_obj[tag] is None:
        return False
      dependencies += [d for d in deplist_ if d not in dependencies]
    elif val.startswith('argument:'):
      replace_obj[tag] = val.replace('argument:','',1)
      if tag not in anchor_values: 
        anchor_values[tag] = replace_obj[tag]
    elif val.startswith('stage:'):
      buildstage = anchor_values[tag] if tag in anchor_values else val
      tagged = vytools.stage.build([buildstage], items, anchor_values, built, build_level, jobpath=eppath)
      if tagged == False: return False
      for k,v in tagged.items():
        stage_versions += [sv for sv in v['stage_versions'] if sv not in stage_versions]
      replace_obj[tag] = tagged[buildstage]['tag']
    elif any([val.startswith(v+':') for v in ['directory','file','artifact','vydir']]):
      val_ = anchor_values[tag] if tag in anchor_values else val
      splitname = val_.split(':',1)
      arttyp = splitname[0]
      artname = splitname[-1]
      if len(splitname) == 2 and len(artname) > 0:
        if arttyp == 'vydir':
          artname = vytools.utils.get_vd_path(val_, items)
          if not artname:
            return False
        replace_obj[tag] = artname
        if build_level == -1 and '..' not in artname and eppath and os.path.exists(eppath):
          artifactpath = os.path.join(eppath, artname)
          if arttyp in ['artifact','file']:
            with open(artifactpath,'w') as w: w.write('')
            os.chmod(artifactpath, 0o666)
          elif arttyp == 'directory':
            os.makedirs(artifactpath,exist_ok=True)

  if build_level == -1:
    compose_file_name = label + '.yaml'
    compose_pth = item['path']
    composition = {}
    with open(compose_pth,'r') as r:
      composition = yaml.safe_load(r.read())
    if 'x-vy' in composition: del composition['x-vy']
    _recursiv_replace(composition, replace_obj, eppath)
    child_anchors.update(replace_obj)
    
    oktowrite = '..' not in compose_file_name and eppath and os.path.exists(eppath)
    if oktowrite:
      cfile = os.path.join(eppath, compose_file_name)
      if not bool(replace_obj):
        shutil.copyfile(compose_pth, cfile)
      else:
        with open(cfile,'w') as w:
          w.write(yaml.safe_dump(composition))
      cmd = cmd + ['-f',compose_file_name]

  return {
    'anchors':child_anchors,
    'command':cmd,
    'stage_versions':sorted(stage_versions),
    'dependencies':dependencies
  }

def _prefx(key,char,replkeys):
  return [r for r in replkeys if key.startswith(r+char)]

def stripkey(key):
  if key.startswith('$'):
    key = key[1:]
    if key.startswith('{'):
      key = ''.join(key[1:].split('}',1))
  return key

def _replkeysf(k, key, obj, repl, eppath):
  replkeys = [str(i) for i in len(repl)] if type(repl) == list else \
    (repl.keys() if type(repl) == dict else [])
  if key in replkeys:
    obj[k] = repl[key]
  else:
    if type(repl) == dict:
      for kkey in replkeys:
        if key.startswith(kkey+':'):
          obj[k] = key.replace(kkey,repl[kkey],1)
          return
    for x in ['.','>']:
      prefx = _prefx(key,x,replkeys)
      if len(prefx) == 1:
        repl_ = repl[prefx[0]]
        key_ = stripkey(key.replace(prefx[0]+x,'',1))
        if x == '.':
          _replkeysf(k, key_, obj, repl_, eppath)
        elif x == '>' and eppath and os.path.exists(eppath):
          with open(os.path.join(eppath, key_),'w') as w:
            if key.endswith('.json'):
              w.write(json.dumps(repl_))
            elif key.endswith('.yaml'):
              w.write(yaml.safe_dump(repl_))
          obj[k] = key_

def _recursiv_replace(obj, repl, eppath):
  if type(obj) == dict:
    ks = obj.keys()
  elif type(obj) == list:
    ks = range(len(obj))
  else:
    return
  for k in ks:
    key = obj[k]
    if type(key) == str and key.startswith('$'):
      key = stripkey(key)
      _replkeysf(k, key, obj, repl, eppath)
    elif type(key) in [list,dict]:
      _recursiv_replace(obj[k], repl, eppath)
      
def artifact_paths(compose_name, items, eppath):
  artifacts = {}
  def get_artifacts(i,artifacts):
    if i in items:
      for tag,val in items[i].get('anchors',{}).items():
        pth = os.path.join(eppath,val.replace('artifact:','',1))
        if val.startswith('artifact:') and '..' not in val and os.path.exists(pth):
          artifacts[tag] = pth
      for sa in items[i]['subcompose']: get_artifacts(sa['name'],artifacts)
  if eppath and os.path.exists(eppath):
    get_artifacts(compose_name,artifacts)
  return artifacts
