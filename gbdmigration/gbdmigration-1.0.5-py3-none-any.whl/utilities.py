import json
import os
import zlib
import shutil
from datetime import datetime
import xmltodict
from gbdindexing.indexer import filter_lire_for_solr
from copy import deepcopy


RAW_DOCUMENTS = '{{RAW_DOCUMENTS}}'
GBD_DOCUMENTS = '{{GBD_DOCUMENTS}}'
IMAGES_BUCKET = '{{IMAGES_BUCKET}}'


def get_gbd_format(path_to_raw, appnum, parser):
    try:
        transformed = parser.run(path_to_raw, raise_errors=False)
        return json.loads(transformed), None
    except Exception as e:
        return {}, '%s - %s' % (appnum, e)

def appnum_to_subdirs(appnum):
    """
    return a properly zfilled 2 level path from the application number:
     - 0123456789 should return 67/89
     - 1 should return 00/01
    """
    appnum = appnum.zfill(4)
    subs_dir = os.path.join(appnum[-4:-2], appnum[-2:])
    return subs_dir

def appnum_to_dirs(appnum, dest_root):
    """
    return the prefix_dir with the properly zfilled 2 level path from
    the application number
    - prefix_dir: /data/brand-data/frtm/xml/  && appnum = 1 >
    /data/brand-data/frtm/xml/00/01/
    """
    return os.path.join(dest_root, appnum_to_subdirs(appnum), appnum)


def get_crc(img_file):
    prev = 0
    fh = open(img_file, 'rb')
    for eachLine in fh:
        prev = zlib.crc32(eachLine, prev)
    fh.close()
    return "%X" % (prev & 0xFFFFFFFF)



def rename_img(img_file, new_name, new_path):
    """
    helper to rename img files
    123.1.png 123.1-th.jpg
    """
    _, basename = os.path.split(img_file)
    name, ext = os.path.splitext(basename)
    renamed = os.path.join(new_path, '%s%s' % (new_name, ext))
    shutil.copyfile(img_file, renamed)
    return renamed


def build_s3_path(bucket_name, filename, s_type, collection):
    store_path = os.path.join(s_type, collection, filename)
    storage_location = os.path.join(bucket_name, store_path)
    return storage_location


def prepare_copies_for_dynamo(st13, meta_info, high_image, icon_image, thumbnail_image,
                              s_type, collection):
    run_id = meta_info['run_id']
    office_extraction_date = '1900-01-01'
    xml_location = build_s3_path(RAW_DOCUMENTS, os.path.basename(meta_info['xml'].replace('.gz', '')),
                                 s_type, collection)
    results = {
        "gbd_extraction_date": datetime.today().strftime("%Y-%m-%d"),
        "run_id": run_id,
        "st13": st13,
        "biblio": {
            "office": xml_location
        },
        "office_extraction_date": office_extraction_date
    }
    if high_image:
        high_image = build_s3_path(IMAGES_BUCKET, os.path.basename(high_image), s_type, collection)
        icon_image = build_s3_path(IMAGES_BUCKET, os.path.basename(icon_image), s_type, collection)
        thumbnail_image = build_s3_path(IMAGES_BUCKET, os.path.basename(thumbnail_image), s_type, collection)
        results["media"] = {
            "logo": [
                {
                    "standard": {
                        "high": high_image,
                        "thum": thumbnail_image,
                        "tiny": icon_image
                    },
                }
            ]
        }
    return results


def prepare_gbd_latest(gbd_format, copies, qc):
    gbd_doc = {
        'biblio': gbd_format,
        'gbd_extraction_date': copies['gbd_extraction_date'],
        'office_extraction_date': copies['office_extraction_date']
    }
    if qc:
        gbd_doc['qc'] = qc
    if copies.get('media', None):
        gbd_doc['media'] = {
            'logo': []
        }
        for img in copies['media']['logo']:
            gbd_doc['media']['logo'].append(img['standard'])
    return gbd_doc


def parse_lire(lire_file):
    with open(lire_file, 'r') as f:
        raw_xml_data = xmltodict.parse(f.read())
        xml_data = {}
        for field in raw_xml_data['doc']['field']:
            key = field.get('@name', None)
            value = field.get('#text', None)
            if key and value:
                xml_data[key] = value
        lire_data = {
            'lireAnalysis': xml_data
        }
        lire_data = filter_lire_for_solr(lire_data)
    return lire_data


def prepare_preprod_for_dynamo(st13, run_id, gbd_latest, lire_json, collection):
    preprod_latest = deepcopy(gbd_latest)
    preprod_latest.pop('biblio')
    results = {
      "lire": lire_json,
      "latest_run_id": run_id,
      "st13": st13,
      "doc_location": os.path.join(GBD_DOCUMENTS, st13, '%s.json' % run_id),
      "gbd_collection": collection,
      "gbd_index": {
        "status": "PENDING",
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
      },
      "latest": preprod_latest
    }
    return results
