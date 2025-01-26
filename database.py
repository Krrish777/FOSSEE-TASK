import sqlite3
def create_database():
    conn = sqlite3.connect('bridge_costs.db')
    cursor = conn.cursor()
    
    # Create table if not exists
    cursor.execute('''CREATE TABLE IF NOT EXISTS bridge_costs (
                        material TEXT PRIMARY KEY,
                        base_rate INTEGER,
                        maintenance_rate INTEGER,
                        repair_rate INTEGER,
                        demolition_rate INTEGER,
                        environmental_factor INTEGER,
                        social_factor REAL,
                        delay_factor REAL)''')
    
    # Insert predefined data
    cursor.execute('DELETE FROM bridge_costs')  # Clear existing data
    cursor.execute('''INSERT INTO bridge_costs (material, base_rate, maintenance_rate, repair_rate, demolition_rate, environmental_factor, social_factor, delay_factor) VALUES('Steel', 3000, 50, 200, 100, 10, 0.5, 0.3),('Concrete', 2500, 75, 150, 80, 8, 0.6, 0.2)''')
    
    conn.commit()
    conn.close()

def fetch_bridge_costs():
    conn = sqlite3.connect('bridge_costs.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bridge_costs")
    data = cursor.fetchall()
    conn.close()
    return data

def update_database(material, base_rate, maintenance_rate, repair_rate, demolition_rate, environmental_factor, social_factor, delay_factor):
    conn = sqlite3.connect('bridge_costs.db')
    cursor = conn.cursor()
    
    cursor.execute('''INSERT INTO bridge_costs (material, base_rate, maintenance_rate, repair_rate, demolition_rate, environmental_factor, social_factor, delay_factor)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                      ON CONFLICT(material) DO UPDATE SET
                      base_rate = excluded.base_rate,
                      maintenance_rate = excluded.maintenance_rate,
                      repair_rate = excluded.repair_rate,
                      demolition_rate = excluded.demolition_rate,
                      environmental_factor = excluded.environmental_factor,
                      social_factor = excluded.social_factor,
                      delay_factor = excluded.delay_factor''',
                   (material, base_rate, maintenance_rate, repair_rate, demolition_rate, environmental_factor, social_factor, delay_factor))
    
    conn.commit()
    conn.close()