from locust import HttpUser, between, task
from random import randint

# PERFOMANCE TEST
# run--> locust -f locustfiles/browse_products.py


class WebsiteUser(HttpUser):

    # weight 1 to 5 seconds b/w each task
    weight_time = between(1, 5)

    # task(2) : 2 is the weight ,arbitrary number ,based on the priority.
    @task(2)
    def view_products(self):
        print('View products')
        collection_id = randint(2, 6)
        # view products in a perticular collection
        self.client.get(f'/store/products/?collection_id={collection_id}',
                        name='/store/products')

    @task(4)
    def view_product(self):
        print('View product details')
        product_id = randint(1, 1000)
        # view a specific product
        self.client.get(f'/store/products/{product_id}/',
                        name='/store/products/:id')

    @task(1)
    def add_to_cart(self):
        print('Add to cart')
        product_id = randint(1, 10)
        self.client.post(f'/store/carts/{self.cart_id}/items/',
                         name='/store/carts/items',
                         json={'product_id': product_id, 'quantity': 1}
                         )

    # life cycle hook , called every time a new user start browse the  website.
    # here we impliment this for create cart.
    def on_start(self):
        response = self.client.post('/store/carts/')
        result = response.json()
        self.cart_id = result['id']
