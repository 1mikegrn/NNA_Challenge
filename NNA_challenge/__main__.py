import NNA_Challenge

def main():
    '''
    Main entry point for NNA_Challenge CLI input. Parses command line inputs, 
    runs the calculation, and toggles the output protocol.
    '''
    input_file, radius, kwargs = NNA_Challenge.src.tools.cmd_reader.reader()

    results = NNA_Challenge.src.calculate.calculate(
        input_file, radius, **kwargs
    )

    NNA_Challenge.src.tools.output.output(results, **kwargs)

if __name__ == "__main__":
    main()