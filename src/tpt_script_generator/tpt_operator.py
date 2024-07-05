from tpt_script_generator.enums import AttributeType

from abc import ABC, abstractmethod


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

    @abstractmethod
    def build(self):
        pass
