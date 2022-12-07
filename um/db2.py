from unicodedata import name
from click import progressbar
import pymysql
from datetime import datetime



#디비연결


#커서생성

#입력데이터저장
#conn.commit()
conn=pymysql.connect(host='127.0.0.1',user='root',password='1234',db='project',charset='utf8')

def dbconnect():
    conn=pymysql.connect(host='127.0.0.1',user='root',password='1234',db='project',charset='utf8')
    return conn

def  search_data(conn):
    cur=conn.cursor()
    sql='select * from visits'
    cur.execute(sql)
    results=cur.fetchall()
    print(results)
    
def insert_data(picture,name):
    conn=pymysql.connect(host='127.0.0.1',user='root',password='1234',db='project',charset='utf8')
    
    
    cur=conn.cursor()
    VisitTime=datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    picture=picture
    name=name
    sql="INSERT INTO visits (VisitTime, picture, name) values('"+VisitTime+"', '"+picture+"', '"+name+"')"
    cur.execute(sql)
    conn.commit()
    print("삽입완료")
    
    
#삭제 미완성
def delete_data(conn):
    cur=conn.cursor()
    name=input("삭제할 데이터입력:")
    cur.execute("SELECT  name from visits where name ='"+name+"'")
    uname=cur.fetchone()
    
    
    
    
def  main():
    conn=dbconnect()#디비연결
    print('연결완료')
    insert_data()
    conn.close()
    print('연결해제')
    

if __name__ == "__main__":
    main() 
    