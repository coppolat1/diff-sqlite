# diff-sqlite
A utility to diff binary (.db) SQLite database files.

## How does it work?
- Connect to both databases using Python's `sqlite3` standard library.
- Dump the contents of both databases into a text-readable `.sql` file.
- Launch a Beyond Compare diff of these two files.
- After Beyond Compare is closed, remove all temporary files.

## Integration with TortoiseSVN
- Navigate to `TSVN Settings -> Diff Viewer -> Advanced -> Add`
- Supply `.db` as the filename
- Supply the following as the external program `python "location/of/diff-sqlite.py" %base %mine`

## Integration with git
To do..

## To Do
- [ ] Figure out dependencies: i.e. get `setuptools` to work.
- [ ] Not everyone has Beyond Compare.. other options should be available.
- [ ] Add script to add registry key, instead of having user edit TSVN settings directly?
`HKEY_CURRENT_USER\Software\TortoiseSVN\DiffTools`