import os
import yaml
from dotenv import load_dotenv

load_dotenv()

def load_config(path="config/config.yaml"):
    with open(path, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)
    cfg["mysql"]["host"] = os.getenv("MYSQL_HOST", cfg["mysql"]["host"])
    cfg["mysql"]["port"] = int(os.getenv("MYSQL_PORT", cfg["mysql"]["port"]))
    cfg["mysql"]["user"] = os.getenv("MYSQL_USER", cfg["mysql"]["user"])
    cfg["mysql"]["password"] = os.getenv("MYSQL_PASSWORD", cfg["mysql"]["password"])
    cfg["mysql"]["database"] = os.getenv("MYSQL_DATABASE", cfg["mysql"]["database"])
    cfg["neo4j"]["uri"] = os.getenv("NEO4J_URI", cfg["neo4j"]["uri"])
    cfg["neo4j"]["user"] = os.getenv("NEO4J_USER", cfg["neo4j"]["user"])
    cfg["neo4j"]["password"] = os.getenv("NEO4J_PASSWORD", cfg["neo4j"]["password"])
    cfg["pipeline"]["export_dir"] = os.getenv("EXPORT_DIR", cfg["pipeline"]["export_dir"])
    return cfg