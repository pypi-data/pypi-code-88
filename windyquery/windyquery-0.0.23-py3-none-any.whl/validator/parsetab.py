
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'conflictactionleftMINUSleftCOMMArightEQrightNOTleftINleftISleftLIKEleftILIKEleftLEleftLSleftGEleftGTleftNEleftNNleftDPIPEleftDISTINCTleftFROMleftPLUSleftMULTIleftDIVIDEleftMODULARARROW COMMA DARROW DISTINCT DIVIDE DO DOT DPIPE EQ FALSE FROM GE GT HOLDER ILIKE IN IS LE LIKE LPAREN LS MINUS MODULAR MULTI NAME NE NN NOT NOTHING NULL NUMBER PLUS QUOTED_NAME RPAREN SET STAR TEXTVAL TRUE UPDATEempty :conflictaction : DO NOTHINGexpr : expr EQ expr\n                   | expr NE expr\n                   | expr NN expr\n                   | expr LE expr\n                   | expr LS expr\n                   | expr GE expr\n                   | expr GT expr\n                   | expr IS expr\n                   | expr LIKE expr\n                   | expr ILIKE expr\n                   | expr DPIPE expr\n                   | expr MINUS expr\n                   | expr PLUS expr\n                   | expr MULTI expr\n                   | expr DIVIDE expr\n                   | expr MODULAR exprupdates : updateconflictaction : DO UPDATE SET updatesfullname : unitname dotnameupdates : updates COMMA updatefullname_json : fullname attributefield : STAR\n                    | NUMBER\n                    | TEXTVAL\n                    | NULL\n                    | TRUE\n                    | FALSEunitname : NAMEupdate : field EQ exprattribute : ARROW NAME attributeunitname : QUOTED_NAMEfield : HOLDERdotname : DOT unitname dotnameexpr : expr IS NOT exprfield : fullname_jsondotname : DOT STARexpr : expr IS DISTINCT FROM exprattribute : ARROW NUMBER attributedotname : emptyexpr : expr IS NOT DISTINCT FROM exprexpr : expr IN LPAREN exprs RPARENexpr : expr NOT IN LPAREN exprs RPARENattribute : ARROW MINUS NUMBER attributeexprs : exprexprs : exprs COMMA exprattribute : DARROW NAMEexpr : fieldattribute : DARROW NUMBERattribute : DARROW MINUS NUMBERattribute : empty'
    
