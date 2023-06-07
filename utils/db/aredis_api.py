import asyncio

from aredis import ConnectionPool, StrictRedis

from utils.singleton import Singleton
import db_conf


class RedisPool(ConnectionPool, metaclass=Singleton):
    pass


pool = RedisPool(host=db_conf.REDISHOST, port=db_conf.REDISPORT, password=db_conf.REDISPASSWORD, db=db_conf.REDISDB)

aredis_client = StrictRedis(connection_pool=pool)  # 支持集群


async def test():
    await aredis_client.set('foo', 'bar')
    print(await aredis_client.get('foo'))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test())
