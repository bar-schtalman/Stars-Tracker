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
