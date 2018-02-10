import psycopg2

#make the connection
try: 
    conn = psycopg2.connect("dbname='nombot' user='nombot' host='localhost' password='feedme'")
except:
    print ("db connection not working")

cursor = conn.cursor()

#get the file with the infos
pathRec = "recipes/recipes.sql"
pathIng = "recipes/ingredients.sql"

recFile = open(pathRec, 'r')
ingFile= open(pathIng, 'r')

for line in recFile:
    line_list = line.split('\t')
    id = int(line_list[0])
    name = line_list[2][1:-1]
    #insert into db
    cursor.execute("""INSERT INTO nombot_recipe(recipe_id, name) VALUES (%d, '%s')""" % (id, name))

for line in ingFile:
    line_list = line.split('\t')   
    ing_id = int(line_list[1])
    recp_id = int(line_list[0])
    fat = float(line_list[8])
    carbohydrates= float(line_list[10])
    protein = float(line_list[9])
    name = line_list[3][1:-1]
    energy = float(line_list[7])
    #insert into db
    cursor.execute("""INSERT INTO nombot_ingredient(ingredient_id, fat, carbohydrates, protein, name, energy, recipe_id) VALUES (%d, %d, %d, %d, '%s', %d, %d)""" % (ing_id, fat, carbohydrates, protein, name, energy, recp_id))

conn.commit()
cursor.close()
conn.close()
