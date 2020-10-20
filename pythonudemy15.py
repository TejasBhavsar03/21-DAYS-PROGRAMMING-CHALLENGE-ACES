import os

list_os = os.walk('C:\\Users\\mohsi\\PycharmProjects\\PAIOM')

for root, direct, files in list_os:
    # print(root)
    # for i in direct:
    #  print(i)
    for j in files:
        if 'Lists.py' in j:
            print(j)
        # print(j)

# Mega Brain Easter Skull Crawler Exercise
# Final





def list_dirouter(s):
    # Enclosed Scope
    def dir_list(d):
        # Local
        nonlocal tab_stop
        files = os.listdir(d)
        for f in files:
            current_dir = os.path.join(d, f)
            if os.path.isdir(current_dir):
                print('\t' * tab_stop + 'directory' + f)
                tab_stop += 1
                dir_list(current_dir)
                tab_stop -= 1
            else:
                print(f)

    tab_stop = 0
    if os.path.exists(s):
        print('Directory Listing of ' + s)
        dir_list(s)
    else:
        print(s + 'Directory Does not exist')


list_dirouter('C:\\Users\\mohsi\\PycharmProjects\\PAIOM')