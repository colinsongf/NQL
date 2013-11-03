
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = 'IsU\xe3\x95\x19\xcf\x7fkd>\x1a\xa0D9\x08'
    
_lr_action_items = {'TK_LESSOREQUAL':([41,42,43,45,],[-39,-37,53,-38,]),'TK_GREATHEROREQUAL':([41,42,43,45,],[-39,-37,54,-38,]),'TK_ORDERBY':([21,22,23,26,27,28,29,30,32,34,37,39,40,41,42,44,45,46,47,48,49,50,59,60,],[-27,-29,-30,-28,36,-14,-16,-18,-15,-17,-12,36,-24,-39,-37,-21,-38,-19,-23,-22,-20,-13,-26,-25,]),'TK_AVG':([8,24,38,],[12,12,12,]),'TK_LAST':([8,24,38,],[14,14,14,]),'TK_MAX':([8,24,38,],[15,15,15,]),'TK_MIN':([8,24,38,],[17,17,17,]),'TK_JOIN':([21,22,23,26,27,28,29,30,32,34,37,39,40,41,42,44,45,46,47,48,49,50,59,60,],[-27,-29,-30,-28,35,-14,-16,-18,-15,-17,-12,35,-24,-39,-37,-21,-38,-19,-23,-22,-20,-13,-26,-25,]),'TK_FIRST':([8,24,38,],[19,19,19,]),'TK_GREATHERTHAN':([41,42,43,45,],[-39,-37,56,-38,]),'TK_ID':([8,11,12,13,14,15,16,17,19,20,24,25,31,33,35,36,38,51,52,53,54,55,56,57,58,],[22,23,-41,-47,-46,-43,-40,-42,-45,-44,22,27,42,42,47,42,22,-34,-32,-35,-36,-31,-33,42,42,]),'TK_SELECT':([0,],[8,]),'$end':([0,1,2,3,4,5,6,7,9,10,21,22,23,26,27,28,29,30,32,34,37,39,40,41,42,44,45,46,47,48,49,50,59,60,],[-2,-4,-9,-11,-1,-5,0,-10,-3,-6,-27,-29,-30,-28,-8,-14,-16,-18,-15,-17,-12,-7,-24,-39,-37,-21,-38,-19,-23,-22,-20,-13,-26,-25,]),'TK_NOTEQUAL':([41,42,43,45,],[-39,-37,51,-38,]),'TK_LEN':([8,24,38,],[13,13,13,]),'TK_DELETE':([0,],[3,]),'TK_AND':([18,21,22,23,26,40,41,42,44,45,46,48,49,59,60,],[24,-27,-29,-30,-28,-24,-39,-37,58,-38,58,58,24,-26,-25,]),'TK_WHERE':([21,22,23,26,27,28,29,30,32,34,37,39,40,41,42,44,45,46,47,48,49,50,59,60,],[-27,-29,-30,-28,33,-14,-16,-18,-15,-17,-12,33,-24,-39,-37,-21,-38,-19,-23,-22,-20,-13,-26,-25,]),'TK_UPDATE':([0,],[7,]),'TK_FROM':([18,21,22,23,26,],[25,-27,-29,-30,-28,]),'TK_LESSTHAN':([41,42,43,45,],[-39,-37,52,-38,]),'TK_COUNT':([8,24,38,],[16,16,16,]),'TK_HAVING':([21,22,23,26,27,28,29,30,32,34,37,39,40,41,42,44,45,46,47,48,49,50,59,60,],[-27,-29,-30,-28,31,-14,-16,-18,-15,-17,-12,31,-24,-39,-37,-21,-38,-19,-23,-22,-20,-13,-26,-25,]),'TK_INSERT':([0,],[2,]),'TK_SUM':([8,24,38,],[20,20,20,]),'TK_EQUALEQUAL':([41,42,43,45,],[-39,-37,55,-38,]),'TK_FLOATNUMBER':([31,33,36,51,52,53,54,55,56,57,58,],[41,41,41,-34,-32,-35,-36,-31,-33,41,41,]),'TK_GROUPBY':([21,22,23,26,27,28,29,30,32,34,37,39,40,41,42,44,45,46,47,48,49,50,59,60,],[-27,-29,-30,-28,38,-14,-16,-18,-15,-17,-12,38,-24,-39,-37,-21,-38,-19,-23,-22,-20,-13,-26,-25,]),'TK_INTERGER':([31,33,36,51,52,53,54,55,56,57,58,],[45,45,45,-34,-32,-35,-36,-31,-33,45,45,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'function':([8,24,38,],[11,11,11,]),'insert':([0,],[1,]),'exp':([31,33,36,57,58,],[43,43,43,59,43,]),'claOrderby':([27,39,],[34,34,]),'claHaving':([27,39,],[29,29,]),'claJoin':([27,39,],[30,30,]),'clausesRec':([27,],[39,]),'columnsFuncListRec':([8,38,],[18,49,]),'dml':([0,],[4,]),'update':([0,],[5,]),'claGroupby':([27,39,],[32,32,]),'columnsFuncList':([8,24,38,],[21,26,21,]),'claWhere':([27,39,],[28,28,]),'condition':([43,],[57,]),'programa':([0,],[6,]),'conditionList':([31,33,36,58,],[40,40,40,60,]),'conditionListRec':([31,33,36,],[44,46,48,]),'clauses':([27,39,],[37,50,]),'select':([0,],[9,]),'delete':([0,],[10,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> dml','programa',1,'p_programa','/Users/Daniel/Documents/PUC/PF/projetoFinal/nql/nql_parser.py',14),
  ('programa -> <empty>','programa',0,'p_programa','/Users/Daniel/Documents/PUC/PF/projetoFinal/nql/nql_parser.py',15),
  ('dml -> select','dml',1,'p_dml','/Users/Daniel/Documents/PUC/PF/projetoFinal/nql/nql_parser.py',22),
  ('dml -> insert','dml',1,'p_dml','/Users/Daniel/Documents/PUC/PF/projetoFinal/nql/nql_parser.py',23),
  ('dml -> update','dml',1,'p_dml','/Users/Daniel/Documents/PUC/PF/projetoFinal/nql/nql_parser.py',24),
  ('dml -> delete','dml',1,'p_dml','/Users/Daniel/Documents/PUC/PF/projetoFinal/nql/nql_parser.py',25),
  ('select -> TK_SELECT columnsFuncListRec TK_FROM TK_ID clausesRec','select',5,'p_select','/Users/Daniel/Documents/PUC/PF/projetoFinal/nql/nql_parser.py',31),
  ('select -> TK_SELECT columnsFuncListRec TK_FROM TK_ID','select',4,'p_select','/Users/Daniel/Documents/PUC/PF/projetoFinal/nql/nql_parser.py',32),
  ('insert -> TK_INSERT','insert',1,'p_insert','/Users/Daniel/Documents/PUC/PF/projetoFinal/nql/nql_parser.py',40),
  ('update -> TK_UPDATE','update',1,'p_update','/Users/Daniel/Documents/PUC/PF/projetoFinal/nql/nql_parser.py',44),
  ('delete -> TK_DELETE','delete',1,'p_delete','/Users/Daniel/Documents/PUC/PF/projetoFinal/nql/nql_parser.py',48),
  ('clausesRec -> clauses','clausesRec',1,'p_clauses_rec','/Users/Daniel/Documents/PUC/PF/projetoFinal/nql/nql_parser.py',52),
  ('clausesRec -> clausesRec clauses','clausesRec',2,'p_clauses_rec','/Users/Daniel/Documents/PUC/PF/projetoFinal/nql/nql_parser.py',53),
  ('clauses -> claWhere','clauses',1,'p_clauses','/Users/Daniel/Documents/PUC/PF/projetoFinal/nql/nql_parser.py',61),
  ('clauses -> claGroupby','clauses',1,'p_clauses','/Users/Daniel/Documents/PUC/PF/projetoFinal/nql/nql_parser.py',62),
  ('clauses -> claHaving','clauses',1,'p_clauses','/Users/Daniel/Documents/PUC/PF/projetoFinal/nql/nql_parser.py',63),
  ('clauses -> claOrderby','clauses',1,'p_clauses','/Users/Daniel/Documents/PUC/PF/projetoFinal/nql/nql_parser.py',64),
  ('clauses -> claJoin','clauses',1,'p_clauses','/Users/Daniel/Documents/PUC/PF/projetoFinal/nql/nql_parser.py',65),
  ('claWhere -> TK_WHERE conditionListRec','claWhere',2,'p_clause_where','/Users/Daniel/Documents/PUC/PF/projetoFinal/nql/nql_parser.py',71),
  ('claGroupby -> TK_GROUPBY columnsFuncListRec','claGroupby',2,'p_clause_groupby','/Users/Daniel/Documents/PUC/PF/projetoFinal/nql/nql_parser.py',76),
  ('claHaving -> TK_HAVING conditionListRec','claHaving',2,'p_clause_having','/Users/Daniel/Documents/PUC/PF/projetoFinal/nql/nql_parser.py',81),
  ('claOrderby -> TK_ORDERBY conditionListRec','claOrderby',2,'p_clause_orderby','/Users/Daniel/Documents/PUC/PF/projetoFinal/nql/nql_parser.py',86),
  ('claJoin -> TK_JOIN TK_ID','claJoin',2,'p_cla_join','/Users/Daniel/Documents/PUC/PF/projetoFinal/nql/nql_parser.py',91),
  ('conditionListRec -> conditionList','conditionListRec',1,'p_condition_list_rec','/Users/Daniel/Documents/PUC/PF/projetoFinal/nql/nql_parser.py',96),
  ('conditionListRec -> conditionListRec TK_AND conditionList','conditionListRec',3,'p_condition_list_rec','/Users/Daniel/Documents/PUC/PF/projetoFinal/nql/nql_parser.py',97),
  ('conditionList -> exp condition exp','conditionList',3,'p_condition_list','/Users/Daniel/Documents/PUC/PF/projetoFinal/nql/nql_parser.py',105),
  ('columnsFuncListRec -> columnsFuncList','columnsFuncListRec',1,'p_columns_func_list_rec','/Users/Daniel/Documents/PUC/PF/projetoFinal/nql/nql_parser.py',110),
  ('columnsFuncListRec -> columnsFuncListRec TK_AND columnsFuncList','columnsFuncListRec',3,'p_columns_func_list_rec','/Users/Daniel/Documents/PUC/PF/projetoFinal/nql/nql_parser.py',111),
  ('columnsFuncList -> TK_ID','columnsFuncList',1,'p_columns_func_list','/Users/Daniel/Documents/PUC/PF/projetoFinal/nql/nql_parser.py',119),
  ('columnsFuncList -> function TK_ID','columnsFuncList',2,'p_columns_func_list','/Users/Daniel/Documents/PUC/PF/projetoFinal/nql/nql_parser.py',120),
  ('condition -> TK_EQUALEQUAL','condition',1,'p_condition_equalequal','/Users/Daniel/Documents/PUC/PF/projetoFinal/nql/nql_parser.py',128),
  ('condition -> TK_LESSTHAN','condition',1,'p_condition_lessthan','/Users/Daniel/Documents/PUC/PF/projetoFinal/nql/nql_parser.py',133),
  ('condition -> TK_GREATHERTHAN','condition',1,'p_condition_greatherthan','/Users/Daniel/Documents/PUC/PF/projetoFinal/nql/nql_parser.py',138),
  ('condition -> TK_NOTEQUAL','condition',1,'p_condition_notequal','/Users/Daniel/Documents/PUC/PF/projetoFinal/nql/nql_parser.py',143),
  ('condition -> TK_LESSOREQUAL','condition',1,'p_condition_lessorequal','/Users/Daniel/Documents/PUC/PF/projetoFinal/nql/nql_parser.py',148),
  ('condition -> TK_GREATHEROREQUAL','condition',1,'p_condition_greatherorequal','/Users/Daniel/Documents/PUC/PF/projetoFinal/nql/nql_parser.py',153),
  ('exp -> TK_ID','exp',1,'p_exp','/Users/Daniel/Documents/PUC/PF/projetoFinal/nql/nql_parser.py',158),
  ('exp -> TK_INTERGER','exp',1,'p_exp','/Users/Daniel/Documents/PUC/PF/projetoFinal/nql/nql_parser.py',159),
  ('exp -> TK_FLOATNUMBER','exp',1,'p_exp','/Users/Daniel/Documents/PUC/PF/projetoFinal/nql/nql_parser.py',160),
  ('function -> TK_COUNT','function',1,'p_function_count','/Users/Daniel/Documents/PUC/PF/projetoFinal/nql/nql_parser.py',172),
  ('function -> TK_AVG','function',1,'p_function_avg','/Users/Daniel/Documents/PUC/PF/projetoFinal/nql/nql_parser.py',177),
  ('function -> TK_MIN','function',1,'p_function_min','/Users/Daniel/Documents/PUC/PF/projetoFinal/nql/nql_parser.py',182),
  ('function -> TK_MAX','function',1,'p_function_max','/Users/Daniel/Documents/PUC/PF/projetoFinal/nql/nql_parser.py',187),
  ('function -> TK_SUM','function',1,'p_function_sum','/Users/Daniel/Documents/PUC/PF/projetoFinal/nql/nql_parser.py',192),
  ('function -> TK_FIRST','function',1,'p_function_first','/Users/Daniel/Documents/PUC/PF/projetoFinal/nql/nql_parser.py',197),
  ('function -> TK_LAST','function',1,'p_function_last','/Users/Daniel/Documents/PUC/PF/projetoFinal/nql/nql_parser.py',202),
  ('function -> TK_LEN','function',1,'p_function_len','/Users/Daniel/Documents/PUC/PF/projetoFinal/nql/nql_parser.py',207),
]
