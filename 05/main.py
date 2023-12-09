FILE_NAME="input05.txt"

def load_file(file_name):
    file=open(file_name, "r")
    return file.read()



if __name__=="__main__":
    seeds, *others = load_file(FILE_NAME).split("\n\n")
    seeds = list(map(lambda x: int(x), seeds.split(":")[1].split()))
    print (seeds)
    
    for item in others:
        intervals = []
        for i in item.split("\n")[1:]:
            intervals.append(list(map(lambda x: int(x), i.split())))
        print (intervals)
        new_seeds = []
        for seed in seeds:
            for start_source, start_desc, increment in intervals:
                if start_desc <= seed< start_desc + increment:
                    new_seeds.append(seed - start_desc + start_source)
                    break
            else:
                new_seeds.append(seed)
        seeds = new_seeds

    print (min(seeds))