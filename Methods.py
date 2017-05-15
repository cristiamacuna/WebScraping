import psycopg2

conn = psycopg2.connect(database="dapa7brg89oltb",
                        user="vtchpzchypwlzh",
                        password="e09e0e013b6a294e3afa76cb139d0ada57f8cbde9dd83daefddafca0bcfdf2e6",
                        host="ec2-184-73-236-170.compute-1.amazonaws.com",
                        port="5432")

def insertMatch(equipoCasa,equipoVisita,marcadorCasa,marcadorVisita,foulsCasa
                ,foulsVisita,amarillasCasa,amarillasVisita,rojasCasa,rojasVisita,
                offsidesCasa,offsidesVisita,cornersCasa,cornersVisita,savesCasa,
                savesVisita):
    cursor = conn.cursor()

    cursor.execute("INSERT INTO match(equipoCasa,equipoVisita,marcadorCasa,marcadorVisita,"
                   "foulsCasa,foulsVisita,amarillasCasa,amarillasVisita,rojasCasa,rojasVisita,"
                   "offsidesCasa,offsidesVisita,cornersCasa,cornersVisita,savesCasa,savesVisita)"
                   "VALUES('"+equipoCasa+"','"+equipoVisita+"','"+marcadorCasa+"','"+marcadorVisita+"','"+foulsCasa+'","'+foulsVisita+'","'+amarillasCasa+'","'+amarillasVisita+'","'+rojasCasa+'","'+rojasVisita+'","'+offsidesCasa+'","'+offsidesVisita+'",+"'+cornersCasa+'","'+cornersVisita+'","'+savesCasa+'","'+savesVisita+''");");
    conn.commit()
    conn.close()