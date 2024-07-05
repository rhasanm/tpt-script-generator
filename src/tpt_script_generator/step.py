class Step:
    def __init__(self, name, operations=None):
        self.name = name
        self.operations = operations if operations else []

    def add_operation(self, operation):
        self.operations.append(operation)
        return self

    def build(self):
        step_content = f"    STEP {self.name}\n    (\n"
        for operation in self.operations:
            step_content += f"        {operation}\n"
        step_content += "    );\n"
        return step_content
