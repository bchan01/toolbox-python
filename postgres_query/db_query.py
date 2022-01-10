import datetime
import psycopg2


sql = 'select organization, database_type, extractor_version, sql_file_version from dev.organization_extractor_management'

def connect():
    conn = psycopg2.connect("dbname='extractor' user='bchan' host='localhost' password='admin'")
    return conn

def run_query(sql, conn = None):
    try:
        if conn is None:
            conn = connect()
        start = datetime.datetime.now()
        
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        for row in rows:
            pass
            #print("{},{},{},{}".format(row[0],row[1], row[2], row[3]))
        end = datetime.datetime.now()
        time_diff = (end - start).total_seconds() * 1000
        #print("{:.4f}".format(time_diff))
        return "{:.4f}".format(time_diff)
    except:
       print("unable to connect to the database")
    finally:
        if conn is not None:
            conn.close()

def main():
    #conn = connect()
    times = []
    times.append('Trial,ElapsedTime')
    for x in range(100):
        time = run_query(sql)
        times.append("{},{}".format(x, time))
    print("\n".join(times))

if __name__ == "__main__":
    main()