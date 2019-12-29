import sqlite3


class Database:
    def __init__(self):
        self.conn = sqlite3.connect(
            'DB.db', detect_types=sqlite3.PARSE_DECLTYPES)
        self.cur = self.conn.cursor()
#  #####Create tables
        self.cur.execute("CREATE TABLE IF NOT EXISTS patients ("
                         "id INTEGER PRIMARY KEY,"
                         "name TEXT NOT NULL UNIQUE, "
                         "image TEXT NOT NULL UNIQUE   )")

        self.conn.commit()

        # insert data###################################
    def add_patient(self, name, image):### add new patient
        r = self.search(name)
        if r is None:
            # the NULL parameter is for the auto-incremented id
            self.cur.execute(
                "INSERT INTO patients VALUES(NULL,?,?)", (name, image))
            self.conn.commit()
        else:
            raise 'Patient already exist!'


    ## SHOW DATA ###################################
    def view_patients(self):### show all patients
        self.cur.execute("SELECT * FROM patients")
        rows = self.cur.fetchall()

        return rows


    def search(self,name):##search for certain patient by name
        exe = "SELECT id ,name,image FROM patients WHERE name = ? "

        self.cur.execute(exe,(name,))
        patient = self.cur.fetchone()
        if patient:
            return patient
        pass


    def delete_patient(self, name=None):# delete certain patient by name
        p = self.search(name)
        if p:
            self.cur.execute(
                "DELETE FROM patients WHERE name = ? ", (name,))
            self.conn.commit()


    def destroyALL(self):## delete all database
        exe = 'DELETE FROM patients'
        self.cur.execute(exe)
        self.conn.commit()


    # destructor-->now we close the connection to our database here
    def __del__(self):
        self.conn.close()



#####how to use:###
if __name__ == "__main__":

    db= Database()#CREATE Database

    # add patients
    db.add_patient(name='ahmad',image="images/ahmad.jpg" )
    db.add_patient(name='mahmoud',image="images/mahmoud.jpg" )

    print(db.view_patients())#return all patients

    db.delete_patient('ahmad')#delete patient

    Patient = db.search('mahmoud') #get mahmoud data

    print(f'patient\'s name: {Patient[1]}\npatient\'s image path: {Patient[2]}') #print mahmoud image path

    db.destroyALL() #Delete all Database
