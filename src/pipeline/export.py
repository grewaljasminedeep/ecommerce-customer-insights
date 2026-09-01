from src.export_powerbi import export_all

def run_export(cfg, category_df, clv_df, affinity_df):
    export_all(cfg["pipeline"]["export_dir"], category_df, clv_df, affinity_df)