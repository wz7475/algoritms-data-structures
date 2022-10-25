from utils.benchmark import BenchmarkManager


def test_benchmark_naive():
    mgr = BenchmarkManager()
    mgr.benchmark()