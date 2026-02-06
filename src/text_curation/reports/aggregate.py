from collections import defaultdict


def aggregate_reports(reports):
    """
    Aggregate a list of per-sample curation reports into a single
    dataset-level summary.

    Assumes TOTAL schema: all expected keys are always present.
    """

    agg_input = defaultdict(int)
    agg_output = defaultdict(int)
    agg_block_stats = defaultdict(lambda: defaultdict(int))
    agg_signals = defaultdict(int)

    for r in reports:
        # Input stats
        for key, value in r["input_stats"].items():
            agg_input[key] += value

        # Output stats
        for key, value in r["output_stats"].items():
            agg_output[key] += value

        # Block stats (always present, may be empty)
        for block, stats in r["block_stats"].items():
            for key, value in stats.items():
                agg_block_stats[block][key] += value

        # Signals summary (always present, may be empty)
        for key, value in r["signals_summary"].items():
            agg_signals[key] += value

    return {
        "samples": len(reports),
        "input_stats": dict(agg_input),
        "output_stats": dict(agg_output),
        "block_stats": {
            block: dict(stats)
            for block, stats in agg_block_stats.items()
        },
        "signals_summary": dict(agg_signals),
    }