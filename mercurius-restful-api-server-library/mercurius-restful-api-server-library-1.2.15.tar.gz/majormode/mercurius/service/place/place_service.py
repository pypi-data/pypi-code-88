# Copyright (C) 2019 Majormode.  All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from typing import Tuple
import collections
import hashlib
import io
import os
import traceback
import uuid

from PIL import Image
from majormode.mercurius.constant.place import SearchIntent
from majormode.mercurius.model.place import AddressComponentName
from majormode.perseus.constant.area import AREA_LEVEL_COUNTRY
from majormode.perseus.constant.area import AREA_LEVEL_DISTRICT
from majormode.perseus.constant.obj import ObjectStatus
from majormode.perseus.constant.privacy import Visibility
from majormode.perseus.constant.team import MemberRole
from majormode.perseus.model.geolocation import BoundingBox
from majormode.perseus.model.geolocation import GeoPoint
from majormode.perseus.model.locale import DEFAULT_LOCALE
from majormode.perseus.model.locale import Locale
from majormode.perseus.model.obj import Object
from majormode.perseus.service.area.area_service import AreaService
from majormode.perseus.service.base_rdbms_service import BaseRdbmsService
from majormode.perseus.service.team.team_service import TeamService
from majormode.perseus.utils import cast
from majormode.perseus.utils import file_util
from majormode.perseus.utils import image_util
from majormode.perseus.utils import string_util
from majormode.perseus.utils.rdbms import RdbmsConnection

import settings


# Default file extensions per image file format.  When not defined, the
# file extension is named after the image file format.
DEFAULT_IMAGE_FILE_FORMAT_EXTENSIONS = {
    'JPEG': 'jpg'
}


