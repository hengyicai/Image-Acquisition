import sqlite3

DATABASE = './app/db/image_ac.db'


def connect_db():
    return sqlite3.connect(DATABASE)


def query_db(query, args=(), one=False):
    db = connect_db()
    cur = db.execute(query, args)
    rv = [dict((cur.description[idx][0], value)
               for idx, value in enumerate(row)) for row in cur.fetchall()]
    # print(rv)
    db.close()
    return (rv[0] if rv else None) if one else rv


def tail(file_name, lines=20):
    f = open(file_name)
    total_lines_wanted = lines

    BLOCK_SIZE = 1024
    f.seek(0, 2)
    block_end_byte = f.tell()
    lines_to_go = total_lines_wanted
    block_number = -1
    blocks = []  # blocks of size BLOCK_SIZE, in reverse order starting
    # from the end of the file
    while lines_to_go > 0 and block_end_byte > 0:
        if (block_end_byte - BLOCK_SIZE > 0):
            # read the last block we haven't yet read
            f.seek(block_number * BLOCK_SIZE, 2)
            blocks.append(f.read(BLOCK_SIZE))
        else:
            # file too small, start from begining
            f.seek(0, 0)
            # only read what was not read
            blocks.append(f.read(block_end_byte))
        lines_found = blocks[-1].count('\n')
        lines_to_go -= lines_found
        block_end_byte -= BLOCK_SIZE
        block_number -= 1
    all_read_text = ''.join(reversed(blocks))
    f.close()
    return '\n'.join(all_read_text.splitlines()[-total_lines_wanted:])
