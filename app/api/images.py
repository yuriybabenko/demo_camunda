import requests
import uuid
import random

from fastapi import APIRouter

import utils.db as db

images = APIRouter()

def get_image_path(file_name):
    return 'assets/' + file_name

@images.get('/image/{source}/{quantity}')
async def get_images(source: str, quantity: int):
    # Enforce min quantity.
    if (quantity < 1):
        quantity = 1

    # Enforce max quantity.
    if (quantity > 5):
        quantity = 5

    # Storing images (binary data) in a database is generally bad practice.
    # We will store the image in the local filesystem and save a reference to
    # it in the database.

    response_images = []

    for i in range (quantity):
        # This serves two purposes: identify the URL for the API we will query, and
        # perform rudimentary validation of the `source` argument.
        if source == 'place_bear':
            # Place Bear API seems to cache the request and return the same exact image
            # until you change the image dimentions.
            api_url = 'https://placebear.com/' + str(random.randrange(200, 800)) + '/' + str(random.randrange(200, 800))
        elif source == 'place_dog':
            api_url = 'https://place.dog/300/300'
        elif source == 'random_duck':
            api_url = 'https://random-d.uk/api/randomimg'
        else:
            # Random Fox API has 105 images to choose from.
            api_url = 'https://randomfox.ca/images/'
            api_url = api_url + str(random.randrange(1, 105)) + '.jpg'

        # UUID1 generates based on the current time and MAC address; guarantees
        # uniqueness, which is all we want in a filename.
        file_name = uuid.uuid1()
        # Cast UUID to string.
        file_name = str(file_name) + '.jpg'

        # TODO: This could be improved with concurrent downloads, file streaming,
        # header & MIME type checks, local permission checks, disk space checks, and
        # countless other verifications.
        response = requests.get(api_url)
        with open(get_image_path(file_name), 'wb') as file:
            file.write(response.content)

        db.insert_image(source, file_name)
        response_images.append(get_image_path(file_name))

    return {"images": response_images}

@images.get('/last-image/')
async def last_image():
    image = db.get_last_image()

    if image is None:
        return {}

    return {"image": get_image_path(image)}