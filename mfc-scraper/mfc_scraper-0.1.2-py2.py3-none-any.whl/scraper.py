from typing import List, Dict, Union
import requests
from tqdm import tqdm
import multiprocessing as mp

from mfc_scraper.pages.figure_collection_page import FigureCollectionPage, NoFiguresFound
from mfc_scraper.pages.figure_page import FigurePage


def get_all_figure_ids(username: str) -> List[int]:
    base_url = "https://myfigurecollection.net/users.v4.php"
    url_parameters = {
        "username": username,
        "mode": "view",
        "tab": "collection",
        "status": 2,
        "categoryId": -1,
        "sort": "category",
        "order": "asc",
    }
    all_figures = []
    current_page = 1
    with tqdm() as progress_bar:
        while True:
            page_content = requests.get(base_url
                                        + "?"
                                        + "&".join(f"{k}={v}" for k, v in url_parameters.items())
                                        + f"&page={current_page}"
                                        ).text
            try:
                all_figures += (f.id for f in FigureCollectionPage(page_content).figures)
                current_page += 1
                progress_bar.update()
            except NoFiguresFound:
                break

    return all_figures


def _get_figure_data(figure_id: int) -> Dict[str, Union[List, str, int]]:
    base_url = "https://myfigurecollection.net/item/"
    return FigurePage(figure_id, requests.get(f"{base_url}{figure_id}").text).data.to_dict()


def get_figures_data(figure_ids: List[int]) -> List[Dict[str, Union[List, str, int]]]:
    with mp.Pool(mp.cpu_count()) as pool:
        return list(tqdm(pool.imap(_get_figure_data, figure_ids), total=len(figure_ids)))


def _get_image(url: str):
    response = requests.get(url, stream=True)
    return response.raw


def _get_figure_images(figure_data):
    return {"id": figure_data["id"], "images": [_get_image(u) for u in figure_data["image_urls"]]}


def get_all_images(figures_data: List[Dict[str, Union[List, str, int]]]):
    return list(tqdm(map(_get_figure_images, figures_data), total=len(figures_data)))
