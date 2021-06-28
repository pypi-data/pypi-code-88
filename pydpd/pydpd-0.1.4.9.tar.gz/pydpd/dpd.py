import os.path
import secrets

from PIL import Image
import cv2
import pdfkit
import requests
import base64
import datetime
import pickle
import tempfile
import functools
import imgkit


def build_xml(user, password, con):
    return f"""<?xml version="1.0" encoding="UTF-8"?>
    <trackingrequest>
    <user>{user}</user>
    <password>{password}</password>
    <trackingnumbers>
    <trackingnumber>{con}</trackingnumber>
    </trackingnumbers>
    </trackingrequest>"""




class Address:

    def __init__(self, *args, **kwargs):
        """
        Base class for address into DPD class for label generation

        Available fields:
            name: STR
            tel: STR
            email: STR
            organisation: STR
            address1: STR
            address2: STR
            address3: STR
            address4: STR
            postcode : STR

        Must has minimum of:
            name
            address1
            address2
            postcode

        """
        self.name = kwargs.get("name", "")
        self.tel = kwargs.get("tel", "")
        self.email = kwargs.get("email", "")
        self.organisation = kwargs.get("organisation", "")
        self.address_1 = kwargs.get("address1", "")
        self.address_2 = kwargs.get("address2", "")
        self.address_3 = kwargs.get("address3", "")
        self.address_4 = kwargs.get("address4", "")
        self.postcode = kwargs.get("postcode", "")

        if len(self.address_1) == 0:
            raise Exception("Delivery address line 1 missing")
        elif len(self.address_2) == 0:
            raise Exception("Delivery address line 2 missing")
        elif len(self.postcode) == 0:
            raise Exception("Delivery postcode missing")
        elif len(self.name) == 0:
            raise Exception("Delivery name missing")

    def __str__(self):
        return f"<Address {self.name}, {self.address_1}, {self.address_2}>"

    def __repr__(self):
        return self.__str__()


class Parcel(Address):
    """

    """

    def __init__(self, *args, **kwargs):
        """
        Order object to be passed into DPD class for label generation

        Available fields:
            name: STR
            tel: STR
            email: STR
            organisation: STR
            address1: STR
            address2: STR
            address3: STR
            address4: STR
            postcode : STR
            shipping ref: STR
            delivery instructions: STR
            email_updates: BOOL
            telephone_updates: BOOL
            weight: FLOAT
            pcs: INT

        Must has minimum of:
            address1
            address2
            postcode
            wight
            pcs

        By default allows communication from DPD via both email and telephone
        """
        self.shipping_ref = kwargs.get("shipping_ref", "")
        self.delivery_instructions = kwargs.get("instructions", "")
        self.email_updates = kwargs.get("email_updates", True)
        self.telephone_updates = kwargs.get("telephone_updates", True)
        self.weight = kwargs.get("weight", 1)
        self.pcs = kwargs.get("pcs", 1)
        super().__init__(*args, **kwargs)

class Tracking:
    def __init__(self, consignment):
        """

        """


