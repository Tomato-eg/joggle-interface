import mysql.connector
from mysql.connector import Error
from src.common.log_utils import LogUtils
from src.common.path_utils import PathUtils

# 日志打印
logger = LogUtils.get_log()
# 根目录
base_path = PathUtils().get_project_path()


class DatabaseManager:

    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()
            logger.info("Connected to MySQL database")
        except Error as e:
            logger.info(f"Error while connecting to MySQL: {e}")
            self.connection = None
            self.cursor = None

    def inspect_connection(self):
        if not self.connection or not self.cursor:
            raise Exception("Database connection not established")

    # 查询
    def execute_query(self, query, params):

        self.inspect_connection()

        try:
            if params is None:
                self.cursor.execute(query)
            else:
                self.cursor.execute(query, params)
            self.connection.commit()
            logger.info("Query executed successfully")
        except Error as e:
            logger.info(f"Error while executing query: {e}")

    # 增加
    def execute_insert(self, table, columns, values):

        self.inspect_connection()

        # 构建SQL插入语句
        query = f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({', '.join(['%s'] * len(values))})"

        try:
            # 执行插入操作
            self.cursor.execute(query, values)
            # 提交事务
            self.connection.commit()
            logger.info(f"Data inserted successfully into {table}")
        except Error as e:
            logger.info(f"Error while inserting into {table}: {e}")
            # 发生错误时回滚事务
            self.connection.rollback()

    def execute_delete(self, table, columns, values):

        self.inspect_connection()

        delete = f"DELETE FROM {table} WHERE {columns} = %s"

        try:
            self.cursor.execute(delete, (values,))
            self.connection.commit()
            logger.info(f"Data deleted successfully into {table}")
        except Error as e:
            logger.error(f"Error while delete into {table}: {e}")
            self.connection.rollback()

    def fetch_all(self):
        return self.cursor.fetchall()

    def fetch_one(self):
        return self.cursor.fetchone()

    def close_connection(self):
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            logger.info("MySQL connection is closed")
