import os
import sqlite3
import click
import subprocess
import tempfile


@click.command()
@click.argument('file1', type=click.Path())
@click.argument('file2', type=click.Path())
def cli(file1, file2):
    """Compares two sqlite .db files by dumping their contents and comparing"""

    bcomp_path = "C:\Program Files\Beyond Compare 4\BComp.exe"
    tmp_dir = tempfile.gettempdir()
    file1_tmp = os.path.join(tmp_dir + os.path.basename(file1))
    file2_tmp = os.path.join(tmp_dir + os.path.basename(file2))

    # Dump databases to temporary files
    dump_sqllite_db(file1, file1_tmp)
    dump_sqllite_db(file2, file2_tmp)

    # Open diff in beyond compare
    tmp = subprocess.Popen([bcomp_path, file1_tmp, file2_tmp])
    tmp.wait()

    os.remove(file1_tmp)
    os.remove(file2_tmp)


def dump_sqllite_db(db, output_file):
    con = sqlite3.connect(db)
    with open(output_file, 'w') as f:
        for line in con.iterdump():
            f.write('%s\n' % line)
    con.close()


if __name__ == '__main__':
    cli()