class Delivery:
    """

    """

    def __init__(self, parcel, service, req, dpd):
        self.parcel = parcel
        self.service = service
        self.shipment_id = req.json()["data"]["shipmentId"]
        self.consignment = req.json()["data"]["consignmentDetail"][0]["consignmentNumber"]
        self.parcels = [x for x in req.json()["data"]["consignmentDetail"][0]["parcelNumbers"]]
        self._dpd = dpd

    def __str__(self):
        return f"<Delivery : consignment: {self.consignment} - weight: {self.parcel.weight}kg - pcs: {self.parcel.pcs} - name: {self.parcel.name}>"

    def __repr__(self):
        return self.__str__()

    @property
    def address(self):
        """

        :return:
        """
        return f"{self.parcel.name}\n{self.parcel.organisation}\n{self.parcel.address_1}\n{self.parcel.address_2}\n{self.parcel.address_3}\n{self.parcel.address_4}\n{self.parcel.postcode}".replace(
            "\n\n", "\n").replace("\n\n", "\n")

    @property
    def service_name(self):
        """Returns the service name from service code"""
        services = {'1^01': 'Parcel Sunday',
                    '1^06': 'Freight Parcel Sunday',
                    '1^08': 'Pallet Sunday',
                    '1^09': 'Expresspak Sunday',
                    '1^11': 'Dpd Two Day',
                    '1^12': 'Dpd Next Day',
                    '1^13': 'Dpd 12:00',
                    '1^14': 'Dpd 10:30',
                    '1^16': 'Parcel Saturday',
                    '1^17': 'Parcel Saturday 12:00',
                    '1^18': 'Parcel Saturday 10:30',
                    '1^22': 'Parcel Return To Shop',
                    '1^29': 'Parcel Sunday 12:00',
                    '1^31': 'Freight Parcel Sunday 12:00',
                    '1^32': 'Expresspak Dpd Next Day',
                    '1^33': 'Expresspak Dpd 12:00',
                    '1^34': 'Expresspak Dpd 10:30',
                    '1^36': 'Expresspak Saturday',
                    '1^37': 'Expresspak Saturday 12:00',
                    '1^38': 'Expresspak Saturday 10:30',
                    '1^51': 'Expresspak Sunday 12:00',
                    '1^69': 'Pallet Sunday 12:00',
                    '1^71': 'Pallet Dpd Two Day',
                    '1^72': 'Pallet Dpd Next Day',
                    '1^73': 'Pallet Dpd 12:00',
                    '1^74': 'Pallet Dpd 10:30',
                    '1^76': 'Pallet Saturday',
                    '1^77': 'Pallet Saturday 12:00',
                    '1^78': 'Pallet Saturday 10:30',
                    '1^81': 'Freight Parcel Dpd Two Day',
                    '1^82': 'Freight Parcel Dpd Next Day',
                    '1^83': 'Freight Parcel Dpd 12:00',
                    '1^84': 'Freight Dpd 10:30',
                    '1^86': 'Freight Parcel Saturday',
                    '1^87': 'Freight Parcel Saturday 12:00',
                    '1^88': 'Freight Parcel Saturday 10:30',
                    '1^91': 'Parcel Ship To Shop',
                    '1^98': 'Expak - Pickup Classic'}

        return services[self.service]

    def get_label(self, out_type=1):
        """
        Gets the raw label data in either HTML or
        :param out_type:  1= html, 2= citizen-clp, 3= eltron-epl
        :return: data
        """
        return self._dpd._get_label(self, out_type)

    def save_pdf_label(self, out_path=None, filename=None, margins=[20, 20, 20, 20], paper_size="A4", zoom=1):
        """
        generates a PDF version of the label, beware this is fairly slow. Around 1 second+

        :param out_path: the output path for the pdf to be saved in
        :param filename: the filename of the pdf. If none supplied then a random filename will be generated and returned.
        :param margins: top, right, bottom, left margins in mm. Can be used to tweak the position of the label on the page
        :param paper_size: default A4
        :param zoom: default 1  - no zoom  NOT WORKING CURRENTLY
        :return: output path string
        """

        # check path
        if not out_path:
            out_path = "./"

        if not os.path.isdir(out_path):
            raise Exception("Out path not valid")

        # create filename if not found
        if not filename:
            filename = secrets.token_urlsafe(10) + ".pdf"

        # get final path
        final_path = out_path + "/" if out_path[-1] != "/" else "" + filename

        # convert margins to inches
        margins = [x / 25.4 for x in margins]

        # get wkhtmltopdf options
        options = {'page-size': paper_size,
                   'margin-top': f'{margins[0]}in',
                   'margin-right': f'{margins[1]}in',
                   'margin-bottom': f'{margins[2]}in',
                   'margin-left': f'{margins[3]}in',
                   '--quiet': '',
                   'zoom': zoom,
                   }

        css = """<style>
                   div{font-family: Arial, Helvetica, sans-serif;}
                   p{font-family: Arial, Helvetica, sans-serif;}
                   body{font-family: Arial, Helvetica, sans-serif;}
                 </style>
        """

        if not pdfkit.from_string(css + self.get_label(1).decode(), final_path, options=options):
            raise Exception("error generating pdf delivery label")
        else:
            return final_path

    def get_png_labels(self, out_type=1):
        """
        used to return labels in a list, can be PIL or Numpy output type.
        This method does not SAVE the images

        :param out_type: 1 = Numpy arrays 2 = Pil Images
        :return: List of images
        """

        #get CSS for label

        css = """<style>
                   div{font-family: Arial, Helvetica, sans-serif;}
                   p{font-family: Arial, Helvetica, sans-serif;}
                   body{font-family: Arial, Helvetica, sans-serif;}
                 </style>
        """

        #get temp file
        temp = tempfile.gettempdir() + "/temp_label.png"
        imgkit.from_string(css + self.get_label().decode(), temp, options={"quality": 4, "width": 400,'--quiet': ''})
        #read image
        label_image = cv2.imread(temp)

        #set positions
        dist = 400
        images = []
        endy = 408
        starty = 11

        for x in range(len(self.parcels)):
            label = label_image[starty:endy, 19:404, :]
            images.append(label if out_type == 1 else Image.fromarray(label))
            endy += dist * 2
            starty += dist * 2

        return images

    def save_png_labels(self, out_path=None, filename=None):
        """
        Used to save PNG label images. When specifying the filename do not put the extension, its inferred already
        :param out_path: path to save images to. If none then will be the current working directory
        :param filename: filename without the .png  i.e   mylabel
        if a blank filename is passed random file name will be used
        :return: list of filenames
        """

        #check out path and use relative if needed
        if not out_path:
            out_path = "./"

        if not os.path.isdir(out_path):
            raise Exception("Out path not valid")

        # create filename if not found
        if not filename:
            filename = secrets.token_urlsafe(10)

        #get the final path
        final_path = out_path + "/" if out_path[-1] != "/" else "" + filename

        #get list for to reutrn
        filenames = []
        for i, img in enumerate(self.get_png_labels(2)):
            filenames.append(f"{final_path}-{str(i)}.png")
            img.save(filenames[-1])

        return filenames

