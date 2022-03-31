import sys
import sqlite3

def main():
    dump_sqllite_db('test/test-db.db', 'test/dump.sql')


def dump_sqllite_db(db, output_file):
    con = sqlite3.connect(db)
    with open(output_file, 'w') as f:
        for line in con.iterdump():
            f.write('%s\n' % line)
    con.close()


if __name__ == '__main__':
    main()