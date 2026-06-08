from pydantic import BaseModel

class CategoriaBase(BaseModel):
    nome: str
    descricao: str | None = None

class ProdutoBase(BaseModel):
    nome: str
    preco: float
    estoque: int
    categoria_id: int