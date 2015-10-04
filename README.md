# Led Gamma Correction
A simple script to generate Gamma-Correction-Tables

## What
This is a python script which generates Gamma-Correction-Tables.

## Why
If you've ever worked with RGB-Leds you'll have noticed that calibrating the Leds is a necessary step to achieve accurate colors. I've written this script to simplify the proccess of generating Gamma-Correction-Tables. It samples the corrected values and outputs an array (Let's call it a lookup table). This is much faster than calculating the values during runtime.

## Usage
`generateGammaCorrectionTable(a,b)`
a := exponent
b := linear factor

```
print(generateGammaCorrectionTable(2,1))
```
outputs:
```
{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 12, 12, 12, 13, 13, 13, 13, 13, 13, 13, 13, 13, 14, 14, 14, 14, 14, 14, 14, 14, 15, 15, 15, 15, 15, 15, 15, 15, 16, 16, 16, 16, 16, 16, 16, 16, 17, 17, 17, 17, 17, 17, 17, 17, 18, 18, 18, 18, 18, 18, 18, 18, 19, 19, 19, 19, 19, 19, 19, 20, 20, 20, 20, 20, 20, 20, 21, 21, 21, 21, 21, 21, 21, 22, 22, 22, 22, 22, 22, 22, 23, 23, 23, 23, 23, 23, 23, 24, 24, 24, 24, 24, 24, 25, 25, 25, 25, 25, 25, 25, 26, 26, 26, 26, 26, 26, 27, 27, 27, 27, 27, 27, 28, 28, 28, 28, 28, 28, 29, 29, 29, 29, 29, 29, 30, 30, 30, 30, 30, 30, 31, 31, 31, 31, 31, 31, 32, 32, 32, 32, 32, 33, 33, 33, 33, 33, 33, 34, 34, 34, 34, 34, 35, 35, 35, 35, 35, 35, 36, 36, 36, 36, 36, 37, 37, 37, 37, 37, 38, 38, 38, 38, 38, 38, 39, 39, 39, 39, 39, 40, 40, 40, 40, 40, 41, 41, 41, 41, 41, 42, 42, 42, 42, 42, 43, 43, 43, 43, 43, 44, 44, 44, 44, 45, 45, 45, 45, 45, 46, 46, 46, 46, 46, 47, 47, 47, 47, 47, 48, 48, 48, 48, 49, 49, 49, 49, 49, 50, 50, 50, 50, 51, 51, 51, 51, 51, 52, 52, 52, 52, 53, 53, 53, 53, 53, 54, 54, 54, 54, 55, 55, 55, 55, 56, 56, 56, 56, 56, 57, 57, 57, 57, 58, 58, 58, 58, 59, 59, 59, 59, 60, 60, 60, 60, 61, 61, 61, 61, 62, 62, 62, 62, 63, 63, 63, 63, 64, 64, 64, 64, 65, 65, 65, 65, 66, 66, 66, 66, 67, 67, 67, 67, 68, 68, 68, 68, 69, 69, 69, 69, 70, 70, 70, 70, 71, 71, 71, 71, 72, 72, 72, 73, 73, 73, 73, 74, 74, 74, 74, 75, 75, 75, 75, 76, 76, 76, 77, 77, 77, 77, 78, 78, 78, 79, 79, 79, 79, 80, 80, 80, 80, 81, 81, 81, 82, 82, 82, 82, 83, 83, 83, 84, 84, 84, 84, 85, 85, 85, 86, 86, 86, 86, 87, 87, 87, 88, 88, 88, 88, 89, 89, 89, 90, 90, 90, 91, 91, 91, 91, 92, 92, 92, 93, 93, 93, 94, 94, 94, 94, 95, 95, 95, 96, 96, 96, 97, 97, 97, 98, 98, 98, 98, 99, 99, 99, 100, 100, 100, 101, 101, 101, 102, 102, 102, 103, 103, 103, 103, 104, 104, 104, 105, 105, 105, 106, 106, 106, 107, 107, 107, 108, 108, 108, 109, 109, 109, 110, 110, 110, 111, 111, 111, 112, 112, 112, 113, 113, 113, 114, 114, 114, 115, 115, 115, 116, 116, 116, 117, 117, 117, 118, 118, 118, 119, 119, 119, 120, 120, 120, 121, 121, 121, 122, 122, 122, 123, 123, 123, 124, 124, 124, 125, 125, 126, 126, 126, 127, 127, 127, 128, 128, 128, 129, 129, 129, 130, 130, 130, 131, 131, 132, 132, 132, 133, 133, 133, 134, 134, 134, 135, 135, 136, 136, 136, 137, 137, 137, 138, 138, 138, 139, 139, 140, 140, 140, 141, 141, 141, 142, 142, 143, 143, 143, 144, 144, 144, 145, 145, 146, 146, 146, 147, 147, 147, 148, 148, 149, 149, 149, 150, 150, 150, 151, 151, 152, 152, 152, 153, 153, 154, 154, 154, 155, 155, 156, 156, 156, 157, 157, 157, 158, 158, 159, 159, 159, 160, 160, 161, 161, 161, 162, 162, 163, 163, 163, 164, 164, 165, 165, 165, 166, 166, 167, 167, 167, 168, 168, 169, 169, 169, 170, 170, 171, 171, 171, 172, 172, 173, 173, 174, 174, 174, 175, 175, 176, 176, 176, 177, 177, 178, 178, 179, 179, 179, 180, 180, 181, 181, 181, 182, 182, 183, 183, 184, 184, 184, 185, 185, 186, 186, 187, 187, 187, 188, 188, 189, 189, 190, 190, 190, 191, 191, 192, 192, 193, 193, 193, 194, 194, 195, 195, 196, 196, 196, 197, 197, 198, 198, 199, 199, 200, 200, 200, 201, 201, 202, 202, 203, 203, 204, 204, 204, 205, 205, 206, 206, 207, 207, 208, 208, 208, 209, 209, 210, 210, 211, 211, 212, 212, 213, 213, 213, 214, 214, 215, 215, 216, 216, 217, 217, 218, 218, 219, 219, 219, 220, 220, 221, 221, 222, 222, 223, 223, 224, 224, 225, 225, 226, 226, 226, 227, 227, 228, 228, 229, 229, 230, 230, 231, 231, 232, 232, 233, 233, 234, 234, 235, 235, 235, 236, 236, 237, 237, 238, 238, 239, 239, 240, 240, 241, 241, 242, 242, 243, 243, 244, 244, 245, 245, 246, 246, 247, 247, 248, 248, 249, 249, 250, 250, 251, 251, 252, 252, 253, 253, 254, 254, 255, 255, 256, 256, 257, 257, 258, 258, 259, 259, 260, 260, 261, 261, 262, 262, 263, 263, 264, 264, 265, 265, 266, 266, 267, 267, 268, 268, 269, 269, 270, 270, 271, 271, 272, 272, 273, 273, 274, 274, 275, 275, 276, 276, 277, 277, 278, 279, 279, 280, 280, 281, 281, 282, 282, 283, 283, 284, 284, 285, 285, 286, 286, 287, 287, 288, 289, 289, 290, 290, 291, 291, 292, 292, 293, 293, 294, 294, 295, 295, 296, 297, 297, 298, 298, 299, 299, 300, 300, 301, 301, 302, 303, 303, 304, 304, 305, 305, 306, 306, 307, 307, 308, 309, 309, 310, 310, 311, 311, 312, 312, 313, 313, 314, 315, 315, 316, 316, 317, 317, 318, 318, 319, 320, 320, 321, 321, 322, 322, 323, 324, 324, 325, 325, 326, 326, 327, 327, 328, 329, 329, 330, 330, 331, 331, 332, 333, 333, 334, 334, 335, 335, 336, 337, 337, 338, 338, 339, 339, 340, 341, 341, 342, 342, 343, 343, 344, 345, 345, 346, 346, 347, 348, 348, 349, 349, 350, 350, 351, 352, 352, 353, 353, 354, 355, 355, 356, 356, 357, 358, 358, 359, 359, 360, 360, 361, 362, 362, 363, 363, 364, 365, 365, 366, 366, 367, 368, 368, 369, 369, 370, 371, 371, 372, 372, 373, 374, 374, 375, 375, 376, 377, 377, 378, 379, 379, 380, 380, 381, 382, 382, 383, 383, 384, 385, 385, 386, 386, 387, 388, 388, 389, 390, 390, 391, 391, 392, 393, 393, 394, 394, 395, 396, 396, 397, 398, 398, 399, 399, 400, 401, 401, 402, 403, 403, 404, 404, 405, 406, 406, 407, 408, 408, 409, 410, 410, 411, 411, 412, 413, 413, 414, 415, 415, 416, 417, 417, 418, 418, 419, 420, 420, 421, 422, 422, 423, 424, 424, 425, 425, 426, 427, 427, 428, 429, 429, 430, 431, 431, 432, 433, 433, 434, 435, 435, 436, 437, 437, 438, 438, 439, 440, 440, 441, 442, 442, 443, 444, 444, 445, 446, 446, 447, 448, 448, 449, 450, 450, 451, 452, 452, 453, 454, 454, 455, 456, 456, 457, 458, 458, 459, 460, 460, 461, 462, 462, 463, 464, 464, 465, 466, 466, 467, 468, 468, 469, 470, 470, 471, 472, 472, 473, 474, 475, 475, 476, 477, 477, 478, 479, 479, 480, 481, 481, 482, 483, 483, 484, 485, 485, 486, 487, 488, 488, 489, 490, 490, 491, 492, 492, 493, 494, 494, 495, 496, 497, 497, 498, 499, 499, 500, 501, 501, 502, 503, 504, 504, 505, 506, 506, 507, 508, 508, 509, 510, 511, 511, 512, 513, 513, 514, 515, 516, 516, 517, 518, 518, 519, 520, 521, 521, 522, 523, 523, 524, 525, 526, 526, 527, 528, 528, 529, 530, 531, 531, 532, 533, 533, 534, 535, 536, 536, 537, 538, 539, 539, 540, 541, 541, 542, 543, 544, 544, 545, 546, 547, 547, 548, 549, 549, 550, 551, 552, 552, 553, 554, 555, 555, 556, 557, 558, 558, 559, 560, 560, 561, 562, 563, 563, 564, 565, 566, 566, 567, 568, 569, 569, 570, 571, 572, 572, 573, 574, 575, 575, 576, 577, 578, 578, 579, 580, 581, 581, 582, 583, 584, 584, 585, 586, 587, 587, 588, 589, 590, 590, 591, 592, 593, 594, 594, 595, 596, 597, 597, 598, 599, 600, 600, 601, 602, 603, 603, 604, 605, 606, 607, 607, 608, 609, 610, 610, 611, 612, 613, 613, 614, 615, 616, 617, 617, 618, 619, 620, 620, 621, 622, 623, 624, 624, 625, 626, 627, 627, 628, 629, 630, 631, 631, 632, 633, 634, 635, 635, 636, 637, 638, 639, 639, 640, 641, 642, 642, 643, 644, 645, 646, 646, 647, 648, 649, 650, 650, 651, 652, 653, 654, 654, 655, 656, 657, 658, 658, 659, 660, 661, 662, 662, 663, 664, 665, 666, 666, 667, 668, 669, 670, 670, 671, 672, 673, 674, 675, 675, 676, 677, 678, 679, 679, 680, 681, 682, 683, 683, 684, 685, 686, 687, 688, 688, 689, 690, 691, 692, 693, 693, 694, 695, 696, 697, 697, 698, 699, 700, 701, 702, 702, 703, 704, 705, 706, 707, 707, 708, 709, 710, 711, 712, 712, 713, 714, 715, 716, 717, 717, 718, 719, 720, 721, 722, 722, 723, 724, 725, 726, 727, 727, 728, 729, 730, 731, 732, 733, 733, 734, 735, 736, 737, 738, 738, 739, 740, 741, 742, 743, 744, 744, 745, 746, 747, 748, 749, 750, 750, 751, 752, 753, 754, 755, 756, 756, 757, 758, 759, 760, 761, 762, 762, 763, 764, 765, 766, 767, 768, 769, 769, 770, 771, 772, 773, 774, 775, 775, 776, 777, 778, 779, 780, 781, 782, 782, 783, 784, 785, 786, 787, 788, 789, 789, 790, 791, 792, 793, 794, 795, 796, 796, 797, 798, 799, 800, 801, 802, 803, 804, 804, 805, 806, 807, 808, 809, 810, 811, 812, 812, 813, 814, 815, 816, 817, 818, 819, 820, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 896, 897, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 911, 912, 912, 913, 914, 915, 916, 917, 918, 919, 920, 921, 922, 923, 924, 925, 926, 927, 928, 929, 930, 930, 931, 932, 933, 934, 935, 936, 937, 938, 939, 940, 941, 942, 943, 944, 945, 946, 947, 948, 949, 950, 951, 952, 953, 953, 954, 955, 956, 957, 958, 959, 960, 961, 962, 963, 964, 965, 966, 967, 968, 969, 970, 971, 972, 973, 974, 975, 976, 977, 978, 979, 980, 981, 982, 983, 984, 985, 986, 987, 988, 989, 990, 991, 992, 992, 993, 994, 995, 996, 997, 998, 999, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019, 1020, 1021, 1022, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033, 1034, 1035, 1036, 1037, 1038, 1039, 1040, 1041, 1042, 1043, 1044, 1045, 1046, 1047, 1048, 1049, 1050, 1051, 1052, 1053, 1054, 1055, 1057, 1058, 1059, 1060, 1061, 1062, 1063, 1064, 1065, 1066, 1067, 1068, 1069, 1070, 1071, 1072, 1073, 1074, 1075, 1076, 1077, 1078, 1079, 1080, 1081, 1082, 1083, 1084, 1085, 1086, 1087, 1088, 1089, 1090, 1091, 1092, 1093, 1094, 1095, 1096, 1098, 1099, 1100, 1101, 1102, 1103, 1104, 1105, 1106, 1107, 1108, 1109, 1110, 1111, 1112, 1113, 1114, 1115, 1116, 1117, 1118, 1119, 1120, 1121, 1123, 1124, 1125, 1126, 1127, 1128, 1129, 1130, 1131, 1132, 1133, 1134, 1135, 1136, 1137, 1138, 1139, 1140, 1141, 1143, 1144, 1145, 1146, 1147, 1148, 1149, 1150, 1151, 1152, 1153, 1154, 1155, 1156, 1157, 1158, 1159, 1161, 1162, 1163, 1164, 1165, 1166, 1167, 1168, 1169, 1170, 1171, 1172, 1173, 1174, 1175, 1177, 1178, 1179, 1180, 1181, 1182, 1183, 1184, 1185, 1186, 1187, 1188, 1189, 1191, 1192, 1193, 1194, 1195, 1196, 1197, 1198, 1199, 1200, 1201, 1202, 1204, 1205, 1206, 1207, 1208, 1209, 1210, 1211, 1212, 1213, 1214, 1215, 1217, 1218, 1219, 1220, 1221, 1222, 1223, 1224, 1225, 1226, 1227, 1229, 1230, 1231, 1232, 1233, 1234, 1235, 1236, 1237, 1238, 1240, 1241, 1242, 1243, 1244, 1245, 1246, 1247, 1248, 1249, 1251, 1252, 1253, 1254, 1255, 1256, 1257, 1258, 1259, 1261, 1262, 1263, 1264, 1265, 1266, 1267, 1268, 1269, 1271, 1272, 1273, 1274, 1275, 1276, 1277, 1278, 1279, 1281, 1282, 1283, 1284, 1285, 1286, 1287, 1288, 1290, 1291, 1292, 1293, 1294, 1295, 1296, 1297, 1299, 1300, 1301, 1302, 1303, 1304, 1305, 1306, 1308, 1309, 1310, 1311, 1312, 1313, 1314, 1316, 1317, 1318, 1319, 1320, 1321, 1322, 1323, 1325, 1326, 1327, 1328, 1329, 1330, 1331, 1333, 1334, 1335, 1336, 1337, 1338, 1339, 1341, 1342, 1343, 1344, 1345, 1346, 1347, 1349, 1350, 1351, 1352, 1353, 1354, 1355, 1357, 1358, 1359, 1360, 1361, 1362, 1364, 1365, 1366, 1367, 1368, 1369, 1370, 1372, 1373, 1374, 1375, 1376, 1377, 1379, 1380, 1381, 1382, 1383, 1384, 1386, 1387, 1388, 1389, 1390, 1391, 1393, 1394, 1395, 1396, 1397, 1398, 1400, 1401, 1402, 1403, 1404, 1405, 1407, 1408, 1409, 1410, 1411, 1412, 1414, 1415, 1416, 1417, 1418, 1420, 1421, 1422, 1423, 1424, 1425, 1427, 1428, 1429, 1430, 1431, 1432, 1434, 1435, 1436, 1437, 1438, 1440, 1441, 1442, 1443, 1444, 1446, 1447, 1448, 1449, 1450, 1451, 1453, 1454, 1455, 1456, 1457, 1459, 1460, 1461, 1462, 1463, 1465, 1466, 1467, 1468, 1469, 1471, 1472, 1473, 1474, 1475, 1477, 1478, 1479, 1480, 1481, 1483, 1484, 1485, 1486, 1487, 1489, 1490, 1491, 1492, 1493, 1495, 1496, 1497, 1498, 1500, 1501, 1502, 1503, 1504, 1506, 1507, 1508, 1509, 1510, 1512, 1513, 1514, 1515, 1516, 1518, 1519, 1520, 1521, 1523, 1524, 1525, 1526, 1527, 1529, 1530, 1531, 1532, 1534, 1535, 1536, 1537, 1538, 1540, 1541, 1542, 1543, 1545, 1546, 1547, 1548, 1550, 1551, 1552, 1553, 1554, 1556, 1557, 1558, 1559, 1561, 1562, 1563, 1564, 1566, 1567, 1568, 1569, 1571, 1572, 1573, 1574, 1575, 1577, 1578, 1579, 1580, 1582, 1583, 1584, 1585, 1587, 1588, 1589, 1590, 1592, 1593, 1594, 1595, 1597, 1598, 1599, 1600, 1602, 1603, 1604, 1605, 1607, 1608, 1609, 1610, 1612, 1613, 1614, 1615, 1617, 1618, 1619, 1620, 1622, 1623, 1624, 1625, 1627, 1628, 1629, 1631, 1632, 1633, 1634, 1636, 1637, 1638, 1639, 1641, 1642, 1643, 1644, 1646, 1647, 1648, 1650, 1651, 1652, 1653, 1655, 1656, 1657, 1658, 1660, 1661, 1662, 1664, 1665, 1666, 1667, 1669, 1670, 1671, 1672, 1674, 1675, 1676, 1678, 1679, 1680, 1681, 1683, 1684, 1685, 1687, 1688, 1689, 1690, 1692, 1693, 1694, 1696, 1697, 1698, 1699, 1701, 1702, 1703, 1705, 1706, 1707, 1708, 1710, 1711, 1712, 1714, 1715, 1716, 1717, 1719, 1720, 1721, 1723, 1724, 1725, 1727, 1728, 1729, 1730, 1732, 1733, 1734, 1736, 1737, 1738, 1740, 1741, 1742, 1743, 1745, 1746, 1747, 1749, 1750, 1751, 1753, 1754, 1755, 1757, 1758, 1759, 1760, 1762, 1763, 1764, 1766, 1767, 1768, 1770, 1771, 1772, 1774, 1775, 1776, 1778, 1779, 1780, 1782, 1783, 1784, 1785, 1787, 1788, 1789, 1791, 1792, 1793, 1795, 1796, 1797, 1799, 1800, 1801, 1803, 1804, 1805, 1807, 1808, 1809, 1811, 1812, 1813, 1815, 1816, 1817, 1819, 1820, 1821, 1823, 1824, 1825, 1827, 1828, 1829, 1831, 1832, 1833, 1835, 1836, 1837, 1839, 1840, 1841, 1843, 1844, 1845, 1847, 1848, 1849, 1851, 1852, 1853, 1855, 1856, 1858, 1859, 1860, 1862, 1863, 1864, 1866, 1867, 1868, 1870, 1871, 1872, 1874, 1875, 1876, 1878, 1879, 1880, 1882, 1883, 1885, 1886, 1887, 1889, 1890, 1891, 1893, 1894, 1895, 1897, 1898, 1900, 1901, 1902, 1904, 1905, 1906, 1908, 1909, 1910, 1912, 1913, 1915, 1916, 1917, 1919, 1920, 1921, 1923, 1924, 1925, 1927, 1928, 1930, 1931, 1932, 1934, 1935, 1936, 1938, 1939, 1941, 1942, 1943, 1945, 1946, 1947, 1949, 1950, 1952, 1953, 1954, 1956, 1957, 1959, 1960, 1961, 1963, 1964, 1965, 1967, 1968, 1970, 1971, 1972, 1974, 1975, 1977, 1978, 1979, 1981, 1982, 1984, 1985, 1986, 1988, 1989, 1990, 1992, 1993, 1995, 1996, 1997, 1999, 2000, 2002, 2003, 2004, 2006, 2007, 2009, 2010, 2011, 2013, 2014, 2016, 2017, 2018, 2020, 2021, 2023, 2024, 2025, 2027, 2028, 2030, 2031, 2033, 2034, 2035, 2037, 2038, 2040, 2041, 2042, 2044, 2045, 2047, 2048, 2049, 2051, 2052, 2054, 2055, 2057, 2058, 2059, 2061, 2062, 2064, 2065, 2066, 2068, 2069, 2071, 2072, 2074, 2075, 2076, 2078, 2079, 2081, 2082, 2084, 2085, 2086, 2088, 2089, 2091, 2092, 2094, 2095, 2096, 2098, 2099, 2101, 2102, 2104, 2105, 2106, 2108, 2109, 2111, 2112, 2114, 2115, 2117, 2118, 2119, 2121, 2122, 2124, 2125, 2127, 2128, 2129, 2131, 2132, 2134, 2135, 2137, 2138, 2140, 2141, 2142, 2144, 2145, 2147, 2148, 2150, 2151, 2153, 2154, 2156, 2157, 2158, 2160, 2161, 2163, 2164, 2166, 2167, 2169, 2170, 2172, 2173, 2174, 2176, 2177, 2179, 2180, 2182, 2183, 2185, 2186, 2188, 2189, 2190, 2192, 2193, 2195, 2196, 2198, 2199, 2201, 2202, 2204, 2205, 2207, 2208, 2210, 2211, 2212, 2214, 2215, 2217, 2218, 2220, 2221, 2223, 2224, 2226, 2227, 2229, 2230, 2232, 2233, 2235, 2236, 2238, 2239, 2240, 2242, 2243, 2245, 2246, 2248, 2249, 2251, 2252, 2254, 2255, 2257, 2258, 2260, 2261, 2263, 2264, 2266, 2267, 2269, 2270, 2272, 2273, 2275, 2276, 2278, 2279, 2281, 2282, 2284, 2285, 2287, 2288, 2290, 2291, 2293, 2294, 2296, 2297, 2299, 2300, 2302, 2303, 2305, 2306, 2308, 2309, 2311, 2312, 2314, 2315, 2317, 2318, 2320, 2321, 2323, 2324, 2326, 2327, 2329, 2330, 2332, 2333, 2335, 2336, 2338, 2339, 2341, 2342, 2344, 2345, 2347, 2348, 2350, 2351, 2353, 2354, 2356, 2357, 2359, 2360, 2362, 2363, 2365, 2366, 2368, 2370, 2371, 2373, 2374, 2376, 2377, 2379, 2380, 2382, 2383, 2385, 2386, 2388, 2389, 2391, 2392, 2394, 2395, 2397, 2399, 2400, 2402, 2403, 2405, 2406, 2408, 2409, 2411, 2412, 2414, 2415, 2417, 2418, 2420, 2422, 2423, 2425, 2426, 2428, 2429, 2431, 2432, 2434, 2435, 2437, 2438, 2440, 2442, 2443, 2445, 2446, 2448, 2449, 2451, 2452, 2454, 2455, 2457, 2459, 2460, 2462, 2463, 2465, 2466, 2468, 2469, 2471, 2473, 2474, 2476, 2477, 2479, 2480, 2482, 2483, 2485, 2487, 2488, 2490, 2491, 2493, 2494, 2496, 2497, 2499, 2501, 2502, 2504, 2505, 2507, 2508, 2510, 2512, 2513, 2515, 2516, 2518, 2519, 2521, 2523, 2524, 2526, 2527, 2529, 2530, 2532, 2534, 2535, 2537, 2538, 2540, 2541, 2543, 2545, 2546, 2548, 2549, 2551, 2552, 2554, 2556, 2557, 2559, 2560, 2562, 2564, 2565, 2567, 2568, 2570, 2571, 2573, 2575, 2576, 2578, 2579, 2581, 2583, 2584, 2586, 2587, 2589, 2590, 2592, 2594, 2595, 2597, 2598, 2600, 2602, 2603, 2605, 2606, 2608, 2610, 2611, 2613, 2614, 2616, 2618, 2619, 2621, 2622, 2624, 2626, 2627, 2629, 2630, 2632, 2634, 2635, 2637, 2638, 2640, 2642, 2643, 2645, 2646, 2648, 2650, 2651, 2653, 2655, 2656, 2658, 2659, 2661, 2663, 2664, 2666, 2667, 2669, 2671, 2672, 2674, 2675, 2677, 2679, 2680, 2682, 2684, 2685, 2687, 2688, 2690, 2692, 2693, 2695, 2697, 2698, 2700, 2701, 2703, 2705, 2706, 2708, 2710, 2711, 2713, 2714, 2716, 2718, 2719, 2721, 2723, 2724, 2726, 2727, 2729, 2731, 2732, 2734, 2736, 2737, 2739, 2741, 2742, 2744, 2745, 2747, 2749, 2750, 2752, 2754, 2755, 2757, 2759, 2760, 2762, 2763, 2765, 2767, 2768, 2770, 2772, 2773, 2775, 2777, 2778, 2780, 2782, 2783, 2785, 2787, 2788, 2790, 2791, 2793, 2795, 2796, 2798, 2800, 2801, 2803, 2805, 2806, 2808, 2810, 2811, 2813, 2815, 2816, 2818, 2820, 2821, 2823, 2825, 2826, 2828, 2830, 2831, 2833, 2835, 2836, 2838, 2840, 2841, 2843, 2845, 2846, 2848, 2850, 2851, 2853, 2855, 2856, 2858, 2860, 2861, 2863, 2865, 2866, 2868, 2870, 2871, 2873, 2875, 2876, 2878, 2880, 2881, 2883, 2885, 2886, 2888, 2890, 2891, 2893, 2895, 2896, 2898, 2900, 2902, 2903, 2905, 2907, 2908, 2910, 2912, 2913, 2915, 2917, 2918, 2920, 2922, 2923, 2925, 2927, 2929, 2930, 2932, 2934, 2935, 2937, 2939, 2940, 2942, 2944, 2945, 2947, 2949, 2951, 2952, 2954, 2956, 2957, 2959, 2961, 2962, 2964, 2966, 2968, 2969, 2971, 2973, 2974, 2976, 2978, 2979, 2981, 2983, 2985, 2986, 2988, 2990, 2991, 2993, 2995, 2997, 2998, 3000, 3002, 3003, 3005, 3007, 3009, 3010, 3012, 3014, 3015, 3017, 3019, 3021, 3022, 3024, 3026, 3027, 3029, 3031, 3033, 3034, 3036, 3038, 3040, 3041, 3043, 3045, 3046, 3048, 3050, 3052, 3053, 3055, 3057, 3058, 3060, 3062, 3064, 3065, 3067, 3069, 3071, 3072, 3074, 3076, 3078, 3079, 3081, 3083, 3084, 3086, 3088, 3090, 3091, 3093, 3095, 3097, 3098, 3100, 3102, 3104, 3105, 3107, 3109, 3111, 3112, 3114, 3116, 3118, 3119, 3121, 3123, 3125, 3126, 3128, 3130, 3132, 3133, 3135, 3137, 3139, 3140, 3142, 3144, 3146, 3147, 3149, 3151, 3153, 3154, 3156, 3158, 3160, 3161, 3163, 3165, 3167, 3168, 3170, 3172, 3174, 3175, 3177, 3179, 3181, 3182, 3184, 3186, 3188, 3189, 3191, 3193, 3195, 3197, 3198, 3200, 3202, 3204, 3205, 3207, 3209, 3211, 3212, 3214, 3216, 3218, 3220, 3221, 3223, 3225, 3227, 3228, 3230, 3232, 3234, 3236, 3237, 3239, 3241, 3243, 3244, 3246, 3248, 3250, 3252, 3253, 3255, 3257, 3259, 3260, 3262, 3264, 3266, 3268, 3269, 3271, 3273, 3275, 3277, 3278, 3280, 3282, 3284, 3286, 3287, 3289, 3291, 3293, 3294, 3296, 3298, 3300, 3302, 3303, 3305, 3307, 3309, 3311, 3312, 3314, 3316, 3318, 3320, 3321, 3323, 3325, 3327, 3329, 3330, 3332, 3334, 3336, 3338, 3339, 3341, 3343, 3345, 3347, 3349, 3350, 3352, 3354, 3356, 3358, 3359, 3361, 3363, 3365, 3367, 3368, 3370, 3372, 3374, 3376, 3378, 3379, 3381, 3383, 3385, 3387, 3388, 3390, 3392, 3394, 3396, 3398, 3399, 3401, 3403, 3405, 3407, 3408, 3410, 3412, 3414, 3416, 3418, 3419, 3421, 3423, 3425, 3427, 3429, 3430, 3432, 3434, 3436, 3438, 3440, 3441, 3443, 3445, 3447, 3449, 3451, 3452, 3454, 3456, 3458, 3460, 3462, 3463, 3465, 3467, 3469, 3471, 3473, 3474, 3476, 3478, 3480, 3482, 3484, 3486, 3487, 3489, 3491, 3493, 3495, 3497, 3498, 3500, 3502, 3504, 3506, 3508, 3510, 3511, 3513, 3515, 3517, 3519, 3521, 3523, 3524, 3526, 3528, 3530, 3532, 3534, 3536, 3537, 3539, 3541, 3543, 3545, 3547, 3549, 3550, 3552, 3554, 3556, 3558, 3560, 3562, 3563, 3565, 3567, 3569, 3571, 3573, 3575, 3577, 3578, 3580, 3582, 3584, 3586, 3588, 3590, 3592, 3593, 3595, 3597, 3599, 3601, 3603, 3605, 3607, 3608, 3610, 3612, 3614, 3616, 3618, 3620, 3622, 3623, 3625, 3627, 3629, 3631, 3633, 3635, 3637, 3638, 3640, 3642, 3644, 3646, 3648, 3650, 3652, 3654, 3655, 3657, 3659, 3661, 3663, 3665, 3667, 3669, 3671, 3672, 3674, 3676, 3678, 3680, 3682, 3684, 3686, 3688, 3690, 3691, 3693, 3695, 3697, 3699, 3701, 3703, 3705, 3707, 3709, 3710, 3712, 3714, 3716, 3718, 3720, 3722, 3724, 3726, 3728, 3730, 3731, 3733, 3735, 3737, 3739, 3741, 3743, 3745, 3747, 3749, 3751, 3752, 3754, 3756, 3758, 3760, 3762, 3764, 3766, 3768, 3770, 3772, 3774, 3775, 3777, 3779, 3781, 3783, 3785, 3787, 3789, 3791, 3793, 3795, 3797, 3799, 3800, 3802, 3804, 3806, 3808, 3810, 3812, 3814, 3816, 3818, 3820, 3822, 3824, 3826, 3828, 3829, 3831, 3833, 3835, 3837, 3839, 3841, 3843, 3845, 3847, 3849, 3851, 3853, 3855, 3857, 3859, 3860, 3862, 3864, 3866, 3868, 3870, 3872, 3874, 3876, 3878, 3880, 3882, 3884, 3886, 3888, 3890, 3892, 3894, 3895, 3897, 3899, 3901, 3903, 3905, 3907, 3909, 3911, 3913, 3915, 3917, 3919, 3921, 3923, 3925, 3927, 3929, 3931, 3933, 3935, 3937, 3939, 3940, 3942, 3944, 3946, 3948, 3950, 3952, 3954, 3956, 3958, 3960, 3962, 3964, 3966, 3968, 3970, 3972, 3974, 3976, 3978, 3980, 3982, 3984, 3986, 3988, 3990, 3992, 3994, 3996, 3998, 4000, 4002, 4004, 4005, 4007, 4009, 4011, 4013, 4015, 4017, 4019, 4021, 4023, 4025, 4027, 4029, 4031, 4033, 4035, 4037, 4039, 4041, 4043, 4045, 4047, 4049, 4051, 4053, 4055, 4057, 4059, 4061, 4063, 4065, 4067, 4069, 4071, 4073, 4075, 4077, 4079, 4081, 4083, 4085, 4087, 4089, 4091, 4093, 4095}
```
