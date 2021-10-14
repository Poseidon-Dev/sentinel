# Sentinel | APC File Tracking System

Sentinel is a file tracking system allowing for the logging of any creation, modification, deletion, or movement of a particular file
with a local system 

Further, it allows for the tracking of network files

## Authors

**[Johnny Whitworth (@Poseidon-dev)](https://github.com/poseidon-dev)** 

## Current Modules

- [x] APC Payroll Tracking
- [x] GCS Payroll Tracking  
- [x] MEC Payroll Tracking 
- [x] APC Garnishment Tracking 
- [x] MEC Garnishment Tracking 
- [x] GCS Garnishment Tracking 
- [x] Email notifications of found files
- [x] Multi-threading checks  


## Settings

Update COMPANIES in config.py for additional file checks
Adding additional source (src) and destinations (dst)
```python
COMPANIES = [
    {
        'src': '09900', 
        'dst': 'TESTCOMPANY'
    }
]
```

Update DELAY_INTERVAL for changes in fetch sensitivity

The lower the number, the greater the amount of fetches within a minute but
an increasd amount of potential issues. 

The larger the number, the lower the amount of fetches within a minute but 
a decreased amount of potential issues.

Defaults to 1 minute
```python
DELAY_INTERVAL = 180
```

When creating a Put, it will check to see if the destination file already exists. If a file is already in the directory 
then it will append the next subsequent letter to the file name.
This will fail if there are more than 10 instances of a file in the same directory
```python
while os.path.exists(path):
    if path[-1] in self.APPENDS:
        path = path[:len(path)-1] + self.APPENDS[count]
    else:
        path = path + self.APPENDS[count]
    count +=1
return path
```

core.apl contains the format for creating new threads 

All function's threads are appended to the "threads" list
```python
paths = [
    {
        'src' : Path(defaults.SourcePath, comp['src']),
        'dst' : Path(defaults.SourcePath, comp['dst'],)
    }
        for comp in config.COMPANIES
    ]

sentinels = [Sentinel(path['src'], path['dst']) for path in paths]
threads = [threading.Thread(target=s.run) for s in sentinels]
```


## Potential future modules
- [ ] APC Positive Pay Tracking 
- [ ] MEC Positive Pay Tracking 
- [ ] GCS Positive Pay Tracking 

## How to use

Sentinel runs multi-threaded as a background process. Launch run.bat or create a scheduled task pointing to run.bat

## Support

If you need some help for something, please reach out to me directly or submit an issue and I'll get to it as soon as I can

## Site

https://poseidon-dev.github.io/sentinel/
