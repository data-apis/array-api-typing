<h1 align='center'> array-api-typing </h1>
<h3 align="center">Type Annotations for the Array APi</h3>

---

## Installation

```bash
pip install array-api-typing
```

<details>
  <summary>using <code>uv</code></summary>

```bash
uv add array-api-typing
```

</details>
<details>
  <summary>from source, using pip</summary>

```bash
pip install git+https://https://github.com/data-apis/array-api-typing.git
```

</details>
<details>
  <summary>building from source</summary>

```bash
cd /path/to/parent
git clone https://https://github.com/data-apis/array-api-typing.git
cd array-api-typing
pip install -e .  # editable mode
```

</details>

### Quick example

```pycon
>>> import array_api_typing as xpt
>>> import numpy as np

>>> def func(x: xpt.HasNamespace) -> xpt.HasNamespace:
...    return x

>>> func(np.array([1, 2, 3]))
array([1, 2, 3])

```