from pipeline.pipeline import TestPipeline

if __name__ == '__main__':
    p = TestPipeline()
    output = p.execute()
    print(output)
