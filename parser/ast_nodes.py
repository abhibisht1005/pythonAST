class ASTNode:
    """Base class for all AST nodes"""
    def print_node(self, indent=0):
        """Print this node with the specified indentation level"""
        raise NotImplementedError("Each AST node must implement print_node")


class IntLiteralNode(ASTNode):
    """Node for integer literals"""
    def __init__(self, value):
        self.value = value
    
    def print_node(self, indent=0):
        print(' ' * indent + f"IntLiteral({self.value})")


class FloatLiteralNode(ASTNode):
    """Node for float literals"""
    def __init__(self, value):
        self.value = value
    
    def print_node(self, indent=0):
        print(' ' * indent + f"FloatLiteral({self.value})")


class StringLiteralNode(ASTNode):
    """Node for string literals"""
    def __init__(self, value, is_f_string=False):
        self.value = value
        self.is_f_string = is_f_string
    
    def print_node(self, indent=0):
        node_type = "FString" if self.is_f_string else "StringLiteral"
        print(' ' * indent + f'{node_type}("{self.value}")')


class BoolLiteralNode(ASTNode):
    """Node for boolean literals"""
    def __init__(self, value):
        self.value = value
    
    def print_node(self, indent=0):
        print(' ' * indent + f"BoolLiteral({str(self.value)})")


class NoneLiteralNode(ASTNode):
    """Node for None literal"""
    def print_node(self, indent=0):
        print(' ' * indent + "None")


class IdentifierNode(ASTNode):
    """Node for identifiers"""
    def __init__(self, name):
        self.name = name
    
    def print_node(self, indent=0):
        print(' ' * indent + f"Identifier({self.name})")


class BinaryOpNode(ASTNode):
    """Node for binary operations"""
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right
    
    def print_node(self, indent=0):
        print(' ' * indent + f"BinaryOp({self.op})")
        self.left.print_node(indent + 2)
        self.right.print_node(indent + 2)


class AssignmentNode(ASTNode):
    """Node for assignment statements"""
    def __init__(self, target, value):
        self.target = target
        self.value = value
    
    def print_node(self, indent=0):
        print(' ' * indent + "Assignment")
        print(' ' * (indent + 2) + "Target:")
        self.target.print_node(indent + 4)
        print(' ' * (indent + 2) + "Value:")
        self.value.print_node(indent + 4)


class FunctionCallNode(ASTNode):
    """Node for function calls"""
    def __init__(self, callable_obj, arguments=None, keyword_args=None):
        self.callable = callable_obj
        self.arguments = arguments or []
        self.keyword_args = keyword_args or {}
    
    def print_node(self, indent=0):
        print(' ' * indent + "FunctionCall")
        print(' ' * (indent + 2) + "Callable:")
        self.callable.print_node(indent + 4)
        
        if self.arguments:
            print(' ' * (indent + 2) + "Arguments:")
            for arg in self.arguments:
                arg.print_node(indent + 4)
        
        if self.keyword_args:
            print(' ' * (indent + 2) + "Keyword Arguments:")
            for key, value in self.keyword_args.items():
                print(' ' * (indent + 4) + f"{key}:")
                value.print_node(indent + 6)


class ParameterNode(ASTNode):
    """Node for function parameters"""
    def __init__(self, name, default_value=None, is_keyword_only=False):
        self.name = name
        self.default_value = default_value
        self.is_keyword_only = is_keyword_only
    
    def print_node(self, indent=0):
        param_info = self.name
        if self.is_keyword_only:
            param_info += ", keyword-only"
        print(' ' * indent + f"Parameter({param_info})")
        
        if self.default_value:
            print(' ' * (indent + 2) + "Default Value:")
            self.default_value.print_node(indent + 4)


class FunctionDefNode(ASTNode):
    """Node for function definitions"""
    def __init__(self, name, parameters=None, body=None):
        self.name = name
        self.parameters = parameters or []
        self.body = body or []
    
    def print_node(self, indent=0):
        print(' ' * indent + f"FunctionDef({self.name})")
        
        print(' ' * (indent + 2) + "Parameters:")
        for param in self.parameters:
            param.print_node(indent + 4)
        
        print(' ' * (indent + 2) + "Body:")
        for stmt in self.body:
            stmt.print_node(indent + 4)


class ClassDefNode(ASTNode):
    """Node for class definitions"""
    def __init__(self, name, bases=None, body=None):
        self.name = name
        self.bases = bases or []
        self.body = body or []
    
    def print_node(self, indent=0):
        print(' ' * indent + f"ClassDef({self.name})")
        
        if self.bases:
            print(' ' * (indent + 2) + "Bases:")
            for base in self.bases:
                base.print_node(indent + 4)
        
        print(' ' * (indent + 2) + "Body:")
        for stmt in self.body:
            stmt.print_node(indent + 4)


