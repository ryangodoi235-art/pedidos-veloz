CREATE TABLE IF NOT EXISTS pedidos (
    id SERIAL PRIMARY KEY,
    cliente_id INTEGER NOT NULL,
    itens TEXT,
    total DECIMAL(10,2),
    status VARCHAR(50)
);
