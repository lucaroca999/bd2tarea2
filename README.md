# Tarea 2 - API de Gestión de Biblioteca

## Descripción
Extensión de una API REST utilizando Litestar y SQLAlchemy. Se han implementado nuevos modelos (Category, Review), lógica de negocio avanzada para préstamos y stock, y validaciones estrictas mediante DTOs.

## Estado de Requerimientos

| Req | Descripción | Estado | Observación |
|---|---|---|---|
| 1 | Modelo Category | ✅ Cumplido | Relación Many-to-Many con Book implementada. |
| 2 | Modelo Review | ✅ Cumplido | Validaciones de rating (1-5) y límite de reseñas. |
| 3 | Actualizar Book | ✅ Cumplido | Gestión de stock, idiomas ISO y validaciones. |
| 4 | Actualizar User | ✅ Cumplido | Validación de email con Regex, campos extra agregados. |
| 5 | Actualizar Loan | ✅ Cumplido | Estados (Enum), fechas y multas. |
| 6 | Repo Book | ✅ Cumplido | Búsquedas por autor/categoría y gestión de stock. |
| 7 | Repo Loan | ✅ Cumplido | Cálculo de multas ($500/día), devoluciones y reportes. |
| 8 | Datos Iniciales | ✅ Cumplido | Script de seed incluido y dump SQL generado. |

## Ejecución
1. Instalar dependencias: `pip install -e .`
2. Migraciones: `alembic upgrade head`
3. Poblar datos (opcional): `python seed_data.py`
4. Correr servidor: `litestar run --reload`