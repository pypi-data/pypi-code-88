import json

from typing import Dict
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

import click

from hycli.commons.request import extract_invoice
from hycli.commons.structure import flatten_invoice


def run_requests(
    files: Dict[Path, str],
    url: str,
    workers: int,
    headers: Dict[str, str],
    params: Dict[str, str],
    token: str,
) -> dict:
    result = {}

    if headers.get("Content-Type") == "application/vnd.hypatos.ocr+json":
        # Input are jsons already processed by OCR
        with ThreadPoolExecutor(max_workers=workers) as exe:
            jobs = {
                exe.submit(
                    extract_invoice,
                    read_pdf(file_path),
                    url,
                    content_type,
                    token,
                    headers,
                    params,
                ): file_path
                for file_path, content_type in files.items()
                if content_type.endswith("json") and json_is_ocr(file_path)
            }
            label = f"Extracting {len(jobs)} documents"

            with click.progressbar(jobs, label=label) as bar:
                for idx, future in enumerate(as_completed(jobs)):
                    file_name = jobs[future].stem

                    try:
                        extracted_invoice = future.result(timeout=300)
                        result[idx] = flatten_invoice(extracted_invoice)
                    except Exception as e:
                        result[idx] = {"error_message": (str(e), None, None)}
                    finally:
                        result[idx]["file_name"] = (file_name, None, None)

                    bar.update(1)
    else:
        with ThreadPoolExecutor(max_workers=workers) as exe:
            # Inputs are invoices images/pdfs
            jobs = {
                exe.submit(
                    extract_invoice,
                    read_pdf(file_path),
                    url,
                    content_type,
                    token,
                    headers,
                    params,
                ): file_path
                for file_path, content_type in files.items()
                if not content_type.endswith("json")
            }
            label = f"Extracting {len(jobs)} documents"

            with click.progressbar(jobs, label=label) as bar:
                for idx, future in enumerate(as_completed(jobs)):
                    file_name = jobs[future].stem

                    try:
                        extracted_invoice = future.result(timeout=300)
                        result[idx] = flatten_invoice(extracted_invoice)
                    except Exception as e:
                        result[idx] = {"error_message": (str(e), None, None)}
                    finally:
                        result[idx]["file_name"] = (file_name, None, None)

                    bar.update(1)

        # Input are jsons already processed by Hypatos extractor
        json_jobs = {
            file_path: json.loads(file_path.read_bytes())
            for file_path, file_extension in files.items()
            if file_extension.endswith("json") and not json_is_ocr(file_path)
        }
        label = f"Merging {len(json_jobs)} invoices"

        with click.progressbar(json_jobs, label=label) as bar:
            for idx, (file_path, document) in enumerate(
                json_jobs.items(), start=len(jobs)
            ):
                result[idx] = flatten_invoice(document)
                result[idx]["file_name"] = (file_path.name, None, None)

                bar.update(1)

    if not result:
        quit("No files found in path")
    return result


def read_pdf(pdf_path: str) -> bytes:
    with open(pdf_path, "rb") as pdf:
        pdf = pdf.read()

    return pdf


def json_is_ocr(pdf_path: str) -> bool:
    possible_ocr = json.loads(read_pdf(pdf_path))
    if "ocr" in possible_ocr:
        if "words" in possible_ocr["ocr"]:
            return True

    return False
