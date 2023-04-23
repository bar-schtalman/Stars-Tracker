# NewSpace Ex1

## Part A
### Pesudo code of stars detecting tool between two pictures (picture 1' has less stars then picture 2')
#### 1. Scan picture 1' and isolate every stars
#### 2. For each star found in step 1, write its x,y cordinates and r - radius
#### 3. Repeat the process for picture 2'
#### 4. For each star in picture 1' calculate the distance between the stars
#### 5. Now repeat the process in picture 2'
#### 6. Look for matching stars from picture 1' in picture 2'
#### 7. Compre the distances and find the best match for each star using treshold value
##### *if the distance is lower then treshold value -> mark as appeard in both pictures

## Example of Part B
### Stars detection tool
#### Insert picture path in terminal (loof for instruction in the code)
#### output examples
##### fr_1.jpg
![pic1](https://github.com/bar-schtalman/Stars-Tracker/blob/8f08bcc63e963ef98c57f8e129776d176d13da9e/readme_pics/fr1_detected.jpeg)
##### ST_db1.png
![pic2](https://github.com/bar-schtalman/Stars-Tracker/blob/8f08bcc63e963ef98c57f8e129776d176d13da9e/readme_pics/st_db1_detected.jpeg)

## Example of Part C
Stars detection between fr1 and fr2
![pic](https://github.com/bar-schtalman/Stars-Tracker/blob/433deb5745caf3879dc5fc8391b3bd5f9952f7de/readme_pics/stars_detected%20fr1_fr2.jpeg)
Stars detection between ST_db1 and ST_db2
![pic3](https://github.com/bar-schtalman/Stars-Tracker/blob/d0953ae4451d05cbf327d2e8994970777c94d066/readme_pics/st1_vs_st2.jpeg)