class ReturnNode(ASTNode):
    """Node for return statements"""
    def __init__(self, value=None):
        self.value = value
    
    def print_node(self, indent=0):
        print(' ' * indent + "Return")
        if self.value:
            self.value.print_node(indent + 2)


class ImportNode(ASTNode):
    """Node for import statements"""
    def __init__(self, module, alias=""):
        self.module = module
        self.alias = alias
    
    def print_node(self, indent=0):
        import_info = self.module
        if self.alias:
            import_info += f" as {self.alias}"
        print(' ' * indent + f"Import({import_info})")


class FromImportNode(ASTNode):
    """Node for from ... import statements"""
    def __init__(self, module, imports=None):
        self.module = module
        self.imports = imports or []  # List of (name, alias) tuples
    
    def print_node(self, indent=0):
        print(' ' * indent + f"FromImport({self.module})")
        print(' ' * (indent + 2) + "Names:")
        for name, alias in self.imports:
            import_info = name
            if alias:
                import_info += f" as {alias}"
            print(' ' * (indent + 4) + import_info)


class IfNode(ASTNode):
    """Node for if statements"""
    def __init__(self, condition, then_body=None, else_body=None):
        self.condition = condition
        self.then_body = then_body or []
        self.else_body = else_body or []
    
    def print_node(self, indent=0):
        print(' ' * indent + "If")
        
        print(' ' * (indent + 2) + "Condition:")
        self.condition.print_node(indent + 4)
        
        print(' ' * (indent + 2) + "Then:")
        for stmt in self.then_body:
            stmt.print_node(indent + 4)
        
        if self.else_body:
            print(' ' * (indent + 2) + "Else:")
            for stmt in self.else_body:
                stmt.print_node(indent + 4)


class WhileNode(ASTNode):
    """Node for while loops"""
    def __init__(self, condition, body=None):
        self.condition = condition
        self.body = body or []
    
    def print_node(self, indent=0):
        print(' ' * indent + "While")
        
        print(' ' * (indent + 2) + "Condition:")
        self.condition.print_node(indent + 4)
        
        print(' ' * (indent + 2) + "Body:")
        for stmt in self.body:
            stmt.print_node(indent + 4)


class ForNode(ASTNode):
    """Node for for loops"""
    def __init__(self, target, iterable, body=None):
        self.target = target
        self.iterable = iterable
        self.body = body or []
    
    def print_node(self, indent=0):
        print(' ' * indent + "For")
        
        print(' ' * (indent + 2) + "Target:")
        self.target.print_node(indent + 4)
        
        print(' ' * (indent + 2) + "Iterable:")
        self.iterable.print_node(indent + 4)
        
        print(' ' * (indent + 2) + "Body:")
        for stmt in self.body:
            stmt.print_node(indent + 4)


class AttributeNode(ASTNode):
    """Node for attribute access (e.g., obj.attr)"""
    def __init__(self, value, attr):
        self.value = value
        self.attr = attr
    
    def print_node(self, indent=0):
        print(' ' * indent + f"Attribute({self.attr})")
        print(' ' * (indent + 2) + "Value:")
        self.value.print_node(indent + 4)


class ListNode(ASTNode):
    """Node for list literals"""
    def __init__(self, elements=None):
        self.elements = elements or []
    
    def print_node(self, indent=0):
        print(' ' * indent + "List")
        
        if self.elements:
            print(' ' * (indent + 2) + "Elements:")
            for element in self.elements:
                element.print_node(indent + 4)


class DictNode(ASTNode):
    """Node for dictionary literals"""
    def __init__(self, items=None):
        self.items = items or []  # List of (key, value) tuples
    
    def print_node(self, indent=0):
        print(' ' * indent + "Dict")
        
        if self.items:
            print(' ' * (indent + 2) + "Items:")
            for key, value in self.items:
                print(' ' * (indent + 4) + "Key:")
                key.print_node(indent + 6)
                print(' ' * (indent + 4) + "Value:")
                value.print_node(indent + 6)


class SubscriptNode(ASTNode):
    """Node for subscript access (e.g., list[index])"""
    def __init__(self, value, index):
        self.value = value
        self.index = index
    
    def print_node(self, indent=0):
        print(' ' * indent + "Subscript")
        print(' ' * (indent + 2) + "Value:")
        self.value.print_node(indent + 4)
        print(' ' * (indent + 2) + "Index:")
        self.index.print_node(indent + 4)


class PassNode(ASTNode):
    """Node for pass statements"""
    def print_node(self, indent=0):
        print(' ' * indent + "Pass")


class BreakNode(ASTNode):
    """Node for break statements"""
    def print_node(self, indent=0):
        print(' ' * indent + "Break")


class ContinueNode(ASTNode):
    """Node for continue statements"""
    def print_node(self, indent=0):
        print(' ' * indent + "Continue")