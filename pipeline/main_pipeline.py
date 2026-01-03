from extractors import Extract_From_Zip


def run_pipeline():
    file_extractor = Extract_From_Zip()
    file_extractor.extract()


if __name__ ==  '__main__':
    run_pipeline()