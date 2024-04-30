# Hardened Weather App :sun_behind_rain_cloud:
Update the previously coded Weather App with security principles learned over the course of the semester.

> [!NOTE]
> Original project located in Weather App file for reference.

  <details>
<summary>Topics Covered</summary>

### Topics Covered Include: 

  - Backup and rollback
  - partitioning
  - validation 
  - sanitization 
  - securing tokens/secrets
  - error handling, 
  - static code testing
  - unit testing 
  - logging 
  - documentation
  - hashing
  - encryption 
  - prepared statements
  - least privilege for any system accounts/file system
  </details>

## Third Party Libraries
### Requests 
Version 2.31.0

  The [Requests](https://requests.readthedocs.io/en/latest/) library is the default for making HTTP requests in Python. 
  
  This needs to be installed before running the application usint the command below.

```
pip install requests
```
**Response Codes**

200 - **Success** :white_check_mark:

404 - **Fail** :x:

### Bandit 
Version 1.7.8

[Bandit](https://pypi.org/project/bandit/0.17.3/) is used as an SAST tool.

Bandit works by processing each file, building an AST from it, and running appropriate plugins against the AST nodes.

Once finished scanning all the files, it generates a report.

### Install
```
pip install bandit
```

### To run Bandit
```
bandit -r ./weather.py
```

  
## Third Party API's
### Open Weather API
This application uses the [5 Day Weather Forecast API](https://openweathermap.org/forecast5) released by Open Weather.

This API returns a 5 day forecast for any location in the world and is available in JSON and XML.



  
