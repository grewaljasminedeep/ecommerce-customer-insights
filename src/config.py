import os
import yaml
from dotenv import load_dotenv

load_dotenv()

def load_config(path="config/config.yaml"):
    with open(path, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)
    cfg["mysql"]["host"] = os.getenv("MYSQL_HOST", cfg["mysql"]["host"])