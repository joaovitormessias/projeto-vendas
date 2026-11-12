"""Exercise UI contracts without importing provider or starting Gradio."""
import ast
from pathlib import Path
import unittest

class CallbackTests(unittest.TestCase):
    def test_empty_pdf_returns_no_file(self):
        tree = ast.parse((Path(__file__).parents[1] / "app.py").read_text())
        function = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == "gerar_pdf")
        namespace = {}
        exec(compile(ast.Module(body=[function], type_ignores=[]), "app.py", "exec"), namespace)
        self.assertIsNone(namespace["gerar_pdf"]([]))
        self.assertIsNone(namespace["gerar_pdf"](None))
