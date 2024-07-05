class TPTSchemaGenerator:
    def __init__(self, name, schema_dict, description=''):
        self.name = name
        self.schema_dict = schema_dict
        self.description = description

    def generate_schema(self):
        schema_lines = [f"DEFINE SCHEMA {self.name.upper()}"]
        
        if self.description:
            schema_lines.append(f"DESCRIPTION '{self.description}'")
        
        schema_lines.append("(")
        
        for field_name, field_type in self.schema_dict.items():
            schema_lines.append(f"    {field_name.upper():<15} {field_type.upper()},")
        
        if schema_lines[-1].endswith(","):
            schema_lines[-1] = schema_lines[-1][:-1]
        
        schema_lines.append(");")
        
        return "\n".join(schema_lines)
