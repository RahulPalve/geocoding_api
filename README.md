# Geoencoding API


## Intructions

- Create a **virtualenv** with `Python 3.8.0`, and activate venv.
- Install required libraries by running `pip install -r requirements.txt`.
- `docker-compose up` for quickly setting up db, Or Setup manually.
- set `GOOGLE_MAP_API_KEY` as an os environment variable (`export GOOGLE_MAP_API_KEY=".."` for linux/mac) 
- `flask run` to start.
- To test API: [Geocoding API postman_collection](/Geocoding API.postman_collection.json)
## Approach

- API performance is improved and cost reduced by caching, lat, long and addresses. Redis can be used here, but as we need to persist data, NoSQL MongoDB seems a better solution.
- `handle_output_format` decorator is used to handle multiple mime-types, Custom middleware can be used here as an alternative to this decorator.
- `Accept` HTTP header advertises which content types the user can understand, so instead of providing `output_format` it can be used. If it is used we can utilise Flasks `api.representation` to simply process of converting data to multiple mime-types.
