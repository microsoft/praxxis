import re
import subprocess


def collect_mtool_sequences(mtool_ipynb_dir='/mtool/ipynb'):
    """
    collect the sequences for all users and all scenes.
    should we record user/scene/time info for training?
    """

    hdfs_ls = 'hdfs dfs -ls -C '
    users = subprocess.check_output(hdfs_ls + mtool_ipynb_dir, shell=True).strip().decode().split('\n')

    sequences = []

    for user in users:
        print(user)
        scenes = subprocess.check_output(hdfs_ls + user, shell=True).strip().decode().split('\n')

        for scene in scenes:
            print(scene)
            notebooks = subprocess.check_output(hdfs_ls + scene, shell=True).strip().decode().split('\n')
            sequences += list(map(lambda nb: re.match(r".+\/(.+) -.+", nb).group(1), notebooks)),

    return sequences


# from pprint import pprint
# sequences = collect_sequences()
# pprint(sequences, width=1e3)


sequences = [
    ['SOP023', 'SOP023', 'SOP023'],
    ['TSG015', 'TSG021'],
    ['SOP003'],
    ['SOP002', 'SOP013'],
    ['ES001', 'ES001', 'ES001', 'ES001', 'ES001', 'ES001', 'ES001', 'ES001', 'ES001', 'ES001', 'ES001', 'ES001', 'ES001', 'ES001', 'SOP003', 'SOP027', 'SOP027'],
    ['TSG015'],
    ['ES001', 'ES001', 'ES001', 'ES001', 'ES001', 'ES001', 'ES001', 'ES001', 'ES001', 'ES001', 'ES002', 'SOP028', 'SOP028', 'SOP028', 'SOP028', 'SOP028', 'SOP028', 'SOP028', 'SOP028', 'SOP028', 'SOP028'],
    ['ES002', 'ES002', 'ES002', 'ES002', 'ES002', 'ES002'],
    ['ES001', 'TSG015'],
    ['SOP002', 'SOP003', 'SOP003', 'SOP022'],
    ['ES001', 'ES002', 'ES002', 'ES002', 'ES002', 'ES002', 'ES002', 'ES002'],
    ['SOP003'],
    ['ES002', 'ES002'],
    ['ES002', 'ES002', 'ES002', 'ES002', 'ES002', 'ES002', 'ES002', 'ES002', 'ES002', 'ES002', 'ES002', 'ES002', 'ES002', 'ES002'],
    ['MAKE001', 'TSG015'],
    ['SOP003'],
    ['SOP001', 'TSG001', 'TSG020', 'TSG021'],
    ['ES001', 'ES001', 'ES001', 'ES001', 'ES001', 'ES001', 'ES001', 'ES001', 'ES001', 'ES001', 'ES001', 'ES001', 'ES002', 'ES002', 'ES002', 'ES002', 'ES002', 'ES002', 'ES002', 'ES002', 'ES002', 'ES002', 'ES002', 'ES002', 'ES002', 'ES002', 'ES002', 'ES002', 'ES002', 'ES002', 'ES002', 'ES002', 'ES002', 'ES002', 'ES002', 'ES002', 'ES002', 'ES002', 'ES002', 'ES002', 'ES002', 'ES002', 'ES002', 'ES003', 'SOP002', 'SOP002', 'SOP002', 'SOP003', 'SOP023', 'SOP027'],
    ['SOP003'],
    ['ES001'],
    ['ES002', 'ES002', 'ES003', 'ES003', 'SOP002', 'SOP003', 'SOP003', 'SOP003', 'SOP003', 'SOP027', 'SOP027', 'SOP027', 'TSG024', 'TSG024']
]
