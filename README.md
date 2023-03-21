ICPC Bolivia QR Generator
===

This generates images with QR codes based on the given csv file, the file will be a list of contestants and staff. The results will be a a png QR file per item in the csv file and a resulting csv file that associates the unique nanoid in the QR code and the csv item entry.

The csv file must have the following format:
```
name,university or organization name,team name or staff
```

Example:
```
Foo Bar Contestant 1,Universidad Mayor de San Andres,Los Maquinolas
Foo Bar Contestant 1,Universidad Mayor de San Andres,Los Maquinolas
Foo Bar Contestant 1,Universidad Mayor de San Andres,Los Maquinolas
...
Foo Bar Staff 1,ICPC Bolivia,Staff
Foo Bar Staff 1,Universidad Mayor de San Andres,Staff
Foo Bar Staff 1,Universidad Mayor de San Andres,Staff
...
```

* The csv file **MUST** not have a header line, otherwise a QR for that header will be generated.
* Remove any comma from Name, University or Organization name, team name or staff

### How to run
```
# Install requirements
$ pip install -r requirements.txt
```

```
# Generate QRs
$ python qrgenerator.py contestants-staff.csv
```

The final csv file and the QR codes will be saved in the `results/` directory.

In case you want to resize QR codes to a specific size use the following Bash one-liner:

```
$ cd results/
$ for x in $(ls -1); do convert $x -resize 300x300 $x; done
```
