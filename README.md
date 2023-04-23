# NewSpace Ex1

## Part A
### Pesudo code of stars detecting tool between two pictures (picture 1' has less stars then picture 2')

    1. Scan picture 1' and isolate every stars
    2. For each star found in step 1, write its x,y cordinates and r - radius
    3. Repeat the process for picture 2'
    4. For each star in picture 1' calculate the distance between the stars
    5. Now repeat the process in picture 2'
    6. Look for matching stars from picture 1' in picture 2'
    7. Compre the distances and find the best match for each star using treshold value
    *if the distance is lower then treshold value -> mark as appeard in both pictures


## Example of Part B
### Stars detection tool
#### Insert picture path in terminal (loof for instruction in the code)
#### output examples
##### fr_1.jpg
![pic1](https://github.com/bar-schtalman/Stars-Tracker/blob/8f08bcc63e963ef98c57f8e129776d176d13da9e/readme_pics/fr1_detected.jpeg)
##### ST_db1.png
![pic2](https://github.com/bar-schtalman/Stars-Tracker/blob/8f08bcc63e963ef98c57f8e129776d176d13da9e/readme_pics/st_db1_detected.jpeg)

## Example of Part C
### Stars detection between fr1 and fr2
![pic](https://github.com/bar-schtalman/Stars-Tracker/blob/433deb5745caf3879dc5fc8391b3bd5f9952f7de/readme_pics/stars_detected%20fr1_fr2.jpeg)
### (x1,y1) - fr1 | (x2,y2) - fr2
| x1        | y1        | x2        | y2        |
|-----------|-----------|-----------|-----------|
| 216.95895 | 94.97821  | 1220.163  | 764.5918  |
| 531.8722  | 241.31648 | 2116.1777 | 91.60743  |
| 792.36084 | 91.20828  | 1835.8959 | 3748.7883 |
| 1084.2327 | 95.74397  | 2144.0957 | 133.01686 |
| 1231.3323 | 2095.8816 | 1311.9305 | 2105.3735 |
| 1300.6771 | 491.1487  | 1173.3966 | 2916.1545 |
| 1436.8859 | 176.19879 | 2334.0767 | 113.66587 |
| 1445.682  | 1151.242  | 2630.2234 | 52.20002  |
| 1531.9741 | 377.3645  | 2169.8667 | 620.41174 |
| 1700.5664 | 262.96823 | 2646.554  | 922.17114 |
| 1720.756  | 435.15457 | 1070.2898 | 138.2113  |
| 1775.7644 | 21.006119 | 3005.0637 | 169.99243 |
| 1909.9714 | 2940.4302 | 1532.9519 | 3735.975  |
| 2072.5198 | 565.1157  | 3004.2817 | 154.1281  |
| 2088.0515 | 726.42596 | 2960.4363 | 304.79974 |
| 2164.773  | 2181.7683 | 2310.0535 | 2778.9065 |
| 2371.064  | 462.12912 | 1709.6995 | 196.62422 |
| 2498.499  | 2655.4138 | 3004.2817 | 154.1281  |
| 2567.1943 | 2418.637  | 2308.313  | 2785.1746 |
| 2662.6018 | 1353.7737 | 2902.8447 | 2823.8618 |
| 2689.2285 | 1101.8165 | 3001.075  | 165.28761 |
| 2728.961  | 93.4178   | 2719.7505 | 600.8535  |
| 3018.1619 | 370.83466 | 1086.475  | 19.66864  |

### Stars detection between ST_db1 and ST_db2
![pic3](https://github.com/bar-schtalman/Stars-Tracker/blob/d0953ae4451d05cbf327d2e8994970777c94d066/readme_pics/st1_vs_st2.jpeg)

### (x1,y1) - st_db1 | (x2,y2) - st_db2
| x1        | y1         | x2         | y2        |
|-----------|------------|------------|-----------|
| 9.33928   | 717.25964  | 836.1418   | 231.76602 |
| 192.7232  | 975.28033  | 1261.5695  | 270.8236  |
| 192.7232  | 975.28033  | 1261.5695  | 270.8236  |
| 192.7232  | 975.28033  | 1261.5695  | 270.8236  |
| 192.7232  | 975.28033  | 1261.5695  | 270.8236  |
| 273.02606 | 153.2839   | 544.41986  | 468.96082 |
| 273.02606 | 153.2839   | 544.41986  | 468.96082 |
| 273.02606 | 153.2839   | 544.41986  | 468.96082 |
| 275.10132 | 162.96217  | 802.9746   | 134.57732 |
| 275.10132 | 162.96217  | 783.15454  | 738.8506  |
| 275.10132 | 162.96217  | 802.9746   | 134.57732 |
| 278.93335 | 339.71066  | 1955.198   | 55.247086 |
| 302.76947 | 486.9266   | 1433.6997  | 925.12305 |
| 302.76947 | 486.9266   | 1433.6997  | 925.12305 |
| 302.76947 | 486.9266   | 1433.6997  | 925.12305 |
| 361.94794 | 11.194635  | 1593.3262  | 520.9706  |
| 364.73883 | 966.0026   | 332.83673  | 189.6379  |
| 391.98724 | 84.064354  | 1017.49695 | 1039.9448 |
| 453.60645 | 358.19537  | 1278.9725  | 654.33344 |
| 453.60645 | 358.19537  | 922.3156   | 363.48026 |
| 486.55682 | 245.20811  | 492.22498  | 376.9455  |
| 486.55682 | 245.20811  | 492.22498  | 376.9455  |
| 486.55682 | 245.20811  | 492.22498  | 376.9455  |
| 529.0672  | 998.32104  | 802.9899   | 1233.426  |
| 529.0672  | 998.32104  | 802.9899   | 1233.426  |
| 529.0672  | 998.32104  | 802.9899   | 1233.426  |
| 579.4127  | 615.16626  | 544.41986  | 468.96082 |
| 579.4127  | 615.16626  | 836.4678   | 877.23596 |
| 579.4127  | 615.16626  | 802.9899   | 1233.426  |
| 585.02637 | 609.847    | 841.42664  | 872.146   |
| 585.02637 | 609.847    | 841.42664  | 872.146   |
| 658.0939  | 262.1413   | 893.9456   | 553.236   |
| 658.0939  | 262.1413   | 893.9456   | 553.236   |
| 680.0369  | 620.1555   | 1899.114   | 31.13005  |
| 700.1664  | 52.728294  | 1284.7501  | 975.1635  |
| 700.1664  | 52.728294  | 1284.7501  | 975.1635  |
| 700.1664  | 52.728294  | 586.7105   | 387.2938  |
| 724.23834 | 632.59357  | 1720.9092  | 401.21698 |
| 724.23834 | 632.59357  | 1720.9092  | 401.21698 |
| 724.23834 | 632.59357  | 1720.9092  | 401.21698 |
| 883.1263  | 1145.3115  | 629.88     | 1220.3962 |
| 897.85065 | 451.36652  | 340.67865  | 773.17395 |
| 897.85065 | 451.36652  | 554.653    | 636.129   |
| 901.2878  | 712.52014  | 1443.2688  | 15.532077 |
| 901.2878  | 712.52014  | 1443.2688  | 15.532077 |
| 901.2878  | 712.52014  | 1443.2688  | 15.532077 |
| 903.22626 | 1115.645   | 586.7105   | 387.2938  |
| 1031.2382 | 1109.6676  | 945.6624   | 40.260975 |
| 1031.2382 | 1109.6676  | 945.6624   | 40.260975 |
| 1031.2382 | 1109.6676  | 945.6624   | 40.260975 |
| 1037.439  | 720.126    | 1899.114   | 31.13005  |
| 1059.2949 | 746.141    | 836.1418   | 231.76602 |
| 1092.1127 | 116.13387  | 1560.7443  | 628.7869  |
| 1096.5918 | 118.16811  | 1579.0438  | 629.9818  |
| 1096.9634 | 124.15624  | 1578.9084  | 623.99713 |
| 1098.407  | 112.24547  | 1567.1805  | 625.08575 |
| 1102.1119 | 185.67987  | 1261.5695  | 270.8236  |
| 1102.1119 | 185.67987  | 1261.5695  | 270.8236  |
| 1102.1119 | 185.67987  | 1261.5695  | 270.8236  |
| 1102.1722 | 106.111824 | 1573.6581  | 642.3423  |
| 1102.8986 | 124.56879  | 1571.9928  | 637.01184 |
| 1103.3501 | 117.765    | 1572.4375  | 630.4102  |
| 1103.3501 | 117.765    | 1572.4375  | 630.4102  |
| 1108.3031 | 123.30803  | 1567.1805  | 625.08575 |
| 1115.8411 | 130.60022  | 1559.9     | 617.5844  |
| 1141.1613 | 942.614    | 488.22153  | 272.44937 |
| 1158.3828 | 902.1521   | 1984.1094  | 634.02637 |
| 1158.3828 | 902.1521   | 1984.1094  | 634.02637 |
| 1219.2812 | 766.87885  | 1289.9061  | 460.87097 |
| 1223.1539 | 703.0018   | 1372.5659  | 1153.1998 |
| 1223.1539 | 703.0018   | 1372.5659  | 1153.1998 |
| 1223.1539 | 703.0018   | 1372.5659  | 1153.1998 |
| 1378.7081 | 343.8928   | 1372.5659  | 1153.1998 |
| 1384.2548 | 868.3002   | 404.2378   | 1045.1635 |
| 1384.2548 | 868.3002   | 404.2378   | 1045.1635 |
| 1384.2548 | 868.3002   | 404.2378   | 1045.1635 |
| 1470.2288 | 556.58954  | 1837.5657  | 1109.2744 |
| 1470.2288 | 556.58954  | 1837.5657  | 1109.2744 |
| 1503.0321 | 443.2842   | 758.78265  | 342.05338 |
| 1582.6967 | 158.73947  | 302.7729   | 854.7597  |
| 1582.6967 | 158.73947  | 302.7729   | 854.7597  |
| 1606.594  | 681.31573  | 1572.0867  | 82.88521  |
| 1606.594  | 681.31573  | 1572.0867  | 82.88521  |
| 1606.594  | 681.31573  | 1572.0867  | 82.88521  |
| 1638.2974 | 934.3244   | 738.9566   | 544.6005  |
| 1638.2974 | 934.3244   | 2045.3439  | 378.32776 |
| 1842.7054 | 475.2135   | 1261.5695  | 270.8236  |
| 1842.7054 | 475.2135   | 1261.5695  | 270.8236  |
| 1842.7054 | 475.2135   | 1261.5695  | 270.8236  |
| 1842.7054 | 475.2135   | 1261.5695  | 270.8236  |
| 1842.7054 | 475.2135   | 1261.5695  | 270.8236  |
| 1842.7054 | 475.2135   | 1433.6997  | 925.12305 |
| 1844.4025 | 441.16412  | 1984.1094  | 634.02637 |
| 1844.4025 | 441.16412  | 1984.1094  | 634.02637 |
| 1854.3378 | 52.58093   | 1278.9725  | 654.33344 |
| 1891.8784 | 788.93805  | 738.9566   | 544.6005  |
| 1891.8784 | 788.93805  | 738.9566   | 544.6005  |
| 1941.0813 | 170.47527  | 800.25385  | 1240.4836 |
| 1941.0813 | 170.47527  | 800.25385  | 1240.4836 |

