from google.genai import types
def make_function_schema(name: str, description: str, params: dict):
    return types.FunctionDeclaration(
        name=name,
        description=description,
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                key: types.Schema(
                    type=value["type"],
                    description=value["description"],
                    items=types.Schema(type=value["items"]["type"]) if "items" in value else None
                )
                for key, value in params.items()
            }
        ),
    )
