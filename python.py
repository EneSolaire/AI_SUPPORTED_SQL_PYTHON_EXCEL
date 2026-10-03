import sqlite3
import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 1000)

DB_PATH = "sql_verileri.db"
EXCEL_PATH = "sql_verileri.xlsx"
SQL_PATH = "sql_verileri.sql"

def baglan_ve_olustur():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS calisanlar")
    cursor.execute(
        """
        CREATE TABLE calisanlar (
            id INTEGER PRIMARY KEY,
            ad TEXT,
            soyad TEXT,
            departman TEXT,
            maas INTEGER
        )
        """
    )

    cursor.executemany(
        "INSERT INTO calisanlar (ad, soyad, departman, maas) VALUES (?, ?, ?, ?)",
        [
            ("Enes", "Bünyamin", "Yazılım", 65000),
            ("Ayşe", "Demir", "Finans", 58000),
            ("Mehmet", "Kaya", "İnsan Kaynakları", 54000),
            ("Zeynep", "Acar", "Satış", 62000),
            ("Eren", "Çetin", "Yazılım", 70000),
        ],
    )

    conn.commit()
    return conn


def veriyi_al(conn):
    sorgu = "SELECT id, ad, soyad, departman, maas FROM calisanlar ORDER BY id"
    df = pd.read_sql_query(sorgu, conn)
    return df


def excel_olarak_yazdir(df):
    df.to_excel(EXCEL_PATH, index=False, engine="openpyxl")
    print(f"\nExcel dosyası oluşturuldu: {EXCEL_PATH}")


def tablo_olarak_yazdir(df):
    print("\n" + "=" * 120)
    print("SQL'den alınan tablo (Excel benzeri görünüm)")
    print("=" * 120)
    print(df.to_string(index=False))
    print("=" * 120)


if __name__ == "__main__":
    conn = baglan_ve_olustur()
    df = veriyi_al(conn)
    tablo_olarak_yazdir(df)
    excel_olarak_yazdir(df)
    conn.close()


