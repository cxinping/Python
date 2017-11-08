from pymining import itemmining

# Frequent Item Set Mining 频繁集
transactions = (('豆奶', '莴笋'), 
                ('莴笋', '尿布' , '葡萄酒', '甜菜'), 
                ('豆奶' , '尿布' , '葡萄酒' , '甜菜' ), 
                ('莴笋', '豆奶', '尿布','葡萄酒'),
                ('莴笋', '豆奶', '尿布' , '橙汁')    )

relim_input = itemmining.get_relim_input(transactions)
report = itemmining.relim(relim_input, min_support=2)

#print( report )

for k,v in enumerate(report):
    print('k=>',v,'v=', report[v])

# Association Rules Mining 关联规则
from pymining import itemmining, assocrules, perftesting
relim_input = itemmining.get_relim_input(transactions)
item_sets = itemmining.relim(relim_input, min_support=2)
rules = assocrules.mine_assoc_rules(item_sets, min_support=2, min_confidence=0.6)
print('--------------\n Association Rules Mining  关联规则'  )
#print( rules )

for i in rules:
    print(i)




