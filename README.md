# CamelCamelCosco

A camelcamelcamel for Cosco 


## usage 

Inside the `app` directory: 

```
uvicorn main:app --reload
http://127.0.0.1:8000/api/scrape?q=macbook
```

## Dev Requirements 

build scraper using playwright or undetected chrome

```python 
python3 -m venv myenv
source myenv/bin/activate
pip install fastapi uvicorn playwright
playwright install
```

