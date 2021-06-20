# -*- coding: utf-8 -*-
#
# Copyright (C) 2019-2021 Mathieu Parent <math.parent@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import annotations

from logging import getLogger
from typing import TYPE_CHECKING, Optional
from urllib.parse import quote

from gitlabracadabra.auth_info import AuthInfo
from gitlabracadabra.packages.destination import Destination
from gitlabracadabra.packages.package_file import PackageFile


if TYPE_CHECKING:
    from gitlabracadabra.gitlab.connection import GitlabConnection


HELM = 'helm'

logger = getLogger(__name__)


class Gitlab(Destination):
    """Gitlab repository."""

    def __init__(
        self,
        *,
        connection: GitlabConnection,
        full_path: str,
    ) -> None:
        """Initialize Gitlab repository.

        Args:
            connection: A Gitlab connection.
            full_path: Project full path.
        """
        self._connection = connection
        self._full_path = full_path
        super().__init__(log_prefix='[{0}] '.format(full_path))

    def upload_method(self, package_file: PackageFile) -> str:
        """Get upload HTTP method.

        Args:
            package_file: Source package file.

        Returns:
            The upload method.
        """
        if package_file.package_type == HELM:
            return 'POST'

        return super().upload_method(package_file)

    def head_url(self, package_file: PackageFile) -> str:
        """Get URL to test existence of destination package file with a HEAD request.

        Args:
            package_file: Source package file.

        Returns:
            An URL.

        Raises:
            NotImplementedError: For unsupported package types.
        """
        if package_file.package_type == 'raw':
            return '{0}/projects/{1}/packages/generic/{2}/{3}/{4}'.format(
                self._connection.api_url,
                quote(self._full_path, safe=''),
                quote(package_file.package_name, safe=''),  # [A-Za-z0-9\.\_\-\+]+
                quote(package_file.package_version, safe=''),  # (\.?[\w\+-]+\.?)+
                quote(package_file.file_name, safe=''),  # [A-Za-z0-9\.\_\-\+]+
            )
        elif package_file.package_type == HELM:
            channel = package_file.metadata.get('channel') or 'stable'
            file_name = '{0}-{1}.tgz'.format(package_file.package_name, package_file.package_version)
            return '{0}/projects/{1}/packages/helm/{2}/charts/{3}'.format(
                self._connection.api_url,
                quote(self._full_path, safe=''),
                quote(channel, safe=''),
                quote(file_name, safe=''),
            )

        raise NotImplementedError

    def upload_url(self, package_file: PackageFile) -> str:
        """Get URL to upload to.

        Args:
            package_file: Source package file.

        Returns:
            The upload URL.
        """
        if package_file.package_type == HELM:
            channel = package_file.metadata.get('channel') or 'stable'
            return '{0}/projects/{1}/packages/helm/api/{2}/charts'.format(
                self._connection.api_url,
                quote(self._full_path, safe=''),
                quote(channel, safe=''),
            )

        return super().upload_url(package_file)

    def files_key(self, package_file: PackageFile) -> Optional[str]:
        """Get files key, to upload to. If None, uploaded as body.

        Args:
            package_file: Source package file.

        Returns:
            The files key, or None.
        """
        if package_file.package_type == HELM:
            return 'chart'

        return super().files_key(package_file)

    def auth_info(self, package_file: PackageFile) -> AuthInfo:
        """Get auth info when testing existence and uploading.

        Args:
            package_file: Source package file.

        Returns:
            An AuthInfo.
        """
        return self._connection.registry_auth_info
