import json
import os
import sys
import warnings
from contextlib import ExitStack
from datetime import datetime, timedelta
from io import BytesIO
from pathlib import Path
from tempfile import TemporaryFile
from typing import (
    IO, Any, BinaryIO, Dict, Iterable, List, Optional, Tuple, Union, cast,
    overload)
from uuid import UUID

import click
import jwt
import requests

from unfolded.data_sdk.errors import (
    AuthenticationError, DataFrameParsingError, DataSDKError,
    UnknownDatasetNameError, UnknownMediaTypeError)
from unfolded.data_sdk.models import (
    Dataset, Map, MapState, MapUpdateParams, MediaType)
from unfolded.data_sdk.utils import (
    compress_fileobj, get_fileobj_length, raise_for_status, read_fileobj_chunks)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

try:
    import pandas as pd
except ImportError:
    pd = None

try:
    import geopandas as gpd
except ImportError:
    gpd = None

REFRESH_BUFFER = timedelta(minutes=1)

CREDENTIALS_NOT_WRITABLE_MSG = """\
Credentials directory not writable.
Either make $HOME/.config/unfolded writable or supply another credentials_dir.
"""


class DataSDK:
    client_id: str = 'v970dpbcqmRtr3y9XwlAB3dycpsvNRZF'
    base_url: str = 'https://api.unfolded.ai'
    auth_url: str = 'https://auth.unfolded.ai/oauth/token'

    def __init__(
        self,
        refresh_token: Optional[str] = None,
        credentials_dir: Union[Path,
                               str] = Path('~/.config/unfolded/').expanduser()):
        """Constructor for DataSDK

        Args:
            refresh_token (optional): a refresh token for interacting with
                Unfolded Studio. This only needs to be provided once; the
                refresh token will be saved to disk and will be transparently
                loaded in future uses of the DataSDK class. Default: loads
                refresh token from saved file path on disk.
            credentials_dir (optional): a path to a directory on disk to be used
                as the credentials directory. By default this is
                $HOME/.config/unfolded. If this path isn't writable, you can
                either make that path writable or define a custom credentials
                directory. If you use a custom directory, you'll need to include
                that every time you use the DataSDK class.
        """
        self.credentials_dir = Path(credentials_dir)

        if refresh_token:
            self._write_refresh_token(refresh_token)
        else:
            try:
                self._load_refresh_token()
            except:
                msg = 'refresh_token was not provided and was not previously saved.'
                raise AuthenticationError(msg)

        self._token: Optional[str] = None

    def list_datasets(self) -> List[Dataset]:
        """List datasets for given user

        Returns:
            List of dataset objects.
        """
        url = f'{self.base_url}/v1/datasets'
        r = requests.get(url, headers=self._headers)
        raise_for_status(r)

        return [Dataset(**item) for item in r.json().get('items', [])]

    def get_dataset_by_id(self, dataset: Union[Dataset, str, UUID]) -> Dataset:
        """Get dataset given its id

        Args:
            dataset: dataset record to retrieve.

        Returns:
            Retrieved dataset record.
        """
        if isinstance(dataset, Dataset):
            dataset = dataset.id

        url = f'{self.base_url}/v1/datasets/{dataset}'
        r = requests.get(url, headers=self._headers)
        raise_for_status(r)

        return Dataset(**r.json())

    def download_dataset(
        self,
        dataset: Union[Dataset, str, UUID],
        output_file: Optional[Union[BinaryIO, str, Path]] = None,
        **kwargs: Any,
    ) -> Optional[bytes]:
        """Download data for dataset

        Args:
            dataset: identifier for dataset whose data should be downloaded.
            output_file: if provided, a path or file object to write dataset's data to.

        Kwargs:
            chunk_size: number of bytes to download at a time. Used for progressbar.
            progress: if True, show progress bar.

        Returns:
            If output_file is None, returns bytes containing dataset's data.
            Otherwise, returns None and writes dataset's data to output_file.
        """
        if isinstance(dataset, Dataset):
            dataset = dataset.id

        url = f'{self.base_url}/v1/datasets/{dataset}/data'
        buf, _ = self._download_url(url=url, output_file=output_file, **kwargs)
        return buf

    # We use typing overloads here to make clear that a `None` response happens
    # when `None` is not passed as `output_file`
    @overload
    def _download_url(
            self,
            url: str,
            output_file: Literal[None] = None,
            **kwargs: Any) -> Tuple[bytes, requests.Response]:
        ...

    @overload
    def _download_url(
            self, url: str, output_file: Union[BinaryIO, str, Path],
            **kwargs: Any) -> Tuple[None, requests.Response]:
        ...

    def _download_url(
            self,
            url: str,
            output_file: Optional[Union[BinaryIO, str, Path]] = None,
            **kwargs: Any) -> Tuple[Optional[bytes], requests.Response]:
        """Low-level helper to download an arbitrary URL"""
        if not output_file:
            return self._download_dataset_to_bytes(url=url, **kwargs)

        with ExitStack() as ctx:
            if isinstance(output_file, (str, Path)):
                # Open file if it isn't already open
                opened_file = ctx.enter_context(open(output_file, 'wb'))
            else:
                opened_file = output_file

            r = self._download_dataset_to_fileobj(
                url=url, fileobj=opened_file, **kwargs)

        return None, r

    def _download_dataset_to_fileobj(
            self,
            url: str,
            fileobj: BinaryIO,
            chunk_size: int = 256 * 1024,
            progress: bool = False) -> requests.Response:
        """Download dataset to file object
        """
        with requests.get(url, headers=self._headers, stream=True) as r:
            raise_for_status(r)

            content_length = int(r.headers['Content-Length'])
            # Not sure why but os.devnull has type Iterable[str]
            fout = sys.stderr if progress else os.devnull
            fout = cast(IO, fout)
            with click.progressbar(label='Downloading data',
                                   length=content_length, file=fout) as bar:
                for data in r.iter_content(chunk_size=chunk_size):
                    fileobj.write(data)
                    bar.update(chunk_size)

            return r

    def _download_dataset_to_bytes(
            self, url: str, **kwargs: Any) -> Tuple[bytes, requests.Response]:
        """Download dataset to bytes object
        """
        with BytesIO() as bio:
            r = self._download_dataset_to_fileobj(
                url=url, fileobj=bio, **kwargs)
            bio.seek(0)
            return bio.read(), r

    def download_dataframe(
            self, dataset: Union[Dataset, str, UUID],
            **kwargs: Any) -> Union['pd.DataFrame', 'gpd.GeoDataFrame']:
        """Download dataset to pandas DataFrame or geopandas GeoDataFrame

        Args:
            dataset: identifier for dataset whose data should be downloaded.

        Kwargs:
            chunk_size: number of bytes to download at a time. Used for progressbar.
            progress: if True, show progress bar.

        Returns:
            Either a pandas DataFrame or a geopandas GeoDataFrame. If the
            dataset is a CSV file, a pandas DataFrame will be returned. If it is
            a GeoJSON file, a geopandas GeoDataFrame will be returned.
        """
        if pd is None:
            raise ImportError('Pandas required to load DataFrame object.')

        if isinstance(dataset, Dataset):
            dataset = dataset.id

        url = f'{self.base_url}/v1/datasets/{dataset}/data'
        buf, r = self._download_url(url=url, output_file=None, **kwargs)
        content_type = r.headers['Content-Type']

        with BytesIO(buf) as bio:
            if content_type == MediaType.CSV:
                return pd.read_csv(bio)

            if content_type == MediaType.GEOJSON:
                if gpd is None:
                    raise ImportError(
                        'GeoPandas required to load GeoJSON response to DataFrame object.'
                    )

                return gpd.read_file(bio)

            # Unfortunately, Studio doesn't put the correct content type on
            # GeoJSON files and saves all JSON data as application/json. Here
            # we'll try to parse as GeoJSON, then fall back to attempting JSON
            # parsing
            if content_type == MediaType.JSON:
                if gpd is not None:
                    try:
                        return gpd.read_file(bio)
                    except:
                        pass

                try:
                    return pd.read_json(bio, orient='records')
                except:
                    pass

                # Unable to parse JSON
                msg = 'Unable to parse JSON data. If a GeoJSON, GeoPandas must be installed to parse GeoJSON to a DataFrame. Otherwise, the JSON file must be an array of records.'
                raise DataFrameParsingError(msg)

            raise UnknownMediaTypeError(f'Unknown Media Type {content_type}')

    def upload_file(
            self,
            file: Union[BinaryIO, str, Path],
            name: Optional[str] = None,
            *,
            dataset: Optional[Union[Dataset, str, UUID]] = None,
            media_type: Optional[Union[str, MediaType]] = None,
            description: Optional[str] = None,
            chunk_size: int = 256 * 1024,
            progress: bool = False) -> Dataset:
        """Upload dataset to Unfolded Studio

        To create a new dataset record, don't pass a dataset parameter. If a
        dataset parameter is passed, that dataset will be updated.

        Args:
            file: path or file object to use for uploading data.
            name: name for dataset record.

        Kwargs:
            dataset: If provided, dataset whose data should be updated. Otherwise, creates a new dataset.
            media_type: media type of data. By default, tries to infer media type from file name.
            description: description for dataset record.

        Kwargs:
            chunk_size: number of bytes to upload at a time. Used for progressbar.
            progress: if True, show progress bar.

        Returns:
            Updated dataset record
        """
        # Name not necessary for updating a dataset
        if not name and not dataset:
            name = self._infer_new_dataset_name(file)

        if not media_type:
            media_type = self._infer_media_type(file=file)

        if isinstance(media_type, MediaType):
            media_type = media_type.value

        if dataset and isinstance(dataset, Dataset):
            dataset = dataset.id

        if dataset:
            url = f'{self.base_url}/v1/datasets/{dataset}/data'
        else:
            url = f'{self.base_url}/v1/datasets/data'

        headers: Dict[str, str] = {
            **self._headers, 'Content-Type': media_type,
            'Content-Encoding': 'gzip'}

        with ExitStack() as ctx:
            # Open file if it isn't already open
            if isinstance(file, (str, Path)):
                opened_file = ctx.enter_context(open(file, 'rb'))
            else:
                opened_file = file

            headers['Content-Length-Uncompressed'] = str(
                get_fileobj_length(opened_file))

            # Create temporary file to write compressed bytes to
            tmpf = ctx.enter_context(TemporaryFile())
            compress_fileobj(opened_file, tmpf)
            tmpf.seek(0)

            # Get compressed file length (used for progress bar)
            compressed_file_length = get_fileobj_length(tmpf)
            fout = sys.stderr if progress else os.devnull
            fout = cast(IO, fout)

            # Enter progressbar context manager
            bar = ctx.enter_context(
                click.progressbar(
                    label='Uploading file',
                    length=compressed_file_length,
                    file=fout))

            # Create iterator for file object (default file iterator uses
            # newlines, not a byte length)
            iterator = read_fileobj_chunks(
                tmpf, chunk_size=chunk_size, callback=bar.update)

            # Upload using iterator
            if dataset:
                # TODO: can updating a dataset also using name and description
                # params?
                r = requests.put(
                    url,
                    data=iterator,  # type: ignore
                    headers=headers)
            else:
                params = {'name': name}
                if description:
                    params['description'] = description
                r = requests.post(
                    url,
                    data=iterator,  # type: ignore
                    params=params,
                    headers=headers)

        raise_for_status(r)
        return Dataset(**r.json())

    def upload_dataframe(
            self,
            df: Union['pd.DataFrame', 'gpd.GeoDataFrame'],
            name: Optional[str] = None,
            index: bool = True,
            **kwargs: Any) -> Dataset:
        """Upload DataFrame or GeoDataFrame to Unfolded Studio

        Args:
            df: Either a pandas DataFrame or a geopandas GeoDataFrame to upload to Unfolded Studio.
            name: Name of dataset record. Required if creating a new dataset record.
            index (optional): if True, include row names in output. Default: True.
            **kwargs: keyword arguments to pass on to DataSDK.upload_file

        Returns:
            Dataset record of new data.
        """
        with BytesIO(df.to_csv(index=index).encode('utf-8')) as bio:
            return self.upload_file(
                file=bio, name=name, media_type=MediaType.CSV, **kwargs)

    def update_dataset(
            self,
            file: Union[BinaryIO, str, Path],
            dataset: Union[Dataset, str, UUID],
            media_type: Optional[Union[str, MediaType]] = None,
            **kwargs: Any) -> Dataset:
        """Update data for existing Unfolded Studio dataset

        Note that this overwrites any existing data attached to the dataset.

        Args:
            file: path or file object to use for uploading data.
            dataset: dataset whose data should be updated.
            media_type: media type of data. By default, tries to infer media type from file name.

        Kwargs:
            chunk_size: number of bytes to upload at a time. Used for progress bar.
            progress: if True, show progress bar.

        Returns:
            Updated dataset record
        """
        warnings.warn(
            'update_dataset is deprecated. Use upload_file with a dataset argument.',
            DeprecationWarning)

        return self.upload_file(
            file=file, dataset=dataset, media_type=media_type, **kwargs)

    def delete_dataset(self, dataset: Union[Dataset, str, UUID]) -> None:
        """Delete dataset from Unfolded Studio

        Warning: This operation cannot be undone. If you delete a dataset
        currently used in one or more maps, the dataset will be removed from
        those maps, possibly causing them to render incorrectly.

        Args:
            dataset: dataset to delete from Unfolded Studio.

        Returns:
            None
        """
        if isinstance(dataset, Dataset):
            dataset = dataset.id

        url = f'{self.base_url}/v1/datasets/{dataset}'
        r = requests.delete(url, headers=self._headers)
        raise_for_status(r)

    def list_maps(self) -> List[Map]:
        """List maps for given user

        Gets the Map records for a given user, without dataset associations and map state. To get
        the full record with the associations, please use get_map_by_id().

        Returns:
            List of map objects.
        """
        url = f'{self.base_url}/v1/maps'
        r = requests.get(url, headers=self._headers)
        raise_for_status(r)
        return [Map(**item) for item in r.json().get('items', [])]

    def get_map_by_id(
            self,
            # pylint:disable = redefined-builtin
            map: Union[Map, str, UUID]) -> Map:
        """Get an Unfolded map given its id

        Gets a full Unfolded map record, which includes the associated dataset records as well the
        latest saved map state.

        Args:
            map: the map record to retrieve. Can be either a shallow record or a string/UUID id.

        Returns:
            Retrieved map record.
        """
        if isinstance(map, Map):
            map = map.id

        url = f'{self.base_url}/v1/maps/{map}'
        r = requests.get(url, headers=self._headers)
        raise_for_status(r)
        return Map(**r.json())

    def create_map(
            self,
            *,
            name: str,
            description: Optional[str] = None,
            map_state: Optional[MapState] = None,
            datasets: Optional[Iterable[Union[Dataset, UUID,
                                              str]]] = None) -> Map:
        """Create an Unfolded Map record

        Args:
            name: the name of the map record (required).
            description: map description (optional).
            map_state: the map state/configuration (optional).
            datasets: list of datasets (records or ids) to add to the map (optional).

        Returns:
            New map record.
        """

        dataset_ids = None
        if datasets:
            dataset_ids = [
                str(dataset.id) if isinstance(dataset, Dataset) else dataset
                for dataset in datasets]
        map_params = MapUpdateParams(
            name=name,
            description=description,
            latest_state=map_state,
            datasets=dataset_ids)

        url = f'{self.base_url}/v1/maps'
        headers = {**self._headers, 'Content-Type': 'application/json'}
        r = requests.post(
            url,
            data=map_params.json(exclude_none=True, by_alias=True),
            headers=headers)
        raise_for_status(r)
        return Map(**r.json())

    def update_map(
            self,
            *,
            map_id: Union[Map, UUID, str],
            name: Optional[str] = None,
            description: Optional[str] = None,
            map_state: Optional[MapState] = None,
            datasets: Optional[Iterable[Union[Dataset, UUID,
                                              str]]] = None) -> Map:
        """Update fields of an Unfolded Map record

        Args:
            map: the map record to update with the new field.

        Returns:
            The updated map record.
        """

        if not map_id:
            raise DataSDKError('Map id is required to perform the update')

        dataset_ids = None
        if datasets:
            dataset_ids = [
                str(dataset.id) if isinstance(dataset, Dataset) else dataset
                for dataset in datasets]

        update_params = MapUpdateParams(
            name=name,
            description=description,
            latest_state=map_state,
            datasets=dataset_ids)

        url = f'{self.base_url}/v1/maps/{map_id}'
        headers = {**self._headers, 'Content-Type': 'application/json'}
        r = requests.put(
            url,
            data=update_params.json(exclude_none=True, by_alias=True),
            headers=headers)
        raise_for_status(r)
        return Map(**r.json())

    def delete_map(self, map_id: Union[Map, UUID, str]) -> None:
        """Delete an Unfolded Map record

        Args:
            map: the map record or id to delete.
        """
        if isinstance(map_id, Map):
            map_id = map_id.id

        url = f'{self.base_url}/v1/maps/{map_id}'
        r = requests.delete(url, headers=self._headers)
        raise_for_status(r)

    def _infer_new_dataset_name(self, file: Union[BinaryIO, str, Path]) -> str:
        general_msg = 'Please supply an explicit name for the dataset.'
        if not isinstance(file, (str, Path)):
            raise UnknownDatasetNameError(
                f"Cannot infer dataset name from binary stream.\n{general_msg}")

        if isinstance(file, Path):
            return file.name

        return Path(file).name

    def _infer_media_type(self, file: Union[BinaryIO, str, Path]) -> MediaType:
        general_msg = 'Please supply an explicit Media Type for the file.'
        if not isinstance(file, (str, Path)):
            raise UnknownMediaTypeError(
                f"Cannot infer Media Type from binary stream.\n{general_msg}")

        media_type = self._infer_media_type_from_path(file)

        if not media_type:
            raise UnknownMediaTypeError(
                f"Could not infer file's Media Type.\n{general_msg}")

        return media_type

    @staticmethod
    def _infer_media_type_from_path(
            path: Union[str, Path]) -> Optional[MediaType]:
        suffix = Path(path).suffix.lstrip('.').upper()

        try:
            return MediaType[suffix]
        except KeyError:
            return None

    @property
    def _headers(self) -> Dict[str, str]:
        """Default headers to send with each request
        """
        return {'Authorization': f'Bearer {self.token}'}

    @property
    def token(self) -> str:
        """Valid access token for interacting with Unfolded Studio's backend
        """
        # If no token in memory, try to load saved access token if one exists
        if not self._token:
            try:
                self.token = self._load_saved_access_token()
            except FileNotFoundError:
                pass

        # If token is expired, refresh it
        if not self._token or (datetime.now() >=
                               self._token_expiration - REFRESH_BUFFER):
            self._refresh_access_token()

        if not self._token:
            raise AuthenticationError('Could not refresh access token.')

        return self._token

    @token.setter
    def token(self, value: str) -> None:
        self._token = value

    @property
    def _token_expiration(self) -> datetime:
        # Use _token to bypass logic that depends on token_expiration to avoid
        # recursion error
        token = self._token

        # If token doesn't exist, provide timestamp in the past to trigger token
        # refresh
        if not token:
            return datetime.now() - timedelta(seconds=1)

        decoded = jwt.decode(token, options={"verify_signature": False})

        # Leave a one minute buffer
        return datetime.fromtimestamp(decoded['exp'])

    @property
    def _refresh_token_path(self) -> Path:
        return self.credentials_dir / 'credentials.json'

    @property
    def _access_token_path(self) -> Path:
        return self.credentials_dir / 'access_token.json'

    def _load_refresh_token(self) -> str:
        """Load saved refresh token
        """
        with open(self._refresh_token_path, encoding='utf-8') as f:
            return json.load(f)['refresh_token']

    def _load_saved_access_token(self) -> str:
        """Load saved access token
        """
        with open(self._access_token_path, encoding='utf-8') as f:
            data = json.load(f)

        return data['access_token']

    def _write_refresh_token(self, refresh_token: str) -> None:
        """Write refresh token to credentials_dir
        """
        if not refresh_token.startswith('v1.'):
            raise ValueError('Refresh token should start with "v1."')

        try:
            # Create credentials directory if it doesn't exist
            self._refresh_token_path.parent.mkdir(parents=True, exist_ok=True)
            with open(self._refresh_token_path, 'w', encoding='utf-8') as f:
                json.dump({'refresh_token': refresh_token}, f)
        except OSError as e:
            raise DataSDKError(CREDENTIALS_NOT_WRITABLE_MSG) from e

    def _write_access_token(self) -> None:
        """Write access token to credentials_dir
        """
        if not self._token:
            raise ValueError("No access token to write.")

        try:
            # Create credentials directory if it doesn't exist
            self._access_token_path.parent.mkdir(parents=True, exist_ok=True)
            with open(self._access_token_path, 'w', encoding='utf-8') as f:
                json.dump({'access_token': self._token}, f)
        except OSError as e:
            raise DataSDKError(CREDENTIALS_NOT_WRITABLE_MSG) from e

    def _refresh_access_token(self) -> None:
        refresh_token = self._load_refresh_token()

        post_data = {
            'grant_type': 'refresh_token',
            'client_id': self.client_id,
            'refresh_token': refresh_token}

        r = requests.post(self.auth_url, json=post_data)
        raise_for_status(r)
        auth_data = r.json()

        # Because we use rotating refresh tokens, we must write the refresh
        # token returned from the API call to disk.
        new_refresh_token = auth_data['refresh_token']
        self._write_refresh_token(new_refresh_token)
        self.token = auth_data['access_token']
        self._write_access_token()
