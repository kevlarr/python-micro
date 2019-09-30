First, install the packages.

```bash
cd common
pip install -e .

cd services/api
pip install -e .
```

Then, fire up a `python` shell.

```python
import micro.services.api as api
quote = api.new_quote()
print(quote.message)
```

Your reward is courtesy of https://api.kanya.rest !
