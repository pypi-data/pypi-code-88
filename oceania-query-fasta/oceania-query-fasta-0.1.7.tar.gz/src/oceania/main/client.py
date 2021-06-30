import requests
import pandas
import urllib
import sys
import traceback

from timeit import default_timer
from .settings import settings
from .utils import download_file_from_stream
import time

logger = settings.logger


def download_result(key, output):
    url = f"{settings.API_URL}query/result/{key}"
    if isinstance(output, str):
        output_handler = open(output, "wb")
    else:
        output_handler = output
    while not download_file_from_stream(url, output_handler):
        time.sleep(10)
        logger.debug(f"Waiting for {key} to be available")


def load_results_to_pandas(key):
    url = f"{settings.API_URL}query/result/{key}"
    timeout = time.time() + 60 * 30  # 30 minutes from now
    while True:
        if time.time() > timeout:
            logger.error("TIMEOUT ERROR: ")
            logger.error("Exception in user code: 02")
            logger.error(url)
            break
        try:
            return pandas.read_csv(url)
        except urllib.error.HTTPError:
            pass
        time.sleep(10)
        logger.debug(f"Waiting for {key} to be available")


def list_fasta_files():
    url = f"{settings.API_URL}query/list-fasta-files/"
    return pandas.read_csv(url)


def get_file_storage_key(sample_id):
    df = list_fasta_files()
    return df[df.sample_id == sample_id].sample_key.item()


def get_sequences_from_fasta(sample_id, positions):
    storage_key = get_file_storage_key(sample_id)
    start_timer = default_timer()
    url = f"{settings.API_URL}query/fasta-sequences/"
    logger.debug(f"Requesting sequences in {url}")
    logger.info("Sending request for fasta sequences")
    body = {
        "storage_key": storage_key,
        "positions": positions,
        "output_format": "csv",
    }

    try:
        response = requests.post(url, json=body)
    except ConnectionError as e:
        logger.error("CONNECTION ERROR: ")
        logger.error("Exception in user code: 01")
        logger.error(e)
        traceback.print_exc(file=sys.stdout)
        sys.exit(1)

    logger.info("Request accepted")

    results_key = response.json().get("results_key")
    logger.debug(f"Received key {results_key}")

    logger.info("Waiting for results...")

    ret = load_results_to_pandas(results_key)

    logger.debug("Done")
    end_timer = default_timer()
    logger.info(f"Done. Elapsed time: {end_timer - start_timer} seconds")

    return ret


def get_sequences_from_fasta_to_file(sample_id, positions, output_format, output):
    storage_key = get_file_storage_key(sample_id)
    start_timer = default_timer()
    url = f"{settings.API_URL}query/fasta-sequences/"
    logger.debug(f"Requesting sequences in {url}")
    logger.info("Sending request for fasta sequences")
    body = {
        "storage_key": storage_key,
        "positions": positions,
        "output_format": output_format,
    }

    try:
        response = requests.post(url, json=body)
    except ConnectionError as e:
        logger.error("CONNECTION ERROR: ")
        logger.error("Exception in user code: 01")
        logger.error(e)
        traceback.print_exc(file=sys.stdout)
        sys.exit(1)

    logger.info("Request accepted")

    results_key = response.json().get("results_key")
    logger.debug(f"Received key {results_key}")

    logger.info("Waiting for results...")

    if isinstance(output, str):
        output_str = output
    else:
        output_str = output.name

    logger.debug(f"Downloading results to {output_str}")

    download_result(results_key, output)

    logger.debug("Done")
    end_timer = default_timer()
    logger.info(
        f"Done. Results saved to {output_str}. Elapsed time: {end_timer - start_timer} seconds"
    )


def list_intergenic_regions(sample_id, min_length=0, page=1, page_size=50):
    url = f"{settings.API_URL}query/list-intergenic_regions/{sample_id}?page={page}&page_size={page_size}&min_length={min_length}"
    return pandas.read_csv(url, sep="\t")
