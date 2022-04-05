# diff-sqlite
A utility to diff binary (.db) SQLite database files.

## Integration with TortoiseSVN
- Navigate to `TSVN Settings -> Diff Viewer -> Advanced -> Add`
- Supply `.db` as the filename
- Supply the following as the external program `python "location/of/diff-sqlite.py" %base %mine`

## Integration with git
To do..