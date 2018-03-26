from flask_restful import Resource
from models.store import StoreModel


class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json(), 200

        return {'err_msg': 'Store {} not found'.format(name)}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'err_msg': 'Store {} already exists'.format(name)}, 400

        store = StoreModel(name)
        try:
            store.save_to_db()
        except Exception:
            return {'err_msg': 'An error occurred while creating the store'}, 500

        return store.json(), 201

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
            return {'message': 'Store {} deleted.'.format(name)}, 200

        return {'message': 'Store {} does not exist. No action performed.'.format(name)}, 200


class StoreList(Resource):
    def get(self):
        return {'Stores': [store.json() for store in StoreModel.query.all()]}
