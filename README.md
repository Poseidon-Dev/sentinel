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

Update DELAY_INTERVAL to for changes in fetch sensitivity
The lower the number, the greater the amount of fetches within a minute but
an increasd amount of potential issues. 
The larger the number, the lower the amount of fetches within a minute but 
a decreased amount of potential issues.
Defaults to 3 minutes
```python
DELAY_INTERVAL = 180
```

core.apl contains the format for creating new threads 
All function's threads are appended to the "threads" list
```python
paths = [
    {
        'src' : Path(SourcePath, comp['src']),
        'dst' : Path(SourcePath, comp['dst'],)
    }
        for comp in defaults.COMPANIES
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
