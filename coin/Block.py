import hashlib
import uuid


class Block(object):
    def __init__(self, data=None, previous_hash=None):
        self.identifier = uuid.uuid4().hex   # 产生唯一标示
        self.nonce = None                    # nonce值
        self.data = data                     # 区块内容
        self.previous_hash = previous_hash   # 父节点哈希值
        
    def hash(self, nonce=None):
        '''
        计算区块的哈希值
        '''
        message = hashlib.sha256()
        message.update(self.identifier.encode('utf-8'))
        message.update(str(nonce).encode('utf-8'))
        message.update(str(self.data).encode('utf-8'))
        message.update(str(self.previous_hash).encode('utf-8'))

        return message.hexdigest()

    def hash_is_valid(self, the_hash):
        '''
        校验区块哈希值有否有效
        '''
        return the_hash.startswith('0000')

    def __repr__(self):
        return 'Block<Hash: {}, Nonce: {}>'.format(self.hash(), self.nonce)