class PlaceService(BaseRdbmsService):
    # Name of the bucket on a local or remote Content Delivery Network
    # (CDN) where the thumbnail versions of place logo pictures are stored
    # into.
    DEFAULT_CDN_BUCKET_NAME_LOGO = 'logo'

    # Name of the bucket on a local or remote Content Delivery Network
    # (CDN) where the thumbnail versions of photos are stored into.
    DEFAULT_CDN_BUCKET_NAME_PHOTO = 'photo'

    # Default image file format to store the logo of a team with (cf.
    # https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html).
    DEFAULT_LOGO_IMAGE_FILE_FORMAT = 'JPEG'

    # Default quality to store the image of a team's logo with, on a scale
    # from `1` (worst) to `95` (best).  Values above `95` should be avoided;
    # `100` disables portions of the JPEG compression algorithm, and results
    # in large files with hardly any gain in image quality.
    DEFAULT_LOGO_IMAGE_QUALITY = 75

    # Default minimal size of the image of a team's logo.
    DEFAULT_LOGO_IMAGE_MINIMAL_SIZE = (400, 400)

    # Default distance in meters of the radius of search for places nearby
    # a given location.
    DEFAULT_SEARCH_RADIUS = 20000

    # Maximal distance in meters of the radius of search for places nearby
    # a given location.
    MAXIMAL_SEARCH_RADIUS = 40000

    def __add_place_address(
            self,
            place_id,
            address,
            account_id=None,
            connection=None,
            locale=None):
        """
        Add a list of address information to a place.


        :param place_id: Identification of a place.

        :param address: A dictionary of address components where the key
            corresponds to an item of the enumeration `AddressComponentName`.

        :param account_id: Identification of the account of the user who adds
            this address information.

        :param connection: An object `RdbmsConnection` supporting the Python
            clause `with ...:`.

        :param locale: An object `Locale` defining the language which the
            textual information of the address component is written in.
        """
        with self.acquire_rdbms_connection(auto_commit=True, connection=connection) as connection:
            connection.execute(
                """
                INSERT INTO place_address (
                    place_id,
                    account_id,
                    locale,
                    property_name,
                    property_value)
                  VALUES 
                    %[values]s
                """,
                {
                    'values': [
                        (
                            place_id,
                            account_id,
                            locale or DEFAULT_LOCALE,
                            property_name,
                            property_value,
                        )
                        for (property_name, property_value) in address.items()
                    ]
                })

    def __add_place_contacts(
            self,
            place_id,
            contacts,
            account_id=None,
            connection=None):
        """
        Add a list of contact information to a place


        :param place_id: Identification of a place.

        :param contacts: A list of `Contact` objects.

        :param account_id: Identification of the account of the user who adds
            this list of contact information.

        :param connection: An object `RdbmsConnection` supporting the Python
            clause `with ...:`.
        """
        with self.acquire_rdbms_connection(auto_commit=True, connection=connection) as connection:
            connection.execute(
                """
                INSERT INTO place_contact(
                    place_id,
                    account_id,
                    property_name,
                    property_value,
                    is_primary,
                    is_verified,
                    visibility)
                  VALUES 
                    %[values]s
                    """,
                {
                    'values': [
                        (
                            place_id,
                            account_id,
                            contact.name,
                            contact.value,
                            contact.is_primary,
                            contact.is_verified,
                            contact.visiblity
                        )
                        for contact in contacts
                    ]
                })

    @staticmethod
    def __build_bounding_box_wkt(bounding_box: BoundingBox) -> str:
        """
        Return a Well-Known Text (WKT) string representing a bounding box

        
        :param bounding_box: An object `BoundingBox`.
        
         
        :return: A Well-Known Text (WKT) "LINESTRING" representing the
            bounding box.
        """
        boundaries = [
            (bounding_box.southwest.longitude, bounding_box.northeast.latitude),
            (bounding_box.northeast.longitude, bounding_box.northeast.latitude),
            (bounding_box.northeast.longitude, bounding_box.southwest.latitude),
            (bounding_box.southwest.longitude, bounding_box.southwest.latitude),
            (bounding_box.southwest.longitude, bounding_box.northeast.latitude)
        ]

        geometry_wkt = 'LINESTRING({})'.format(','.join([
            f'{longitude} {latitude}'
            for (longitude, latitude) in boundaries
        ]))

        return geometry_wkt

    @staticmethod
    def __build_picture_file_path_name(
            picture_id,
            root_path,
            image_file_format,
            logical_size):
        """
        Return the path and name of a picture stored in the local CDN.


        :param picture_id: Identification of the picture of an account.

        :param root_path: Absolute root path where the image files of team
            logos are stored into.

        :param image_file_format: File format to store the image with  (cf.
            https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html).

        :param logical_size: A string representation of the image size, such
            as "thumbnail", "small", "medium", and "large".


        :return: A string representing the path and name of an image file.
        """
        # Name the file against its identification and its logical size.
        file_name = f'{str(picture_id)}_{logical_size}'

        # Create the path of the folder where the image file will be stored in.
        path = os.path.join(
            root_path,
            file_util.build_tree_pathname(file_name))

        # Add the extension to the file depending on the image format.
        file_extension = DEFAULT_IMAGE_FILE_FORMAT_EXTENSIONS.get(image_file_format) or image_file_format.lower()

        # Build the absolute path and name of the image file.
        file_path_name = os.path.join(path, f'{file_name}.{file_extension}')

        return file_path_name

    @staticmethod
    def __find_area_with_ip_address(
            ip_address,
            area_level=None,
            locale=None):
        """
        Find an administrative subdivision with an IP address


        :param ip_address: IPv4 address of the machine of a user.  It
            corresponds to a tuple consisting of four decimal numbers, each
            ranging from `0` to `255`.

        :param area_level: The level of the administrative subdivision to
            return a list of schools.  By default, it corresponds to a country
            level.  The minimal area level is `AREA_LEVEL_DISTRICT`.

        :param locale: An object `Locale` specifying the language to return
            the name of the country.


        :return: An object representing the information of the country found
            with this IP address.
        """
        if area_level is None:
            area_level = AREA_LEVEL_COUNTRY

        # Search from the smallest possible administrative subdivision to
        # improve a lot the performance (milliseconds v.s. a few seconds).
        areas = AreaService().find_areas_with_ip_address(
            ip_address,
            lowest_area_level=min(AREA_LEVEL_DISTRICT, area_level),
            highest_area_level=area_level,
            locale=locale)

        # Filter the country area.
        areas = [
            area
            for area in areas
            if area.area_level == area_level
        ]

        area = None if len(areas) == 0 else areas[0]
        return area


    @staticmethod
    def __find_area_with_location(
            location,
            area_level=None,
            locale=None):
        """
        Find an administrative subdivision with a geographical location


        :param location: An object `GeoPoint`.

        :param area_level: The level of the administrative subdivision to
            return a list of schools.  By default, it corresponds to a country
            level.  The minimal area level is `AREA_LEVEL_DISTRICT`.

        :param locale: An object `Locale` specifying the language to return
            the name of the country.


        :return: An object representing the information of the country found
            with this IP address.
        """
        if area_level is None:
            area_level = AREA_LEVEL_COUNTRY

        # Search from the smallest possible administrative subdivision to
        # improve a lot the performance (milliseconds v.s. a few seconds).
        areas = AreaService().find_areas_with_location(
            location,
            lowest_area_level=min(AREA_LEVEL_DISTRICT, area_level),
            highest_area_level=area_level,
            locale=locale)

        # Filter the country area.
        areas = [
            area
            for area in areas
            if area.area_level == area_level
        ]

        area = None if len(areas) == 0 else areas[0]
        return area

    @staticmethod
    def __get_multiple_pixel_resolutions(bucket_name):
        """
        Return the multiple pixel resolutions of the scaled-down raster images
        to be generated


        :param bucket_name: The name of the bucket where multiple pixel
            resolutions of the scaled-down raster images will be stored in.
            It corresponds to the name of a Content Delivery Network (CDN)
            bucket.


        :return: A List of tuple `(width, height, logical image size)` where:

            * `width`: Positive integer corresponding to the number of pixel columns
              of the image.

            * height: positive integer corresponding to the number of pixel rows.

            * logical image size: string representation of the image size, such as
             'thumbnail', 'small', 'medium', and 'large'.
        """
        resolutions = settings.IMAGE_PIXEL_RESOLUTIONS[bucket_name] or settings.IMAGE_PIXEL_RESOLUTIONS[None]
        return resolutions

    def __get_place_photos(
            self,
            place_id,
            account_id=None,
            connection=None,
            limit=None,
            offset=None):
        """
        Return a list of photos related to a place.


        :param place_id: Identification of a place.

        :param account_id: Identification of the account of a user on behalf
            of whom this function is called.

        :param connection: A `RdbmsConnection` instance to be used supporting
            the Python clause `with ...:`.

        :param limit: Constrain the number of photos that are returned to the
            specified number.

        :param offset: Require to skip that many photos before beginning to
            return them.  If both `limit` and `offset` are specified, then
            `offset` photos are skipped before starting to count the `limit`
            photos that are returned.  The default value is `0`.


        :return: A list of objects containing the following attributes:

            * `account_id`: Identification of the account of the user who posted
              this photo.

            * `capture_time` (optional): Time when this photo has been captured.

            * `creation_time` (required): Time when this photo has been registered
              to the platform.

            * `object_status` (required): Current status of this photo.

            * `photo_id` (required): Identification of a photo.

            * `team_id` (optional): Identification of the organization on behalf of
              which this photo has been posted.

            * `visibility` (required): Visibility of this photo to other users.
        """
        with self.acquire_rdbms_connection(auto_commit=False, connection=connection) as connection:
            cursor = connection.execute(
                """
                SELECT 
                    photo_id,
                    account_id,
                    team_id,
                    capture_time,
                    object_status,
                    creation_time
                  FROM 
                    place_photo
                  WHERE
                    place_id = %(place_id)s
                    AND (object_status = %(OBJECT_STATUS_ENABLED)s
                         OR (object_status IN (%(OBJECT_STATUS_PENDING)s, %(OBJECT_STATUS_DISABLED)s)  
                             AND (account_id = %(account_id)s 
                                  OR (team_id IS NOT NULL AND team_is_administrator(account_id, team_id)))))
                    AND (visibility = %(VISIBILITY_PUBLIC)s 
                         OR (visibility = %(VISIBILITY_PRIVATE)s AND account_id = %(account_id)s)
                         OR (visibility = %(VISIBILITY_TEAM)s
                             AND (account_id = %(account_id)s OR team_is_member(account_id, team_id))))
                  ORDER BY
                    creation_time DESC
                  LIMIT %(limit)s
                  OFFSET %(offset)s
                """,
                {
                    'OBJECT_STATUS_DISABLED': ObjectStatus.disabled,
                    'OBJECT_STATUS_ENABLED': ObjectStatus.enabled,
                    'OBJECT_STATUS_PENDING': ObjectStatus.pending,
                    'VISIBILITY_PRIVATE': Visibility.private,
                    'VISIBILITY_PUBLIC': Visibility.public,
                    'VISIBILITY_TEAM': Visibility.team,
                    'account_id': account_id,
                    'limit': min(limit, self.MAXIMUM_LIMIT) or self.DEFAULT_LIMIT,
                    'offset': offset or 0,
                    'place_id': place_id
                })

            photos = [
                row.get_object({
                    'account_id': cast.string_to_uuid,
                    'capture_time': cast.string_to_timestamp,
                    'creation_time': cast.string_to_timestamp,
                    'object_status': ObjectStatus,
                    'photo_id': cast.string_to_uuid,
                    'team_id': cast.string_to_uuid,
                    'visibility': Visibility
                })
                for row in cursor.fetch_all()
            ]

            return photos

    def __index_place(self, place_id, connection=None):
        """
        Index a place with its information.

        The function retrieves the address component `recipient_name` and
        latinizes each word to index the place with.


        :param place_id: Identification of the place to index.

        :param connection: An object `RdbmsConnection` supporting the Python
            clause `with ...:`.
        """
        with self.acquire_rdbms_connection(auto_commit=True, connection=connection) as connection:
            cursor = connection.execute(
                """
                SELECT 
                    property_value AS name
                  FROM 
                    place_address
                  WHERE 
                    place_id = %(place_id)s
                    AND property_name = %(ADDRESS_COMPONENT_RECIPIENT_NAME)s
                """,
                {
                    'ADDRESS_COMPONENT_RECIPIENT_NAME': AddressComponentName.recipient_name,
                    'place_id': place_id
                })

            keywords = string_util.string_to_keywords(' '.join([
                row.get_value('name')
                for row in cursor.fetch_all()
            ]))

            if keywords:
                connection.execute(
                    """
                    DELETE FROM 
                        place_index 
                      WHERE 
                        place_id = %(place_id)s
                    """,
                    {
                        'place_id': place_id
                    })

                connection.execute(
                    """
                    INSERT INTO place_index(
                        place_id,
                        keyword)
                      VALUES %[values]s
                    """,
                    {
                        'values': [(place_id, keyword) for keyword in keywords]
                    })

    @classmethod
    def __load_image_from_bytes(cls, data):
        """
        Load an image from a bytes-like object.


        :param data: A bytes-like object that contains the image's data.


        :return: An object `PIL.Image`.


        :raise InvalidArgumentException: If the format of the image is not
            supported.
        """
        try:
            bytes_stream = io.BytesIO(data)
            image = image_util.convert_image_to_rgb_mode(Image.open(bytes_stream))
        except:
            traceback.print_exc()
            raise cls.InvalidArgumentException("Unsupported image file format")

        return image

    @classmethod
    def __save_multiple_resolution_logo_files(
            cls,
            picture_id,
            image,
            resolutions,
            image_file_format=DEFAULT_LOGO_IMAGE_FILE_FORMAT,
            image_quality=DEFAULT_LOGO_IMAGE_QUALITY):
        """
        Generate multiple resolutions of the logo's image.


        :param picture_id: Identification of the logo.

        :param image: An object `PIL.Image` corresponding to the logo's image.

        :param resolutions: An array of pixel resolutions of the scaled-down
            JPEG raster images to be generated:

               [
                 (width, height, logical_size),
                 ...
               ]

            where:

            - width: Positive integer corresponding to the number of pixel colunms
              of the image.

            - height: Positive integer corresponding to the number of pixel rows.

            - logical_size (string): String representation of the image size, such
              as "thumbnail", "small", "medium", and "large".

        :param image_file_format: Image file format to store the image with
            (cf. https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html).

        :param image_quality: The image quality to store locally, on a scale from `1`
            (worst) to `95` (best).  Values above `95` should be avoided; `100`
            disables portions of the JPEG compression algorithm, and results
            in large files with hardly any gain in image quality.
        """
        for logical_size, scaled_image in image_util.generate_multiple_pixel_resolutions(
                image,
                resolutions,
                does_crop=True,
                filter=image_util.Filter.AntiAlias):
            scaled_image.save(
                cls.__build_picture_file_path_name(
                    picture_id,
                    os.path.join(settings.CDN_NFS_ROOT_PATH, cls.DEFAULT_CDN_BUCKET_NAME_LOGO),
                    image_file_format,
                    logical_size),
                image_file_format,
                quality=image_quality)

    @classmethod
    def __store_logo_image_file(
            cls,
            picture_id,
            image,
            image_file_format=DEFAULT_LOGO_IMAGE_FILE_FORMAT,
            image_quality=DEFAULT_LOGO_IMAGE_QUALITY):
        """
        Store the image of a team's logo onto the Network File System (NFS)

        The function generates the multiple resolutions of this image.


        :param picture_id: The identification of the team's logo.

        :param image: An object `PIL.Image`.

        :param image_file_format: Image file format to store the image with
            (cf. https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html).

        :param image_quality: The image quality to store locally, on a scale from `1`
            (worst) to `95` (best).  Values above `95` should be avoided; `100`
            disables portions of the JPEG compression algorithm, and results
            in large files with hardly any gain in image quality.
        """
        # Create the path of the folder to store the image file in.
        path = os.path.join(
            settings.CDN_NFS_ROOT_PATH,
            cls.DEFAULT_CDN_BUCKET_NAME_LOGO,
            file_util.build_tree_pathname(str(picture_id)))

        file_util.make_directory_if_not_exists(path)

        # Retrieve the multiple pixel resolutions of the images to generate.
        resolutions = cls.__get_multiple_pixel_resolutions(cls.DEFAULT_CDN_BUCKET_NAME_LOGO)

        # Generate and store the multiple pixel resolutions of the images of
        # this logo.
        cls.__save_multiple_resolution_logo_files(
            picture_id,
            image,
            resolutions,
            image_file_format=image_file_format,
            image_quality=image_quality)

    def __update_place_address(
            self,
            place_id,
            address,
            account_id=None,
            connection=None,
            locale=None):
        """
        Update the address information of an existing place


        :param place_id: Identification of a place.

        :param address: A dictionary of address components where the key
            corresponds to an item of the enumeration `AddressComponentName`.

        :param account_id: Identification of the account of the user who
            updates the address information of the place.

        :param connection: An object `RdbmsConnection`.

        :param locale: An object `Locale` defining the language in which the
            textual information of the address component is written.
        """
        with self.acquire_rdbms_connection(auto_commit=True, connection=connection) as connection:
            connection.execute(
                """
                DELETE FROM 
                    place_address
                  WHERE
                    place_id = %(place_id)s
                    AND account_id = %(account_id)s
                    AND locale = %(locale)s
                """,
                {
                    'account_id': account_id,
                    'locale': locale or DEFAULT_LOCALE,
                    'place_id': place_id,
                }
            )

            self.__add_place_address(
                place_id,
                address,
                account_id=account_id,
                connection=connection,
                locale=locale)

    @classmethod
    def __validate_image_size(cls, image, minimal_size):
        """
        Validate the resolution of the image of the new logo of a team.


        :param image: An object `PIL.Image`.

        :param minimal_size: A tuple of two integers `(width, height)`
            representing the minimal size of the image of a photo.


        :raise InvalidArgumentException: If the image is too small, or if the
            image dimension is not in a square aspect ratio.
        """
        image_width, image_height = image.size
        min_width, min_height = minimal_size

        if (image_width < min_width and image_height < min_height) or \
           (image_width < min_height and image_height < min_width):
            raise cls.InvalidArgumentException(f"Image is too small: minimal size is {min_width}x{min_height}")

        if image_width != image_height:
            raise cls.InvalidArgumentException("Image dimensions must be in a square aspect ratio")

    def add_place(
            self,
            account_id=None,
            boundaries=None,
            category=None,
            connection=None,
            contacts=None,
            address=None,
            is_address_edited=False,
            is_location_edited=False,
            locale=None,
            location=None):
        """
        Register a new place


        :param account_id: Identification of the account of of the user who
            adds this place.

        :param boundaries: A collection of one or more polygons that delimit
            the topological space of the place.  All of the polygons are
            within the spatial reference system.

        :param category: A string representation, or an item of an enumeration,
            of a category qualifying this place.

        :param connection: An object `RdbmsConnection`.

        :param contacts: A list of `Contact` objects representing the contact
            information of the place.

        :param address: Postal address of places, composed of one or more
            address components, which textual information is written in the
            specified locale.  An address component is defined with a
            component name (an item of the enumeration `AddressComponentName`)
            and its corresponding value.

        :param is_address_edited: Indicate whether the user has manually
            edited the address, or whether a reverse geocoder has
            automatically provided this address.

        :param is_location_edited: Indicate whether the location has been
            manually edited by the user, more likely by dragging/dropping a
            marker on an electronic map, or whether the device of the user has
            detected the user's current location or a geocoder has converted
            the formatted address of this place to a location.

        :param locale: An object `Locale` defining the language which the
            textual information of the address component is written in.

        :param location: An object `GeoPoint` representing the geographical
            location of the place's location (e.g., main entrance).


        :return: An object containing the following attributes:

            * `object_status` (required): The current status of the place.

            * `place_id` (required): Identification of the place.

            * `update_time` (required): Time of the most recent modification of
              one or more attributes of this place.
        """
        with self.acquire_rdbms_connection(auto_commit=True, connection=connection) as connection:
            cursor = connection.execute(
                """
                INSERT INTO place(
                    account_id,
                    category,
                    location,
                    boundaries,
                    is_address_edited,
                    is_location_edited)
                  VALUES 
                    (%(account_id)s,
                     %(category)s,
                     ST_SetSRID(ST_MakePoint(%(longitude)s, %(latitude)s, %(altitude)s), 4326),
                     ST_MakePolygon(ST_GeomFromText(%(boundaries)s, 4326)),                     
                     %(is_address_edited)s,
                     %(is_location_edited)s)
                  RETURNING 
                    object_status,
                    place_id,
                    update_time
                """,
                {
                    'account_id': account_id,
                    'altitude': (location and location.altitude) or 0,
                    'boundaries': boundaries and 'LINESTRING(%s)' % ','.join([
                        f'{longitude} {latitude} {altitude}'
                        for longitude, latitude, altitude in boundaries]),
                    'category': category,  # @todo: `category.strip().lower()` when category won't be a enumeration anymore
                    'is_address_edited': is_address_edited,
                    'is_location_edited': is_location_edited,
                    'latitude': location and location.latitude,
                    'longitude': location and location.longitude
                })

            place = cursor.fetch_one().get_object({
                'object_status': ObjectStatus,
                'place_id': cast.string_to_uuid,
                'update_time': cast.string_to_timestamp
            })

            # Add the address information of the place, if any defined.
            if address:
                self.__add_place_address(
                    place.place_id,
                    address,
                    account_id=account_id,
                    connection=connection,
                    locale=locale)

            # Add the contact information of the place, if any defined.
            if contacts:
                self.__add_place_contacts(
                    place.place_id,
                    contacts,
                    account_id=account_id,
                    connection=connection)

            # Index the place so that it can be searchable providing a list of
            # keywords.
            self.__index_place(place.place_id, connection=connection)

            return place

    @classmethod
    def build_cover_photo_url(cls, picture_id):
        """
        Return the Uniform Resource Locator of the cover photos of a place.


        :param picture_id: Identification of the place's cover photo.


        :return: A string representing the Uniform Resource Locator of the
            place's cover photo.
        """
        return picture_id and os.path.join(
            settings.CDN_URL_HOSTNAME,
            cls.DEFAULT_CDN_BUCKET_NAME_PHOTO,
            str(picture_id))

    @classmethod
    def build_picture_url(cls, picture_id):
        """
        Return the Uniform Resource Locator of a place's picture (logo).


        :param picture_id: Identification of the logo of a place.


        :return: A string representing the Uniform Resource Locator of the
            picture.
        """
        return picture_id and os.path.join(
            settings.CDN_URL_HOSTNAME,
            cls.DEFAULT_CDN_BUCKET_NAME_LOGO,
            str(picture_id))

    def delete_place(
            self,
            place_id,
            account_id=None,
            connection=None):
        """
        Delete an existing place


        :param place_id: Identification of an existing place.

        :param account_id: Identification of the account of the user on behalf
            of whom the place is deleted.

        :param connection: An object `RdbmsConnection`.


        :raise DeletedObjectException: If this place has been deleted.

        :raise DisabledObjectException: If this place has been disabled.

        :raise IllegalAccessException: If the user is not the owner of this
            place.

        :raise UndefinedObjectException: If the place doesn't exist.
        """
        with self.acquire_rdbms_connection(auto_commit=True, connection=connection) as connection:
            place = self.get_place(place_id, check_status=True, connection=connection)

            if account_id and place.account_id != account_id:
                raise self.IllegalAccessException('The user is not the owner of this place')

            connection.execute(
                """
                UPDATE 
                    place
                  SET
                    object_status = %(OBJECT_STATUS_DELETED)s,
                    update_time = current_timestamp
                  WHERE
                    place_id = %(place_id)s
                """,
                {
                    'OBJECT_STATUS_DELETED': ObjectStatus.deleted,
                    'place_id': place_id
                }
            )

    def get_place(
            self,
            place_id,
            account_id=None,
            check_status=True,
            connection=None,
            include_address=False,
            include_contacts=False,
            include_geometries=False,
            include_photos=False,
            locale=DEFAULT_LOCALE):
        """
        Return the information about the specified place.


        :param place_id: Identification of the place to return information.

        :param account_id: Identification of the account of behalf of whom
            the function is called.  If defined, the function returns
            customized information that this user may have defined for this
            place.

        :param check_status: Indicate whether the function must check the
            current status of this place and raise an exception if it is not
            of enabled.

        :param connection: A `RdbmsConnection` instance to be used supporting
            the Python clause `with ...:`.

        :param include_address: Indicate whether to return the address
            information of this place.

        :param include_contacts: Indicate whether to return the contact
            information of this place.

        :param include_geometries: Indicate whether to return spatial data
            (geometries) related to this place, such as its boundaries and its
            pathway.

        :param include_photos: Indicate whether to return a first set of
            photos taken at this place.

        :param locale: An object `Locale` to return textual information of the
            place.


        :return: An instance containing the following attributes:

            * `account_id`: Identification of the account of the user who
              registered this place.

            * `agent_id`: Identification of the account of the official
              representative of this place, i.e., the user user who claimed
              this place.

            * `category`: The category qualifying the best this place.

            * `cover_photo_id`: Identification of the cover photo of the place,
              if any defined.

            * `cover_photo_url`: Uniform Resource Locator (URL) that specifies
              the location of the cover photo of the place, if any defined.

            * `place_id`: Identification of the place.

            * `team_id`: Identification of the organization that manages
              this place.

            * `timezone`: time zone of the location of the place.  It is the
              difference between the time at this location and UTC (Universal
              Time Coordinated). UTC is also  known as GMT or  Greenwich Mean
              Time or Zulu Time.

            * `object_status`: Current status of this place.

            * `creation_time`: Time when this place has been registered
              against the platform.

            * `update_time`: Time of the most recent modification of one or
              more attributes of this place.


        :raise DeletedObjectException: if the place has been deleted while the
            argument `check_status` has been set to `True`.

        :raise DisabledObjectException: if the place has been disabled while
            the argument `check_status` has been set to `True`.

        :raise UndefinedObjectException: if the specified identification
            doesn't refer to a place registered against the platform.
        """
        with self.acquire_rdbms_connection(auto_commit=False, connection=connection) as connection:
            cursor = connection.execute(
                """
                SELECT 
                    account_id,
                    accuracy,
                    agent_id,
                    ST_Z(location) AS altitude,
                    area_id,
                    ST_AsText(boundaries) AS boundaries,
                    cover_photo_id,
                    creation_time,
                    is_address_edited,
                    is_location_edited,
                    ST_Y(location) AS latitude,
                    ST_X(location) AS longitude,
                    object_status,
                    ST_AsText(pathway) AS pathway,
                    picture_id,
                    place_id,
                    radius,
                    reviewer_id,
                    team_id,
                    update_time,
                    visibility
                  FROM 
                    place
                  WHERE 
                    place_id = %(place_id)s
                    AND (object_status = %(OBJECT_STATUS_ENABLED)s
                         OR (object_status IN (%(OBJECT_STATUS_PENDING)s, %(OBJECT_STATUS_DISABLED)s)  
                             AND (account_id = %(account_id)s
                                  OR (team_id IS NOT NULL AND team_is_administrator(account_id, team_id)))))
                    AND (visibility = %(VISIBILITY_PUBLIC)s 
                         OR (visibility = %(VISIBILITY_PRIVATE)s AND account_id = %(account_id)s)
                         OR (visibility = %(VISIBILITY_TEAM)s
                             AND (account_id = %(account_id)s OR team_is_member(account_id, team_id))))
                """,
                {
                    'OBJECT_STATUS_DISABLED': ObjectStatus.disabled,
                    'OBJECT_STATUS_ENABLED': ObjectStatus.enabled,
                    'OBJECT_STATUS_PENDING': ObjectStatus.pending,
                    'VISIBILITY_PRIVATE': Visibility.private,
                    'VISIBILITY_PUBLIC': Visibility.public,
                    'VISIBILITY_TEAM': Visibility.team,
                    'account_id': account_id,
                    'place_id': place_id
                })

            row = cursor.fetch_one()
            if row is None:
                raise self.UndefinedObjectException(
                    "The specified place is not registered to the platform",
                    payload={'place_id': place_id})

            # Build the instance containing the information of the place.
            place = row.get_object({
                'account_id': cast.string_to_uuid,
                'cover_photo_id': cast.string_to_uuid,
                'creation_time': cast.string_to_timestamp,
                'agent_id': cast.string_to_uuid,
                'team_id': cast.string_to_uuid,
                'update_time': cast.string_to_timestamp,
                'place_id': cast.string_to_uuid })

            # Check whether the place is currently enable, and raise an exception
            # if not.
            if check_status:
                if place.object_status == ObjectStatus.disabled:
                    raise self.DisabledObjectException()
                elif place.object_status == ObjectStatus.deleted:
                    raise self.DeletedObjectException()

            # Build the Uniform Resource Locator (URL) of the place's cover photo,
            # if any.
            place.cover_photo_url = place.cover_photo_id and os.path.join(
                settings.CDN_URL_HOSTNAME,
                self.DEFAULT_CDN_BUCKET_NAME_PHOTO,
                str(place.cover_photo_id))

            # Build the geographical location of the place.
            if place.longitude and place.latitude:
                GeoPoint.objectify_attributes(place)

            if not include_geometries:
                del place.boundaries
                del place.pathway

            # Include the address information of the place in the required locale
            # if defined, or the default locale.
            if include_address:
                place.address = self.get_place_address(
                    place_id,
                    account_id=account_id,
                    connection=connection,
                    locale=locale)

            # Include the contacts information of the place, when required.
            if include_contacts:
                place.contacts = self.get_place_contacts(
                    place_id,
                    account_id=account_id,
                    connection=connection)

            # Include an initial set of photos of the place, when required.
            if include_photos:
                place.photos = self.__get_place_photos(
                    place_id,
                    account_id=account_id,
                    connection=connection)

            return place

    def get_place_address(
            self,
            place_id,
            account_id=None,
            connection=None,
            locale=None):
        """
        Return the components of the postal address of a place.


        :param place_id: Identification of the place to return information.

        :param account_id: Identification of the account of behalf of whom
            the function is called.  If defined, the function returns
            customized information that this user may have defined for this
            place.

        :param connection: A `RdbmsConnection` instance to be used supporting
            the Python clause `with ...:`.

        :param locale: An object `Locale` to return textual information of
            the place.


        :return: A dictionary where the key corresponds to an item of the
            enumeration `AddressComponentName` and the value corresponds to
            the address component's value.
        """
        with self.acquire_rdbms_connection(auto_commit=False, connection=connection) as connection:
            cursor = connection.execute(
                """
                SELECT 
                    account_id,
                    property_name,
                    property_value,
                    locale
                  FROM (
                    SELECT
                        account_id,
                        property_name,
                        property_value,
                        locale,
                        row_number() OVER (
                            PARTITION BY 
                                place_id,
                                property_name
                            ORDER BY 
                                compare_locale(locale, %(locale)s) DESC,
                                account_id NULLS LAST) AS position
                      FROM place_address
                      WHERE place_id = %(place_id)s
                        AND ((%(account_id)s IS NULL AND account_id IS NULL) OR
                             (%(account_id)s IS NOT NULL 
                              AND (account_id IS NULL OR account_id = %(account_id)s)))
                        AND (compare_locale(locale, %(locale)s) > 0 
                             OR compare_locale(locale, %(DEFAULT_LOCALE)s) > 0)) AS foo
                  WHERE position = 1
                """,
                {
                    'DEFAULT_LOCALE': DEFAULT_LOCALE,
                    'account_id': account_id,
                    'locale': locale or DEFAULT_LOCALE,
                    'place_id': place_id
                })

            # Build the dictionary of the address components registered for this
            # place.
            #
            # @todo: Do we need to also return the locale and the identification of the account?
            address = dict([
                (component.property_name, component.property_value)
                for component in [
                    row.get_object({
                        'account_id': cast.string_to_uuid,
                        'locale': cast.string_to_locale,
                        'property_name': AddressComponentName})
                    for row in cursor.fetch_all()
                ]
            ])

            return address

    def get_place_contacts(
            self,
            place_id,
            account_id=None,
            connection=None):
        """

        :param place_id:
        :param account_id:
        :param connection:
        :return:
        """
        with self.acquire_rdbms_connection(auto_commit=False, connection=connection) as connection:
            cursor = connection.execute(
                """
                SELECT 
                    *
                  FROM (
                    SELECT
                        property_name,
                        property_value,
                        visibility,
                        is_primary,
                        is_verified,
                        row_number() OVER (
                            PARTITION BY 
                                place_id, 
                                property_name
                            ORDER BY 
                                account_id NULLS LAST) AS position
                      FROM place_contact
                      WHERE place_id = %(place_ids)s
                        AND ((%(account_id)s IS NULL AND account_id IS NULL) OR
                             (%(account_id)s IS NOT NULL AND (account_id IS NULL OR account_id = %(account_id)s)))) AS foo
                    WHERE position = 1
                """,
                {
                    'account_id': account_id,
                    'place_id': place_id
                })

            contacts = [
                row.get_object({'visibility': Visibility})
                for row in cursor.fetch_all()
            ]

            return contacts

    def get_places(
            self,
            place_ids,
            account_id=None,
            connection=None,
            include_address=False,
            include_all_locales=False,
            include_contacts=False,
            include_geometries=False,
            include_photos=False,
            locale=DEFAULT_LOCALE):
        """
        Return extended information about the specified places.


        :param place_ids: A list of identifications of the places to return
            information.

        :param account_id: Identification of the account of behalf of whom
            the function is called.  If defined, the function returns
            customized information that this user may have defined for these
            places.

        :param connection: An object `RdbmsConnection` supporting the Python
            clause `with ...:`.

        :param include_address: Indicate whether to return the address
            information of each place.

        :param include_all_locales: Indicate to return the address of the
            places in all the available languages.

        :param include_contacts: Indicate whether to return the contact
            information of each place.

        :param include_geometries: Indicate whether to return spatial data
            (geometries) related to this place, such as its boundaries and its
            pathway.

        :param include_photos: Indicate whether to return a list of photos
            related to each place.

        :param locale: An object `Locale` to return textual information of
            each place.

        :return:
        """
        if not place_ids:
            return []

        with self.acquire_rdbms_connection(auto_commit=False, connection=connection) as connection:
            cursor = connection.execute(
                """
                SELECT
                    account_id,
                    accuracy,
                    agent_id,
                    ST_Z(location) AS altitude,
                    area_id,
                    ST_AsText(boundaries) AS boundaries,
                    cover_photo_id,
                    creation_time,
                    is_address_edited,
                    is_location_edited,
                    ST_Y(location) AS latitude,
                    ST_X(location) AS longitude,
                    object_status,
                    ST_AsText(pathway) AS pathway,
                    picture_id,
                    place_id,
                    radius,
                    reviewer_id,
                    team_id,
                    update_time,
                    visibility
                  FROM
                    place
                  WHERE
                    place_id IN (%(place_ids)s)
                """,
                {
                    'place_ids': place_ids
                })

            # @todo: convert "pathway" and "boundaries" into list of points.
            places = {
                place.place_id: place
                for place in [
                    row.get_object({
                        'account_id': cast.string_to_uuid,
                        'agent_id': cast.string_to_uuid,
                        'area_id': cast.string_to_uuid,
                        'cover_photo_id': cast.string_to_uuid,
                        'creation_time': cast.string_to_timestamp,
                        'object_status': ObjectStatus,
                        'picture_id': cast.string_to_uuid,
                        'place_id': cast.string_to_uuid,
                        'reviewer_id': cast.string_to_uuid,
                        'team_id': cast.string_to_uuid,
                        'update_time': cast.string_to_timestamp,
                        'visibility': Visibility
                    })
                    for row in cursor.fetch_all()
                ]
            }

            for place in places.values():
                if place.longitude and place.latitude:
                    GeoPoint.objectify_attributes(place)

                place.picture_url = place.picture_id and os.path.join(
                    settings.CDN_URL_HOSTNAME,
                    self.DEFAULT_CDN_BUCKET_NAME_LOGO,
                    str(place.picture_id))

                place.cover_photo_url = place.cover_photo_id and os.path.join(
                    settings.CDN_URL_HOSTNAME,
                    self.DEFAULT_CDN_BUCKET_NAME_PHOTO,
                    str(place.cover_photo_id))

                if not include_geometries:
                    del place.boundaries
                    del place.pathway

            # Retrieve the address information of the specified places, when
            # requested.
            if include_address:
                places_address = self.get_places_address(
                    place_ids,
                    account_id=account_id,
                    connection=connection,
                    include_all_locales=include_all_locales,
                    locale=locale)

                for place_id, place_address in places_address.items():
                    places[place_id].address = place_address

            # Retrieve the contact information of the specified places, when
            # requested.
            if include_contacts:
                places_contacts = self.get_places_contacts(
                    place_ids,
                    account_id=account_id,
                    connection=connection)

                for place_id, place_contacts in places_contacts.items():
                    places[place_id].contacts = place_contacts

            return list(places.values())

    def get_places_address(
            self,
            place_ids,
            account_id=None,
            connection=None,
            include_all_locales=False,
            locale=None):
        """
        Return the address information of a list of places.


        :param place_ids: List of identifications of the places to return the
            address information.

        :param account_id: Identification of the account of behalf of whom
            the function is called.  If defined, the function returns
            customized information that this user may have defined for this
            place.

        :param connection: An object `RdbmsConnection`.

        :param include_all_locales: Indicate whether to return the address of
            the places in all available languages.

        :param locale: An object `Locale` to return textual information of the
            place.


        :return: A dictionary of address information where a key corresponds
            to the identification of a place.

            If the argument `include_all_locales` is `False`, the value is a
            dictionary of address components where the key corresponds to an
            item of the enumeration `AddressComponentName` and the value is
            the string of this address component.

            If the argument `include_all_locales` is `True`, the value is a
            dictionary where the key is an object `Locale` and the value is
            a dictionary of address components.
        """
        with self.acquire_rdbms_connection(auto_commit=False, connection=connection) as connection:
            if include_all_locales:
                cursor = connection.execute(
                    """
                    SELECT 
                        account_id,
                        locale,
                        place_id,
                        property_name,
                        property_value
                      FROM 
                        place_address
                      WHERE
                        place_id IN (%(place_ids)s)
                        AND ((%(account_id)s IS NULL AND account_id IS NULL) 
                             OR (%(account_id)s IS NOT NULL 
                                 AND (account_id IS NULL OR account_id = %(account_id)s)))
                    """,
                    {
                        'account_id': account_id,
                        'place_ids': place_ids
                    })
            else:
                cursor = connection.execute(
                    """
                    SELECT 
                        account_id,
                        locale,
                        place_id,
                        property_name,
                        property_value
                      FROM (
                        SELECT 
                            place_id,
                            account_id,
                            property_name,
                            property_value,
                            locale,
                            row_number() OVER (
                              PARTITION BY 
                                place_id,
                                property_name
                              ORDER BY
                                compare_locale(locale, %(locale)s) DESC,
                                account_id NULLS LAST) AS position
                          FROM
                            place_address
                          WHERE
                            place_id IN (%(place_ids)s)
                            AND ((%(account_id)s IS NULL AND account_id IS NULL) 
                                 OR (%(account_id)s IS NOT NULL 
                                     AND (account_id IS NULL OR account_id = %(account_id)s)))
                            AND (compare_locale(locale, %(locale)s) > 0 
                                 OR compare_locale(locale, %(DEFAULT_LOCALE)s) > 0)) AS foo
                        WHERE
                          position = 1
                    """,
                    {
                        'DEFAULT_LOCALE': DEFAULT_LOCALE,
                        'account_id': account_id,
                        'locale': locale or DEFAULT_LOCALE,
                        'place_ids': place_ids
                    })

            addresses = [
                row.get_object({
                    'account_id': cast.string_to_uuid,
                    'locale': cast.string_to_locale,
                    'place_id': cast.string_to_uuid
                })
                for row in cursor.fetch_all()
            ]

            if include_all_locales:
                places_address = collections.defaultdict(dict)
                for address in addresses:
                    if places_address[address.place_id].get(address.locale) is None:
                        places_address[address.place_id][address.locale] = {}
                    places_address[address.place_id][address.locale][address.property_name] = address.property_value
            else:
                places_address = collections.defaultdict(dict)
                for address in addresses:
                    places_address[address.place_id][address.property_name] = address.property_value

            return places_address

    def get_places_contacts(
            self,
            place_ids,
            account_id=None,
            connection=None):
        """
        Return the contact information of a list of places.


        :param place_ids: List of identifications of the places to return the
            contact information.

        :param account_id: Identification of the account of behalf of whom
            the function is called.  If defined, the function returns
            customized information that this user may have defined for this
            place.

        :param connection: An object ``RdbmsConnection`` supporting the Python
            clause ``with ...:``, or ``None``.


        :return: A dictionary of contact information where a key corresponds
            to the identification of a place, and the value is a dictionary of
            contact information.
        """
        with self.acquire_rdbms_connection(auto_commit=False, connection=connection) as connection:
            cursor = connection.execute(
                """
                SELECT *
                  FROM (
                    SELECT 
                        place_id,
                        property_name,
                        property_value,
                        is_primary,
                        is_verified,
                        row_number() OVER (
                          PARTITION BY
                            place_id, 
                            property_name
                          ORDER BY
                            account_id NULLS LAST) AS position
                      FROM
                        place_contact
                      WHERE
                        place_id IN (%[place_ids]s)
                        AND ((%(account_id)s IS NULL AND account_id IS NULL) 
                             OR (%(account_id)s IS NOT NULL 
                                 AND (account_id IS NULL OR account_id = %(account_id)s)))) AS foo
                  WHERE position = 1
                """,
                {
                    'account_id': account_id,
                    'place_ids': place_ids
                })

            contacts = [
                row.get_object({'place_id': cast.string_to_uuid})
                for row in cursor.fetch_all()
            ]

            places_contacts = collections.defaultdict(dict)
            for contact in contacts:
                places_contacts[contact.place_id][contact.property_name] = contact.property_value

            return places_contacts

    def index_all_places(self, connection=None):

        """
        Reindex all the places


        :note: This function MUST NOT be surfaced to any client applications,
            but called from Python terminal as follows:

            ```bash
            $ python
            Python 3.7.4 (default, Jul 12 2019, 18:26:19)
            [GCC 5.4.0 20160609] on linux
            Type "help", "copyright", "credits" or "license" for more information.
            >>> from majormode.mercurius.service.place.place_service import PlaceService
            >>> PlaceService().index_all_places()
            ```

        :todo: This function SHOULD be replaced with the use of another
            technology such as Elasticsearch more suitable for indexing and
            indexing data.


        :param connection: An object `RdbmsConnection` with auto commit.
        """
        with self.acquire_rdbms_connection(auto_commit=True, connection=connection) as connection:
            cursor = connection.execute(
                """
                SELECT
                    place_id
                  FROM ONLY
                    place
                  WHERE 
                    object_status <> %(OBJECT_STATUS_DELETED)s
                """,
                {
                    'OBJECT_STATUS_DELETED': ObjectStatus.deleted,
                }
            )

            place_ids = [
                row.get_value('place_id', cast.string_to_uuid)
                for row in cursor.fetch_all()
            ]

            for place_id in place_ids:
                self.__index_place(place_id, connection=connection)

    def search_places(
            self,
            account_id: uuid.UUID = None,
            area_id: uuid.UUID = None,
            area_level: int = None,
            bounding_box: BoundingBox = None,
            categories=None,
            client_ip_address: Tuple[int, int, int,int] = None,
            connection: RdbmsConnection = None,
            include_address: bool = False,
            include_contacts: bool = False,
            include_photos: bool = False,
            intent: SearchIntent = None,
            keywords=None,
            limit: int = None,
            locale: Locale = None,
            location: GeoPoint = None,
            offset: int = None,
            radius: float = None):
        """
        Search a list of places corresponding to the specified criteria


        :param account_id: The account identification of a user of behalf of
            whom this search is initiated.

        :param area_id: The identification of an administrative subdivision to
            search for place.

        :param area_level: The level of the administrative subdivision to
            return a list of schools.  By default, it corresponds to a country
            level.  This argument is used when the argument `location` is
            passed to this function.

        :param bounding_box: An object `BoundingBox` that represent the
            rectangle area to search for places.

        :param categories: A category or a list of categories that indicate
            the particular use that places to return.

        :param client_ip_address: IPv4 address of the machine of the user.  It
            corresponds to a tuple consisting of four decimal numbers, each
            ranging from `0` to `255`.  The IP address is used to identify the
            geographical location of the user.

        :param connection: An object `RdbmsConnection`.

        :param include_address: Indicate whether to include the address
            information of the places returned.

        :param include_contacts: Indicate whether to include the contacts
            information of the places returned.

        :param include_photos: Indicate whether to include a limited set of
            photos associated to the places that are returned.

        :param intent: An item of the enumeration `SearchItent` that indicates
            the intent in performing the search.

        :param keywords: A list of keywords to search places for.

        :param limit: Constrain the number of places that are returned to the
            specified number.  If not specified, the default value is
            `BaseService.DEFAULT_LIMIT`.  The maximum value is
            `BaseService.MAXIMUM_LIMIT`.

        :param locale: An object `Locale` in which to return the places'
            textual information.  If not specified, the default value is
            `Locale.DEFAULT_LOCALE`.

        :param location: An object `GeoPoint` of the geographical location
            to search nearby places.  The function uses the argument `radius`
            to define the search area.

        :param offset: Require to skip that many places before beginning to
            return them.  If both `limit` and `offset` are specified, then
            `offset` places are skipped before starting to count the `limit`
            places that are returned.  The default value is `0`.

        :param radius: Maximal distance in meters of the radius of search for
            places nearby.  The center of the search area is either defined
            by the argument `location`, either the location corresponding to
            the IP address of the user as defined by the argument
            `client_ip_address`.


        :return: A list of objects containing the following attributes:

            * `address` (optional): The postal address of the place.  The address
              is represented with a dictionary.  The key corresponds to an item of
              the enumeration `AddressComponentName`.  The value is the textual
              information of this component, written in the specified locale when
              available, or in the default locale.

            * `category` (optional): The code name of a category qualifying the
              place.

            * `contacts` (optional): A list of objects `Contact`.

            * `location` (required): An object `GeoPoint` of the place (e.g., main
              entrance)

            * `picture_id` (optional): The identification of the place's logo
              picture.

            * `picture_url` (optional): The Uniform Resource Locator (URL) that
              specifies the location of the place's logo picture.

            * `place_id` (required): The identification of the place.

            * `score` (optional): An estimation of the probability that the place is
              relevant to the search, given the intent.  A perfect precision score
              of `1.0` means that the place returned is totally relevant.  This
              value is only returned if the intent of the search is `checkin` or
              `social`.

            * `update_time` (required): The time of the most recent modification of
              one or more attributes of this place.


        :raise InvalidArgumentException: if no location has been found
            arguments `area_id`, `location`, `bounding_box`, or
            `client_ip_address`, has been passed to this function.
        """
        # Validate arguments.
        if bounding_box and not isinstance(bounding_box, BoundingBox):
            raise ValueError("The argument 'bounding_box' MUST be an instance of 'BoundingBox'")

        if location and not isinstance(location, GeoPoint):
            raise ValueError("The argument 'location' MUST be an instance of 'GeoPoint'")

        if keywords:
            if not isinstance(keywords, (list, set, tuple)):
                raise ValueError("The argument 'keywords' MUST be a list, a set, or a tuple")
            if any(not isinstance(keyword, str) for keyword in keywords):
                raise ValueError("The element of the argument 'keywords' MUST be strings")
            keywords = string_util.string_to_keywords(keywords, keyword_minimal_length=2)

        if not isinstance(categories, (list, set, tuple)):
            categories = [categories]

        # Determine which argument need to be used to filter places within a
        # geographical area:
        #
        # 1. The identification of an administrative subdivision `area_id`
        # 2. The location of a geographical area:
        #    2.1. A circle defined with a center `location` and a `radius`
        #    2.2. An administrative subdivision of level `area_level` that contains
        #         the given `location`
        # 3. An administrative subdivision of level `area_level` that contains
        #    the location corresponding to the `client_ip_address`
        if area_id:
            location = None  # Clear this argument if defined to avoid conflict
        elif location:
            if area_level is not None and not radius:
                area_id = self.__find_area_with_location(
                    location,
                    area_level=area_level,
                    locale=locale)
                if area_id:
                    location = None  # Disable this search criteria
        elif client_ip_address:
            area = self.__find_area_with_ip_address(
                client_ip_address,
                area_level=area_level,
                locale=locale)
            if area is not None:
                area_id = area.area_id

        if not area_id and not location:
            raise ValueError('No geographical restriction is defined to filter places')

        # Find places that correspond to the specified criteria.
        with self.acquire_rdbms_connection(connection=connection) as connection:
            if keywords:
                cursor = connection.execute(
                    """
                    SELECT
                        place_id,
                        COUNT(*) AS score
                      FROM 
                        place_index
                      INNER JOIN place
                        USING (place_id)
                      WHERE keyword ~ %(keywords)s
                        AND (%(categories)s IS NULL OR category IN (%(categories)s))
                        AND (object_status = %(OBJECT_STATUS_ENABLED)s
                             OR (object_status = %(OBJECT_STATUS_PENDING)s AND account_id = %(account_id)s))
                        AND ((%(longitude)s IS NULL AND %(area_id)s IS NULL)
                             OR (%(longitude)s IS NOT NULL AND ST_Distance_Sphere(
                                     location,
                                     ST_SetSRID(ST_MakePoint(%(longitude)s, %(latitude)s), 4326)) <= %(radius)s)
                             OR (%(area_id)s IS NOT NULL AND ST_Contains(get_area_boundaries(%(area_id)s), location)))
                      GROUP BY 
                        place_id
                      ORDER BY
                        score DESC,
                        place_id ASC
                      LIMIT %(limit)s
                      OFFSET %(offset)s
                    """,
                    {
                        'OBJECT_STATUS_ENABLED': ObjectStatus.enabled,
                        'OBJECT_STATUS_PENDING': ObjectStatus.pending,
                        'account_id': account_id,
                        'area_id': area_id,
                        'categories': categories,
                        'keywords': keywords and '|'.join(keywords),
                        'latitude': location and location.latitude,
                        'limit': min(limit or self.DEFAULT_LIMIT, self.MAXIMUM_LIMIT),
                        'longitude': location and location.longitude,
                        'offset': offset or 0,
                        'radius': min(radius or self.DEFAULT_SEARCH_RADIUS, self.MAXIMAL_SEARCH_RADIUS)
                    })
            else:
                cursor = connection.execute(
                    """
                    SELECT
                        place_id
                      FROM 
                        place
                      WHERE (%(categories)s IS NULL OR category IN (%(categories)s))
                        AND (object_status = %(OBJECT_STATUS_ENABLED)s
                             OR (object_status = %(OBJECT_STATUS_PENDING)s AND account_id = %(account_id)s))
                        AND ((%(longitude)s IS NOT NULL 
                              AND ST_Distance_Sphere(
                                  location,
                                  ST_SetSRID(ST_MakePoint(%(longitude)s, %(latitude)s), 4326)) <= %(radius)s)
                             OR (%(area_id)s IS NOT NULL 
                                 AND ST_Contains(get_area_boundaries(%(area_id)s), location)))                      
                      ORDER BY
                        place_id DESC
                      LIMIT %(limit)s
                      OFFSET %(offset)s
                    """,
                    {
                        'OBJECT_STATUS_ENABLED': ObjectStatus.enabled,
                        'OBJECT_STATUS_PENDING': ObjectStatus.pending,
                        'account_id': account_id,
                        'area_id': area_id,
                        'categories': categories,
                        'latitude': location and location.latitude,
                        'limit': min(limit or self.DEFAULT_LIMIT, self.MAXIMUM_LIMIT),
                        'longitude': location and location.longitude,
                        'offset': offset or 0,
                        'radius': min(radius or self.DEFAULT_SEARCH_RADIUS, self.MAXIMAL_SEARCH_RADIUS)
                    })

            places_dict = {
                place.place_id: place
                for place in [
                    row.get_object({
                        'place_id': cast.string_to_uuid,
                    })
                    for row in cursor.fetch_all()
                ]
            }

            places = self.get_places(
                list(places_dict.keys()),
                account_id=account_id,
                connection=connection,
                include_address=include_address,
                include_contacts=include_contacts,
                include_photos=include_photos,
                locale=locale)

            # for place in places:
            #     place.score = places_dict[place.place_id].score

            return places

