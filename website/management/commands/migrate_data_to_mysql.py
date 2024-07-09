# myapp/management/commands/migrate_data_to_mysql.py

from django.core.management.base import BaseCommand
import redis
import mysql.connector

class Command(BaseCommand):
    help = 'Migrate data from Redis to MySQL'

    def handle(self, *args, **kwargs):
        self.stdout.write("Migrating data from Redis to MySQL...")

        # Connect to Redis
        redis_client = redis.StrictRedis(host='redis', port=6379, db=0)

        # Connect to MySQL
        mysql_conn = mysql.connector.connect(
            host='sql-container',
            user='arham',
            password='Jain@321',
            database='eldercop'
        )
        cursor = mysql_conn.cursor()

        # Example migration logic
        keys = redis_client.keys('*')
        for key in keys:
            value = redis_client.get(key)
            # Assuming key-value pairs are strings
            cursor.execute("INSERT INTO mytable (key, value) VALUES (%s, %s)", (key.decode('utf-8'), value.decode('utf-8')))

        mysql_conn.commit()
        cursor.close()
        mysql_conn.close()

        self.stdout.write("Data migration completed.")
