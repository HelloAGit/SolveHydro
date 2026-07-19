import argparse
from .core import metrics
from .formulas import routing

def main():
    parser = argparse.ArgumentParser(prog="hydrocomplex", description="Hydrocomplex CLI")
    sub = parser.add_subparsers(dest="cmd")

    t = sub.add_parser("metrics", help="Compute hydrologic metrics")
    t.add_argument("--obs", required=True, help="CSV file with observed series (single column)")
    t.add_argument("--sim", required=True, help="CSV file with simulated series (single column)")

    r = sub.add_parser("muskingum", help="Run Muskingum routing from CSV inflow")
    r.add_argument("--inflow", required=True, help="CSV inflow series")
    r.add_argument("--k", type=float, default=1.0)
    r.add_argument("--x", type=float, default=0.2)

    args = parser.parse_args()
    if args.cmd == "metrics":
        import pandas as pd
        obs = pd.read_csv(args.obs, header=None).squeeze()
        sim = pd.read_csv(args.sim, header=None).squeeze()
        print("NSE:", metrics.nse(obs, sim))
        print("KGE:", metrics.kge(obs, sim))
    elif args.cmd == "muskingum":
        import pandas as pd
        inflow = pd.read_csv(args.inflow, header=None).squeeze()
        out = routing.muskingum_routing(inflow.values, k=args.k, x=args.x)
        print("Routed series length:", len(out))
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