#             # if intent == SearchIntent.checkin:
#             #     connection.execute("""
#             #         INSERT INTO _place_search_history_(
#             #                         imei,
#             #                         device_model,
#             #                         os_version,
#             #                         location,
#             #                         accuracy,
#             #                         place_id)
#             #           VALUES (%(imei)s,
#             #                   %(device_model)s,
#             #                   %(os_version)s,
#             #                   ST_SetSRID(ST_MakePoint(%(longitude)s, %(latitude)s, %(altitude)s), 4326),
#             #                   %(accuracy)s,
#             #                   %(place_id)s)""",
#             #         { 'accuracy': location.accuracy,
#             #           'altitude': location.altitude or 0,
#             #           'device_model': _device_model_,
#             #           'imei': _imei_,
#             #           'latitude': location.latitude,
#             #           'longitude': location.longitude,
#             #           'os_version': _os_version_,
#             #           'place_id': places.values()[0].place_id if len(places.values()) > 0 else None })

    def update_place(
            self,
            place_id,
            account_id,
            address=None,
            check_status=False,
            connection=None,
            is_address_edited=False,
            is_location_edited=False,
            locale=None,
            location=None):
        """
        Update the information about an existing place.


        :param place_id: Identification of a place.

        :param account_id: Identification of the account of the user who
            updates the place's information.

        :param address: A dictionary of address components where the key
            corresponds to an item of the enumeration `AddressComponentName`.

        :param check_status: Indicate whether the chech the current status of
            the place.

        :param connection: An object `RdbmsConnection`.

        :param is_address_edited: Indicate whether the user has manually
            edited the address, or whether a reverse geocoder has
            automatically provided this address.

        :param is_location_edited: Indicate whether the location has been
            manually edited by the user, more likely by dragging/dropping a
            marker on an electronic map, or whether the device of the user has
            detected the user's current location or a geocoder has converted
            the formatted address of this place to a location.

        :param locale: An object `Locale` defining the language which the
            textual information of the address component is written in.

        :param location: An object `GeoPoint` representing the geographical
            location of the place's location (e.g., main entrance).


        :return: An object containing the following attributes:

            * `object_status` (required): Current status of the place.

            * `place_id` (required): Identification of the place.

            * `update_time` (required): Time of the most recent modification of the
              place's information.
        """
        with self.acquire_rdbms_connection(auto_commit=True, connection=connection) as connection:
            cursor = connection.execute(
                """
                UPDATE  
                    place
                  SET
                    is_address_edited = %(is_address_edited)s,
                    is_location_edited = %(is_location_edited)s,
                    location = ST_SetSRID(ST_MakePoint(%(longitude)s, %(latitude)s, %(altitude)s), 4326)
                  WHERE 
                    place_id = %(place_id)s
                    AND account_id = %(account_id)s
                  RETURNING
                    object_status,
                    place_id,
                    update_time
                """,
                {
                    'account_id': account_id,
                    'altitude': location.altitude or 0,
                    'is_address_edited': is_address_edited,
                    'is_location_edited': is_location_edited,
                    'latitude': location.latitude,
                    'longitude': location.longitude,
                    'place_id': place_id,
                }
            )

            row = cursor.fetch_one()
            if row is None:
                raise self.UndefinedObjectException("The place doesn't exist")

            place = row.get_object({
                'object_status': ObjectStatus,
                'place_id': cast.string_to_uuid,
                'update_time': cast.string_to_timestamp,
            })

            if check_status:
                if place.object_status == ObjectStatus.deleted:
                    raise self.DeletedObjectException("The place has been deleted")
                elif place.object_status == ObjectStatus.disabled:
                    raise self.DisabledObjectException("The place has been disabled")

            if address:
                self.__update_place_address(
                    place_id,
                    address,
                    account_id=account_id,
                    connection=connection,
                    locale=locale)

            return place

    def upload_logo(
            self,
            place_id,
            account_id,
            logo_file,
            connection=None,
            image_file_format=DEFAULT_LOGO_IMAGE_FILE_FORMAT,
            image_quality=DEFAULT_LOGO_IMAGE_QUALITY,
            image_minimal_size=DEFAULT_LOGO_IMAGE_MINIMAL_SIZE):
        """
        Upload the new logo image of a place


        :param place_id: Identification of a place.

        :param account_id: Identification of the account of an administrator
            of the place who is uploading an image as the logo of his place.

        :param logo_file: An object `HttpRequest.HttpRequestUploadedFile`.

        :param connection: An object `RdbmsConnection` supporting the Python
            clause `with ...:`.

        :param image image_file_format: Image file format to store the image
            of the team's logo {@link https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html}.

        :param image_quality: Quality to store the image of the team's logo
            with, on a scale from `1` (worst) to `95` (best).  Values above
            `95` should be avoided; `100` disables portions of the JPEG
            compression algorithm, and results in large files with hardly any
            gain in image quality.

        :param image_minimal_size: A tuple `width, height` representing the
            minimal size of the image of a team's logo.


        :return: An object containing the following members:

            * `file_name` (required): Original local file name as the `filename`
              parameter of the `Content-Disposition` header.

            * `picture_id` (required): Identification of the new image of the team's
              logo.

            * `picture_url` (required): Uniform Resource Locator (URL) that
              specifies the location of the new image of the team's logo.

            * `update_time` (required): Time of the most recent modification of
              the properties of the team.


        :raise DeletedObjectException: If the place has been deleted.

        :raise DisabledObjectException: If the place has been disabled.

        :raise IllegalAccessException: If the user on behalf of whom the
            function is called is not an administrator of the place.

        :raise InvalidArgumentException: If the format of the image is not
            supported, or if the size of the image is too small.

        :raise UndefinedObjectException: If the place doesn't exist.
        """
        # Check whether the user has sufficient privileges to change the logo of
        # this place:
        #
        # - The user is the agent of the place
        # - The user is an administrator of the organization that managers the
        #   place
        place = self.get_place(place_id)
        if account_id != place.account_id:
            if place.team_id is None:
                raise self.IllegalAccessException("Only the owner of this place can change the logo of this place")

            TeamService().assert_member_role(account_id, place.team_id, MemberRole.administrator)

        # Retrieve the pixel resolution of the photo image, and check whether
        # it respects the minimal size required.
        image = self.__load_image_from_bytes(logo_file.data)
        self.__validate_image_size(image, image_minimal_size)
        image_width, image_height = image.size

        # Determine the signature and the size of the data of the uploaded photo
        # image.
        image_file_checksum = hashlib.md5(logo_file.data).hexdigest()
        image_file_size = len(logo_file.data)

        # Generate the identification of the photo.
        picture_id = uuid.uuid1()

        # Set this image as the new logo of this team.  The function checks
        # whether this same image has not been already set for this team (same
        # image data checksum and same image binary size).
        with self.acquire_rdbms_connection(auto_commit=True, connection=connection) as connection:
            cursor = connection.execute(
                """
                UPDATE
                    place
                  SET
                    image_height = %(image_height)s,
                    image_file_checksum = %(image_file_checksum)s,
                    image_file_size = %(image_file_size)s,
                    image_width = %(image_width)s,
                    picture_id = %(picture_id)s,
                    update_time = current_timestamp
                  WHERE
                    place_id = %(place_id)s
                    AND (image_file_checksum IS NULL OR image_file_checksum <> %(image_file_checksum)s)
                    AND (image_file_size IS NULL OR image_file_size <> %(image_file_size)s)
                  RETURNING
                    picture_id,
                    place_id,
                    update_time
                """,
                {
                    'image_height': image_height,
                    'image_file_checksum': image_file_checksum,
                    'image_file_size': image_file_size,
                    'image_width': image_width,
                    'picture_id': picture_id,
                    'place_id': place_id,
                })

            row = cursor.fetch_one()
            if row is None:
                raise self.InvalidOperationException("This logo has been already set for this place")

            # Retrieve the properties of the team's logo.
            logo = row.get_object({
                'picture_id': cast.string_to_uuid,
                'place_id': cast.string_to_uuid,
                'update_time': cast.string_to_timestamp,
            })

            # Add the URL link to access this picture and the original file name
            # that was uploaded.
            logo.picture_url = self.build_picture_url(logo.picture_id)
            logo.file_name = logo_file.file_name

            # Store the photo image file in the temporary directory of the local
            # Network File System (NFS).  This file will be read by background task
            # for additional processing.
            self.__store_logo_image_file(
                picture_id,
                image,
                image_file_format=image_file_format,
                image_quality=image_quality)

        return logo






























    # def get_distance(
    # self, place_id, location,
    #         connection=None):
    #     """
    #     Return the linear distance in meters between the place and the
    #     specified location.  The function uses a spherical earth and radius
    #     of 6370986 meters
    #
    #     If the place is defined a boundary, the function returns the linear
    #     distance between the closest point and the specified location,
    #     otherwise it returns the linear distance between the centroid location
    #     of the place and the specified location.
    #
    #
    #     :param place_id: identification of a place.
    #
    #     :param location: the geographical location to return the distance from
    #         the place.
    #
    #     :param connection: a `RdbmsConnection` instance to be used         supporting the Python clause `with ...:`.
    #
    #
    #     :return: the linear distance in meters between the place and the
    #         specified location.
    #     """
    #     with self.acquire_rdbms_connection(auto_commit=True, connection=connection) as connection:
    #         cursor = connection.execute("""
    #             SELECT ST_Distance_Sphere(
    #                      COALESCE(ST_3DClosestPoint(boundaries, ST_SetSRID(ST_MakePoint(%(longitude)s, %(latitude)s, %(altitude)s), 4326)),
    #                               location),
    #                      ST_SetSRID(ST_MakePoint(%(longitude)s, %(latitude)s, %(altitude)s), 4326)) AS distance
    #               FROM place
    #               WHERE place_id = %(place_id)s
    #                 AND object_status = %(OBJECT_STATUS_ENABLED)s""",
    #             {'OBJECT_STATUS_ENABLED': ObjectStatus.enabled,
    #              'altitude': location.altitude,
    #              'latitude': location.latitude,
    #              'longitude': location.longitude,
    #              'place_id': place_id})
    #
    #         row = cursor.fetch_one()
    #         if row is None:
    #             raise self.UndefinedObjectException('The specified identificartion does not refer to a place registered to the platform',
    #                     payload={ 'place_id': place_id })
    #
    #         return row.get_value('distance')




