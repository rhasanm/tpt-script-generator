from abc import ABC
from tpt_script_generator.enums import AttributeType

class Operator(ABC):
    def __init__(self, operator_name, operator_type):
        self.operator_name = operator_name
        self.operator_type = operator_type
        self.schema_name = ""
        self.attributes = {}

    def with_schema(self, schema_name):
        self.schema_name = schema_name
        return self

    def with_attribute(self, attr_type: AttributeType, attr_key, attr_value):
        self.attributes[attr_key] = (attr_type.value, attr_value)
        return self

    def build(self):
        definition = f"    DEFINE OPERATOR {self.operator_name}\n"
        definition += f"    TYPE {self.operator_type}\n"
        if self.schema_name:
            definition += f"    SCHEMA {self.schema_name}\n"
        if self.attributes:
            definition += "    ATTRIBUTES\n    (\n"
            for attr_key, (attr_type, attr_value) in self.attributes.items():
                if attr_type != AttributeType.VARCHAR.value or attr_value.startswith("@"):
                    definition += f"        {attr_type} {attr_key} = {attr_value},\n"
                else:
                    definition += f"        {attr_type} {attr_key} = '{attr_value}',\n"

            definition = definition.rstrip(",\n")
            definition += "\n    );\n"
        return definition

