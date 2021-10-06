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
- [x] Email notifications of found files
- [x] Multi-threading checks  


## Settings

Update config.py to allow for mutiple companies
Update the delay interval for changes in fetch sensitivity

```python
COMPANIES = [('09900', 'TEST')]

DELAY_INTERVAL = 180
```


## Potential future modules

- [ ] APC Garnishment Tracking 
- [ ] MEC Garnishment Tracking 
- [ ] GCS Garnishment Tracking 
- [ ] APC Positive Pay Tracking 
- [ ] MEC Positive Pay Tracking 
- [ ] GCS Positive Pay Tracking 

## How to use

Sentinel runs multi-threaded as a background process. Launch run.bat or create a scheduled task pointing to run.bat

## Support

If you need some help for something, please reach out to me directly or submit an issue and I'll get to it as soon as I can

## Site

https://poseidon-dev.github.io/sentinel/
