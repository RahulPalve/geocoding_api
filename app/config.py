import os


class DevConfig(object):

    DEBUG = True
    TESTING = True
    SECRET_KEY = os.getenv("SECRET_KEY", "changeth1s3cr3tKeyTh1si5un5@fe")

    MONGO_URI = "mongodb://{username}:{password}@{host}:{port}/?authSource={auth_source}".format(
        username=os.getenv("DB_USERNAME", "admin"),
        password=os.getenv("DB_PASSWORD", "rahpal399"),
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", 27017),
        auth_source="admin"
    )

    GOOGLE_MAP_API_KEY = os.environ.get(
        "GOOGLE_MAP_API_KEY", " ")


class ProdConfig(object):

    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv("PROD_SECRET_KEY", "changeth1s3cr3tKeyTh1si5un5@fe")

    MONGO_URI = "mongodb://{username}:{password}@{host}:{port}/?authSource={auth_source}".format(
        username=os.getenv("DB_USERNAME", "admin"),
        password=os.getenv("DB_PASSWORD", "rahpal399"),
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", 27017),
        auth_source="admin"
    )

    GOOGLE_MAP_API_KEY = os.environ.get(
        "GOOGLE_MAP_API_KEY", " ")


configs = {"development": DevConfig, "production": ProdConfig}
