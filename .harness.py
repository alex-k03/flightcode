
import json, sys, importlib.util

code_path, func_name, case_json = sys.argv[1], sys.argv[2], sys.argv[3]
spec = importlib.util.spec_from_file_location("solution", code_path)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

fn = getattr(mod, func_name, None)
if fn is None:
    print(json.dumps({"error": f"function '{func_name}' not found in code.py"}))
    sys.exit(2)

case = json.loads(case_json)
try:
    result = fn(**case["input"])
    print(json.dumps({"result": result}))
except Exception as e:
    print(json.dumps({"error": f"{type(e).__name__}: {e}"}))
    sys.exit(1)
