from pymining import itemmining

# Frequent Item Set Mining
transactions = (('a', 'b'), 
                ('b', 'c' , 'd', 'f'), 
                ('a' , 'c' , 'd' , 'e' ), 
                ('b', 'a', 'c','d'),
                ('b', 'a', 'c' , 'e')    )
#relim_input = itemmining.get_relim_input(transactions)
#report = itemmining.relim(relim_input, min_support=2)

#print( report )

#for k,v in enumerate(report):
#    print('k=>',v,'v=', report[v])

# Frequent Sequence Mining
#from pymining import seqmining
#seqs = ( 'ab', 'bcdf', 'acde', 'bacd' , 'bace')
#freq_seqs = seqmining.freq_seq_enum(seqs, 2)
#sorted(freq_seqs)

#print( freq_seqs)
 
# Association Rules Mining
from pymining import itemmining, assocrules, perftesting
#transactions = perftesting.get_default_transactions()
relim_input = itemmining.get_relim_input(transactions)
item_sets = itemmining.relim(relim_input, min_support=2)
rules = assocrules.mine_assoc_rules(item_sets, min_support=2, min_confidence=0.5)
print('--------------\n Association Rules Mining'  )
print( rules )

for i in rules:
    print(i)