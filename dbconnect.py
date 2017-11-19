import sqlite3
DATABASE = 'database.db'

def insert(Roll_no,Name,Class,Password):
	con1 = sqlite3.connect(DATABASE)
	cur1 = con1.cursor()
	cur1.execute("INSERT INTO Student (Roll_no,Name,Class,Password) values (?,?,?,?)", (Roll_no,Name,Class,Password))
	con1.commit()
	con1.close()

def fetch():
	con2 = sqlite3.connect(DATABASE)
	cur2 = con2.cursor()
	cur2.execute("SELECT Roll_no,Name,Class,Password from Student")	
	data=cur2.fetchall()
	con2.close()
	return data

def insert(Staff_id,Password,Class):
	con3 = sqlite3.connect(DATABASE)
	cur3 = con3.cursor()
	cur3.execute("INSERT INTO Staff (Fac_id,Password) values (?,?)", (Fac_id,Password))
	con3.commit()
	con3.close()

def fetch():
	con4 = sqlite3.connect(DATABASE)
	cur4 = con4.cursor()
	cur4.execute("SELECT Fac_id,Password from Staff")	
	data=cur4.fetchall()
	con4.close()
	return data

def insert(Activity,Activity_level,Point):
	con5 = sqlite3.connect(DATABASE)
	cur5 = con5.cursor()
	cur5.execute("INSERT INTO Act (Aid,Activity,Activity_level,Point) values (?,?,?,?)", (Aid,Activity,Activity_level,Point))
	con5.commit()
	con5.close()

def fetch():
	con6 = sqlite3.connect(DATABASE)
	cur6 = con6.cursor()
	cur6.execute("SELECT Aid,Activity,Activity_level,Point from Act")	
	data=cur6.fetchall()
	con6.close()
	return data

def insert(Activity,Activity_level,Point):
	con7 = sqlite3.connect(DATABASE)
	cur7 = con7.cursor()
	cur7.execute("INSERT INTO StudAct (Roll_no,Aid) values (?,?)", (Roll_no,Aid))
	con7.commit()
	con7.close()

def fetch():
	con8 = sqlite3.connect(DATABASE)
	cur8 = con8.cursor()
	cur8.execute("SELECT Roll_no,Aid from StudAct")	
	data=cur8.fetchall()
	con8.close()
	return data





	
