from platform import uname

import pymongo


def db_writer(field, value, user='', password=''):
    comp = uname().node

    cluster = pymongo.MongoClient(f'mongodb+srv://{user}:{password}@cluster0.izgzhsi.mongodb.net/?retryWrites=true&w=majority')
    db = cluster.get_database('Banca')
    collection = db.get_collection(comp) if comp in db.list_collection_names() else db.create_collection(comp)
    data_collection = dict()
    for document in value:
        for i in range(len(field)):
            data_collection.update({field[i]: document[i]})
        collection.insert_one(data_collection)
        data_collection.clear()
