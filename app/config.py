import os


class DevConfig(object):

    DEBUG = True
    TESTING = True
    SECRET_KEY = os.getenv("SECRET_KEY", "changeth1s3cr3tKeyTh1si5un5@fe")

    MONGO_URI = "mongodb://{username}:{password}@{host}:{port}/{db}?authSource={auth_source}".format(
        username=os.getenv("DB_USERNAME", "vl_user"),
        password=os.getenv("DB_PASSWORD", "vl_password"),
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", 27017),
        db=os.getenv("DB_NAME", "db"),
        auth_source="admin"
    )

    GOOGLE_MAP_API_KEY = os.environ.get(
        "GOOGLE_MAP_API_KEY", "")


class ProdConfig(object):

    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv("PROD_SECRET_KEY", "changeth1s3cr3tKeyTh1si5un5@fe")

    MONGO_URI = "mongodb://{username}:{password}@{host}:{port}/{db}?authSource={auth_source}".format(
        username=os.getenv("DB_USERNAME", "vl_user"),
        password=os.getenv("DB_PASSWORD", "vl_password"),
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", 27017),
        db=os.getenv("DB_NAME", "db"),
        auth_source="admin"
    )

    GOOGLE_MAP_API_KEY = os.environ.get(
        "GOOGLE_MAP_API_KEY", "")


configs = {"development": DevConfig, "production": ProdConfig}
