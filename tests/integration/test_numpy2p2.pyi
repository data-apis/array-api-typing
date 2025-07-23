from test_numpy2p0 import nparr

import array_api_typing as xpt

_: xpt.HasArrayNamespace[dict[str, int]] = nparr  # type: ignore[assignment]