#     # def sync_place(self, app_id, account_id, place,
#     #         optimistic_match=False,
#     #         team_id=None,
#     #         visibility=Visibility.public):
#     #     with self.acquire_rdbms_connection(True) as connection:
#     #         #     cursor = connection.execute("""
#     #         #         SELECT place_id
#     #         #           FROM place
#     #         #           WHERE (boundaries IS NOT NULL AND %(boundaries_defined)s
#     #         #                  AND ST_Intersects(boundaries, ST_MakePolygon(ST_GeomFromText('LINESTRING(%s)', 4326))""",
#     #         #
#     #         #         { 'boundaries_defined': place.boundaries is not None,
#     #         #           (True, ','.join([ '%s %s %s' % (longitude, latitude, altitude)
#     #         #                         for (longitude, latitude, altitude) in place.boundaries ])),
#     #
#     #
#     #         cursor = connection.execute("""
#     #             INSERT INTO place(
#     #                     account_id,
#     #                     team_id,
#     #                     location,
#     #                     boundaries)
#     #               VALUES (%(account_id)s,
#     #                       %(team_id)s,
#     #                       ST_SetSRID(ST_MakePoint(%(longitude)s, %(latitude)s, %(altitude)s), 4326),
#     #                       ST_MakePolygon(ST_GeomFromText(%(boundaries)s, 4326)))
#     #               RETURNING place_id,
#     #                         update_time""",
#     #             { 'account_id': account_id,
#     #               'altitude': place.location and place.location.altitude,
#     #               'boundaries': 'LINESTRING(%s)' % ','.join([ '%s %s %s' % (longitude, latitude, altitude)
#     #                     for (longitude, latitude, altitude) in place.boundaries ]),
#     #               'latitude': place.location and place.location.latitude,
#     #               'longitude': place.location and place.location.longitude,
#     #               'team_id': team_id })
#     #
#     #         result = cursor.fetch_one().get_object({
#     #                 'place_id': cast.string_to_uuid,
#     #                 'update_time': cast.string_to_timestamp })
#     #
#     #         if place.address:
#     #             if isinstance(place.address, dict):
#     #                 values = [ (result.place_id, account_id, locale, property_name, property_value)
#     #                         for property_name, property_value in place.address.iteritems() ]
#     #             else:
#     #                 values = [ (result.place_id, account_id, address[AddressComponentName.locale], property_name, property_value)
#     #                         for address in place.address
#     #                             for property_name, property_value in address.iteritems()
#     #                                 if property_name != AddressComponentName.locale ]
#     #
#     #             connection.execute("""
#     #                 INSERT INTO place_address(
#     #                         place_id,
#     #                         account_id,
#     #                         locale,
#     #                         property_name,
#     #                         property_value)
#     #                   VALUES %[values]s""",
#     #                { 'values': values })
#     #
#     #         if place.contacts:
#     #             connection.execute("""
#     #                 INSERT INTO place_contact(
#     #                         place_id,
#     #                         property_name,
#     #                         property_value,
#     #                         is_primary,
#     #                         is_verified)
#     #                   VALUES %[values]s""",
#     #                 { 'values': [ (result.place_id, property_type, property_value, is_primary, is_verified)
#     #                         for (property_type, property_value, is_primary, is_verified) in place.contacts ] })
