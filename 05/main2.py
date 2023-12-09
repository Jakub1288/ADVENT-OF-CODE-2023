FILE_NAME="input05.txt"

def load_file(file_name):
    file=open(file_name, "r")
    return file.read()



if __name__=="__main__":
    t_seeds, *others = load_file(FILE_NAME).split("\n\n")
    t_seeds = list(map(lambda x: int(x), t_seeds.split(":")[1].split()))
    seeds = []
    for i in range(0, len(t_seeds)-1, 2):
        seeds.append((t_seeds[i], t_seeds[i] + t_seeds[i+1]))

    for slice in others:
        intervals = []
        for l in slice.split('\n')[1:]:
            intervals.append(list(map(lambda x:int(x), l.split())))
        new_seed = []
        while seeds:
            start, end = seeds.pop()
            for start_des, start_sour, increment in intervals:
                if start > start_sour:
                    overlap_start = start
                else:
                    overlap_start = start_sour
                if end < start_sour + increment:
                    overlap_end = end
                else:
                    overlap_end = start_sour + increment
                if overlap_start < overlap_end:
                    new_seed.append((overlap_start - start_sour + start_des, overlap_end -start_sour + start_des))
                    if overlap_start > start:
                        seeds.append((start, overlap_start))
                    if overlap_end < end:
                        seeds.append((overlap_end, end))
                    break
            else:
                new_seed.append((start,end))
        seeds=new_seed
    min = seeds[0][0]
    for x, _ in seeds:
        if x < min:
            min = x

    print(min)
