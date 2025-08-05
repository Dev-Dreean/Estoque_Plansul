# test_db.py

from sqlalchemy import create_engine

# Substitua os dados reais abaixo:
DB_URL = "mysql+mysqlconnector://plansul04:A33673170a@mysql.plansul.kinghost.net:3306/plansul04"

try:
    engine = create_engine(DB_URL)
    conn = engine.connect()
    print("✅ Conexão com o banco de dados funcionando!")
    conn.close()
except Exception as e:
    print("❌ Erro na conexão com o banco:")
    print(e)
