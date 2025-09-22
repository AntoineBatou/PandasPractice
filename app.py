import pandas as pd
avocado = pd.read_csv("/Users/marc/Downloads/avocado.csv").rename(columns={"AveragePrice": "price"})
avocado_work = avocado[["year", "region", "type", "price"]]

# Je veux savoir quelle région avait le prix moyen le plus bas pour les avocats cultivés
# de manière conventionnelle chaque année, et je veux connaître la même information pour les
# avocats biologiques.

#1 - Je récupère la liste en filtrant uniquement les avocats conventionnels et les bio

conv = avocado_work[avocado_work["type"] == 'conventional'].drop(columns="type")
bio = avocado_work[avocado_work["type"] == 'organic'].drop(columns="type")

#2 Je récupère une variable avec chaque année en mode unique et je crée un dictionnaire vide pour chacune des catégories

years = avocado_work.year.unique()
dict_conv = {}
dict_bio = {}

#3 - Je groupe par région, par année en faisant la moyenne sur le prix (je garde un DF avec as_index = False)

avg_conv = conv.groupby(["year", "region"], as_index=False)["price"].mean()
avg_bio = bio.groupby(["year", "region"], as_index=False)["price"].mean()

#4 Je récupère un dictionnaire pour chaque cat, contenant les années en clé et un DF avec les prix moyens pour cette annee en valeur

for i in years:
    dict_conv[i] = avg_conv.loc[avg_conv["year"] == i].drop(columns="year")
    dict_bio[i] = avg_bio.loc[avg_bio["year"] == i].drop(columns="year")

print(dict_conv)