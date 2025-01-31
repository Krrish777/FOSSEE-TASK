import sqlite3

def create_database():
    """
    Create the bridge_costs database and table if it does not exist.
    Insert predefined data into the table.
    """
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
    cursor.execute('''INSERT INTO bridge_costs (material, base_rate, maintenance_rate, repair_rate, demolition_rate, environmental_factor, social_factor, delay_factor) 
                      VALUES ('Steel', 3000, 50, 200, 100, 10, 0.5, 0.3),
                             ('Concrete', 2500, 75, 150, 80, 8, 0.6, 0.2)''')
    
    conn.commit()
    conn.close()

def fetch_bridge_costs():
    """
    Fetch all records from the bridge_costs table.
    
    Returns:
        list of tuples: Each tuple contains the data of a row in the table.
    """
    conn = sqlite3.connect('bridge_costs.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bridge_costs")
    data = cursor.fetchall()
    conn.close()
    return data

def update_database(material, base_rate, maintenance_rate, repair_rate, demolition_rate, environmental_factor, social_factor, delay_factor):
    """
    Insert or update a record in the bridge_costs table.
    
    If a record with the given material already exists, update it with the new values.
    Otherwise, insert a new record.
    
    Args:
        material (str): The material of the bridge.
        base_rate (int): The base rate of the bridge.
        maintenance_rate (int): The maintenance rate of the bridge.
        repair_rate (int): The repair rate of the bridge.
        demolition_rate (int): The demolition rate of the bridge.
        environmental_factor (int): The environmental factor of the bridge.
        social_factor (float): The social factor of the bridge.
        delay_factor (float): The delay factor of the bridge.
    """
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