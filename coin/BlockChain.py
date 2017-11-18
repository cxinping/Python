
class BlockChain(object):
    def __init__(self):
        self.head = None   # 指向最新的一个区块
        self.blocks = {}   # 包含所有区块的一个字典

    '''
        添加区块函数
    '''
    def add_block(self, new_block):
        previous_hash = self.head.hash() if self.head else None
        new_block.previous_hash = previous_hash

        self.blocks[new_block.identifier] = {
            'block': new_block,
            'previous_hash': previous_hash,
            'previous': self.head,
        }
        self.head = new_block

    def __repr__(self):
        num_existing_blocks = len(self.blocks)
        return 'Blockchain<{} Blocks, Head: {}>'.format(
            num_existing_blocks,
            self.head.identifier if self.head else None
        )

# 初始化
#chain = BlockChain()

## 打印
#print( chain  )


from Block import Block
block = Block('Hello World')
# 添加区块
chain.add_block(block)
#
# 打印
print( chain  )


