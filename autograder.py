from BoundedMSTProblem import BoundedMSTProblem as bm


for i in range(1,21):
    inst = bm.from_file('../test_files/input{0:0>2}.txt'.format(i))
    e, cost = inst.score_file('../outputs_2023_05_15/output{0:0>2}.txt'.format(i))

    print("Results for test", i, "are", e, cost)