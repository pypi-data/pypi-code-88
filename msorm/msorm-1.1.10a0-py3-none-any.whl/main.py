import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=80.93.220.74;'
                      'Database=dbDiscordBot;'
                      'UID=discordBot;'
                      'PWD=!discord2021!;')
cursor = conn.cursor()
cursor.execute('SELECT * FROM dbDiscordBot.dbo.Announce')

for row in cursor:
    print(row)
