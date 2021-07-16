from mongoengine import connect


def config_db():
    connect("mongodb-ecofire")
