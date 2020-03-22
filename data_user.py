import requests
import psycopg2
with requests.get("http://127.0.0.1:5000/data_generator/100000000", stream = True) as req_respond:
    buffer = ""
    conn = psycopg2.connect(dbname="demo_data_pipeline",
                     user="postgres",
                     password="*******")
    cur = conn.cursor()
    sql = "INSERT INTO transactions (txid, uid, amount) VALUES (%s, %s, %s)"
    for chunk in req_respond.iter_content(chunk_size = 1):
        if chunk.endswith(b'\n'):
            # print(type(buffer))
            t = eval(buffer)
            print(t)
            cur.execute(sql,(t[0], t[1], t[2]))
            conn.commit()
            buffer = ""
        else:
            # print(chunk.decode())
            buffer += chunk.decode()