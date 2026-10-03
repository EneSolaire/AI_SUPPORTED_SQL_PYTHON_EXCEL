DROP TABLE IF EXISTS calisanlar;

CREATE TABLE calisanlar (
    id INTEGER PRIMARY KEY,
    ad TEXT,
    soyad TEXT,
    departman TEXT,
    maas INTEGER
);

INSERT INTO calisanlar (ad, soyad, departman, maas) VALUES
    ('Enes', 'Bünyamin', 'Yazılım', 65000),
    ('Ayşe', 'Demir', 'Finans', 58000),
    ('Mehmet', 'Kaya', 'İnsan Kaynakları', 54000),
    ('Zeynep', 'Acar', 'Satış', 62000),
    ('Eren', 'Çetin', 'Yazılım', 70000);

SELECT *
FROM calisanlar
ORDER BY id;
