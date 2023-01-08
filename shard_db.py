class ShardedDatabase:
    def my_hash(self, key):
        """Простейшая хэш функция"""
        res = 0
        for i in key:
            res += ord(i)
        return res    

    def __init__(self, num_shards):
        self.num_shards = num_shards
        self.shards = [{} for _ in range(num_shards)]
    
    def _get_shard(self, key):
        """"Определяем в какой шард записать используя хэш по модулю num_shards"""
        return self.shards[self.my_hash(key) % self.num_shards]
    
    def add(self, key, value):
        """Добавляем данные в базу"""
        shard = self._get_shard(key)
        shard[key] = value
    
    def get(self, key):
        """Получаем данные из шарда"""
        shard = self._get_shard(key)
        return shard.get(key)
