import argparse
from src.config import load_config
from src.pipeline.ingest import run_ingest
from src.pipeline.graph import run_graph
from src.pipeline.analyze import run_analyze
from src.pipeline.export import run_export

def main():
    parser = argparse.ArgumentParser(description="E-commerce Customer Insights Pipeline")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("ingest")
    sub.add_parser("graph")
    sub.add_parser("analyze")
    sub.add_parser("export")
    sub.add_parser("run_all")
    args = parser.parse_args()
    cfg = load_config()

    if args.command == "ingest":
        users_df, products_df, orders_df = run_ingest(cfg)
        print(f"Loaded users={len(users_df)}, products={len(products_df)}, orders={len(orders_df)}")
    elif args.command == "graph":
        users_df, products_df, orders_df = run_ingest(cfg)
        run_graph(cfg, users_df, products_df, orders_df)
        print("Neo4j graph updated")
    elif args.command == "analyze":
        users_df, products_df, orders_df = run_ingest(cfg)
        category_df, clv_df, affinity_df = run_analyze(products_df, orders_df)
        print(category_df.head().to_string(index=False))
        print(clv_df.head().to_string(index=False))
        print(affinity_df.head().to_string(index=False))
    elif args.command == "export":
        users_df, products_df, orders_df = run_ingest(cfg)
        category_df, clv_df, affinity_df = run_analyze(products_df, orders_df)
        run_export(cfg, category_df, clv_df, affinity_df)
        print("Exports written")
    elif args.command == "run_all":
        users_df, products_df, orders_df = run_ingest(cfg)
        run_graph(cfg, users_df, products_df, orders_df)
        category_df, clv_df, affinity_df = run_analyze(products_df, orders_df)
        run_export(cfg, category_df, clv_df, affinity_df)
        print("Pipeline completed")

if __name__ == "__main__":
    main()