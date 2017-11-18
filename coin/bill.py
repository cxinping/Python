from Block import Block
from BlockChain import BlockChain

from datetime import datetime

# 定义收支记录
class AccountBill(Block):
    
    def __init__(self, content, amount):
        t = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        data = "{}|{}|{}".format(t, content, amount)
        return super(AccountBill, self).__init__(data)
    
    '''
        获取金额数量
    '''
    def get_amount(self):
        amount = 0
        if self.data:
            amount = int(self.data.split('|')[2])
        return amount
    
    def get_content(self):
        content = ''
        if self.data:
            content = self.data.split('|')[1]
        return content

    def __repr__(self):
        return 'Bill: {}>'.format(
            self.data
        )
        

# 创建记录
#bill = AccountBill('测试', 100)
#print( bill )

from collections import OrderedDict

class AccountBook(BlockChain):
    
    def __init__(self):
        self.head = None   # 指向最新的一个区块
        self.blocks = OrderedDict()   # 包含所有区块的一个字典

    '''
        添加记录
    '''
    def add_block(self, new_bill):
        new_bill.mine()
        super(AccountBook, self).add_block(new_bill)
        
    '''
        计算当前余额
    '''
    def balance(self):
        balance = 0
        if self.blocks:
            for k, v in self.blocks.items():
                balance += v['block'].get_amount()
        return balance

    
    def __repr__(self):
        num_existing_blocks = len(self.blocks)
        return 'AccountBook<{} Bills, Head: {}>'.format(
            num_existing_blocks,
            self.head.identifier if self.head else None
        )
        
        
# 创建几笔记录

book = AccountBook()

b1 = AccountBill('工资', 10000)
book.add_block(b1)

b2 = AccountBill('房租', -2500)
book.add_block(b2)

b3 = AccountBill('衣服', -1500)
book.add_block(b3)

b4 = AccountBill('吃饭', -1000)
book.add_block(b4)

b5 = AccountBill('股票收入', 200)
book.add_block(b5)

b6 = AccountBill('看电影', -200)
book.add_block(b6)

b7 = AccountBill('购物', -1000)
book.add_block(b7)

b8 = AccountBill('水电费等', -100)
book.add_block(b8)

# 计算当前余额
print( '当前余额=', book.balance() )

# 打印收支记录

for k,v in book.blocks.items():
    print(v['block'].data)
    
    

import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签


# 初始化数据
x_data = []  # 金额
y_data = []  # 描述
colors = []  # 颜色

for k,v in book.blocks.items():
    bill = v['block']
    y_data.append(bill.get_content())
    amount = bill.get_amount()
    if amount > 0:
        x_data.append(amount)
        colors.append('blue')
    else:
        x_data.append(-amount)
        colors.append('red')

        
y_pos = np.arange(len(y_data))
 
plt.bar(y_pos, x_data, align='center', alpha=0.5, color=colors)
plt.xticks(y_pos, y_data)
plt.ylabel('金额')
plt.title('收支记录')
 
plt.show()


# 简单分析支出组成
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签

labels = []
amounts = []
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue'] # 用不同颜色显示
 
for k,v in book.blocks.items():
    bill = v['block']  
    amount = bill.get_amount()
    
    # 只展示支出
    if amount < 0:
        labels.append(bill.get_content())
        amounts.append(-amount)
        
plt.axes(aspect=1)
plt.pie(amounts, labels=labels, colors=colors, shadow=True, autopct='%1.1f%%')

plt.show()
    