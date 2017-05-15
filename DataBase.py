import psycopg2

conn = psycopg2.connect(database="dapa7brg89oltb",
                        user="vtchpzchypwlzh",
                        password="e09e0e013b6a294e3afa76cb139d0ada57f8cbde9dd83daefddafca0bcfdf2e6",
                        host="ec2-184-73-236-170.compute-1.amazonaws.com",
                        port="5432")

def initiateDatabase():
    cur = conn.cursor();

    cur.execute('''CREATE TABLE Auditorias
    (ID SERIAL PRIMARY KEY      NOT NULL,
    Error        TEXT        NOT NULL);''')


    cur.execute('''CREATE TABLE match
    (ID SERIAL PRIMARY KEY      NOT NULL,
    equipoCasa      TEXT,
    equipoVisita    TEXT,
    marcadorCasa    TEXT,
    marcadorVisita  TEXT,
    foulsCasa       TEXT,
    foulsVisita     TEXT,
    amarillasCasa   TEXT,
    amarillasVisita TEXT,
    rojasCasa       TEXT,
    rojasVisita     TEXT,
    offsidesCasa    TEXT,
    offsidesVisita  TEXT,
    cornersCasa     TEXT,
    cornersVisita   TEXT,
    savesCasa       TEXT,
    savesVisita     TEXT
    );''')

    conn.commit()
    conn.close()


initiateDatabase()

