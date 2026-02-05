def dedupe_report(report: dict):
    """
    Pretty-print a dataset-level deduplication report.
    """

    print("Dataset Deduplication Report")
    print("=" * 28)
    print()

    print(f"Operation:   {report['operation']}")
    print(f"Scope:       {report['scope']}")
    print(f"Column:      {report['column']}")
    print()

    strategy = report["strategy"]
    print("Strategy:")
    print(f"  Type:           {strategy['type']}")
    print(f"  Normalization:  {strategy['normalization'] or 'none'}")
    print()

    policy = report["policy"]
    print("Policy:")
    print(f"  Keep:           {policy['keep']}")
    print()

    inp = report["input"]["samples"]
    out = report["output"]["samples"]
    rem = report["removed"]["samples"]
    frac = report["removed"]["fraction"] * 100

    print("Samples:")
    print(f"  Input:          {inp:,}")
    print(f"  Output:         {out:,}")
    print(f"  Removed:        {rem:,} ({frac:.1f}%)")
    print()

    dup = report["duplicates"]
    print("Duplicates:")
    print(f"  Groups:         {dup['groups']:,}")
    print(f"  Max group size: {dup['max_group_size']}")
    print()

    det = report["determinism"]
    print("Determinism:")
    print(f"  Order independent: {'yes' if det['order_independent'] else 'no'}")
    print()

def filter_report(report: dict):
    """
    Pretty-print a dataset-level filtering report.
    """

    print("Dataset Filtering Report")
    print("=" * 26)
    print()

    print(f"Operation:   {report['operation']}")
    print(f"Scope:       {report['scope']}")
    print()
    print("Description:")
    print(f"  {report['description']}")
    print()

    inp = report["input"]["samples"]
    out = report["output"]["samples"]
    rem = report["removed"]["samples"]
    frac = report["removed"]["fraction"] * 100

    print("Samples:")
    print(f"  Input:    {inp:,}")
    print(f"  Output:   {out:,}")
    print(f"  Removed:  {rem:,} ({frac:.1f}%)")
    print()

    det = report["determinism"]
    print("Determinism:")
    print(f"  Predicate assumed pure: yes")
    print()
