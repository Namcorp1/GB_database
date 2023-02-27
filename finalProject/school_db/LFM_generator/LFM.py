# male = open('LFM_male.txt','r')
# female = open('LFM_female.txt','r')
# lnm = []
# fnm = []
# mnm = []
# lnf = []
# fnf = []
# mnf = []
# for line in male:
#     data = line.split(' ')
#     lnm.append(data[0])
#     fnm.append(data[1])
#     mnm.append(data[2][:len(data[2])-1])
# for line in female:
#     data = line.split(' ')
#     lnf.append(data[0])
#     fnf.append(data[1])
#     mnf.append(data[2][:len(data[2])-1])

teachers = open('LFM_teachers.txt','r')
lnt = []
fnt = []
mnt = []
gt = []
for line in teachers:
    data = line.split(' ')
    lnt.append(data[0])
    fnt.append(data[1])
    mnt.append(data[2])
    gt.append(data[3][:len(data[3])-1])