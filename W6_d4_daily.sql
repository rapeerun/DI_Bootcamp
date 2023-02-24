
CREATE TABLE product_orders (
  order_id INTEGER PRIMARY KEY,
  user_id INTEGER,
  order_date DATE,
  delivery_address VARCHAR(100)
);

CREATE TABLE items (
  item_id INTEGER PRIMARY KEY,
  order_id INTEGER,
  name VARCHAR(50),
  price DECIMAL(8, 2),
  FOREIGN KEY (order_id) REFERENCES product_orders(order_id)
);

CREATE TABLE users (
  user_id INTEGER PRIMARY KEY,
  name VARCHAR(50)
);


-- Function to return the total price for a given order
CREATE FUNCTION total_order_price(order_id INTEGER) RETURNS DECIMAL(8, 2)
BEGIN
  DECLARE @ (total_price DECIMAL(8, 2)
  SELECT SUM(price) INTO total_price FROM items WHERE order_id = order_id;
  RETURN total_price;
END;

