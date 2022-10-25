from utils.benchmark import BenchmarkManager


def main():
    print("Beginning pattern searching time comparison...");

    mgr = BenchmarkManager()
    mgr.benchmark()


if __name__ == "__main__":
    main()
