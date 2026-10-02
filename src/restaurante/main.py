from fastapi import FastAPI, HTTPException


app = FastAPI(title="API Restaurante", description="API para gestión de restaurante", version="0.0.1")


# --- DATOS DE EJEMPLO EN MEMORIA (FASE 1) ---

CATEGORIAS = [
    {"id": 1, "nombre": "Bebidas"},
    {"id": 2, "nombre": "Entrantes"},
    {"id": 3, "nombre": "Platos Principales"},
    {"id": 4, "nombre": "Postres"}
]

MESAS = [

    {"id": 1, "nombre": "Mesa 1"},
    {"id": 2, "nombre": "Mesa 2"},

    {"id": 3, "nombre": "Mesa 3"},

    {"id": 4, "nombre": "Mesa 4"}

]


PRODUCTOS = [

    {"id": 1, "nombre": "Coca Cola", "category_id": 1},

    {"id": 2, "nombre": "Agua Mineral", "category_id": 1},

    {"id": 3, "nombre": "Patatas Bravas", "category_id": 2},

    {"id": 4, "nombre": "Croquetas de Jamón", "category_id": 2},

    {"id": 5, "nombre": "Hamburguesa de la Casa", "category_id": 3},

    {"id": 6, "nombre": "Tarta de Queso", "category_id": 4}

]


# --- ENDPOINTS ---


@app.get("/health", tags=["Sistema"])

def check_health():

    """Confirma que la API funciona correctamente."""

    return {"status": "ok", "message": "El servidor del restaurante está operativo"}


@app.get("/categories", tags=["Carta"])

def get_categories():

    """Devuelve las categorías de ejemplo de la carta."""

    return CATEGORIAS

@app.get("/tables", tags=["Mesas"])
def get_tables():
    """Devuelve las mesas dadas de alta en el sistema."""
    return MESAS


@app.get("/categories/{category_id}/products", tags=["Carta"])

def get_products_by_category(category_id: int):

    """Devuelve los productos pertenecientes a una categoría específica."""

    productos_filtrados = [p for p in PRODUCTOS if p["category_id"] == category_id]
    

    # Si la categoría no tiene productos o no existe, lanzamos un 404 opcional

    if not productos_filtrados:

        # Verificamos si al menos la categoría existe

        if not any(c["id"] == category_id for c in CATEGORIAS):

            raise HTTPException(status_code=404, detail="Categoría no encontrada")
    

    return productos_filtrados