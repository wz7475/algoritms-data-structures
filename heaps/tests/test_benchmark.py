from utils.benchmark import BenchmarkManager


def test_benchmark_fill():
    mgr = BenchmarkManager()
    mgr.init_benchmark()


def test_benchmark_remove():
    mgr = BenchmarkManager()
    mgr.remove_benchmark()
