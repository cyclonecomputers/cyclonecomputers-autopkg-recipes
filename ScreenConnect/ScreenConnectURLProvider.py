#!/usr/local/autopkg/python
#
# Copyright 2024 Cyclone Computer Company Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""See docstring for ScreenConnectURLProvider class"""

from distutils.version import LooseVersion
import plistlib
import urllib.parse
import re

from autopkglib import ProcessorError # type: ignore
from autopkglib.URLGetter import URLGetter # type: ignore

__all__ = ["ScreenConnectURLProvider"]


class ScreenConnectURLProvider(URLGetter):
    """Provides a customer (Company) specific download URL for the ScreenConnect Client on a specified server."""

    description = __doc__
    input_variables = {
        "server_url": {
            "required": True,
            "description": "The base URL of the ScreenConnect server (including https:// and any port numbers if not using 443).",
        },
        "company_name": {
            "required": True,
            "description": "The name of the Company to be used when generating the URL.",
        },
        "site_name": {
            "required": False,
            "description": "The name of the Site to be used when generating the URL.",
        },
        "department_name": {
            "required": False,
            "description": "The name of the Department to be used when generating the URL.",
        },
    }
    output_variables = {
        "url": {"description": "Download URL."},
        "client-id": {"description": "A client specific identifier intended to be used in the file name for the installer."}
    }

    def main(self):
        """Build the download URL"""

        server_url = self.env.get("server_url").rstrip("/")
        company_name = self.env.get("company_name")
        site_name = self.env.get("site_name")
        department_name = self.env.get("department_name")

        company_encoded = urllib.parse.quote(company_name, safe='')
        site_encoded = urllib.parse.quote(site_name, safe='')
        department_encoded = urllib.parse.quote(department_name, safe='')

        if not company_name and not site_name and not department_name:
            client_id = "DEFAULT"
        else:
            company_normalised = re.sub('[^A-Za-z0-9]+', '', company_name)
            site_normalised = re.sub('[^A-Za-z0-9]+', '', site_name)
            department_normalised = re.sub('[^A-Za-z0-9]+', '', department_name)

            client_id = f"{company_normalised}-{site_normalised}-{department_normalised}".replace("--", "-").strip("-")

        self.env["client_id"] = client_id
        self.output("Client ID set to '%s'" % self.env["client_id"])

        url = f"{server_url}/Bin/ScreenConnect.ClientSetup.pkg?e=Access&y=Guest&c={company_encoded}&c={site_encoded}&c={department_encoded}&c=&c=&c=&c=&c="
        self.env["url"] = url
        self.output("Download URL set to %s" % self.env["url"])


if __name__ == "__main__":
    PROCESSOR = ScreenConnectURLProvider()
    PROCESSOR.execute_shell()
