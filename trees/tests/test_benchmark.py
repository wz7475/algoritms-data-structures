from utils.benchmark import BenchmarkManager


def test_benchmark_fill():
    mgr = BenchmarkManager()
    mgr.fill_benchmark()


def test_benchmark_find():
    mgr = BenchmarkManager()
    mgr.find_benchmark()


def test_benchmark_delete():
    mgr = BenchmarkManager()
    mgr.delete_benchmark()
