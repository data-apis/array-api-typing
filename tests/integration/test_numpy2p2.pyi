from test_numpy2p0 import nparr

import array_api_typing as xpt

# Incorrect values are caught when using `__array_namespace__` and
# backpropagated to the type of `a_ns`
a_ns: xpt.HasArrayNamespace[dict[str, int]] = nparr  # type: ignore[assignment]
