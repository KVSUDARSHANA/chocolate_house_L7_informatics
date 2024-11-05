from database import connect_db, create_tables, add_seasonal_flavor, add_ingredient, add_customer_suggestion

# Connect to the database
conn = connect_db()
create_tables(conn)

# Add sample data
add_seasonal_flavor(conn, "Mint Delight", "A refreshing mint chocolate flavor", "Winter")
add_ingredient(conn, "Cocoa", 50, "kg")
add_customer_suggestion(conn, "Alice", "Lavender Truffle", "No nuts")

# Print to verify
print("Sample data initialized successfully.")

# Close the database connection
conn.close()