class DPD:

    def __init__(self, user, password, account_no, sender_address, host="https://api.dpd.co.uk"):
        """

        :param user: DPD user name
        :param password: DPD Password
        :param account_no: DPD account number
        :param sender_address: Address object for senders address
        :param host: Can specify any alternative host URL if needed
        """

        self.user = user
        self.login = base64.b64encode(f"{user}:{password}".encode("utf-8"))
        self.host = host
        self.account_no = account_no
        self.sender_address = sender_address
        self.geo = None

    def _get_check_geosession(func):

        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            """Used to get the geosession string from DPD,
               will obtain a new session if the previous one is a day old

               returns: geosession string
            """
            now = datetime.datetime.now

            # get pickle object
            try:
                geo = pickle.load(open(f"{tempfile.gettempdir()}/geo.pk", "rb"))
            except FileNotFoundError:
                geo = [None, datetime.datetime(year=1980, month=now().month, day=now().day)]

            # if geosession is over 12 hours old get a new one
            if geo[1] < now() - datetime.timedelta(hours=3):
                # get the header for request
                headers_data = {'Content-Type': 'application/json',
                                'Accept': 'application/json',
                                'Authorization': f'Basic {self.login.decode()}'}

                # request geosession
                req = requests.post(self.host + "/user/?action=login", headers=headers_data)

                # check respose is valid
                self._check_response_valid(req)

                # get the geosession object
                geo = [req.json()["data"]["geoSession"], datetime.datetime.now()]

                # set and store
                pickle.dump(geo, open(f"{tempfile.gettempdir()}/geo.pk", "wb"))

            self.geo = geo[0]

            return func(self, *args, **kwargs)

        return wrapper

    def _check_response_valid(self, rep):
        if rep.status_code != 200:
            if rep.status_code == 401:
                raise Exception(
                    "Authentication error, login details incorrect or API access not enabled. Check credentials or speak to DPD intergration")
            elif rep.status_code == 404:
                raise Exception("Endpoint not found")
            else:
                raise Exception("Unspecified geosession error")

    def _get_header(self):
        return {'Accept': 'application/json', "GeoClient": f"{self.user}/{self.account_no}", "GeoSession": self.geo}

    @_get_check_geosession
    def get_available_services(self, parcel):
        """

        :param parcel:
        :return:
        """
        # get available header service

        # construct the URL
        url = f"/shipping/network/?businessUnit=0&deliveryDirection=1&numberOfParcels={parcel.pcs}&shipmentType=0&totalWeight={parcel.weight}&deliveryDetails.address.countryCode=GB&deliveryDetails.address.countryName=&deliveryDetails.address.locality=&deliveryDetails.address.organisation=test&deliveryDetails.address.postcode={parcel.postcode}&deliveryDetails.address.street={parcel.address_1}&deliveryDetails.address.town={parcel.address_2}&collectionDetails.address.countryCode=GB&collectionDetails.address.postcode={self.sender_address.postcode}"
        # get the request
        req = requests.get(self.host + url, headers=self._get_header())
        # check the response
        self._check_response_valid(req)

        # create dictionary for available services
        services = {}
        if req.json()["data"]:
            for i in req.json()["data"]:
                services[i["network"]["networkDescription"].title()] = i["network"]["networkCode"]
        else:
            raise Exception("Issue with parcel, no services found, possibly postcode not valid")

        return services

    @_get_check_geosession
    def _get_label(self, delivery, out_type=1):

        """
        Used to get a label from a shipment

        :param delivery: Delivery object
        :param out_type: 1= html, 2= citizen-clp, 3= eltron-epl
        :return: Delivery Object

        """
        if not delivery or type(delivery) is not Delivery:
            raise Exception("delivery not found, please add a Delivery object")
        if not out_type in [1, 2, 3]:
            raise Exception("invalid out_put type")

        # get output type as per DPD Api docs
        if out_type == 1:
            # makes sense
            accept = "text/html"
        elif out_type == 2:
            # these are to be sent directly to the printer, not human readable
            accept = "text/vnd.citizen-clp"
        elif out_type == 3:
            # these are to be sent directly to the printer, not human readable
            accept = "text/vnd.eltron-epl"

        # change header
        header = self._get_header()
        header["accept"] = accept

        # get the request
        req = requests.get(self.host + "/shipping/shipment/" + str(delivery.shipment_id) + "/label/", headers=header)
        # validate the request
        self._check_response_valid(req)

        return req.content

    @_get_check_geosession
    def create_delivery(self, parcel, service):

        """
        Used to create a DPD shipment

        :param parcel: Parcel object
        :param service: DPD service code i.e 1^12
        :return: Delivery Object

        """
        if not parcel or type(parcel) is not Parcel:
            raise Exception("Parcel not found, please add a Parcel object")
        if not service or type(service) is not str:
            raise Exception("service not valid")

        # get the DPD shipping object
        ship_obj = self._get_ship_obj(parcel, service)
        # get the request
        req = requests.post(self.host + "/shipping/shipment", headers=self._get_header(), json=ship_obj)
        # validate the request
        self._check_response_valid(req)

        # check for error code
        if not req.json()["error"]:
            # get the delivery object
            return Delivery(parcel, service, req, self)
        else:
            raise Exception(req.json()["error"])

    def _get_ship_obj(self, parcel, service):
        """creates the shipping object for the request"""

        now = datetime.datetime.now().strftime("%Y-%m-%dT15:00:00")
        base = {
            "jobId": None,
            "collectionOnDelivery": None,
            "invoice": None,
            "collectionDate": now,
            "consolidate": None,
            "consignment": [
                {
                    "consignmentNumber": None,
                    "consignmentRef": None,
                    "parcel": [],
                    "collectionDetails": {
                        "contactDetails": {
                            "contactName": self.sender_address.name,
                            "telephone": self.sender_address.tel,
                        },
                        "address": {
                            "organisation": self.sender_address.organisation,
                            "countryCode": "GB",
                            "postcode": self.sender_address.postcode,
                            "street": self.sender_address.address_1,
                            "locality": self.sender_address.address_2 if not self.sender_address.address_3 == "" else "",
                            "town": self.sender_address.address_2 if self.sender_address.address_3 == "" else self.sender_address.address_3,
                            "county": self.sender_address.address_4,
                        }
                    },
                    "deliveryDetails": {
                        "contactDetails": {
                            "contactName": parcel.name,
                            "telephone": parcel.tel
                        },
                        "address": {
                            "organisation": parcel.name,
                            "countryCode": "GB",
                            "postcode": parcel.postcode,
                            "street": parcel.address_1,
                            "locality": parcel.address_2 if not parcel.address_3 == "" else "",
                            "town": parcel.address_2 if parcel.address_3 == "" else parcel.address_3,
                            "county": parcel.address_4,
                        },
                        "notificationDetails": {
                            "email": parcel.email if parcel.email_updates else None,
                            "mobile": parcel.tel if parcel.telephone_updates else None
                        }
                    },
                    "networkCode": service,
                    "numberOfParcels": parcel.pcs,
                    "totalWeight": parcel.weight,
                    "shippingRef1": str(parcel.shipping_ref),
                    "customsValue": None,
                    "deliveryInstructions": parcel.delivery_instructions,
                    "parcelDescription": "",
                    "liabilityValue": None,
                    "liability": None
                }
            ]
        }
        return base
