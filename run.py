from datetime import datetime
from pathlib import Path
import subprocess


for path in sorted(Path(".").glob("p*.py")):
    start = datetime.now()
    output = subprocess.check_output(["python", str(path)]).strip().decode()
    seconds = (datetime.now() - start).total_seconds()
    print(f"{path.name}: {output: <20} ({seconds:.2f}s)")
