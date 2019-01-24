# shopify-challenge

Basic REST API for an ecommerce site from the shopify challenge (Spring 2019)

**Basic Setup:** <br/>
Clone repository, and create a virtual environment in the project directory. Then run
```
pip install -r requirements.txt
```
Run these commands in order

```
python manage.py migrate
python populate.py
python manage.py runserver
```
Now the development server should be up and running

**API Endpoints:** <br/>
Host is your local machine, and the port is by default 8000
```
GET /api/item - returns an item with 'id' (GET parameter)
GET /api/list - returns a listing of items (optional in_stock=[true, false] parameter and sort=[(-)name, (-)inventory])
GET /api/purchase - returns an item with 'id' after a purchase update
```
