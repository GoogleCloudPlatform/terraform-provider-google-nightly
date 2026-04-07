# Copyright IBM Corp. 2014, 2026
# SPDX-License-Identifier: MPL-2.0

import json
from typing import Any


class FixedProductNameGenerator:

  def stream_query(self, product: str) -> Any:
    response_data = {
        "output": "updated-reasoning-engine-prober: expected query response"
    }
    yield json.dumps(response_data)


fixed_name_generator = FixedProductNameGenerator()