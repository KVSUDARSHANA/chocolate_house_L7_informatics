## SQL Query Abstraction

This project uses a separate `database.py` file to handle all SQL operations, which improves code readability and maintainability. 

### Database Functions

- **connect_db**: Connects to the SQLite database.
- **create_tables**: Initializes tables for `SeasonalFlavors`, `IngredientInventory`, and `CustomerSuggestions`.
- **add_seasonal_flavor**: Adds a new seasonal flavor to the `SeasonalFlavors` table.
- **add_ingredient**: Adds a new ingredient to the `IngredientInventory` table.
- **add_customer_suggestion**: Adds a customer suggestion, including any allergy concerns.
- **view_seasonal_flavors**: Fetches all seasonal flavors.
- **view_ingredients**: Fetches all ingredients in the inventory.
- **view_customer_suggestions**: Fetches all customer suggestions with allergy concerns.

The main application (`chocolate_house.py`) uses these functions to interact with the database, abstracting away direct SQL query handling.
