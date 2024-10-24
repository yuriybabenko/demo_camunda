### About

This is a Python application utilizing the FastAPI framework, Python
modules, and Python's built-in SQLite database engine.

Application can be accessed at http://0.0.0.0:8000/, which will show a
basic UI to interact with the API. 

### API

There are two API paths that accept requests:

GET `/image/{source}/{quantity}` - Will query an external image API for the
specified number of images, save them locally, and return a JSON object
with local file paths to the saved images.
- `source` - Determines which image API to query. Can be one of:
  - `place_bear`
  - `place_dog`
  - `random_duck`
  - `random_fox` - default
- `quantity` - an integer from 1 to 5. Minimum & maximum values are 
automatically enforced.

GET `/last-image/` - Will return a JSON object with the local file path to
the latest image. If no image is available, an empty JSON object is
returned.