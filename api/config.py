"""
 This file is part of the wv_cdm_api project (https://github.com/GetWVKeys/wv_cdm_api)
 Copyright (C) 2022 Notaghost, Puyodead1 and GetWVKeys contributors 
 
 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU Affero General Public License as published
 by the Free Software Foundation, version 3 of the License.
 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU Affero General Public License for more details.
 You should have received a copy of the GNU Affero General Public License
 along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import os

import toml

IS_DEVELOPMENT = bool(os.environ.get("DEVELOPMENT", False))
parsed_toml = toml.load("config.toml")

API_HOST = parsed_toml.get("API_HOST")
API_PORT = int(parsed_toml.get("API_PORT", 8080))
API_URL = parsed_toml.get("API_URL", "https://server1.getwvkeys.cc")
API_SECRETS = parsed_toml.get("API_SECRETS", [])
