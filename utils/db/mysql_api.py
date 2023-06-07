import asyncio
from logging import getLogger

import aiomysql

import db_conf
from utils import add_logger_handler

logger = getLogger(__name__)
add_logger_handler(logger, __name__)


class AIOMySQL:
    """docstring for Pmydql."""
    __connection = None

    def __init__(self, ):
        self.conn = None
        self.cursor = None

    @staticmethod
    async def getconnection():
        if not AIOMySQL.__connection:
            conn = await aiomysql.create_pool(host=db_conf.MYSQLHOST_MAGE,
                                              port=db_conf.MYSQLPORT_MAGE,
                                              user=db_conf.MYSQLUSER_MAGE, password=db_conf.MYSQLPASSWORD_MAGE,
                                              db=db_conf.MYSQLDATABASE_MAGE)
            if conn:
                AIOMySQL.__connection = conn
                logger.info('connect to mysql correct!')
                return conn
            else:
                raise ("connect to mysql error ")
        else:
            return AIOMySQL.__connection
