from os import path

def output(results, **kwargs):
    '''Reformats data (mostly) in accordance to requested file format'''

    lines = []
    for i in range(1, len(results)+1):
        node = '#{}'.format(i)
        res = [int(x.strip('#')) for x in results[node]]
        lines.append(
            node + ', ' + 'neighbors=' + str(len(res)) + ', ' 
            + str(sorted(res))
        )
    
    if kwargs['output'] == 'print':
        for line in lines:
            print(line)

    else:
        try:
            with open(path.join(kwargs['output'], 'NNA_results.txt'), 'w') as w:
                w.writelines(
                    [x+'\n' if x != lines[-1] else x
                    for x in lines]
            )
        except: AssertionError(
            '\n\n output path should be formatted as /path/to/directory'
        )

