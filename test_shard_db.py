import unittest
from shard_db import ShardedDatabase

class TestShardedDatabase(unittest.TestCase):
    def test_add_and_get(self):
        db = ShardedDatabase(4)
        db.add('key1', 'value1')
        db.add('key2', 'value2')
        db.add('key3', 'value3')
        
        self.assertEqual(db.get('key1'), 'value1')
        self.assertEqual(db.get('key2'), 'value2')
        self.assertEqual(db.get('key3'), 'value3')
        self.assertIsNone(db.get('key4'))
    
    def test_sharding(self):
        db = ShardedDatabase(4)
        db.add('key1', 'value1')
        db.add('key2', 'value2')
        db.add('key3', 'value3')
        db.add('key4', 'value4')
        db.add('key5', 'value5')
        
        self.assertEqual(len(db.shards[0]), 1)
        self.assertEqual(len(db.shards[1]), 1)
        self.assertEqual(len(db.shards[2]), 2)
        self.assertEqual(len(db.shards[3]), 1)
        
    def test_overwrite(self):
        db = ShardedDatabase(4)
        db.add('key1', 'value1')
        db.add('key1', 'value2')
        
        self.assertEqual(db.get('key1'), 'value2')
        
if __name__ == '__main__':
    unittest.main()