_lr_action_items = {'DO':([0,],[2,]),'$end':([1,3,6,7,9,10,11,12,13,14,15,16,17,18,19,20,23,26,27,29,30,31,32,33,34,36,37,39,40,59,60,61,62,63,64,65,66,67,68,69,70,71,74,75,76,77,78,79,80,81,84,85,92,94,96,97,],[0,-2,-20,-19,-24,-25,-26,-27,-28,-29,-34,-37,-1,-1,-30,-33,-23,-52,-21,-41,-22,-49,-31,-1,-1,-48,-50,-1,-38,-32,-40,-1,-51,-35,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-45,-36,-39,-43,-42,-44,]),'NOTHING':([2,],[3,]),'UPDATE':([2,],[4,]),'SET':([4,],[5,]),'STAR':([5,21,22,28,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,72,83,87,88,91,95,],[9,9,9,40,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'NUMBER':([5,21,22,24,25,35,38,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,72,83,87,88,91,95,],[10,10,10,34,37,61,62,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'TEXTVAL':([5,21,22,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,72,83,87,88,91,95,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'NULL':([5,21,22,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,72,83,87,88,91,95,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'TRUE':([5,21,22,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,72,83,87,88,91,95,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'FALSE':([5,21,22,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,72,83,87,88,91,95,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'HOLDER':([5,21,22,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,72,83,87,88,91,95,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'NAME':([5,21,22,24,25,28,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,72,83,87,88,91,95,],[19,19,19,33,36,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'QUOTED_NAME':([5,21,22,28,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,72,83,87,88,91,95,],[20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'COMMA':([6,7,9,10,11,12,13,14,15,16,17,18,19,20,23,26,27,29,30,31,32,33,34,36,37,39,40,59,60,61,62,63,64,65,66,67,68,69,70,71,74,75,76,77,78,79,80,81,84,85,89,90,92,93,94,96,97,98,],[21,-19,-24,-25,-26,-27,-28,-29,-34,-37,-1,-1,-30,-33,-23,-52,-21,-41,-22,-49,-31,-1,-1,-48,-50,-1,-38,-32,-40,-1,-51,-35,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-45,-36,-46,95,-39,95,-43,-42,-44,-47,]),'EQ':([8,9,10,11,12,13,14,15,16,17,18,19,20,23,26,27,29,31,32,33,34,36,37,39,40,59,60,61,62,63,64,65,66,67,68,69,70,71,74,75,76,77,78,79,80,81,84,85,89,92,94,96,97,98,],[22,-24,-25,-26,-27,-28,-29,-34,-37,-1,-1,-30,-33,-23,-52,-21,-41,-49,41,-1,-1,-48,-50,-1,-38,-32,-40,-1,-51,-35,41,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,41,-15,-16,-17,-18,-45,-36,41,-39,-43,-42,-44,41,]),'NE':([9,10,11,12,13,14,15,16,17,18,19,20,23,26,27,29,31,32,33,34,36,37,39,40,59,60,61,62,63,64,65,66,67,68,69,70,71,74,75,76,77,78,79,80,81,84,85,89,92,94,96,97,98,],[-24,-25,-26,-27,-28,-29,-34,-37,-1,-1,-30,-33,-23,-52,-21,-41,-49,42,-1,-1,-48,-50,-1,-38,-32,-40,-1,-51,-35,42,-4,-5,42,42,42,42,42,42,42,-13,42,-15,-16,-17,-18,-45,42,42,-39,-43,-42,-44,42,]),'NN':([9,10,11,12,13,14,15,16,17,18,19,20,23,26,27,29,31,32,33,34,36,37,39,40,59,60,61,62,63,64,65,66,67,68,69,70,71,74,75,76,77,78,79,80,81,84,85,89,92,94,96,97,98,],[-24,-25,-26,-27,-28,-29,-34,-37,-1,-1,-30,-33,-23,-52,-21,-41,-49,43,-1,-1,-48,-50,-1,-38,-32,-40,-1,-51,-35,43,43,-5,43,43,43,43,43,43,43,-13,43,-15,-16,-17,-18,-45,43,43,-39,-43,-42,-44,43,]),'LE':([9,10,11,12,13,14,15,16,17,18,19,20,23,26,27,29,31,32,33,34,36,37,39,40,59,60,61,62,63,64,65,66,67,68,69,70,71,74,75,76,77,78,79,80,81,84,85,89,92,94,96,97,98,],[-24,-25,-26,-27,-28,-29,-34,-37,-1,-1,-30,-33,-23,-52,-21,-41,-49,44,-1,-1,-48,-50,-1,-38,-32,-40,-1,-51,-35,44,-4,-5,-6,-7,-8,-9,44,44,44,-13,44,-15,-16,-17,-18,-45,44,44,-39,-43,-42,-44,44,]),'LS':([9,10,11,12,13,14,15,16,17,18,19,20,23,26,27,29,31,32,33,34,36,37,39,40,59,60,61,62,63,64,65,66,67,68,69,70,71,74,75,76,77,78,79,80,81,84,85,89,92,94,96,97,98,],[-24,-25,-26,-27,-28,-29,-34,-37,-1,-1,-30,-33,-23,-52,-21,-41,-49,45,-1,-1,-48,-50,-1,-38,-32,-40,-1,-51,-35,45,-4,-5,45,-7,-8,-9,45,45,45,-13,45,-15,-16,-17,-18,-45,45,45,-39,-43,-42,-44,45,]),'GE':([9,10,11,12,13,14,15,16,17,18,19,20,23,26,27,29,31,32,33,34,36,37,39,40,59,60,61,62,63,64,65,66,67,68,69,70,71,74,75,76,77,78,79,80,81,84,85,89,92,94,96,97,98,],[-24,-25,-26,-27,-28,-29,-34,-37,-1,-1,-30,-33,-23,-52,-21,-41,-49,46,-1,-1,-48,-50,-1,-38,-32,-40,-1,-51,-35,46,-4,-5,46,46,-8,-9,46,46,46,-13,46,-15,-16,-17,-18,-45,46,46,-39,-43,-42,-44,46,]),'GT':([9,10,11,12,13,14,15,16,17,18,19,20,23,26,27,29,31,32,33,34,36,37,39,40,59,60,61,62,63,64,65,66,67,68,69,70,71,74,75,76,77,78,79,80,81,84,85,89,92,94,96,97,98,],[-24,-25,-26,-27,-28,-29,-34,-37,-1,-1,-30,-33,-23,-52,-21,-41,-49,47,-1,-1,-48,-50,-1,-38,-32,-40,-1,-51,-35,47,-4,-5,47,47,47,-9,47,47,47,-13,47,-15,-16,-17,-18,-45,47,47,-39,-43,-42,-44,47,]),'IS':([9,10,11,12,13,14,15,16,17,18,19,20,23,26,27,29,31,32,33,34,36,37,39,40,59,60,61,62,63,64,65,66,67,68,69,70,71,74,75,76,77,78,79,80,81,84,85,89,92,94,96,97,98,],[-24,-25,-26,-27,-28,-29,-34,-37,-1,-1,-30,-33,-23,-52,-21,-41,-49,48,-1,-1,-48,-50,-1,-38,-32,-40,-1,-51,-35,48,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,48,-15,-16,-17,-18,-45,48,48,-39,-43,-42,-44,48,]),'LIKE':([9,10,11,12,13,14,15,16,17,18,19,20,23,26,27,29,31,32,33,34,36,37,39,40,59,60,61,62,63,64,65,66,67,68,69,70,71,74,75,76,77,78,79,80,81,84,85,89,92,94,96,97,98,],[-24,-25,-26,-27,-28,-29,-34,-37,-1,-1,-30,-33,-23,-52,-21,-41,-49,49,-1,-1,-48,-50,-1,-38,-32,-40,-1,-51,-35,49,-4,-5,-6,-7,-8,-9,49,-11,-12,-13,49,-15,-16,-17,-18,-45,49,49,-39,-43,-42,-44,49,]),'ILIKE':([9,10,11,12,13,14,15,16,17,18,19,20,23,26,27,29,31,32,33,34,36,37,39,40,59,60,61,62,63,64,65,66,67,68,69,70,71,74,75,76,77,78,79,80,81,84,85,89,92,94,96,97,98,],[-24,-25,-26,-27,-28,-29,-34,-37,-1,-1,-30,-33,-23,-52,-21,-41,-49,50,-1,-1,-48,-50,-1,-38,-32,-40,-1,-51,-35,50,-4,-5,-6,-7,-8,-9,50,50,-12,-13,50,-15,-16,-17,-18,-45,50,50,-39,-43,-42,-44,50,]),'DPIPE':([9,10,11,12,13,14,15,16,17,18,19,20,23,26,27,29,31,32,33,34,36,37,39,40,59,60,61,62,63,64,65,66,67,68,69,70,71,74,75,76,77,78,79,80,81,84,85,89,92,94,96,97,98,],[-24,-25,-26,-27,-28,-29,-34,-37,-1,-1,-30,-33,-23,-52,-21,-41,-49,51,-1,-1,-48,-50,-1,-38,-32,-40,-1,-51,-35,51,51,51,51,51,51,51,51,51,51,-13,51,-15,-16,-17,-18,-45,51,51,-39,-43,-42,-44,51,]),'MINUS':([9,10,11,12,13,14,15,16,17,18,19,20,23,24,25,26,27,29,31,32,33,34,36,37,39,40,59,60,61,62,63,64,65,66,67,68,69,70,71,74,75,76,77,78,79,80,81,84,85,89,92,94,96,97,98,],[-24,-25,-26,-27,-28,-29,-34,-37,-1,-1,-30,-33,-23,35,38,-52,-21,-41,-49,52,-1,-1,-48,-50,-1,-38,-32,-40,-1,-51,-35,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-45,-36,52,-39,-43,-42,-44,52,]),'PLUS':([9,10,11,12,13,14,15,16,17,18,19,20,23,26,27,29,31,32,33,34,36,37,39,40,59,60,61,62,63,64,65,66,67,68,69,70,71,74,75,76,77,78,79,80,81,84,85,89,92,94,96,97,98,],[-24,-25,-26,-27,-28,-29,-34,-37,-1,-1,-30,-33,-23,-52,-21,-41,-49,53,-1,-1,-48,-50,-1,-38,-32,-40,-1,-51,-35,53,53,53,53,53,53,53,53,53,53,53,53,-15,-16,-17,-18,-45,53,53,53,-43,53,-44,53,]),'MULTI':([9,10,11,12,13,14,15,16,17,18,19,20,23,26,27,29,31,32,33,34,36,37,39,40,59,60,61,62,63,64,65,66,67,68,69,70,71,74,75,76,77,78,79,80,81,84,85,89,92,94,96,97,98,],[-24,-25,-26,-27,-28,-29,-34,-37,-1,-1,-30,-33,-23,-52,-21,-41,-49,54,-1,-1,-48,-50,-1,-38,-32,-40,-1,-51,-35,54,54,54,54,54,54,54,54,54,54,54,54,54,-16,-17,-18,-45,54,54,54,-43,54,-44,54,]),'DIVIDE':([9,10,11,12,13,14,15,16,17,18,19,20,23,26,27,29,31,32,33,34,36,37,39,40,59,60,61,62,63,64,65,66,67,68,69,70,71,74,75,76,77,78,79,80,81,84,85,89,92,94,96,97,98,],[-24,-25,-26,-27,-28,-29,-34,-37,-1,-1,-30,-33,-23,-52,-21,-41,-49,55,-1,-1,-48,-50,-1,-38,-32,-40,-1,-51,-35,55,55,55,55,55,55,55,55,55,55,55,55,55,55,-17,-18,-45,55,55,55,-43,55,-44,55,]),'MODULAR':([9,10,11,12,13,14,15,16,17,18,19,20,23,26,27,29,31,32,33,34,36,37,39,40,59,60,61,62,63,64,65,66,67,68,69,70,71,74,75,76,77,78,79,80,81,84,85,89,92,94,96,97,98,],[-24,-25,-26,-27,-28,-29,-34,-37,-1,-1,-30,-33,-23,-52,-21,-41,-49,56,-1,-1,-48,-50,-1,-38,-32,-40,-1,-51,-35,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,-18,-45,56,56,56,-43,56,-44,56,]),'IN':([9,10,11,12,13,14,15,16,17,18,19,20,23,26,27,29,31,32,33,34,36,37,39,40,57,59,60,61,62,63,64,65,66,67,68,69,70,71,74,75,76,77,78,79,80,81,84,85,89,92,94,96,97,98,],[-24,-25,-26,-27,-28,-29,-34,-37,-1,-1,-30,-33,-23,-52,-21,-41,-49,58,-1,-1,-48,-50,-1,-38,82,-32,-40,-1,-51,-35,58,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,58,-15,-16,-17,-18,-45,58,58,-39,-43,-42,-44,58,]),'NOT':([9,10,11,12,13,14,15,16,17,18,19,20,23,26,27,29,31,32,33,34,36,37,39,40,48,59,60,61,62,63,64,65,66,67,68,69,70,71,74,75,76,77,78,79,80,81,84,85,89,92,94,96,97,98,],[-24,-25,-26,-27,-28,-29,-34,-37,-1,-1,-30,-33,-23,-52,-21,-41,-49,57,-1,-1,-48,-50,-1,-38,72,-32,-40,-1,-51,-35,57,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,57,-15,-16,-17,-18,-45,57,57,-39,-43,-42,-44,57,]),'RPAREN':([9,10,11,12,13,14,15,16,17,18,19,20,23,26,27,29,31,33,34,36,37,39,40,59,60,61,62,63,64,65,66,67,68,69,70,71,74,75,76,77,78,79,80,81,84,85,89,90,92,93,94,96,97,98,],[-24,-25,-26,-27,-28,-29,-34,-37,-1,-1,-30,-33,-23,-52,-21,-41,-49,-1,-1,-48,-50,-1,-38,-32,-40,-1,-51,-35,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-45,-36,-46,94,-39,97,-43,-42,-44,-47,]),'ARROW':([17,18,19,20,27,29,33,34,39,40,61,63,],[24,-1,-30,-33,-21,-41,24,24,-1,-38,24,-35,]),'DARROW':([17,18,19,20,27,29,33,34,39,40,61,63,],[25,-1,-30,-33,-21,-41,25,25,-1,-38,25,-35,]),'DOT':([18,19,20,39,],[28,-30,-33,28,]),'DISTINCT':([48,72,],[73,86,]),'LPAREN':([58,82,],[83,88,]),'FROM':([73,86,],[87,91,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'conflictaction':([0,],[1,]),'updates':([5,],[6,]),'update':([5,21,],[7,30,]),'field':([5,21,22,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,72,83,87,88,91,95,],[8,8,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'fullname_json':([5,21,22,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,72,83,87,88,91,95,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'fullname':([5,21,22,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,72,83,87,88,91,95,],[17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'unitname':([5,21,22,28,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,72,83,87,88,91,95,],[18,18,18,39,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'attribute':([17,33,34,61,],[23,59,60,84,]),'empty':([17,18,33,34,39,61,],[26,29,26,26,29,26,]),'dotname':([18,39,],[27,63,]),'expr':([22,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,72,83,87,88,91,95,],[32,64,65,66,67,68,69,70,71,74,75,76,77,78,79,80,81,85,89,92,89,96,98,]),'exprs':([83,88,],[90,93,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> conflictaction","S'",1,None,None,None),
  ('empty -> <empty>','empty',0,'p_empty','empty.py',9),
  ('conflictaction -> DO NOTHING','conflictaction',2,'p_conflictaction_do_nothing','conflict_action.py',14),
  ('expr -> expr EQ expr','expr',3,'p_expr','expr.py',15),
  ('expr -> expr NE expr','expr',3,'p_expr','expr.py',16),
  ('expr -> expr NN expr','expr',3,'p_expr','expr.py',17),
  ('expr -> expr LE expr','expr',3,'p_expr','expr.py',18),
  ('expr -> expr LS expr','expr',3,'p_expr','expr.py',19),
  ('expr -> expr GE expr','expr',3,'p_expr','expr.py',20),
  ('expr -> expr GT expr','expr',3,'p_expr','expr.py',21),
  ('expr -> expr IS expr','expr',3,'p_expr','expr.py',22),
  ('expr -> expr LIKE expr','expr',3,'p_expr','expr.py',23),
  ('expr -> expr ILIKE expr','expr',3,'p_expr','expr.py',24),
  ('expr -> expr DPIPE expr','expr',3,'p_expr','expr.py',25),
  ('expr -> expr MINUS expr','expr',3,'p_expr','expr.py',26),
  ('expr -> expr PLUS expr','expr',3,'p_expr','expr.py',27),
  ('expr -> expr MULTI expr','expr',3,'p_expr','expr.py',28),
  ('expr -> expr DIVIDE expr','expr',3,'p_expr','expr.py',29),
  ('expr -> expr MODULAR expr','expr',3,'p_expr','expr.py',30),
  ('updates -> update','updates',1,'p_updates_update','update.py',17),
  ('conflictaction -> DO UPDATE SET updates','conflictaction',4,'p_conflictaction_do_update','conflict_action.py',18),
  ('fullname -> unitname dotname','fullname',2,'p_fullname','fullname.py',21),
  ('updates -> updates COMMA update','updates',3,'p_updates_comma_update','update.py',21),
  ('fullname_json -> fullname attribute','fullname_json',2,'p_fullname_json','fullname_json.py',22),
  ('field -> STAR','field',1,'p_field_items','field.py',23),
  ('field -> NUMBER','field',1,'p_field_items','field.py',24),
  ('field -> TEXTVAL','field',1,'p_field_items','field.py',25),
  ('field -> NULL','field',1,'p_field_items','field.py',26),
  ('field -> TRUE','field',1,'p_field_items','field.py',27),
  ('field -> FALSE','field',1,'p_field_items','field.py',28),
  ('unitname -> NAME','unitname',1,'p_unitname_name','fullname.py',25),
  ('update -> field EQ expr','update',3,'p_update','update.py',25),
  ('attribute -> ARROW NAME attribute','attribute',3,'p_attribute','fullname_json.py',27),
  ('unitname -> QUOTED_NAME','unitname',1,'p_unitname_quoted_name','fullname.py',29),
  ('field -> HOLDER','field',1,'p_field_param','field.py',32),
  ('dotname -> DOT unitname dotname','dotname',3,'p_dotname_dot','fullname.py',33),
  ('expr -> expr IS NOT expr','expr',4,'p_expr2','expr.py',34),
  ('field -> fullname_json','field',1,'p_field_name','field.py',36),
  ('dotname -> DOT STAR','dotname',2,'p_dotname_star','fullname.py',37),
  ('expr -> expr IS DISTINCT FROM expr','expr',5,'p_expr3','expr.py',38),
  ('attribute -> ARROW NUMBER attribute','attribute',3,'p_attribute_num','fullname_json.py',39),
  ('dotname -> empty','dotname',1,'p_dotname_empty','fullname.py',41),
  ('expr -> expr IS NOT DISTINCT FROM expr','expr',6,'p_expr4','expr.py',42),
  ('expr -> expr IN LPAREN exprs RPAREN','expr',5,'p_expr5','expr.py',46),
  ('expr -> expr NOT IN LPAREN exprs RPAREN','expr',6,'p_expr6','expr.py',50),
  ('attribute -> ARROW MINUS NUMBER attribute','attribute',4,'p_attribute_minus_num','fullname_json.py',50),
  ('exprs -> expr','exprs',1,'p_exprs_expr','expr.py',54),
  ('exprs -> exprs COMMA expr','exprs',3,'p_exprs_comma_expr','expr.py',58),
  ('attribute -> DARROW NAME','attribute',2,'p_attribute_darrow','fullname_json.py',61),
  ('expr -> field','expr',1,'p_expr_field','expr.py',62),
  ('attribute -> DARROW NUMBER','attribute',2,'p_attribute_darrow_num','fullname_json.py',67),
  ('attribute -> DARROW MINUS NUMBER','attribute',3,'p_attribute_darrow_minus_num','fullname_json.py',72),
  ('attribute -> empty','attribute',1,'p_attribute_empty','fullname_json.py',77),
]
