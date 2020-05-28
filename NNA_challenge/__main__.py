import NNA_challenge

def main():
    '''
    Main entry point for NNA_challenge CLI input. Parses command line inputs, 
    runs the calculation, and toggles the output protocol.
    '''
    input_file, radius, kwargs = NNA_challenge.src.tools.cmd_reader.reader()

    results = NNA_challenge.src.calculate.calculate(
        input_file, radius, **kwargs
    )

    NNA_challenge.src.tools.output.output(results, **kwargs)

if __name__ == "__main__":
    main()