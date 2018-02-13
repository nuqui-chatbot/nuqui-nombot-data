# Nombot recipes and ingredients data
This repository contains recipes and ingrediants of german food. They are saved in .sql files and so get transfered into a postgresql database.

### Tables
* RECIPES.SQL: recipe_id, name

* INGREDIENTS.SQL: ingredient_id, fat, carbohydrates, protein, name, energy, recipe_id

### Setup
You need:
* Python 3
* postgresql 8
  * A Database called "nombot"
  * A user (name: nombot ;password: feedme)
  * The two tables (nombot_recipe & nombot_ingredient)

### How to use

Start yout postgresql program and go into the CLI mode. 
Create the two tables:
```
CREATE TABLE nombot_recipe(recipe_id INT NOT NULL, name CHAR(255) NOT NULL);
CREATE TABLE nombot_ingredient(ingredient_id INT NOT NULL, fat REAL NOT NULL, carbohydrates REAL NOT NULL, protein REAL NOT NULL, name CHAR(255) NOT NULL, energy REAL NOT NULL, recipe_id INT NOT NULL);
```

Then execute the script to fill in the data into the database:
```
python insert_script.py
```
